"""
Observer Pattern - Weather Station Example
Real-world usage: IoT systems, sensor networks, dashboards, monitoring systems
"""

from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime


class Observer(ABC):
    """Observer interface"""
    
    @abstractmethod
    def update(self, data: Dict[str, float]):
        """Called when weather data changes"""
        pass


class Subject(ABC):
    """Subject interface"""
    
    @abstractmethod
    def attach(self, observer: Observer):
        """Attach an observer"""
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        """Detach an observer"""
        pass
    
    @abstractmethod
    def notify(self):
        """Notify all observers"""
        pass


class WeatherStation(Subject):
    """Concrete subject - weather station"""
    
    def __init__(self):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"  → {observer.__class__.__name__} subscribed to weather updates")
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"  → {observer.__class__.__name__} unsubscribed from weather updates")
    
    def notify(self):
        data = {
            "temperature": self._temperature,
            "humidity": self._humidity,
            "pressure": self._pressure,
            "timestamp": datetime.now()
        }
        for observer in self._observers:
            observer.update(data)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        """Update weather measurements and notify observers"""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        print(f"\n🌡️  Weather Station: New measurements received")
        print(f"   Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")
        self.notify()


class CurrentConditionsDisplay(Observer):
    """Concrete observer - current conditions display"""
    
    def __init__(self):
        self._temperature = None
        self._humidity = None
    
    def update(self, data: Dict[str, float]):
        self._temperature = data["temperature"]
        self._humidity = data["humidity"]
        self.display()
    
    def display(self):
        print(f"  📺 Current Conditions Display:")
        print(f"     Temperature: {self._temperature}°C")
        print(f"     Humidity: {self._humidity}%")


class StatisticsDisplay(Observer):
    """Concrete observer - statistics display"""
    
    def __init__(self):
        self._readings = []
        self._max_temp = float('-inf')
        self._min_temp = float('inf')
        self._avg_temp = 0.0
    
    def update(self, data: Dict[str, float]):
        temp = data["temperature"]
        self._readings.append(temp)
        self._max_temp = max(self._max_temp, temp)
        self._min_temp = min(self._min_temp, temp)
        self._avg_temp = sum(self._readings) / len(self._readings)
        self.display()
    
    def display(self):
        print(f"  📊 Statistics Display:")
        print(f"     Max Temperature: {self._max_temp}°C")
        print(f"     Min Temperature: {self._min_temp}°C")
        print(f"     Average Temperature: {self._avg_temp:.1f}°C")
        print(f"     Total Readings: {len(self._readings)}")


class ForecastDisplay(Observer):
    """Concrete observer - forecast display"""
    
    def __init__(self):
        self._last_pressure = None
        self._current_pressure = None
    
    def update(self, data: Dict[str, float]):
        self._last_pressure = self._current_pressure
        self._current_pressure = data["pressure"]
        self.display()
    
    def display(self):
        if self._last_pressure is None:
            print(f"  🌤️  Forecast Display: Waiting for more data...")
        else:
            if self._current_pressure > self._last_pressure:
                forecast = "Improving weather on the way!"
            elif self._current_pressure < self._last_pressure:
                forecast = "Watch out for cooler, rainy weather"
            else:
                forecast = "More of the same"
            print(f"  🌤️  Forecast Display: {forecast}")
            print(f"     Pressure trend: {self._last_pressure:.1f} → {self._current_pressure:.1f} hPa")


class AlertSystem(Observer):
    """Concrete observer - alert system for extreme conditions"""
    
    def __init__(self):
        self._alerts = []
    
    def update(self, data: Dict[str, float]):
        temp = data["temperature"]
        humidity = data["humidity"]
        
        alerts = []
        if temp > 35:
            alerts.append("🔥 HIGH TEMPERATURE ALERT: Above 35°C!")
        elif temp < 0:
            alerts.append("❄️  FREEZE ALERT: Temperature below freezing!")
        
        if humidity > 80:
            alerts.append("💧 HIGH HUMIDITY ALERT: Above 80%!")
        elif humidity < 20:
            alerts.append("🌵 LOW HUMIDITY ALERT: Below 20%!")
        
        if alerts:
            print(f"  🚨 Alert System:")
            for alert in alerts:
                print(f"     {alert}")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Observer Pattern - Weather Station Example")
    print("=" * 60)
    print()
    
    # Create weather station
    weather_station = WeatherStation()
    
    # Create displays
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()
    alert_system = AlertSystem()
    
    # Subscribe displays
    print("Setting up weather displays:")
    print("-" * 60)
    weather_station.attach(current_display)
    weather_station.attach(stats_display)
    weather_station.attach(forecast_display)
    weather_station.attach(alert_system)
    print()
    
    # Simulate weather updates
    print("Simulating weather updates:")
    print("=" * 60)
    weather_station.set_measurements(25.0, 65.0, 1013.2)
    print()
    
    weather_station.set_measurements(27.5, 70.0, 1012.8)
    print()
    
    weather_station.set_measurements(30.0, 75.0, 1010.5)
    print()
    
    weather_station.set_measurements(28.5, 68.0, 1011.2)
    print()
    
    # Test extreme conditions
    print("Testing extreme conditions:")
    print("-" * 60)
    weather_station.set_measurements(38.0, 85.0, 1008.0)
    print()
    
    weather_station.set_measurements(-2.0, 15.0, 1020.0)
    print()
    
    print("=" * 60)
    print("Key Benefit: Weather station doesn't need to know about")
    print("specific display types. Displays can be added/removed dynamically!")
    print("=" * 60)

