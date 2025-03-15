import re  # Add this at the top

def generate_events():
    try:
        with open('lecture.txt', 'r') as file:
            input_text = file.read()
    except FileNotFoundError:
        print("Error: lecture.txt not found")
        return None

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
                'description': None,
                'lectures': []
            }
        elif line.startswith('Total Content Duration: '):
            duration_str = line.split(': ')[1]
            duration = int(''.join(filter(str.isdigit, duration_str)))
            current_day['duration'] = duration
        elif ' - ' in line and line.split(' - ')[0].strip():
            lecture_info = line.split(' [')[0].strip()
            section_lecture, title = lecture_info.split(' - ', 1)
            
            # Skip non-lecture lines like quizzes
            if 'L' not in section_lecture:
                continue
                
            # Extract section and lecture numbers safely
            try:
                section_part, lecture_part = section_lecture.split('L')
                section = int(section_part[1:])  # Remove 'S' and convert
                lecture = int(lecture_part)
            except ValueError:
                continue  # Skip invalid formats
                
            # Extract day using regex pattern matching
            day_match = re.search(r'$$Day (\d+)$$', line)
            if not day_match:
                continue  # Skip lines without valid Day marker
            day = int(day_match.group(1))

            lecture_data = {
                'section': section,
                'lecture': lecture,
                'title': title,
                'day': day
            }
            current_day['lectures'].append(lecture_data)
        else:
            if current_day and current_day['description'] is None:
                current_day['description'] = line.strip()

    if current_day:
        events_data.append(current_day)
        print(events_data)

    return events_data
