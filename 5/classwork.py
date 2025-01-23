# Base class: Person
class Person:
    def __init__(self, name: str = None):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
    
    def display(self):
        print(f"name = {self._name}")
    
    def dowork(self):
        print(f"{self._name} is working.")

# Derived class: Programmer, inheriting from Person
class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float):
        self._name = name
        self._skills = skills
        self._salary = salary
    
    @property
    def skills(self):
        return self._skills
    
    @skills.setter
    def skills(self, value: str):
        self._skills = value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value: float):
        self._salary = value
    
    def display(self):
        print(f"name = {self._name}")
        print(f"skills = {self._skills}")
        print(f"salary = {self._salary}")
    
    def dowork(self):
        print(f"Programmer {self._name} is writing a program.")
    
    def get_annual_income(self):
        # Explicit multiplication for annual income (avoiding sum)
        total_income = 0
        for _ in range(12):
            total_income += self._salary
        return total_income

# Derived class: Manager, inheriting from Programmer
class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float):
        self._name = name
        self._skills = skills
        self._salary = salary
        self._bonus = bonus
    
    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self, value: float):
        self._bonus = value
    
    def display(self):
        print(f"name = {self._name}")
        print(f"skills = {self._skills}")
        print(f"salary = {self._salary}")
        print(f"bonus = {self._bonus}")
    
    def dowork(self):
        print(f"Manager {self._name} is supervising a team of programmers.")
    
    def get_annual_income(self):
        # Explicit addition of bonus and monthly salary
        total_income = 0
        for _ in range(12):
            total_income += self._salary
        return total_income + self._bonus

# Class: Project
class Project:
    def __init__(self, projname: str, budget: float, active: bool):
        self._projname = projname
        self._budget = budget
        self._active = active
    
    @property
    def projname(self):
        return self._projname
    
    @projname.setter
    def projname(self, value: str):
        self._projname = value
    
    @property
    def budget(self):
        return self._budget
    
    @budget.setter
    def budget(self, value: float):
        self._budget = value
    
    @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, value: bool):
        self._active = value
    
    def display(self):
        print(f"projname = {self._projname}")
        print(f"budget = {self._budget}")
        print(f"active = {self._active}")

# Class: Group
class Group:
    def __init__(self, groupname: str):
        self._groupname = groupname
        self._members = []  # List of Programmer (or Manager) objects
    
    def add_member(self, member):
        self._members.append(member)
    
    def remove_member(self, name: str):
        new_members = []
        for member in self._members:
            if member.name != name:
                new_members.append(member)
        self._members = new_members
    
    def ask_anyone_dowork(self):
        for member in self._members:
            member.dowork()
    
    def ask_manager_dowork(self):
        for member in self._members:
            if isinstance(member, Manager):
                member.dowork()
    
    def get_allmembers_morethan(self, income: float):
        high_income_members = []
        for member in self._members:
            if member.get_annual_income() > income:
                high_income_members.append(member)
        return high_income_members
    
    def display(self):
        print(f"\nThe group has these members:")
        for member in self._members:
            member.display()

# Class: ITGroup, inheriting from Group
class ITGroup(Group):
    def __init__(self, groupname: str):
        self._groupname = groupname
        self._members = []  # List of Programmer (or Manager) objects
        self._projects = []  # List of Project objects
    
    def add_project(self, project: Project):
        self._projects.append(project)
    
    def find_largest_project(self):
        if len(self._projects) == 0:
            return None
        largest_project = self._projects[0]
        for project in self._projects:
            # Avoiding max function
            if project.budget > largest_project.budget:
                largest_project = project
        return largest_project
    
    def get_active_projects(self):
        active_projects = []
        for project in self._projects:
            if project.active:
                active_projects.append(project)
        return active_projects
    
    def display(self):
        print(f"\nThe group has these members:")
        for member in self._members:
            member.display()
        
        print(f"\nThe group has these projects:")
        for project in self._projects:
            project.display()


# Sample main() function to test the classes
def main() -> None:
    # Create Programmer and Manager objects
    p1 = Programmer("Lily", "C++, Java", 10000)
    p2 = Programmer("Judy", "Python, Java", 18000)
    m = Manager("Peter", "Management", 20000, 20000)

    # Create Project objects
    proj1 = Project("MAX-5", 200000, True)
    proj2 = Project("FOX-4", 100000, False)
    proj3 = Project("FOX-XP", 500000, True)

    # Create ITGroup and add members and projects
    itgrp = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)

    # Display group members and projects
    itgrp.display()

    # Test dowork method
    print("\nTesting dowork method:\n")
    itgrp.ask_anyone_dowork()

    # Ask manager to dowork
    print("\nTesting manager dowork method:\n")
    itgrp.ask_manager_dowork()

    # Get the largest project
    print("\nGet the largest project...")
    maxProj = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()

    # Get the active projects
    print("\nGet the active projects...")
    projects = itgrp.get_active_projects()
    for proj in projects:
        proj.display()

    # Display group members with high income
    print("\nGet the members with high income...")
    members = itgrp.get_allmembers_morethan(200000)
    for member in members:
        member.display()

if __name__ == "__main__":
    main()
