
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import random

# ---------------- CONFIGURATION ----------------

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

PERIODS = [
    "9:00-10:00",
    "10:00-11:00",
    "11:15-12:15",
    "12:15-1:15",
    "2:00-3:00",
    "3:00-4:00"
]

# Class, Subject, Teacher, Room, Periods per week
DEFAULT_CLASSES = [
    ("CSE-A", "Python", "Mr. Kumar", "Room 101", 4),
    ("CSE-A", "Database", "Ms. Priya", "Room 102", 3),
    ("CSE-A", "Mathematics", "Mr. Ravi", "Room 101", 4),
    ("CSE-A", "Networks", "Ms. Anu", "Room 103", 3),
    ("CSE-B", "Python", "Mr. Kumar", "Room 102", 4),
    ("CSE-B", "Database", "Ms. Priya", "Room 103", 3),
    ("CSE-B", "Mathematics", "Mr. Ravi", "Room 102", 4),
    ("CSE-B", "Networks", "Ms. Anu", "Room 101", 3),
]


# ---------------- MAIN APPLICATION ----------------

class TimetableGenerator:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart Timetable Generator")
        self.root.geometry("1250x750")
        self.root.minsize(950, 600)

        self.classes = list(DEFAULT_CLASSES)
        self.schedule = []

        self.setup_ui()

    # ---------------- USER INTERFACE ----------------

    def setup_ui(self):

        header = tk.Frame(self.root, bg="#17365D", pady=18)
        header.pack(fill="x")

        tk.Label(
            header,
            text="SMART TIMETABLE GENERATOR",
            font=("Arial", 23, "bold"),
            bg="#17365D",
            fg="white"
        ).pack()

        tk.Label(
            header,
            text="Automatic Weekly Scheduling with Conflict Prevention",
            font=("Arial", 11),
            bg="#17365D",
            fg="white"
        ).pack(pady=(5, 0))

        # Buttons
        controls = tk.Frame(self.root, pady=15)
        controls.pack()

        tk.Button(
            controls,
            text="Generate Timetable",
            command=self.generate_timetable,
            bg="#1976D2",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8
        ).pack(side="left", padx=7)

        tk.Button(
            controls,
            text="Export CSV",
            command=self.export_csv,
            font=("Arial", 10),
            padx=15,
            pady=8
        ).pack(side="left", padx=7)

        tk.Button(
            controls,
            text="View Sample Data",
            command=self.show_sample_data,
            font=("Arial", 10),
            padx=15,
            pady=8
        ).pack(side="left", padx=7)

        self.status = tk.Label(
            self.root,
            text="Click Generate Timetable to create a schedule.",
            font=("Arial", 11),
            fg="#17365D"
        )
        self.status.pack(pady=5)

        # Notebook tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        # Table styling
        style = ttk.Style()
        style.configure(
            "Treeview",
            rowheight=42,
            font=("Arial", 9)
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        # Weekly timetable tab
        self.week_tab = tk.Frame(notebook)
        notebook.add(self.week_tab, text="Weekly Timetable")

        self.week_tree = ttk.Treeview(
            self.week_tab,
            columns=tuple(DAYS),
            show="tree headings"
        )

        self.week_tree.heading("#0", text="Period")
        self.week_tree.column(
            "#0", width=130, minwidth=110, anchor="center"
        )

        for day in DAYS:
            self.week_tree.heading(day, text=day)
            self.week_tree.column(
                day, width=190, minwidth=140, anchor="center"
            )

        self.week_tree.pack(
            fill="both", expand=True, padx=8, pady=8
        )

        # Detailed schedule tab
        self.details_tab = tk.Frame(notebook)
        notebook.add(self.details_tab, text="Detailed Schedule")

        columns = (
            "day", "period", "group",
            "subject", "teacher", "room"
        )

        self.details_tree = ttk.Treeview(
            self.details_tab,
            columns=columns,
            show="headings"
        )

        headings = {
            "day": "Day",
            "period": "Period",
            "group": "Class",
            "subject": "Subject",
            "teacher": "Teacher",
            "room": "Room"
        }

        widths = {
            "day": 120,
            "period": 130,
            "group": 110,
            "subject": 180,
            "teacher": 170,
            "room": 130
        }

        for col in columns:
            self.details_tree.heading(
                col, text=headings[col]
            )
            self.details_tree.column(
                col, width=widths[col], anchor="center"
            )

        self.details_tree.pack(
            fill="both", expand=True, padx=8, pady=8
        )

        # Footer
        tk.Label(
            self.root,
            text="Educational Scheduling Prototype | Developed using Python and Tkinter",
            font=("Arial", 9),
            fg="gray"
        ).pack(pady=7)

    # ---------------- TIMETABLE GENERATION ----------------

    def generate_timetable(self):

        tasks = []

        for group, subject, teacher, room, count in self.classes:
            for _ in range(count):
                tasks.append({
                    "group": group,
                    "subject": subject,
                    "teacher": teacher,
                    "room": room
                })

        slots = [
            (day, period)
            for day in DAYS
            for period in PERIODS
        ]

        best_schedule = []
        best_unscheduled = len(tasks)

        # Try multiple schedules and keep the best valid result.
        for attempt in range(100):

            shuffled_tasks = tasks[:]
            random.shuffle(shuffled_tasks)

            # Schedule tasks with more constrained teachers first.
            teacher_load = {}

            for task in shuffled_tasks:
                teacher = task["teacher"]
                teacher_load[teacher] = (
                    teacher_load.get(teacher, 0) + 1
                )

            shuffled_tasks.sort(
                key=lambda task: teacher_load[task["teacher"]],
                reverse=True
            )

            occupied_groups = set()
            occupied_teachers = set()
            occupied_rooms = set()

            current_schedule = []

            for task in shuffled_tasks:

                available_slots = []

                for day, period in slots:

                    slot = (day, period)

                    if (slot, task["group"]) in occupied_groups:
                        continue

                    if (slot, task["teacher"]) in occupied_teachers:
                        continue

                    if (slot, task["room"]) in occupied_rooms:
                        continue

                    available_slots.append((day, period))

                if not available_slots:
                    continue

                day, period = random.choice(available_slots)
                slot = (day, period)

                occupied_groups.add((slot, task["group"]))
                occupied_teachers.add((slot, task["teacher"]))
                occupied_rooms.add((slot, task["room"]))

                current_schedule.append({
                    "day": day,
                    "period": period,
                    **task
                })

            unscheduled_count = len(tasks) - len(current_schedule)

            if unscheduled_count < best_unscheduled:
                best_schedule = current_schedule
                best_unscheduled = unscheduled_count

            if best_unscheduled == 0:
                break

        self.schedule = sorted(
            best_schedule,
            key=lambda item: (
                DAYS.index(item["day"]),
                PERIODS.index(item["period"]),
                item["group"]
            )
        )

        self.refresh_views()

        if best_unscheduled == 0:
            self.status.config(
                text=(
                    f"Success! All {len(self.schedule)} periods "
                    "scheduled without teacher, room, or class clashes."
                ),
                fg="green"
            )
        else:
            self.status.config(
                text=(
                    f"Scheduled {len(self.schedule)} of {len(tasks)} "
                    f"periods. {best_unscheduled} could not be placed."
                ),
                fg="red"
            )

    # ---------------- DISPLAY TIMETABLE ----------------

    def refresh_views(self):

        # Clear old table entries
        for tree in (self.week_tree, self.details_tree):
            for item in tree.get_children():
                tree.delete(item)

        # Create weekly timetable rows
        for index, period in enumerate(PERIODS):
            self.week_tree.insert(
                "",
                "end",
                iid=f"period_{index}",
                text=period
            )

        # Fill both timetable views
        for item in self.schedule:

            day = item["day"]
            period = item["period"]

            period_index = PERIODS.index(period)
            row_id = f"period_{period_index}"

            # Keep weekly cells short and readable.
            description = (
                f'{item["group"]}: {item["subject"]}'
            )

            self.week_tree.set(
                row_id,
                day,
                description
            )

            # Detailed schedule includes teacher and room.
            self.details_tree.insert(
                "",
                "end",
                values=(
                    day,
                    period,
                    item["group"],
                    item["subject"],
                    item["teacher"],
                    item["room"]
                )
            )

    # ---------------- EXPORT CSV ----------------

    def export_csv(self):

        if not self.schedule:
            messagebox.showwarning(
                "No Timetable",
                "Please generate a timetable before exporting."
            )
            return

        path = filedialog.asksaveasfilename(
            title="Save Generated Timetable",
            defaultextension=".csv",
            initialfile="generated_timetable.csv",
            filetypes=[("CSV Files", "*.csv")]
        )

        if not path:
            return

        try:

            fields = [
                "day",
                "period",
                "group",
                "subject",
                "teacher",
                "room"
            ]

            with open(
                path,
                "w",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=fields
                )

                writer.writeheader()
                writer.writerows(self.schedule)

            messagebox.showinfo(
                "Export Successful",
                f"Timetable saved successfully!\n\n{path}"
            )

        except OSError as error:

            messagebox.showerror(
                "Export Failed",
                str(error)
            )

    # ---------------- SAMPLE DATA ----------------

    def show_sample_data(self):

        details = "\n".join(
            f"{group} | {subject} | {teacher} | "
            f"{room} | {count} periods/week"
            for group, subject, teacher, room, count
            in self.classes
        )

        messagebox.showinfo(
            "Sample Class Data",
            details
        )


# ---------------- START APPLICATION ----------------

if __name__ == "__main__":

    root = tk.Tk()
    app = TimetableGenerator(root)
    root.mainloop()
