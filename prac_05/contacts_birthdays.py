"""
Name: Alakazam
Date Started: 13/04/2022
Github URL: https://www.git....
"""

CONTACTS_FILE = "names_and_birthdays.csv"


def main():
    """Start of Program."""
    names = []
    dates_of_birth = []
    load_data(names, dates_of_birth)     # load file into names and dates_of_birth
    name_to_date_of_birth = convert_to_dictionary(names, dates_of_birth)

    number_of_people = int(input("How many people do you want to enter? "))

    for i in range(number_of_people):
        name = input("Name? ")
        dob = input("DOB? ")
        name_to_date_of_birth[name] = convert_date_to_tuple(dob)     # store key-value pair as string to tuple pair
    print(f"{number_of_people} people added.")

    print("Saving ...")
    save_data(name_to_date_of_birth)

    print("~~~ Thank you and have a nice day ~~~")


def load_data(names, dates_of_birth):
    """Load data from file into names and dates_of_birth lists."""
    with open(CONTACTS_FILE) as in_file:
        names.extend(in_file.readline().strip().split(","))
        dob_data = in_file.readline().strip().split(",")
        for dob in dob_data:
            dates_of_birth.append(convert_date_to_tuple(dob))


def save_data(name_to_date_of_birth):
    """Save dictionary to file."""
    names = []
    dates_of_birth = []
    with open(CONTACTS_FILE, "w") as out_file:
        for name, date_of_birth in name_to_date_of_birth.items():
            names.append(name)
            dates_of_birth.append(convert_tuple_to_date(date_of_birth))
        out_file.write(",".join(names) + "\n")             # convert list to string delimited by comma
        out_file.write(",".join(dates_of_birth) + "\n")


def convert_date_to_tuple(date_of_birth):
    """Convert date to tuple of 3 numbers."""
    dob = date_of_birth.split("/")
    return int(dob[0]), int(dob[1]), int(dob[2])  # return a tuple


def convert_tuple_to_date(date_tuple):
    """Convert tuple to dd/mm/yyyy format."""
    return date_tuple[0] + "/" + date_tuple[1] + "/" + date_tuple[2]


def convert_to_dictionary(names, dates_of_birth):
    """Convert lists to dictionary format."""
    return dict(zip(names, dates_of_birth))


if __name__ == '__main__':
    main()
