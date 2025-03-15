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
            if current_day:  # Added safety check
                duration_str = line.split(': ')[1]
                duration = int(''.join(filter(str.isdigit, duration_str)))
                current_day['duration'] = duration
        elif ' - ' in line:
            # Handle lecture/quiz lines
            parts = line.split(' - ', 1)
            if len(parts) != 2:
                continue
                
            left_side, right_side = parts
            lecture_info = left_side.split(' [')[0].strip()
            
            # Handle both uppercase and lowercase L
            if 'l' in lecture_info.lower():
                try:
                    # Handle formats like S3L2 or Section3-L2
                    section_lecture = lecture_info.replace('Section', 'S').replace('-', '')
                    section_part, lecture_part = section_lecture.lower().split('l')
                    
                    # Extract section number
                    section = int(section_part[1:])  # Remove 'S'
                    # Extract lecture number
                    lecture = int(lecture_part.split()[0])  # Handle any trailing text
                    
                    # Extract title from right side before duration
                    title = right_side.split(' [')[0].strip()
                    
                    lecture_data = {
                        'section': section,
                        'lecture': lecture,
                        'title': title,
                        # Use current day's number instead of parsing again
                        'day': current_day['day'] if current_day else 0
                    }
                    
                    if current_day:
                        current_day['lectures'].append(lecture_data)
                        
                except (ValueError, IndexError, AttributeError):
                    # Skip lines that don't match the pattern
                    continue
            else:
                # Handle description if not set yet
                if current_day and current_day['description'] is None:
                    current_day['description'] = right_side.split(' [')[0].strip()
        else:
            # Capture multi-line descriptions
            if current_day and current_day['description']:
                current_day['description'] += "\n" + line
            elif current_day:
                current_day['description'] = line

    if current_day:  # Add the last day
        events_data.append(current_day)

    return events_data