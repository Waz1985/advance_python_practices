from actions import (
    add_student,
    show_all_students,
    show_top_3,
    get_general_average,
)
from data import export_data, import_data

students = []  # List shared across modules

def show_menu():
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add students")
        print("2. Show all students")
        print("3. Show top 3 by average")
        print("4. Show general average")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("7. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_student(students)

        elif option == "2":
            show_all_students(students)

        elif option == "3":
            show_top_3(students)

        elif option == "4":
            get_general_average(students)

        elif option == "5":
            export_data(students)

        elif option == "6":
            imported = import_data()
            if imported is not None:
                students.clear()
                students.extend(imported)

        elif option == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")