"""
Name: Lex Luthor
Date Started: 14/04/2022
Github URL: https://github.com/JCUS-CP1404/....
"""

CONTACTS_FILE = "names_and_birthdays.csv"


def main():
    """Start of Program."""
    names = []
    dates_of_birth = []
    load_data(names, dates_of_birth)  # populate the lists with data from file
    name_to_date_of_birth = convert_to_dictionary(names, dates_of_birth)

    number_of_people = int(input("How many people do you want to enter? "))

    for i in range(number_of_people):
        name = input("Name? ")
        dob = input("DOB? ")
        name_to_date_of_birth[name] = convert_date_to_tuple(dob)  # store key-value pair as name-date tuple
    print(f"{number_of_people} people added.")

    print("Saving ...")
    save_data(name_to_date_of_birth)
    print("~~~ Thank you and have a nice day ~~~")


def load_data(names, dates_of_birth):
    """Load data from file into names and dates_of_birth lists.
    @:param names List of names of contacts
    @:param dates_of_birth List of Dates of Birth
    """
    with open(CONTACTS_FILE) as in_file:
        names.extend(in_file.readline().strip().split(","))  # read first line into name list
        dob_data = in_file.readline().strip().split(",")  # read second line into dob list
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
        out_file.write(",".join(names) + "\n")
        out_file.write(",".join(dates_of_birth) + "\n")


def convert_date_to_tuple(date_of_birth):
    """Convert dd/mm/yyyy format to (dd, mm, yyyy) tuple."""
    dob = date_of_birth.split("/")
    return int(dob[0]), int(dob[1]), int(dob[2])  # return a tuple


def convert_tuple_to_date(date_tuple):
    """Convert (dd, mm, yyyy) tuple to dd/mm/yyyy string."""
    return date_tuple[0] + "/" + date_tuple[1] + "/" + date_tuple[2]


def convert_to_dictionary(names, dates_of_birth):
    """Return a dictionary created from 2 parallel lists."""
    return dict(zip(names, dates_of_birth))


if __name__ == '__main__':
    main()
