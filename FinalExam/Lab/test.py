from state_machine import State, Event, acts_as_state_machine, before, after

@acts_as_state_machine
class HouseBuyingProcess:
    # States
    browsing = State(initial=True)
    selected = State()
    viewing = State()
    offer = State()
    counter_offer = State()
    offer_accepted = State()
    pre_approval = State()
    approved = State()
    disapproved = State()
    inspection = State()
    closing = State()
    get_keys = State()
    offer_rejected = State()

    # Events
    browse = Event(from_states=browsing, to_state=selected)
    schedule_viewing = Event(from_states=selected, to_state=viewing)
    finish_viewing = Event(from_states=viewing, to_state=offer)
    make_offer = Event(from_states=offer, to_state=counter_offer)
    accept_offer = Event(from_states=counter_offer, to_state=offer_accepted)
    apply_preapproval = Event(from_states=offer_accepted, to_state=pre_approval)
    approve_loan = Event(from_states=pre_approval, to_state=approved)
    disapprove_loan = Event(from_states=pre_approval, to_state=disapproved)
    inspect_house = Event(from_states=approved, to_state=inspection)
    sign_closing_docs = Event(from_states=inspection, to_state=closing)
    receive_keys = Event(from_states=closing, to_state=get_keys)
    reject_offer = Event(from_states=offer, to_state=offer_rejected)
    reset = Event(from_states=[disapproved, offer_rejected], to_state=browsing)

    @before('browse')
    def before_browse(self):
        print("Getting house details...")

    @after('browse')
    def after_browse(self):
        print("House selected.")

    @before('schedule_viewing')
    def before_schedule_viewing(self):
        print("Scheduling house viewing...")

    @after('schedule_viewing')
    def after_schedule_viewing(self):
        print("House viewing scheduled.")

    @before('finish_viewing')
    def before_finish_viewing(self):
        print("Finishing house viewing...")

    @after('finish_viewing')
    def after_finish_viewing(self):
        print("House viewing finished.")

    @before('make_offer')
    def before_make_offer(self):
        print("Making an offer...")

    @after('make_offer')
    def after_make_offer(self):
        print("Offer made.")

    @before('accept_offer')
    def before_accept_offer(self):
        print("Accepting counter offer...")

    @after('accept_offer')
    def after_accept_offer(self):
        print("Counter offer accepted.")

    @before('apply_preapproval')
    def before_apply_preapproval(self):
        print("Applying for pre-approval...")

    @after('apply_preapproval')
    def after_apply_preapproval(self):
        print("Pre-approval applied.")

    @before('approve_loan')
    def before_approve_loan(self):
        print("Approving loan application...")

    @after('approve_loan')
    def after_approve_loan(self):
        print("Loan approved.")

    @before('disapprove_loan')
    def before_disapprove_loan(self):
        print("Disapproving loan application...")

    @after('disapprove_loan')
    def after_disapprove_loan(self):
        print("Loan disapproved.")

    @before('inspect_house')
    def before_inspect_house(self):
        print("Inspecting house...")

    @after('inspect_house')
    def after_inspect_house(self):
        print("House inspected.")

    @before('sign_closing_docs')
    def before_sign_closing_docs(self):
        print("Signing closing documents...")

    @after('sign_closing_docs')
    def after_sign_closing_docs(self):
        print("Closing documents signed.")

    @before('receive_keys')
    def before_receive_keys(self):
        print("Receiving house keys...")

    @after('receive_keys')
    def after_receive_keys(self):
        print("House keys received.")

    @before('reject_offer')
    def before_reject_offer(self):
        print("Rejecting offer...")

    @after('reject_offer')
    def after_reject_offer(self):
        print("Offer rejected.")

    @before('reset')
    def before_reset(self):
        print("Resetting the process...")

    @after('reset')
    def after_reset(self):
        print("Process reset to browsing stage.")

class RealEstate:
    def __init__(self):
        self.process = HouseBuyingProcess()

    def handle_action(self, action):
        try:
            if action == '1':
                self.process.browse()
            elif action == '2':
                self.process.schedule_viewing()
            elif action == '3':
                self.process.finish_viewing()
            elif action == '4':
                self.process.make_offer()
            elif action == '5':
                self.process.accept_offer()
            elif action == '6':
                self.process.apply_preapproval()
            elif action == '7':
                self.process.approve_loan()
            elif action == '8':
                self.process.disapprove_loan()
            elif action == '9':
                self.process.inspect_house()
            elif action == '10':
                self.process.sign_closing_docs()
            elif action == '11':
                self.process.receive_keys()
            elif action == '12':
                self.process.reject_offer()
            elif action == '13':
                if self.process.current_state in [self.process.disapproved, self.process.offer_rejected]:
                    self.process.reset()
                else:
                    print("Reset option is only available after loan disapproval or offer rejection.")
            else:
                print("Invalid option.")
            print(f"Current state: {self.process.current_state}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    real_estate = RealEstate()
    while True:
        menu = """
        1. Select House
        2. Schedule Viewing
        3. Finish Viewing
        4. Make Offer
        5. Accept Counter Offer
        6. Apply for Pre-Approval
        7. Approve Loan
        8. Disapprove Loan
        9. Inspect House
        10. Sign Closing Documents
        11. Receive House Keys
        12. Reject Offer
        13. Reset Process
        14. Exit
        """
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == '14':
            print("Exiting the house buying process.")
            break
        real_estate.handle_action(choice)

if __name__ == "__main__":
    main()
