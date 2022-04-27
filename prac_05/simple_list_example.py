

def main():

    students = []

    for i in range(3):
        name = input("Name? ")
        student_number = input("SID? ")
        age = int(input("Age? "))
        student = [student_number, name, age]   # create a list
        students.append(student)    # append the list to students list

    print(students)   # list of lists



if __name__ == '__main__':
    main()