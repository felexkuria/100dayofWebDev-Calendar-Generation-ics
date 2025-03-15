# pip install ics pytz
from ics import Calendar, Event
from ics.alarm import DisplayAlarm
from datetime import datetime, timedelta
import pytz

# Define timezone for East African Time (e.g., Africa/Nairobi is UTC+3)
tz = pytz.timezone("Africa/Nairobi")

# The starting date for Day 16 is 15/03/2025 at 07:00 local time.
start_date = tz.localize(datetime(2025, 3, 15, 7, 0))

# Sample data for Days 16 to 20.
# Each dictionary contains:
#   - "day": the day number in the course
#   - "duration": total content duration in minutes for that day
#   - "lectures": a list of sub-lessons to include as checkboxes in the event description
# (Extend this list with data for Days 21 to 100 as needed.)
events_data = [
    {
        "day": 16,
        "duration": 45,  # minutes
        "lectures": [
            "S7L121 - Your Flexbox Challenge!",
            "S7L122 - Adding Flexbox to our Project",
            "S7L123 - Adding a Background Image",
            "S7L124 - Creating a Container for the Hero-Content",
            "S7L125 - Positioning Elements",
            "S7L126 - Styling the Hero Content",
            "S7L127 - Understanding Fixed & Absolute Positioning"
        ]
    },
    {
        "day": 17,
        "duration": 53,
        "lectures": [
            "S7L128 - Working with % Units & Creating a Top Navigation Bar",
            "S7L129 - Finishing the Header",
            "S7L130 - Introducing the 'Highlights' Section",
            "S7L131 - Creating the HTML Code",
            "S7L135 - Styling Text"
        ]
    },
    {
        "day": 18,
        "duration": 42,
        "lectures": [
            "S7L136 - Understanding Parent-Child Margin Collapsing",
            "S7L138 - The Next Step",
            "S7L139 - Creating a Footer Section",
            "S7L140 - Styling the Footer",
            "S7L141 - Places Page - Overview & Preparations",
            "S7L143 - Using 'position: static'"
        ]
    },
    {
        "day": 19,
        "duration": 48,
        "lectures": [
            "S7L144 - Creating the Card Look",
            "S7L145 - Understanding 'overflow' & Your Challenge!",
            "S7L146 - Solving the Challenge",
            "S7L147 - Creating all Cards",
            "S7L148 - The CSS Grid - The Theory",
            "S7L149 - Understanding the 'nth-type' Selector & 'grid-template-columns'"
        ]
    },
    {
        "day": 20,
        "duration": 50,
        "lectures": [
            "S7L150 - Your Grid Challenge",
            "S7L151 - Working with Unicode UTF-8",
            "S7L152 - Finishing Touches",
            "S7L153 - Module Summary",
            "S7L154 - Optional: Diving Deeper Into 'position', Flexbox & the Grid",
            "S8L155 - Module Introduction",
            "S8L156 - Project Overview",
            "S8L157 - Please Read: Optional Lectures",
            "S8L158 - Optional: Your Challenge - Creating the HTML Structure",
            "S8L159 - Optional: Challenge Solution - The HTML Structure"
        ]
    },
    # ... add events for Days 21 to 100 here
]

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

    # Build the description with a checklist for the lectures.
    lectures_str = "\n".join(f"- [ ] {lecture}" for lecture in event_data["lectures"])
    # Build the description with a checklist for the lectures.
    lectures_str = "\n".join(f"- [ ] {lecture}" for lecture in event_data["lectures"])
    # Add two alarms: one at the event start and one 5 minutes before.
    alarm_at_start = DisplayAlarm(trigger=timedelta(minutes=0))
    # Add two alarms: one at the event start and one 5 minutes before.
    alarm_at_start = DisplayAlarm(trigger=timedelta(minutes=0))
    alarm_five_before = DisplayAlarm(trigger=timedelta(minutes=-5))
    event.alarms.append(alarm_at_start)
    cal.events.add(event)

# Write the calendar to an .ics file using serialize() method
with open("course_schedule.ics", "w") as f:
    f.write(cal.serialize())
print("ICS file 'course_schedule.ics' has been generated.")
