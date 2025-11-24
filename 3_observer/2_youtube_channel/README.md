# Observer Pattern - Example 2: YouTube Channel

## Problem Description

A YouTube channel needs to notify all its subscribers whenever a new video is uploaded. The channel (Subject) shouldn't need to know the specific details of each subscriber (Observer), only that they can be notified. The Observer pattern allows for a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.

**Real-world usage**: Event handling systems (DOM events), MVC architecture (Model notifying View), Pub-Sub systems (Kafka, RabbitMQ), and social media feeds.

## Class Diagram

```
    ┌─────────────────────┐              ┌─────────────────────┐
    │       Subject       │              │      Observer       │
    ├─────────────────────┤              ├─────────────────────┤
    │ + attach(observer)  │◄─────────────┤ + update()          │
    │ + detach(observer)  │              └──────────▲──────────┘
    │ + notify()          │                         │
    └──────────▲──────────┘                         │
               │                                    │
    ┌──────────┴──────────┐              ┌──────────┴──────────┐
    │   YoutubeChannel    │              │     Subscriber      │
    │  (ConcreteSubject)  │              │ (ConcreteObserver)  │
    ├─────────────────────┤              ├─────────────────────┤
    │ - subscribers       │              │ - name              │
    │ - videos            │              │                     │
    │ + upload_video()    │              │ + update()          │
    └─────────────────────┘              └─────────────────────┘
```

