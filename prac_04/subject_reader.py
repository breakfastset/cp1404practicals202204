"""
CP1404/CP5632 Practical
Data file -> lists program
"""
from operator import itemgetter

FILENAME = "subject_data.txt"


def main():
    subject_details = get_data()  # retrieve from file to populate subject details list
    # if there is any menu, it should be here.
    # get user input here
    print("A. Print All Subject Details")
    print("B. Add a Subject")
    print("Q. Quit")
    choice = input("> Select an Option >> ")
    # while user_input != "Q":
    #     if ...
    #        do_function1(subject_details)
    #     elif ...
    #        do_function2(subject_details)
    #     ....
    #     get user input here
    while choice != "Q":
        if choice == "A":
            print_subjects(subject_details)  # print report using subject_details
        elif choice == "B":
            add_subject(subject_details)
        print("A. Print All Subject Details")
        print("B. Add a Subject")
        print("Q. Quit")
        choice = input("> Select an Option >> ")
    # saving to file / database done here


def add_subject(subject_details):
    """Add new subject, lecturer, number of students to list of lists."""
    subject_id = input("Subject ID? ")
    lecturer = input("Lecturer Name? ")
    number_of_students = int(input("Number of students? "))
    subject_details.append([subject_id, lecturer, number_of_students])


def print_subjects(subject_details):
    """Print subject, lecturer and number of students in a nicely formatted report."""
    subject_details.sort(key=itemgetter(2), reverse=True)
    print("\n===== Subject Report =========")
    max_subject_length = max(len(subject_detail[1]) for subject_detail in subject_details)
    max_number_of_students_length = max(len(str(subject_detail[2])) for subject_detail in subject_details)
    for subject_detail in subject_details:
        print(f"{subject_detail[0]} is taught by {subject_detail[1]:{max_subject_length}} and has {subject_detail[2]:{max_number_of_students_length}} students")
    print()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []  # will be a list of lists
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_details.append(parts)  # append individual subject lists to a main list
    input_file.close()
    return subject_details


main()
