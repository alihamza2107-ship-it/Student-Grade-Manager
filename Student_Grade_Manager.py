import json
import os

# Main data storage
students = {}
FILE_NAME = "students.json"

# ========================
# FUNCTION 1 — Add Student
# ========================
def add_student():
    try:
        name = input("Enter student name: ").strip().title()

        if name in students:
            print(f"❌ {name} already exists!")
            return

        grades = []
        subjects = ["Math", "English", "Science"]
        
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"Enter {subject} grade (0-100): "))
                    if 0 <= grade <= 100:
                        grades.append(grade)
                        break
                    else:
                        print("❌ Grade must be between 0 and 100!")
                except ValueError:
                    print("❌ Please enter a valid number!")

        students[name] = {
            "grades": grades,
            "subjects": subjects
        }
        print(f"✅ {name} added successfully!")

    except Exception as e:
        print(f"Error: {e}")

# ========================
# FUNCTION 2 — Display Menu
# ========================
def show_menu():
    print("\n" + "="*35)
    print("     🎓 STUDENT GRADE MANAGER")
    print("="*35)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Grade")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")
    print("="*35)

# ========================
# FUNCTION 3 — Calculate Average
# ========================
def get_average(grades):
    if not grades: return 0
    return sum(grades) / len(grades)

# ========================
# FUNCTION 4 — Get Letter Grade
# ========================
def get_letter(average):
    if average >= 90: return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else: return "F"

# ========================
# FUNCTION 5 — View All Students
# ========================
def view_all_students():
    if not students:
        print("❌ No students found!")
        return

    print("\n" + "="*65)
    print(f"{'NAME':<15} {'MATH':<8} {'ENGLISH':<10} {'SCIENCE':<10} {'AVG':<8} {'GRADE'}")
    print("="*65)

    for name, data in students.items():
        g = data["grades"]
        avg = get_average(g)
        letter = get_letter(avg)
        # We use .get to handle cases where a list might be shorter than expected
        print(f"{name:<15} {g[0]:<8} {g[1]:<10} {g[2]:<10} {avg:<8.1f} {letter}")

    print("="*65)
    print(f"Total Students: {len(students)}")

# ========================
# FUNCTION 6 — Search Student
# ========================
def search_student():
    name = input("Enter student name to search: ").strip().title()

    if name not in students:
        print(f"❌ Student '{name}' not found!")
        return

    data = students[name]
    grades = data["grades"]
    subjects = data["subjects"]
    avg = get_average(grades)
    letter = get_letter(avg)

    print("\n" + "="*35)
    print(f"   📋 Student: {name}")
    print("="*35)
    for i in range(len(subjects)):
        print(f"  {subjects[i]:<12}: {grades[i]}")
    print("-" * 35)
    print(f"  Average      : {avg:.1f}")
    print(f"  Letter Grade : {letter}")
    print("="*35)

# ========================
# FUNCTION 7 — Delete Student
# ========================
def delete_student():
    name = input("Enter student name to delete: ").strip().title()

    if name not in students:
        print(f"❌ Student '{name}' not found!")
        return

    confirm = input(f"⚠️ Are you sure you want to delete {name}? (yes/no): ").strip().lower()

    if confirm == "yes":
        del students[name]
        print(f"✅ {name} deleted successfully!")
    else:
        print("❌ Deletion cancelled!")

# ========================
# FUNCTION 8 — Update Grade
# ========================
def update_grade():
    name = input("Enter student name to update: ").strip().title()

    if name not in students:
        print(f"❌ Student '{name}' not found!")
        return

    subjects = students[name]["subjects"]

    print(f"\n📋 Current grades for {name}:")
    for i, subject in enumerate(subjects):
        print(f"  {i+1}. {subject}: {students[name]['grades'][i]}")

    while True:
        try:
            choice = int(input("\nEnter choice (1-3) to update: "))
            if 1 <= choice <= 3:
                break
            else:
                print("❌ Please enter 1, 2 or 3!")
        except ValueError:
            print("❌ Please enter a valid number!")

    while True:
        try:
            new_grade = float(input(f"Enter new grade for {subjects[choice-1]} (0-100): "))
            if 0 <= new_grade <= 100:
                old_grade = students[name]["grades"][choice-1]
                students[name]["grades"][choice-1] = new_grade
                print(f"✅ {subjects[choice-1]} grade updated!")
                print(f"   {old_grade} → {new_grade}")
                break
            else:
                print("❌ Grade must be between 0 and 100!")
        except ValueError:
            print("❌ Please enter a valid number!")

# ========================
# FUNCTION 9 — Save Data
# ========================
def save_data():
    if not students:
        print("⚠️ No data to save.")
        return
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
        print(f"✅ Data saved successfully! ({len(students)} students)")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

# ========================
# FUNCTION 10 — Load Data
# ========================
def load_data():
    global students
    if not os.path.exists(FILE_NAME):
        return # Just exit if file doesn't exist yet

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            students.update(data)
        print(f"✅ Data loaded successfully! ({len(students)} students)")
    except Exception as e:
        print(f"❌ Error loading data: {e}")

# ========================
# MAIN LOOP
# ========================
load_data()

while True:
    show_menu()
    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_grade()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        save_data()
    elif choice == "7":
        load_data()
    elif choice == "8":
        save_data()
        print("👋 Goodbye Ali Hamza!")
        break
    else:
        print("❌ Invalid choice! Please enter 1-8")