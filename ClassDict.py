# Course lookup program
# CSC500 Mod 7 Critical Thinking Assignment

def main():
    # Dictionaries
    course_rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    course_instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    course_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    # Ask the user for a course number
    user_input = input("Enter a course number (e.g. CSC101, NET110, COM241): ").strip()

    # Check if that course exists
    if user_input in course_rooms and user_input in course_instructors and user_input in course_times:
        room = course_rooms[user_input]
        instructor = course_instructors[user_input]
        time = course_times[user_input]

        print("\nCourse information:")
        print("-------------------")
        print(f"Course:     {user_input}")
        print(f"Room:       {room}")
        print(f"Instructor: {instructor}")
        print(f"Time:       {time}")
    else:
        # Handle invalid course code
        print("\nSorry, that course was not found.")

# Run the program
if __name__ == "__main__":
    main()
