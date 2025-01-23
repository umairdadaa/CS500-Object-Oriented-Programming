from abc import ABC, abstractmethod
from enum import Enum

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class ConferenceType(Enum):
    WEBINAR = "Webinar"
    SEMINAR = "Seminar"
    WORKSHOP = "Workshop"
    TRADE_SHOW = "Trade Show"

class Member(Displayable):
    def __init__(self, member_id: int, member_name: str, income: float):
        self._member_id = member_id
        self._member_name = member_name
        self._income = income

    @property
    def member_id(self):
        return self._member_id

    @property
    def member_name(self):
        return self._member_name

    @property
    def income(self):
        return self._income

    def __str__(self):
        return "Member ID: {}\nMember Name: {}\nIncome: ${:.2f}".format(self._member_id, self._member_name, self._income)

    def display(self):
        print(self.__str__())

class ConferenceRoom(Displayable):
    def __init__(self, conference_room_name: str, area: float, seats: int, room_type: ConferenceType):
        self._conference_room_name = conference_room_name
        self._area = area
        self._seats = seats
        self._type = room_type
        self._members = []

    @property
    def conference_room_name(self):
        return self._conference_room_name

    @property
    def area(self):
        return self._area

    @property
    def seats(self):
        return self._seats

    @property
    def type(self):
        return self._type

    def add_member(self, member: Member):
        self._members.append(member)

    def __str__(self):
        result = "Conference Room Details:\n"
        result += "Room Name: {}\nArea: {} sq meters\nSeats: {}\nType: {}\n".format(
            self._conference_room_name, self._area, self._seats, self._type.value)
        result += "Members:\n"
        if not self._members:
            result += "  No members added yet.\n"
        else:
            for member in self._members:
                result += "  - {}\n".format(str(member).replace("\n", "\n    "))

        return result

    def display(self):
        print(self.__str__())

class Organization(Displayable):
    def __init__(self, organization_name: str):
        self._organization_name = organization_name
        self._members = []

    @property
    def organization_name(self):
        return self._organization_name

    def add_member(self, member: Member):
        self._members.append(member)

    def __str__(self):
        result = "Organization Details:\n"
        result += "Organization Name: {}\n".format(self._organization_name)
        result += "Members:\n"
        if not self._members:
            result += "  No members added yet.\n"
        else:
            for member in self._members:
                result += "  - {}\n".format(str(member).replace("\n", "\n    "))

        return result

    def display(self):
        print(self.__str__())

def main():
    member1 = Member(member_id=112, member_name="Ahmad Raza", income=173000)
    member2 = Member(member_id=1022, member_name="Umair Dada", income=95000)

    organization = Organization(organization_name="TalkTheTech")
    organization.add_member(member1)
    organization.add_member(member2)

    conference_room = ConferenceRoom(conference_room_name="GITEX Arena", area=200.75, seats=150000, room_type=ConferenceType.TRADE_SHOW)
    conference_room.add_member(member1)
    conference_room.add_member(member2)

    organization.display()
    conference_room.display()

if __name__ == "__main__":
    main()