from state_machine import State, Event, acts_as_state_machine
import random

# DriverLicenseApplicationProcess Class
@acts_as_state_machine
class DriverLicenseApplicationProcess:
    ready = State(initial=True)
    information_entry = State()
    information_complete = State()
    browse_offices = State()
    knowledge_test = State()
    vision_test = State()
    driving_test = State()
    final_review = State()
    issued = State()
    application_denial = State()

    enter_information = Event(from_states=ready, to_state=information_entry)
    cancel_application = Event(from_states=ready, to_state=application_denial)
    submit_information = Event(from_states=information_entry, to_state=information_complete)
    missing_information = Event(from_states=information_entry, to_state=information_entry)
    select_dmv_office = Event(from_states=information_complete, to_state=browse_offices)
    schedule_knowledge_test = Event(from_states=browse_offices, to_state=knowledge_test)
    pass_knowledge_test = Event(from_states=knowledge_test, to_state=vision_test)
    fail_knowledge_test = Event(from_states=knowledge_test, to_state=application_denial)
    pass_vision_test = Event(from_states=vision_test, to_state=driving_test)
    fail_vision_test = Event(from_states=vision_test, to_state=application_denial)
    pass_driving_test = Event(from_states=driving_test, to_state=final_review)
    fail_driving_test = Event(from_states=driving_test, to_state=application_denial)
    approve_application = Event(from_states=final_review, to_state=issued)
    deny_application = Event(from_states=final_review, to_state=application_denial)

    def begin(self):
        print("Starting the Driver License Application Process.")

    def after(self):
        print("Exiting the current state.")

# DMV Class
class DMV:
    def __init__(self):
        self.__process = DriverLicenseApplicationProcess()
        self.__offices = ["Fremont", "Santa Clara", "SunnyVale", "San Jose", "San Francisco", "Hayward", "Oakland", "Milpitas"]
        self.__user_info = {
            "first_name": None,
            "last_name": None,
            "dob": None,
            "address": None
        }
        self.__information_complete = False
        self.__dmv_office_selected = False
        self.__knowledge_test_scheduled = False
        self.__knowledge_test_passed = False
        self.__vision_test_passed = False

    def reset_application(self):
        self.__process = DriverLicenseApplicationProcess()
        self.__user_info = {
            "first_name": None,
            "last_name": None,
            "dob": None,
            "address": None
        }
        self.__information_complete = False
        self.__dmv_office_selected = False
        self.__knowledge_test_scheduled = False
        self.__knowledge_test_passed = False
        self.__vision_test_passed = False
        print("Application has been reset.")

    def start_application(self):
        try:
            self.__process.enter_information()
            self.__user_info["first_name"] = input("Enter First Name: ") or None
            self.__user_info["last_name"] = input("Enter Last Name: ") or None
            self.__user_info["dob"] = input("Enter Date of Birth (YYYY-MM-DD): ") or None
            self.__user_info["address"] = input("Enter Address: ") or None
            
            self.__check_missing_information()
        except Exception:
            current_state = self.__process.current_state
            print(f"Cannot start the application: Invalid state transition. Current state: {current_state.name}")

    def __check_missing_information(self):
        missing_fields = [key for key, value in self.__user_info.items() if not value]
        if missing_fields:
            print(f"Missing fields: {', '.join(missing_fields)}")
            for field in missing_fields:
                self.__user_info[field] = input(f"Enter {field.replace('_', ' ').title()}: ") or None
            self.__check_missing_information()
        else:
            self.__information_complete = True
            print(f"Information Entered: {self.__user_info}")

    def cancel_application(self):
        try:
            self.__process.cancel_application()
            print("Application Denied: Canceled by User")
        except Exception:
            print("Cannot cancel the application: Invalid state transition.")

    def submit_information(self):
        if not self.__information_complete:
            print("Cannot submit incomplete information.")
        else:
            try:
                self.__process.submit_information()
                print("State: Information Complete")
            except Exception:
                print("Cannot submit information: Invalid state transition.")

    def select_office(self):
        if not self.__information_complete:
            print("Cannot select DMV office before completing information.")
        else:
            try:
                self.__process.select_dmv_office()
                print("Available DMV Offices:")
                for idx, office in enumerate(self.__offices, start=1):
                    print(f"{idx}. {office}")
                choice = input("Select an office by number: ")
                try:
                    selected_office = self.__offices[int(choice) - 1]
                    self.__dmv_office_selected = True
                    print(f"You selected: {selected_office}")
                except (IndexError, ValueError):
                    print("Invalid selection. Please try again.")
            except Exception:
                print("Cannot select office: Invalid state transition.")

    def schedule_test(self):
        if not self.__dmv_office_selected:
            print("Cannot schedule knowledge test without selecting a DMV office.")
        else:
            try:
                self.__process.schedule_knowledge_test()
                self.__knowledge_test_scheduled = True
                print("State: Knowledge Test")
            except Exception:
                print("Cannot schedule knowledge test: Invalid state transition.")

    def pass_knowledge_test(self):
        if not self.__knowledge_test_scheduled:
            print("Cannot pass knowledge test without scheduling it.")
        else:
            try:
                self.__process.pass_knowledge_test()
                self.__knowledge_test_passed = True
                print("State: Vision Test")
            except Exception:
                print("Cannot pass knowledge test: Invalid state transition.")

    def fail_knowledge_test(self):
        if not self.__knowledge_test_scheduled:
            print("Cannot fail knowledge test without scheduling it.")
        else:
            try:
                self.__process.fail_knowledge_test()
                print("State: Application Denial")
            except Exception:
                print("Cannot fail knowledge test: Invalid state transition.")

    def pass_vision_test(self):
        if not self.__knowledge_test_passed:
            print("Cannot pass vision test without passing knowledge test.")
        else:
            try:
                self.__process.pass_vision_test()
                self.__vision_test_passed = True
                print("State: Driving Test")
            except Exception:
                print("Cannot pass vision test: Invalid state transition.")

    def fail_vision_test(self):
        if not self.__knowledge_test_passed:
            print("Cannot fail vision test without passing knowledge test.")
        else:
            try:
                self.__process.fail_vision_test()
                self.__process.deny_application()
                print("Application Denied: Vision Test Failed")
            except Exception:
                print("Cannot fail vision test: Invalid state transition.")

    def simulate_driving_test(self):
        if not self.__vision_test_passed:
            print("Cannot simulate driving test without passing vision test.")
        else:
            try:
                if random.random() < 0.6:
                    self.__process.pass_driving_test()
                    print("Driving Test Passed")
                else:
                    self.__process.fail_driving_test()
                    print("Application Denied: Driving Test Failed")
            except Exception:
                print("Cannot simulate driving test: Invalid state transition.")

    def approve_application(self):
        if not self.__vision_test_passed:
            print("Cannot approve application without completing driving test.")
        else:
            try:
                self.__process.approve_application()
                print("Driver's License Issued")
            except Exception:
                print("Cannot approve application: Invalid state transition.")

    def deny_application(self):
        try:
            self.__process.deny_application()
            print("Application Denied")
        except Exception:
            print("Cannot deny application: Invalid state transition.")

# Main Function
def main():
    dmv = DMV()
    while True:
        print("\nMenu:")
        print("1. Start Application")
        print("2. Cancel Application")
        print("3. Submit Information")
        print("4. Select DMV Office")
        print("5. Schedule Knowledge Test")
        print("6. Pass Knowledge Test")
        print("7. Fail Knowledge Test")
        print("8. Pass Vision Test")
        print("9. Fail Vision Test")
        print("10. Simulate Driving Test")
        print("11. Approve Application")
        print("12. Deny Application")
        print("13. Reset Application")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dmv.start_application()
        elif choice == "2":
            dmv.cancel_application()
        elif choice == "3":
            dmv.submit_information()
        elif choice == "4":
            dmv.select_office()
        elif choice == "5":
            dmv.schedule_test()
        elif choice == "6":
            dmv.pass_knowledge_test()
        elif choice == "7":
            dmv.fail_knowledge_test()
        elif choice == "8":
            dmv.pass_vision_test()
        elif choice == "9":
            dmv.fail_vision_test()
        elif choice == "10":
            dmv.simulate_driving_test()
        elif choice == "11":
            dmv.approve_application()
        elif choice == "12":
            dmv.deny_application()
        elif choice == "13":
            dmv.reset_application()
        elif choice == "14":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
