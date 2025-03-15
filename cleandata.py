# Parse input text and generate events_data structure
input_text = """Day 55
Total Content Duration: ~45 minutes
E x p l o r e m o r e a d v a n c e d J a v a S c r i p t c o n c e p t s - c o n c e p t s w h i c h m a t t e r f o r b o t h f r o n t e n d a n d b a c k e n d d e v e l o p m e n t .
S21L386 - Custom Error Handling With try / catch [Day 55]
S21L387 - Error Data & Throwing Custom Errors [Day 55]
S21L388 - Variable Scoping & Shadowing [Day 55]
S21 Quiz 15 - Learning Check: More Advanced JavaScript Concepts [Day 55]
S21L389 - Introducing Classes As Object Blueprints [Day 55]
S21L390 - Classes & Methods (and "this") [Day 55]
S21L391 - Destructuring Objects & Arrays [Day 55]
S21 Quiz 16 - Learning Check: More on Objects [Day 55]
Day 56
Total Content Duration: ~45 minutes
E x p l o r e m o r e a d v a n c e d J a v a S c r i p t c o n c e p t s - c o n c e p t s w h i c h m a t t e r f o r b o t h f r o n t e n d a n d b a c k e n d d e v e l o p m e n t .
S21L386 - Custom Error Handling With try / catch [Day 55]
S21L387 - Error Data & Throwing Custom Errors [Day 55]
S21L388 - Variable Scoping & Shadowing [Day 55]
S21 Quiz 15 - Learning Check: More Advanced JavaScript Concepts [Day 55]
S21L389 - Introducing Classes As Object Blueprints [Day 55]
S21L390 - Classes & Methods (and "this") [Day 55]
S21L391 - Destructuring Objects & Arrays [Day 55]
S21 Quiz 16 - Learning Check: More on Objects [Day 55]"""

# Process the input text
lines = [line.strip() for line in input_text.split('\n') if line.strip()]
events_data = []
current_day = None

for line in lines:
    if line.startswith('Day '):
        if current_day:
            events_data.append(current_day)
        day_number = int(line.split()[1])
        current_day = {
            'day': day_number,
            'duration': None,
            'lectures': []
        }
    elif line.startswith('Total Content Duration: '):
        duration_str = line.split(': ')[1]
        if '~' in duration_str:
            duration = int(duration_str.split('~')[1].split()[0])
        else:
            duration = int(duration_str.split()[0])
        current_day['duration'] = duration
    else:
        # Only process lines that contain lecture markers
        if ' - ' in line and line.split(' - ')[0].strip():
            lecture = line.split(' [')[0].strip()
            current_day['lectures'].append(lecture)

# Add the last day if exists
if current_day:
    events_data.append(current_day)

# Print the formatted output
print("events_data = [")
for event in events_data:
    print(f"    {{\n        \"day\": {event['day']},")
    print(f"        \"duration\": {event['duration']},  # minutes")
    print("        \"lectures\": [")
    for lecture in event['lectures']:
        print(f"            \"{lecture}\",")
    print("        ]\n    },")
print("]")