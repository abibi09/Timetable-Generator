
# PROJECT REPORT
# SMART TIMETABLE GENERATOR

## 1. ABSTRACT

Smart Timetable Generator is a Python-based educational scheduling application designed to automate the process of creating weekly class timetables.

Manual timetable preparation can be time-consuming and may result in scheduling conflicts involving teachers, classrooms, and student groups.

This project uses a rule-based scheduling algorithm to assign subjects to available time slots while checking for conflicts. It provides a graphical interface using Python Tkinter and allows users to view and export generated timetables.

## 2. INTRODUCTION

Timetable management is an important activity in educational institutions. A properly organized timetable ensures that teachers, classrooms, and student groups are assigned efficiently.

Traditional timetable preparation involves considerable manual effort. This project demonstrates how programming can simplify the scheduling process.

The Smart Timetable Generator automatically creates a weekly timetable using predefined educational data.

## 3. PROBLEM STATEMENT

Manual timetable preparation creates several challenges:

- Teacher scheduling conflicts.
- Classroom allocation conflicts.
- Overlapping classes.
- Time-consuming timetable preparation.
- Difficulty organizing multiple subjects and classes.

The project aims to reduce these problems through automated scheduling and conflict checking.

## 4. OBJECTIVES

The main objectives are:

1. Automate weekly timetable generation.
2. Prevent teacher scheduling conflicts.
3. Prevent classroom allocation conflicts.
4. Avoid overlapping periods for the same class.
5. Display schedules in an organized format.
6. Allow timetable export in CSV format.

## 5. SYSTEM REQUIREMENTS

### Hardware Requirements

- Computer or laptop.
- Minimum 4 GB RAM recommended.
- Keyboard and display.

### Software Requirements

- Operating System: Windows, Linux, or macOS.
- Programming Language: Python 3.
- Development Environment: Visual Studio Code.
- GUI Library: Tkinter.

### Python Modules

- tkinter
- csv
- random

These modules are included with standard Python installations that support Tkinter.

## 6. SYSTEM DESIGN

The application follows a simple scheduling workflow.

1. Load predefined class and subject information.
2. Create scheduling tasks based on weekly period requirements.
3. Identify available days and periods.
4. Check teacher availability.
5. Check classroom availability.
6. Check class-group availability.
7. Assign valid time slots.
8. Display the completed timetable.
9. Export the timetable as a CSV file.

## 7. ALGORITHM

The application uses a randomized rule-based scheduling algorithm.

### Algorithm Steps

1. Start the application.
2. Read the predefined educational dataset.
3. Generate individual scheduling tasks.
4. Randomize the task order.
5. Sort tasks using teacher scheduling load.
6. Find available time slots for each task.
7. Check whether the teacher, classroom, and class group are available.
8. Assign the task to a valid time slot.
9. Repeat the scheduling process with different randomized orders.
10. Retain the schedule containing the highest number of successfully assigned periods.
11. Display the weekly timetable.
12. Allow CSV export.
13. Stop.

## 8. IMPLEMENTATION

The project is implemented using Python and Tkinter.

### Main Components

**A. Graphical User Interface**

Tkinter provides the graphical interface, including buttons, tabs, and timetable tables.

**B. Timetable Generation**

The scheduling algorithm assigns subjects to available weekly time slots.

**C. Conflict Prevention**

The application checks:

- Class-group availability.
- Teacher availability.
- Classroom availability.

**D. Weekly Timetable Display**

The weekly view displays days and periods in a grid format.

**E. Detailed Schedule**

The detailed view displays the day, period, class, subject, teacher, and classroom.

**F. CSV Export**

The generated schedule can be saved as a CSV file for further use.

## 9. TESTING AND RESULTS

The application was tested using the predefined sample dataset containing two classes and four subjects.

### Sample Dataset

- Classes: CSE-A and CSE-B.
- Subjects: Python, Database, Mathematics, and Networks.
- Working days: Monday to Friday.
- Periods per day: Six.
- Total weekly periods: 28.

### Test Cases

| Test Case | Expected Result |
|---|---|
| Generate timetable | Schedule is generated |
| Teacher conflict check | No teacher overlaps |
| Room conflict check | No room overlaps |
| Class conflict check | No class overlaps |
| Weekly timetable view | Schedule displayed in grid |
| Detailed schedule view | Complete schedule displayed |
| CSV export | File saved successfully |

### Result

The application successfully generated all 28 sample periods during testing without teacher, classroom, or class-group conflicts.

The generated timetable was displayed in both weekly and detailed views. CSV export was also tested successfully.

## 10. LIMITATIONS

- The current application uses predefined sample data.
- The scheduling algorithm is rule-based rather than a trained machine learning model.
- Changes to subjects, teachers, rooms, and weekly requirements currently require editing the source code.
- Database integration is not included.
- Advanced scheduling preferences are not yet supported.

## 11. FUTURE ENHANCEMENTS

The project can be improved by adding:

1. User-friendly forms for entering subjects and teacher details.
2. Database integration.
3. Multiple department and classroom management.
4. Advanced timetable optimization.
5. PDF export functionality.
6. Web-based timetable management.
7. Teacher-specific availability preferences.

## 12. CONCLUSION

The Smart Timetable Generator demonstrates how Python programming can automate educational scheduling.

The application generates weekly timetables while checking teacher, classroom, and class-group conflicts. It provides an organized graphical interface and supports CSV export.

This project serves as a functional prototype for educational timetable management and can be extended with additional scheduling and optimization features.

## 13. REFERENCES

1. Python Official Documentation – https://docs.python.org/3/
2. Tkinter Documentation – https://docs.python.org/3/library/tkinter.html
3. Python CSV Module – https://docs.python.org/3/library/csv.html
4. Visual Studio Code Documentation – https://code.visualstudio.com/docs
