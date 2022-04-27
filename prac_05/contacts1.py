

def main():
    # 0. load data from file
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

    name_to_date_of_birth = create_dictionary(names, dates_of_birth)   # create a dictionary out of 2 lists

    # 1. user input + 2. process
    number_of_contacts = int(input("How many contacts do you wish to add? "))
    for i in range(number_of_contacts):
        name = input("Name? ")
        dob = input("DOB? ")
        name_to_date_of_birth[name] = convert_date_to_tuple(dob)
        print()

    # 3. output (print to screen or save to file)
    print(name_to_date_of_birth)


def create_dictionary(names, dates_of_birth):
    return dict(zip(names, dates_of_birth))

def convert_date_to_tuple(dob):
    date_of_birth = dob.split("/")
    return int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2])      # return a tuple


if __name__ == '__main__':
    main()