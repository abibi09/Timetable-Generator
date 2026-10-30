
# Smart Timetable Generator

## Project Overview

Smart Timetable Generator is a Python-based educational scheduling application that automatically creates weekly class timetables.

The application helps educational institutions organize classes, subjects, teachers, classrooms, and time slots while avoiding scheduling conflicts.

It uses a rule-based scheduling algorithm to assign available time slots and checks for teacher, classroom, and class clashes.

## Features

- Automatic weekly timetable generation.
- Teacher conflict prevention.
- Classroom conflict prevention.
- Class scheduling conflict prevention.
- Weekly timetable visualization.
- Detailed schedule displaying subjects, teachers, and rooms.
- Export generated timetables as CSV files.
- Sample educational dataset.

## Technologies Used

- Python 3
- Tkinter (Graphical User Interface)
- CSV module
- Random module

## Project Structure

```text
Timetable-Generator/
│
├── app.py
├── README.md
└── generated_timetable.csv
```

Note: The CSV file is created when the user exports a generated timetable.

## Requirements

- Python 3.10 or later
- Windows, Linux, or macOS
- Tkinter support

No additional Python packages are required for the current version.

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Run the following command:

```bash
python app.py
```

6. The Smart Timetable Generator application will open.

## How to Use

1. Click **Generate Timetable** to automatically create a weekly schedule.
2. View the generated schedule in the Weekly Timetable tab.
3. Open the Detailed Schedule tab to view teacher and classroom information.
4. Click **View Sample Data** to see the example classes and subjects.
5. Click **Export CSV** to save the generated timetable.

## Sample Dataset

The project includes two example classes:

- CSE-A
- CSE-B

Subjects include:

- Python
- Database
- Mathematics
- Networks

The sample dataset contains 28 weekly class periods.

## Conflict Prevention

The scheduling algorithm checks three conditions before assigning a class to a time slot:

1. A class group cannot have two subjects in the same period.
2. A teacher cannot teach two classes at the same time.
3. A classroom cannot be assigned to two classes simultaneously.

If a suitable slot cannot be found, the application reports the unscheduled periods.

## Algorithm

The application uses a randomized, rule-based scheduling approach.

1. Read the subject, teacher, classroom, and weekly period requirements.
2. Create individual scheduling tasks.
3. Randomize the task order.
4. Find available time slots.
5. Check teacher, classroom, and class availability.
6. Assign valid slots.
7. Repeat scheduling attempts and retain the best result.
8. Display and export the generated timetable.

## Limitations

- The current application uses sample educational data.
- The scheduling algorithm is rule-based and does not use a trained machine learning model.
- Users must modify the sample dataset in the source code to change subjects, teachers, classrooms, and period requirements.
- The application does not currently include a database or user authentication.

## Future Enhancements

- Add a graphical form to enter subjects and teacher details.
- Support multiple departments and academic years.
- Add database integration.
- Improve scheduling optimization.
- Add PDF timetable export.
- Develop a web-based version.

## Conclusion

Smart Timetable Generator demonstrates how Python can be used to automate educational scheduling.

By checking teacher, classroom, and class availability, the application generates organized weekly timetables and reduces manual scheduling effort.
