# pip install ics pytz
from ics import Calendar, Event
from ics.alarm import DisplayAlarm
from datetime import datetime, timedelta
import pytz
import warnings
import cleandata

# Suppress FutureWarning
warnings.filterwarnings('ignore', category=FutureWarning)

# Configure timezone
tz = pytz.timezone("Africa/Nairobi")

def get_user_input():
    """Get and validate user inputs with improved prompts"""
    print("📅 Enter start date for your current schedule (format: DD/MM/YYYY HH:MM):")
    date_str = input("👉 Example: 15/03/2025 07:00\n> ").strip()
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
        return tz.localize(start_date)
    except ValueError:
        print("❌ Error: Invalid date format. Please use DD/MM/YYYY HH:MM")
        exit(1)

def get_current_day():
    """Get and validate current day input"""
    print("\n🔢 Enter your current progress day (0-100):")
    print("   - New students: Enter 0")
    print("   - Continuing students: Enter your current day (e.g., 16)")
    try:
        current_day = int(input("> ").strip())
        if not 0 <= current_day <= 100:
            raise ValueError
        return current_day
    except ValueError:
        print("❌ Error: Please enter a number between 0 and 100")
        exit(1)

def create_calendar_events(start_date, current_day, events_data):
    """Create calendar events with dynamic scheduling"""
    cal = Calendar()
    
    # Filter and sort events based on current progress
    filtered_events = [e for e in events_data if e['day'] >= current_day]
    filtered_events.sort(key=lambda x: x['day'])
    
    # Validate continuing students' input
    if current_day > 0 and not any(e['day'] == current_day for e in filtered_events):
        print(f"❌ Error: Day {current_day} content not found in lectures data")
        exit(1)

    # Create events with progressive scheduling
    for idx, event_data in enumerate(filtered_events):
        event_date = start_date + timedelta(days=idx)
        event_end = event_date + timedelta(minutes=event_data["duration"])
        
        event = Event()
        event.name = f"📆 Day {event_data['day']} of #100DaysWebDev"
        event.begin = event_date
        event_end = event_end
        
        # Build lesson plan description
        desc = f"📘 Daily Overview:\n{event_data['description']}\n\n"
        desc += "🎯 Lessons Covered:\n"
        # Add numbered lessons with emojis
        lessons = []
        for lesson_idx, lesson in enumerate(event_data["lectures"], 1):
             lessons.append(
                 f"📌 Lesson {lesson_idx:02d}: {lesson['title']}\n"
                 f"   🖊️ Notes: Add your personal notes here\n"
                #  f"   🔗 Resources: {lesson.get('resources', 'Check course platform')}"
    )
        
        # # Add numbered lessons with emojis
        # lessons = []
        # for lesson_idx, lesson in enumerate(event_data["lectures"], 1):
        #     lessons.append(
        #         f"🎯 {lesson_idx}. {lesson['title']}\n"
        #         f"   📝 Notes: Add your personal notes here"
        #     )
        
        event.description = desc + "\n".join(lessons)
        
        # Configure reminders
        event.alarms.extend([
            DisplayAlarm(trigger=timedelta(minutes=-15)),
            DisplayAlarm(trigger=timedelta(minutes=0))
        ])
        
        cal.events.add(event)
    
    return cal

def main():
    # Get user inputs
    start_date = get_user_input()
    current_day = get_current_day()
    
    # Load lecture data
    events_data = cleandata.generate_events()
    if not events_data:
        print("❌ Error: No lecture data found")
        exit(1)

    # Generate calendar
    calendar = create_calendar_events(start_date, current_day, events_data)
    
    # Save output
    with open("webdev_journey.ics", "w") as f:
        f.write(calendar.serialize())
    print("\n✅ Success! Calendar 'webdev_journey.ics' created!")

if __name__ == "__main__":
    main()