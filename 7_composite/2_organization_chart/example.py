"""
Composite Pattern - Organization Chart Example
Real-world usage: HR systems, organizational management, project management
"""

from abc import ABC, abstractmethod
from typing import List


class OrganizationUnit(ABC):
    """Component interface"""
    
    @abstractmethod
    def get_name(self) -> str:
        """Get unit name"""
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        """Get total salary"""
        pass
    
    @abstractmethod
    def get_employee_count(self) -> int:
        """Get employee count"""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display organization structure"""
        pass


class Employee(OrganizationUnit):
    """Leaf class - represents an employee"""
    
    def __init__(self, name: str, position: str, salary: float):
        self._name = name
        self._position = position
        self._salary = salary
    
    def get_name(self) -> str:
        return self._name
    
    def get_salary(self) -> float:
        return self._salary
    
    def get_employee_count(self) -> int:
        return 1
    
    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix}👤 {self._name} - {self._position} (${self._salary:,.0f})"


class Department(OrganizationUnit):
    """Composite class - represents a department"""
    
    def __init__(self, name: str):
        self._name = name
        self._members: List[OrganizationUnit] = []
    
    def get_name(self) -> str:
        return self._name
    
    def get_salary(self) -> float:
        """Calculate total salary of department and all members"""
        total = 0.0
        for member in self._members:
            total += member.get_salary()
        return total
    
    def get_employee_count(self) -> int:
        """Calculate total employee count"""
        total = 0
        for member in self._members:
            total += member.get_employee_count()
        return total
    
    def add(self, member: OrganizationUnit):
        """Add a member to the department"""
        self._members.append(member)
    
    def remove(self, member: OrganizationUnit):
        """Remove a member from the department"""
        if member in self._members:
            self._members.remove(member)
    
    def get_members(self) -> List[OrganizationUnit]:
        """Get all members"""
        return self._members
    
    def display(self, indent: int = 0) -> str:
        """Display department structure recursively"""
        prefix = "  " * indent
        total_salary = self.get_salary()
        employee_count = self.get_employee_count()
        result = [
            f"{prefix}🏢 {self._name} "
            f"({employee_count} employees, ${total_salary:,.0f} total salary)"
        ]
        for member in self._members:
            result.append(member.display(indent + 1))
        return "\n".join(result)


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Composite Pattern - Organization Chart Example")
    print("=" * 60)
    print()
    
    # Create organization structure
    company = Department("TechCorp Inc.")
    
    # Engineering Department
    engineering = Department("Engineering")
    engineering.add(Employee("Alice Johnson", "Engineering Manager", 120000))
    engineering.add(Employee("Bob Smith", "Senior Developer", 95000))
    engineering.add(Employee("Charlie Brown", "Developer", 75000))
    engineering.add(Employee("Diana Prince", "QA Engineer", 70000))
    
    # Sales Department
    sales = Department("Sales")
    sales.add(Employee("Eve Wilson", "Sales Manager", 110000))
    sales.add(Employee("Frank Miller", "Sales Representative", 60000))
    sales.add(Employee("Grace Lee", "Sales Representative", 58000))
    
    # Marketing Department
    marketing = Department("Marketing")
    marketing.add(Employee("Henry Davis", "Marketing Director", 130000))
    
    # Marketing has sub-departments
    digital_marketing = Department("Digital Marketing")
    digital_marketing.add(Employee("Ivy Chen", "SEO Specialist", 65000))
    digital_marketing.add(Employee("Jack Taylor", "Content Writer", 55000))
    
    social_media = Department("Social Media")
    social_media.add(Employee("Kate Anderson", "Social Media Manager", 70000))
    social_media.add(Employee("Liam O'Brien", "Graphic Designer", 60000))
    
    marketing.add(digital_marketing)
    marketing.add(social_media)
    
    # HR Department
    hr = Department("Human Resources")
    hr.add(Employee("Mia Rodriguez", "HR Manager", 100000))
    hr.add(Employee("Noah Kim", "Recruiter", 65000))
    
    # Add departments to company
    company.add(engineering)
    company.add(sales)
    company.add(marketing)
    company.add(hr)
    company.add(Employee("Oliver White", "CEO", 250000))
    
    # Display organization
    print("Organization Chart:")
    print("-" * 60)
    print(company.display())
    print()
    
    # Statistics
    print("Organization Statistics:")
    print("-" * 60)
    print(f"Total Employees: {company.get_employee_count()}")
    print(f"Total Payroll: ${company.get_salary():,.0f}")
    print()
    
    print("Department Breakdown:")
    print("-" * 60)
    departments = [engineering, sales, marketing, hr]
    for dept in departments:
        print(f"{dept.get_name()}:")
        print(f"  Employees: {dept.get_employee_count()}")
        print(f"  Total Salary: ${dept.get_salary():,.0f}")
        print(f"  Average Salary: ${dept.get_salary() / dept.get_employee_count():,.0f}")
    print()
    
    # Demonstrate uniform interface
    print("Uniform Interface Demo:")
    print("-" * 60)
    units = [
        company,
        engineering,
        Employee("Test Employee", "Tester", 50000)
    ]
    for unit in units:
        print(f"{unit.get_name()}: {unit.get_employee_count()} employees, "
              f"${unit.get_salary():,.0f} salary")
    print()
    
    print("=" * 60)
    print("Key Benefit: Can treat employees and departments uniformly!")
    print("Operations work the same way on both individual employees and departments!")
    print("=" * 60)

