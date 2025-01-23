from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, List, Dict

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

    def remove_members(self, member_name: str):
        index = 0
        while index < len(self._members):
            if self._members[index].member_name == member_name:
                del self._members[index]
            else:
                index += 1

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

    def get_top_five_members(self):
        if len(self._members) <= 5:
            return self._members

        top_members = []
        for member in self._members:
            if len(top_members) < 5:
                top_members.append(member)
            else:
                # Find the minimum income in top_members
                min_income_member = top_members[0]
                for top_member in top_members:
                    if top_member.income < min_income_member.income:
                        min_income_member = top_member
                # Replace the lowest income member if current has higher income
                if member.income > min_income_member.income:
                    top_members.remove(min_income_member)
                    top_members.append(member)
        return top_members

    def get_member(self, member_id: int):
        for member in self._members:
            if member.member_id == member_id:
                return member
        return None

    def __str__(self):
        # result = "Organization Details:\n"
        result = "Organization Name: {}\n".format(self._organization_name)
        result += "Members:\n"
        if not self._members:
            result += "  No members added yet.\n"
        else:
            for member in self._members:
                result += "  - {}\n".format(str(member).replace("\n", "\n    "))

        return result

    def display(self):
        print(self.__str__())


class OrganizationType(Enum):
    CHARITABLE_ORG = "Charitable Organization"
    LABOR_ORG = "Labor Organization"
    BUSINESS_ORG = "Business Organization"

class NonProfitOrganization(Organization):  
    def __init__(self, organization_name: str, category: OrganizationType):
        super().__init__(organization_name)
        self._category = category
        self._conference_rooms = []
    
    def category(self):
        return self._category
    
    def add_conference_room(self, conference_room: ConferenceRoom):
        self._conference_rooms.append(conference_room)

    def find_largest_conference_room(self):
        if not self._conference_rooms:
            return None

        largest_room = self._conference_rooms[0]
        for room in self._conference_rooms:
            if room.area > largest_room.area:
                largest_room = room
        return largest_room
    
    def get_conference_room_by_type(self, room_type: ConferenceType):
        rooms = []
        for room in self._conference_rooms:
            if room.type == room_type:
                rooms.append(room)
        return rooms
    
    def assign_member_to_conference_room(self, member: Member, room_name: str):
        member = self.get_member(member.member_id)
        if not member:
            print("Member not found.")
            return False
        
        for room in self._conference_rooms:
            if room.conference_room_name == room_name:
                room.add_member(member)
                return True
        print("Conference room not found.")
            
        return False

    def find_members_no_conference_rooms(self) -> List[Member]:
        # assigned_members = set()
        # for room in self._conference_rooms:
        #     for member in room._members:
        #         assigned_members.add(member)

        unassigned_members = []
        for member in self._members:
            if member not in assigned_members:
                unassigned_members.append(member)

        return unassigned_members



def main():
    member1 = Member(member_id=1112, member_name="Ahmad Raza", income=273000)
    member2 = Member(member_id=1022, member_name="Umair Dada", income=195000)
    member3 = Member(member_id=1234, member_name="Ali Raza", income=120000)
    member4 = Member(member_id=1324, member_name="Ayaan Khan", income=112000)
    member5 = Member(member_id=1424, member_name="Zain Khan", income=100000)
    member6 = Member(member_id=1723, member_name="Mustafa Aqib", income=333000)
    member7 = Member(member_id=1953, member_name="Ahsan Ali", income=123000)
    member8 = Member(member_id=1230, member_name="Danish Goheer", income=120000)
    member9 = Member(member_id=1235, member_name="Arif Soda", income=132000)
    member10 = Member(member_id=1392, member_name="Ahsan Khan", income=112000)
    

    organization = Organization(organization_name="TalkTheTech")
    organization.add_member(member1)
    organization.add_member(member2)
    organization.add_member(member3)
    organization.add_member(member4)
    organization.add_member(member5)
    organization.add_member(member6)
    organization.add_member(member7)
    organization.add_member(member8)
    organization.add_member(member9)
    organization.add_member(member10)

    organization = NonProfitOrganization(organization_name="DalmaDere", category=OrganizationType.CHARITABLE_ORG)

    conference_room = ConferenceRoom(conference_room_name="GITEX Arena", area=200.75, seats=150000, room_type=ConferenceType.TRADE_SHOW)
    conference_room1 = ConferenceRoom(conference_room_name="Gatsby Space", area=200.75, seats=150000, room_type=ConferenceType.TRADE_SHOW)
    conference_room.add_member(member1)
    conference_room.add_member(member2)
    conference_room.add_member(member3)
    conference_room1.add_member(member4)
    conference_room1.add_member(member5)
    conference_room1.add_member(member6)
    

    print("Organization Details:")
    organization.display()

    print("\nTop 5 members by income in the organization:")
    top_members = organization.get_top_five_members()
    for member in top_members:
        print(member)

    print("\nGet member with ID 1022:")
    member = organization.get_member(1022)
    if member:
        print(member)
    else:
        print("Member not found.")

    print("\nGet member with ID 1130:")
    member = organization.get_member(1130)
    if member:
        print(member)
    else:
        print("Member not found.")

    print("\n\n --- Conference Room ---")

    print("\n\nConference Room before removal:")
    conference_room.display()

    print("\nRemoving member Ali Raza from Conference Room")
    conference_room.remove_members("Ali Raza")

    print("\nConference Room after removal:")
    conference_room.display()


    print("\n\n --- Non Profit Organization ---")

    largest_room = organization.find_largest_conference_room()
    print(f"\nLargest Conference Room: {largest_room}")

    rooms_by_type = organization.get_conference_room_by_type()

    print("\nConference Rooms by type:")
    for room in rooms_by_type:
        print(room.conference_room_name)

    organization.assign_member_to_conference_room(1022, ConferenceType.SEMINAR)

    unassigned_members = organization.find_members_no_conference_rooms()
    print("Members not assigned to any conference rooms:")
    for member in unassigned_members:
        print(f"  - {member.member_name}")



if __name__ == "__main__":
    main()