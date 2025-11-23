# Factory Pattern - Example 1: UI Components

## Problem Description

A cross-platform application needs to create UI components (buttons, dialogs, menus) that look native on different operating systems (Windows, macOS, Linux). The Factory pattern encapsulates object creation logic and returns platform-specific implementations without the client knowing the concrete class.

**Real-world usage**: Used in GUI frameworks (Qt, Java Swing), game engines (Unity, Unreal), database connection pools, and dependency injection frameworks (Spring, Angular).

## Class Diagram

```
                    ┌─────────────────────┐
                    │  UIFactory          │
                    │  (Factory)          │
                    ├─────────────────────┤
                    │ + createButton()    │
                    │ + createDialog()    │
                    │ + createMenu()      │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │ WindowsFactory   │ │ MacOSFactory│ │ LinuxFactory│
    ├──────────────────┤ ├────────────┤ ├────────────┤
    │ + createButton() │ │ + create() │ │ + create() │
    │ + createDialog() │ │ + create() │ │ + create() │
    │ + createMenu()   │ │ + create() │ │ + create() │
    └──────────────────┘ └────────────┘ └────────────┘
                │              │              │
                └──────────────┼──────────────┘
                               │
                    ┌──────────▼──────────┐
                    │     Button         │
                    │  (Product)         │
                    ├────────────────────┤
                    │ + render()         │
                    │ + onClick()        │
                    └────────────────────┘
```

