# State Pattern - Example 1: Music Player

## Problem Description

A music player behaves differently depending on its current state. For example, pressing "Play" when stopped starts the music, but pressing "Play" when playing pauses it. Pressing "Lock" prevents other buttons from working. Using a massive switch statement or if-else blocks to handle these transitions becomes unmanageable. The State pattern encapsulates each state's behavior in a separate class.

**Real-world usage**: TCP Connection states (Established, Closed, Listening), Order processing (New, Paid, Shipped), Game character states, and Workflow engines.

## Class Diagram

```
                    ┌─────────────────────┐
                    │     MusicPlayer     │
                    │      (Context)      │
                    ├─────────────────────┤
                    │ - state: State      │
                    │ + change_state()    │
                    │ + click_play()      │◄───────────┐
                    │ + click_lock()      │            │
                    └──────────┬──────────┘            │
                               │                       │
                ┌──────────────▼──────────────┐        │
                │            State            │        │
                │         (Interface)         │        │
                ├─────────────────────────────┤        │
                │ + click_play(player)        │        │
                │ + click_lock(player)        │────────┘
                └──────────────▲──────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
┌───────┴───────┐      ┌───────┴───────┐      ┌───────┴───────┐
│ PlayingState  │      │ StoppedState  │      │  LockedState  │
├───────────────┤      ├───────────────┤      ├───────────────┤
│ + click_play()│      │ + click_play()│      │ + click_play()│
│ + click_lock()│      │ + click_lock()│      │ + click_lock()│
└───────────────┘      └───────────────┘      └───────────────┘
```

