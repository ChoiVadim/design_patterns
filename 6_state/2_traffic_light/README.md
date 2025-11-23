# State Pattern - Example 2: Traffic Light

## Problem Description

A traffic light system cycles through different states (Red, Yellow, Green) with specific behaviors and transitions. Each state has different durations and next states. The State pattern manages these transitions cleanly.

**Real-world usage**: Used in embedded systems, IoT devices, automation systems, workflow management, and state machines in general.

## Class Diagram

```
                    ┌─────────────────────┐
                    │   TrafficLightState  │
                    │  (State Interface)   │
                    ├─────────────────────┤
                    │ + handle()          │
                    │ + getDuration()     │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │   RedState      │ │YellowState │ │GreenState │
    ├──────────────────┤ ├────────────┤ ├───────────┤
    │ + handle()       │ │ + handle()  │ │ + handle()│
    │ + getDuration()  │ │ + getDuration()│ │ + getDuration()│
    └──────────────────┘ └────────────┘ └───────────┘
                │              │              │
                └──────────────┼──────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  TrafficLight       │
                    ├─────────────────────┤
                    │ - currentState       │
                    │ + changeState()      │
                    │ + start()            │
                    └──────────────────────┘
```

