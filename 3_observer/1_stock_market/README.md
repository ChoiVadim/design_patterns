# Observer Pattern - Example 1: Stock Market

## Problem Description

A stock trading application needs to notify multiple users (traders, analysts, mobile apps) when stock prices change. Instead of the stock object directly calling each subscriber, the Observer pattern decouples the subject (stock) from its observers (subscribers), allowing dynamic subscription/unsubscription.

**Real-world usage**: Used in event-driven systems, GUI frameworks (button clicks), reactive programming (RxJS), Model-View-Controller (MVC), and real-time data feeds (stock prices, news feeds).

## Class Diagram

```
                    ┌─────────────────────┐
                    │     Subject         │
                    │  (Observable)       │
                    ├─────────────────────┤
                    │ + attach(observer)  │
                    │ + detach(observer)  │
                    │ + notify()          │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │    StockPrice      │
                    ├────────────────────┤
                    │ - price            │
                    │ - observers[]      │
                    │ + setPrice()       │
                    └────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
        ┌───────────▼──────┐   ┌─────────▼──────────┐
        │    Observer      │   │  MobileApp         │
        │  (Interface)     │   │  (Observer)        │
        ├──────────────────┤   ├────────────────────┤
        │ + update()       │   │ + update()         │
        └──────────┬───────┘   └────────────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
┌───────▼───┐ ┌────▼────┐ ┌───▼──────────┐
│Trader     │ │Analyst  │ │EmailNotifier │
│(Observer) │ │(Observer)│ │(Observer)   │
├───────────┤ ├─────────┤ ├──────────────┤
│+ update() │ │+ update()│ │+ update()    │
└───────────┘ └─────────┘ └──────────────┘
```

