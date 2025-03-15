# pip install ics pytz
from ics import Calendar, Event
from ics.alarm import DisplayAlarm
from datetime import datetime, timedelta
import pytz
import warnings
import cleandata

# Suppress FutureWarning about str(Component) behavior
warnings.filterwarnings('ignore', category=FutureWarning)

# Define timezone for East African Time (e.g., Africa/Nairobi is UTC+3)
tz = pytz.timezone("Africa/Nairobi")

# The starting date for Day 16 is 15/03/2025 at 07:00 local time.
start_date = tz.localize(datetime(2025, 3, 15, 7, 0))

# Get events data from cleandata.py
events_data = cleandata.generate_events()

# Check if events_data is None before proceeding
if events_data is None:
    print("Error: No events data received from cleandata.generate_events()")
    exit(1)

cal = Calendar()

# Loop through each day's data to create an event.
for event_data in events_data:
    # Calculate the date for the event:
    # Day 16 is on start_date, so the offset is (current day - 16)
    day_offset = event_data["day"] - 16
    event_date = start_date + timedelta(days=day_offset)
    
    # The event's end time is the start time plus the day's duration (in minutes)
    event_end = event_date + timedelta(minutes=event_data["duration"])
    
    event = Event()
    event.name = f"Day {event_data['day']} of #100Webdevchallenge - {event_data['lectures'][0]}"
    event.begin = event_date
    event.end = event_end

    # Build the description with a checklist for the lectures and student notes
    lectures_str = "\nStudent Notes:\n" + "\n".join(f"- [ ] {lecture}\nNotes:\n" for lecture in event_data["lectures"])
    event.description = lectures_str
    
    # Add two alarms: one at the event start and one 5 minutes before.
    alarm_at_start = DisplayAlarm(trigger=timedelta(minutes=0))
    alarm_five_before = DisplayAlarm(trigger=timedelta(minutes=-5))
    event.alarms.append(alarm_at_start)
    event.alarms.append(alarm_five_before)
    cal.events.add(event)

# Write the calendar to an .ics file using serialize() method
with open("course_schedule.ics", "w") as f:
    f.write(cal.serialize())
print("ICS file 'course_schedule.ics' has been generated.")
