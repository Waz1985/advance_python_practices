from typing import List, Optional
from student import Student
import re

class StudentManager:
    def __init__(self):
        self.students: List[Student] = []

def valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except:
            print("Invalid number.")

def add_student(students):
    print("\n--- ADD NEW STUDENT ---")

    name = input("Full name: ").strip()
    section = input("Section (example: 11B): ").strip()

    spanish = valid_grade("Spanish grade: ")
    english = valid_grade("English grade: ")
    socials = valid_grade("Social studies grade: ")
    science = valid_grade("Science grade: ")

    student = {
        "name": name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "socials": socials,
        "science": science,
    }

    students.append(student)
    print("\nStudent added successfully!")


def show_all_students(students):
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n--- ALL STUDENTS ---")
    for s in students:
        print(
            f"{s['name']} | {s['section']} | "
            f"SPA: {s['spanish']} | ENG: {s['english']} | "
            f"SOC: {s['socials']} | SCI: {s['science']}"
        )


def calculate_average(student):
    return (
        student["spanish"] +
        student["english"] +
        student["socials"] +
        student["science"]
    ) / 4


def show_top_3(students):
    if not students:
        print("\nNo students available.")
        return

    sorted_students = sorted(students, key=calculate_average, reverse=True)
    top3 = sorted_students[:3]

    print("\n--- TOP 3 STUDENTS ---")
    for s in top3:
        print(f"{s['name']} | {s['section']} | Average: {calculate_average(s):.2f}")


def get_general_average(students):
    if not students:
        print("\nNo students to calculate average.")
        return

    total = sum(calculate_average(s) for s in students)
    general_avg = total / len(students)
    print(f"\nGeneral average of all students: {general_avg:.2f}")