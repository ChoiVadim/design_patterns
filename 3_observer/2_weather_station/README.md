# Observer Pattern - Example 2: Weather Station

## Problem Description

A weather monitoring system needs to update multiple displays (current conditions, statistics, forecast) when weather data changes. The Observer pattern allows the weather station to notify all displays without knowing their specific implementations.

**Real-world usage**: Used in IoT systems, sensor networks, dashboard applications, real-time monitoring systems, and data visualization tools.

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
                    │  WeatherStation    │
                    ├────────────────────┤
                    │ - temperature      │
                    │ - humidity         │
                    │ - pressure         │
                    │ - observers[]      │
                    │ + setMeasurements()│
                    └────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
        ┌───────────▼──────┐   ┌─────────▼──────────┐
        │    Observer      │   │  StatisticsDisplay │
        │  (Interface)     │   │  (Observer)        │
        ├──────────────────┤   ├────────────────────┤
        │ + update()       │   │ + update()         │
        └──────────┬───────┘   └────────────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
┌───────▼───┐ ┌────▼────┐ ┌───▼──────────┐
│Current    │ │Forecast │ │AlertSystem   │
│Conditions │ │Display  │ │(Observer)  │
│(Observer) │ │(Observer)│ │             │
├───────────┤ ├─────────┤ ├──────────────┤
│+ update() │ │+ update()│ │+ update()    │
└───────────┘ └─────────┘ └──────────────┘
```

