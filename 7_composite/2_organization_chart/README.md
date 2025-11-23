# Composite Pattern - Example 2: Organization Chart

## Problem Description

An organization has employees and departments. Departments can contain employees and sub-departments. We need to calculate total salary, get employee count, and display the hierarchy uniformly. The Composite pattern allows treating individual employees and departments the same way.

**Real-world usage**: Used in organizational management systems, HR software, project management tools, and hierarchical data structures.

## Class Diagram

```
                    ┌─────────────────────┐
                    │   OrganizationUnit  │
                    │  (Component)        │
                    ├─────────────────────┤
                    │ + getName()         │
                    │ + getSalary()       │
                    │ + getEmployeeCount()│
                    │ + display()         │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │                              │
    ┌───────────▼──────┐          ┌───────────▼──────────┐
    │     Employee     │          │     Department      │
    │  (Leaf)          │          │  (Composite)         │
    ├──────────────────┤          ├──────────────────────┤
    │ - name           │          │ - name               │
    │ - position       │          │ - members[]          │
    │ - salary         │          │ + getName()          │
    │ + getName()      │          │ + getSalary()       │
    │ + getSalary()    │          │ + getSalary()        │
    │ + display()      │          │ + display()          │
    └──────────────────┘          │ + add(member)        │
                                  │ + remove(member)     │
                                  └──────────────────────┘
```

