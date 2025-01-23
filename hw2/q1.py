class Education:
    def __init__(self, level, school, period_from, period_to, degree):
        self.__level = level
        self.__school = school
        self.__period_from = period_from
        self.__period_to = period_to
        self.__degree = degree

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def get_school(self):
        return self.__school

    def set_school(self, school):
        self.__school = school

    def get_period_from(self):
        return self.__period_from

    def set_period_from(self, period_from):
        self.__period_from = period_from

    def get_period_to(self):
        return self.__period_to

    def set_period_to(self, period_to):
        self.__period_to = period_to

    def get_degree(self):
        return self.__degree

    def set_degree(self, degree):
        self.__degree = degree


class WorkExperience:
    def __init__(self, company, location, period_from, period_to, position, reason_for_leaving):
        self.__company = company
        self.__location = location
        self.__period_from = period_from
        self.__period_to = period_to
        self.__position = position
        self.__reason_for_leaving = reason_for_leaving

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_period_from(self):
        return self.__period_from

    def set_period_from(self, period_from):
        self.__period_from = period_from

    def get_period_to(self):
        return self.__period_to

    def set_period_to(self, period_to):
        self.__period_to = period_to

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_reason_for_leaving(self):
        return self.__reason_for_leaving

    def set_reason_for_leaving(self, reason_for_leaving):
        self.__reason_for_leaving = reason_for_leaving


class EmergencyContact:
    def __init__(self, name, relationship, contact_number):
        self.__name = name
        self.__relationship = relationship
        self.__contact_number = contact_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_relationship(self):
        return self.__relationship

    def set_relationship(self, relationship):
        self.__relationship = relationship

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number


class Applicant:
    auto_increment_id = 1  # Class variable for applicant ID

    def __init__(self, name, dob, position, address, home_phone, mobile_phone, email, place_of_birth, citizenship):
        self.__id = Applicant.auto_increment_id
        Applicant.auto_increment_id += 1  # Increment the ID for the next applicant
        self.__name = name
        self.__dob = dob
        self.__position = position
        self.__address = address
        self.__home_phone = home_phone
        self.__mobile_phone = mobile_phone
        self.__email = email
        self.__place_of_birth = place_of_birth
        self.__citizenship = citizenship
        self.__primary_contact = None
        self.__secondary_contact = None
        self.__education = []
        self.__work_experience = []
        self.__major_skills = None

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_emergency_contacts(self, primary, secondary):
        self.__primary_contact = primary
        self.__secondary_contact = secondary

    def add_education(self, education):
        self.__education.append(education)

    def add_work_experience(self, experience):
        self.__work_experience.append(experience)

    def set_major_skills(self, skills):
        self.__major_skills = skills

    def get_major_skills(self):
        return self.__major_skills

    def display_info(self):
        print("\n" + "-" * 50)
        print(f"Applicant ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Date of Birth: {self.__dob}")
        print(f"Position Applying: {self.__position}")
        print(f"Address: {self.__address}")
        print(f"Telephone (Home): {self.__home_phone} | Mobile: {self.__mobile_phone}")
        print(f"Email Address: {self.__email}")
        print(f"Place of Birth: {self.__place_of_birth}")
        print(f"Citizenship: {self.__citizenship}")

        print("\nIn Case of Accident:")
        if self.__primary_contact:
            print(f"  Primary Contact: {self.__primary_contact.get_name()}")
            print(f"    Relationship: {self.__primary_contact.get_relationship()}")
            print(f"    Contact: {self.__primary_contact.get_contact_number()}")
        if self.__secondary_contact:
            print(f"  Secondary Contact: {self.__secondary_contact.get_name()}")
            print(f"    Relationship: {self.__secondary_contact.get_relationship()}")
            print(f"    Contact: {self.__secondary_contact.get_contact_number()}")

        print("\nEducation:")
        for edu in self.__education:
            print(f"  - {edu.get_level()} at {edu.get_school()} ({edu.get_period_from()} - {edu.get_period_to()}), Degree: {edu.get_degree()}")

        print("\nWork Experience:")
        for exp in self.__work_experience:
            print(f"  - {exp.get_company()} in {exp.get_location()} ({exp.get_period_from()} - {exp.get_period_to()})")
            print(f"    Position: {exp.get_position()}, Reason for Leaving: {exp.get_reason_for_leaving()}")

        print(f"\nMajor Skills: {self.__major_skills}")
        print("-" * 50)


class Institution:
    def __init__(self):
        self.__applicants = []

    def add_applicant(self, applicant):
        self.__applicants.append(applicant)

    def search_applicants(self, keyword):
        print(f"\nSearch Results for '{keyword}':")
        found = False
        for applicant in self.__applicants:
            if (keyword.lower() in applicant.get_name().lower() or
                    keyword.lower() in applicant.get_major_skills().lower()):
                applicant.display_info()
                found = True
        if not found:
            print("No matching applicants found.")

    def update_applicant(self, name):
        for applicant in self.__applicants:
            if applicant.get_name().lower() == name.lower():
                new_name = input("Enter new name (or press Enter to skip): ")
                if new_name:
                    applicant.set_name(new_name)
                print("Applicant updated successfully.")
                return
        print("Applicant not found.")

    def delete_applicant(self, name):
        for i, applicant in enumerate(self.__applicants):
            if applicant.get_name().lower() == name.lower():
                del self.__applicants[i]
                print("Applicant deleted successfully.")
                return
        print("Applicant not found.")

    def display_applicants(self):
        if not self.__applicants:
            print("No applicants available.")
        else:
            for applicant in self.__applicants:
                applicant.display_info()


def is_valid_dob(dob_str):
    try:
        month, day, year = map(int, dob_str.split('/'))
        return 1 <= month <= 12 and 1 <= day <= 31 and year >= 1900  # Basic date validation
    except ValueError:
        return False


def is_valid_year(year_str):
    try:
        year = int(year_str)
        return year >= 1900  # Accept years 1900 and onwards
    except ValueError:
        return False


def is_valid_month_year(month_year_str):
    try:
        month, year = map(int, month_year_str.split('/'))
        return 1 <= month <= 12 and year >= 1900  # Basic month/year validation
    except ValueError:
        return False


def is_valid_phone(phone_str):
    return phone_str.isdigit() and (len(phone_str) == 10 or len(phone_str) == 7)  # Accepts 7-digit or 10-digit numbers


def main():
    institution = Institution()

    while True:
        print("\nMenu:")
        print("1. Add New Job Application")
        print("2. Search Applications")
        print("3. Update Application")
        print("4. Delete Application")
        print("5. Display All Applications")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Name (Lastname, Firstname, MI): ")
            dob = input("Enter Date of Birth (MM/DD/YYYY): ")

            while not is_valid_dob(dob):
                print("Invalid date format. Please enter a valid date (MM/DD/YYYY).")
                dob = input("Enter Date of Birth (MM/DD/YYYY): ")

            position = input("Enter Position Applying For: ")
            address = input("Enter Address: ")
            home_phone = input("Enter Home Phone Number: ")

            while not is_valid_phone(home_phone):
                print("Invalid phone number. Please enter a 7 or 10 digit phone number.")
                home_phone = input("Enter Home Phone Number: ")

            mobile_phone = input("Enter Mobile Phone: ")

            while not is_valid_phone(mobile_phone):
                print("Invalid phone number. Please enter a 7 or 10 digit phone number.")
                mobile_phone = input("Enter Mobile Phone: ")

            email = input("Enter Email Address: ")
            place_of_birth = input("Enter Place of Birth: ")
            citizenship = input("Enter Citizenship: ")

            applicant = Applicant(name, dob, position, address, home_phone, mobile_phone, email, place_of_birth, citizenship)

            primary_name = input("Enter Primary Emergency Contact Name: ")
            primary_relationship = input("Enter Primary Emergency Contact Relationship: ")
            primary_contact_number = input("Enter Primary Emergency Contact Number: ")

            while not is_valid_phone(primary_contact_number):
                print("Invalid phone number. Please enter a 7 or 10 digit phone number.")
                primary_contact_number = input("Enter Primary Emergency Contact Number: ")

            primary_contact = EmergencyContact(primary_name, primary_relationship, primary_contact_number)

            secondary_name = input("Enter Secondary Emergency Contact Name: ")
            secondary_relationship = input("Enter Secondary Emergency Contact Relationship: ")
            secondary_contact_number = input("Enter Secondary Emergency Contact Number: ")

            while not is_valid_phone(secondary_contact_number):
                print("Invalid phone number. Please enter a 7 or 10 digit phone number.")
                secondary_contact_number = input("Enter Secondary Emergency Contact Number: ")

            secondary_contact = EmergencyContact(secondary_name, secondary_relationship, secondary_contact_number)

            applicant.set_emergency_contacts(primary_contact, secondary_contact)

            while True:
                add_education = input("Do you want to add education information? (y/n): ")
                if add_education.lower() == 'y':
                    level = input("Enter Education Level: ")
                    school = input("Enter School Name: ")
                    period_from = input("Enter Period From (YYYY): ")

                    while not is_valid_year(period_from):
                        print("Invalid year format. Please enter a valid year (YYYY).")
                        period_from = input("Enter Period From (YYYY): ")

                    period_to = input("Enter Period To (YYYY): ")

                    while not is_valid_year(period_to):
                        print("Invalid year format. Please enter a valid year (YYYY).")
                        period_to = input("Enter Period To (YYYY): ")

                    degree = input("Enter Degree: ")
                    education = Education(level, school, period_from, period_to, degree)
                    applicant.add_education(education)
                else:
                    break

            while True:
                add_experience = input("Do you want to add work experience? (y/n): ")
                if add_experience.lower() == 'y':
                    company = input("Enter Company Name: ")
                    location = input("Enter Company Location: ")
                    period_from = input("Enter Period From (MM/YYYY): ")

                    while not is_valid_month_year(period_from):
                        print("Invalid month/year format. Please enter a valid period (MM/YYYY).")
                        period_from = input("Enter Period From (MM/YYYY): ")

                    period_to = input("Enter Period To (MM/YYYY): ")

                    while not is_valid_month_year(period_to):
                        print("Invalid month/year format. Please enter a valid period (MM/YYYY).")
                        period_to = input("Enter Period To (MM/YYYY): ")

                    position = input("Enter Position: ")
                    reason_for_leaving = input("Enter Reason for Leaving: ")
                    experience = WorkExperience(company, location, period_from, period_to, position, reason_for_leaving)
                    applicant.add_work_experience(experience)
                else:
                    break

            major_skills = input("Enter Major Skills: ")
            applicant.set_major_skills(major_skills)

            institution.add_applicant(applicant)

        elif choice == "2":
            keyword = input("Enter name or skills to search for: ")
            institution.search_applicants(keyword)

        elif choice == "3":
            name = input("Enter the name of the applicant to update: ")
            institution.update_applicant(name)

        elif choice == "4":
            name = input("Enter the name of the applicant to delete: ")
            institution.delete_applicant(name)

        elif choice == "5":
            institution.display_applicants()

        elif choice == "6":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")


if __name__ == "__main__":
    main()
