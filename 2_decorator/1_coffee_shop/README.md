# Decorator Pattern - Example 1: Coffee Shop

## Problem Description

A coffee shop application needs to allow customers to customize their coffee with various add-ons (milk, sugar, whipped cream, caramel). Instead of creating a class for every possible combination (which would be exponential), the Decorator pattern allows us to dynamically add features to a base coffee.

**Real-world usage**: Used in GUI frameworks (adding borders, scrollbars to components), I/O streams (Java, Python), middleware in web frameworks (Express.js, Django), and text formatting systems.

## Class Diagram

```
                    ┌─────────────────────┐
                    │    Beverage         │
                    │  (Component)        │
                    ├─────────────────────┤
                    │ + getDescription()  │
                    │ + getCost()         │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │                              │
    ┌───────────▼──────┐          ┌───────────▼──────────┐
    │   Espresso       │          │  BeverageDecorator   │
    │  (Concrete)      │          │   (Decorator)        │
    ├──────────────────┤          ├──────────────────────┤
    │ + getDescription()│          │ - beverage          │
    │ + getCost()      │          │ + getDescription()   │
    └──────────────────┘          │ + getCost()          │
                                   └──────────┬───────────┘
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                         │                         │
        ┌───────────▼──────┐    ┌─────────────▼──────┐    ┌─────────────▼──────┐
        │  MilkDecorator   │    │ SugarDecorator     │    │ WhipDecorator      │
        ├──────────────────┤    ├────────────────────┤    ├────────────────────┤
        │ + getDescription()│    │ + getDescription() │    │ + getDescription() │
        │ + getCost()      │    │ + getCost()        │    │ + getCost()        │
        └──────────────────┘    └────────────────────┘    └────────────────────┘
```

