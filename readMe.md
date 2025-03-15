# 100 Days of Web Dev Calendar Generator

A Python script to create calendar events (.ics file) for tracking progress in a 100-day web development challenge, complete with lessons, reminders, and progress tracking.

## 📌 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [File Structure](#-file-structure)
- [Contributing](#-contributing)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## 🚀 Features

- Generate ICS calendar files compatible with Google Calendar, Outlook, and Apple Calendar
- Automatic progress tracking with day numbering
- Customizable lesson plans with duration tracking
- Reminder system with 15-minute and event-start alerts
- Support for continuing students to resume progress
- Clear error handling and user prompts
- Lecture parsing from text files

## 📋 Prerequisites

Before using this project, you need:

1. **Python 3.6+** installed on your system
2. **lecture.txt** file with your course content
3. Basic understanding of command line/terminal usage
4. GitHub account (for collaboration)
5. Git installed locally (for version control)

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/100days-webdev-calendar.git
   ```
   cd 100days-webdev-calendar
   Install required packages:
   ```bash
   pip install ics pytz
   ```
   Prepare your lecture.txt file (see File Structure )
   🖥️ Usage
   

Prepare your lecture.txt: Create a text file following this format:
Day 1
Total Content Duration: 120 minutes
Introduction to HTML basics
S1L1 - HTML Structure [30m]
S1L2 - Basic Tags [45m]
QUIZ - HTML Fundamentals [15m]
Run the script:
python main.py
Follow the prompts:
📅 Enter start date for your current schedule (format: DD/MM/YYYY HH:MM):
👉 Example: 15/03/2025 07:00

> 15/03/2025 07:00

🔢 Enter your current progress day (0-100):

- New students: Enter 0
- Continuing students: Enter your current day (e.g., 16)
  > 0
  > Import the generated file:
  > Find webdev_journey.ics in your project folder
  > Import to your preferred calendar application
  >
  ### 📂 File Structure

- ├── main.py # Main script
- ├── cleandata.py # Data parsing module
- ├── lecture.txt # Course content (sample included)
-  webdev_journey.ics # Generated calendar file
- ├── requirements.txt # Dependency list
- └── README.md # This documentation
🤝 Contributing

We welcome contributions! Here's how to collaborate:
Fork the Repository
Click 'Fork' at top-right of GitHub repository page
Clone Your Fork
 ```bash
git clone https://github.com/your-username/100days-webdev-calendar.git
 ```
Create a Feature Branch
 ```bash
git checkout -b feature/your-feature-name
 ```
Make Changes
Follow existing code style
Add comments for complex logic
Update documentation when needed
Commit Changes
 ```bash
git commit -m "feat: add new validation checks"
 ```
Use conventional commit messages:
feat: for new features
fix: for bug fixes
docs: for documentation changes
chore: for maintenance tasks
Push to Your Fork
 ```bash
git push origin feature/your-feature-name
 ```
Create Pull Request
Open PR from your branch to main repository's main branch
Describe changes clearly in PR description

###🔮 Future Enhancements
Planned improvements:
- Web interface for non-technical users
- Automatic progress synchronization
- Integration with learning platforms
- Mobile app notifications
- Progress visualization dashboard
- Multiple calendar export formats
- Collaborative learning features
📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

 - [ICS Python library](https://github.com/ics-py/ics-py)
- Python datetime and pytz maintainers
- [Original 100DaysOfCode concept by Alexander Kallaway](https://www.100daysofcode.com)
