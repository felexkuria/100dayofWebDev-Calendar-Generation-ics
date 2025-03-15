def generate_events():
    # Parse input text and generate events_data structure
    input_text = """Day 29
    Total Content Duration: ~53 minutes
    M o r e f o r m s p r a c t i c e A N D t h e i n t r o d u c t i o n o f a n o t h e r k e y f r o n t e n d t e c h n o l o g y : J a v a S c r i p t !
    S10L211 - Your Challenge! [Day 29]
    S10L212 - Challenge: Base Page Structure & Styling [Day 29]
    S10 Quiz 4 - Learning Check: Web Forms [Day 29]
    S10L213 - Challenge: First Set of Input Elements [Day 29]
    S10L214 - Challenge: Adding Remaining Elements [Day 29]
    S10L215 - Challenge: Submission & Validation [Day 29]
    S10L216 - Challenge: Styling [Day 29]
    S11L217 - Module Introduction [Day 29]
    S11L218 - What is JavaScript & Why would we use it? [Day 29]
    S11L219 - What You Will Learn In this Module [Day 29]
    S11L220 - Introducing Values & Variables [Day 29]
    Day 30
    Total Content Duration: ~45 minutes
    L e a r n a b o u t i m p o r t a n t J a v a S c r i p t f u n d a m e n t a l s a n d k e y l a n g u a g e c o n c e p t s .
    S11L221 - Adding the "script" HTML Element [Day 30]
    S11L222 - Working with Values & Basic JavaScript Commands [Day 30]
    S11L223 - Introducing Variables ("Data Containers") [Day 30]
    S11L224 - A Closer Look At The JavaScript Syntax [Day 30]
    S11L225 - A Second Variable & Practice Time! [Day 30]
    S11L226 - Outsourcing JavaScript Code Into External Files [Day 30]
    S11L227 - Introducing Arrays (Managing Lists Of Data) [Day 30]
    S11L228 - Introducing Objects (Grouping Related Data) [Day 30]"""

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
        print(events_data.append(current_day))

    return events_data
