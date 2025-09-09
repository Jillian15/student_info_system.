import csv

students = {}

def add_student(student_id, name, age, *grades):
    if student_id in students:
        print("Student ID already exists.")
        return
    students[student_id] = {
        "name": name,
        "age": age,
        "grades": list(grades)
    }
    print(f"Student {name} added successfully!")

def display_students():
    if not students:
        print("No students found.")
        return
    for sid, info in students.items():
        print(f"\nID: {sid}, Name: {info['name']}, Age: {info['age']}")
        print("Grades: ", end="")
        for g in info['grades']:
            print(g, end=" ")
        print()

def update_student(student_id):
    if student_id not in students:
        print("Student not found.")
        return
    print("1. Update Name\n2. Update Age\n3. Update Grades")
    choice = input("Enter field to update: ")
    if choice == "1":
        new_name = input("Enter new name: ")
        students[student_id]['name'] = new_name
    elif choice == "2":
        new_age = input("Enter new age: ")
        students[student_id]['age'] = int(new_age)
    elif choice == "3":
        new_grades = input("Enter grades separated by commas: ").split(",")
        students[student_id]['grades'] = [int(g.strip()) for g in new_grades]
    else:
        print("Invalid choice")
        return
    print("Student updated successfully.")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print("Student deleted.")
    else:
        print("Student not found.")

def save_to_file(filename="students.csv"):
    with open(filename, mode="w", newline='') as f:
        writer = csv.writer(f)
        for sid, info in students.items():
            writer.writerow([sid, info['name'], info['age']] + info['grades'])
    print("Data saved to file.")

def load_from_file(filename="students.csv"):
    try:
        with open(filename, mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                sid, name, age, *grades = row
                students[sid] = {
                    "name": name,
                    "age": int(age),
                    "grades": [int(g) for g in grades]
                }
        print("Data loaded from file.")
    except FileNotFoundError:
        print("File not found. Starting with empty data.")

def tuple_demo():
    tup = ("S123", "Alice")
    print(f"Tuple: {tup}")
    print("Length:", len(tup))
    print("Max (alphabetical):", max(tup))
    print("Min (alphabetical):", min(tup))

average = lambda grades: sum(grades) / len(grades) if grades else 0

def main():
    load_from_file()
    tuple_demo()
    while True:
        print("\n===== Student Information System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grades_input = input("Enter grades separated by commas: ").split(",")
            grades = [int(g.strip()) for g in grades_input]
            add_student(student_id, name, age, *grades)

        elif choice == "2":
            display_students()

        elif choice == "3":
            sid = input("Enter student ID to update: ")
            update_student(sid)

        elif choice == "4":
            sid = input("Enter student ID to delete: ")
            delete_student(sid)

        elif choice == "5":
            save_to_file()

        elif choice == "6":
            load_from_file()

        elif choice == "7":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
            continue

if __name__ == "__main__":
    main()
