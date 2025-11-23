# State Pattern - Example 1: Vending Machine

## Problem Description

A vending machine has different states (NoMoney, HasMoney, Sold, SoldOut) and behaves differently in each state. Using if-else statements for state management becomes complex and error-prone. The State pattern encapsulates state-specific behavior in separate classes.

**Real-world usage**: Used in game development (character states), workflow engines, order processing systems, TCP connection states, and UI state management (React, Vue).

## Class Diagram

```
                    ┌─────────────────────┐
                    │    VendingState     │
                    │  (State Interface)  │
                    ├─────────────────────┤
                    │ + insertMoney()     │
                    │ + ejectMoney()      │
                    │ + selectProduct()   │
                    │ + dispense()        │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │  NoMoneyState    │ │HasMoneyState│ │SoldState   │
    ├──────────────────┤ ├────────────┤ ├────────────┤
    │ + insertMoney()  │ │ + select() │ │ + dispense()│
    │ + ejectMoney()   │ │ + eject()  │ └────────────┘
    │ + selectProduct()│ └────────────┘
    └──────────────────┘
                │
    ┌───────────▼──────────┐
    │  VendingMachine      │
    ├──────────────────────┤
    │ - currentState       │
    │ - products           │
    │ + insertMoney()      │
    │ + ejectMoney()       │
    │ + selectProduct()    │
    │ + setState()         │
    └──────────────────────┘
```

