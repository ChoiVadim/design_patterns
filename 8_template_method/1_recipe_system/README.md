# Template Method Pattern - Example 1: Recipe System

## Problem Description

Different recipes (Coffee, Tea, Soup) follow similar steps but with variations. The Template Method pattern defines the skeleton of an algorithm in a base class, allowing subclasses to override specific steps while keeping the overall structure.

**Real-world usage**: Used in frameworks (Django, Spring), build systems (Maven, Gradle), data processing pipelines, and algorithm frameworks.

## Class Diagram

```
                    ┌─────────────────────┐
                    │   Recipe            │
                    │  (Abstract Class)  │
                    ├─────────────────────┤
                    │ + prepareRecipe()   │
                    │ # boilWater()       │
                    │ # brew()            │
                    │ # pourInCup()       │
                    │ # addCondiments()   │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │  CoffeeRecipe   │ │  TeaRecipe │ │  SoupRecipe│
    ├──────────────────┤ ├────────────┤ ├────────────┤
    │ # brew()         │ │ # brew()   │ │ # brew()   │
    │ # addCondiments()│ │ # addCondiments()│ │ # addCondiments()│
    └──────────────────┘ └────────────┘ └────────────┘
```

