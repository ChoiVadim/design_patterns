"""
Observer Pattern - Stock Market Example
Real-world usage: Event-driven systems, GUI frameworks, reactive programming, MVC
"""

from abc import ABC, abstractmethod
from typing import List
from datetime import datetime


class Observer(ABC):
    """Observer interface"""
    
    @abstractmethod
    def update(self, symbol: str, price: float, change: float):
        """Called when subject state changes"""
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


class StockPrice(Subject):
    """Concrete subject - stock price"""
    
    def __init__(self, symbol: str, initial_price: float):
        self._symbol = symbol
        self._price = initial_price
        self._previous_price = initial_price
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"  → {observer.__class__.__name__} subscribed to {self._symbol}")
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"  → {observer.__class__.__name__} unsubscribed from {self._symbol}")
    
    def notify(self):
        change = self._price - self._previous_price
        for observer in self._observers:
            observer.update(self._symbol, self._price, change)
    
    def set_price(self, new_price: float):
        if new_price != self._price:
            self._previous_price = self._price
            self._price = new_price
            print(f"\n📈 {self._symbol} price changed: ${self._previous_price:.2f} → ${self._price:.2f}")
            self.notify()


class Trader(Observer):
    """Concrete observer - stock trader"""
    
    def __init__(self, name: str, threshold: float = 0.05):
        self._name = name
        self._threshold = threshold  # Alert if change > 5%
    
    def update(self, symbol: str, price: float, change: float):
        change_percent = (change / (price - change)) * 100 if (price - change) > 0 else 0
        if abs(change_percent) >= self._threshold * 100:
            direction = "📈 BUY SIGNAL" if change > 0 else "📉 SELL SIGNAL"
            print(f"  🔔 Trader {self._name}: {direction} for {symbol}!")
            print(f"     Change: {change_percent:+.2f}% (${change:+.2f})")


class Analyst(Observer):
    """Concrete observer - financial analyst"""
    
    def __init__(self, name: str):
        self._name = name
        self._price_history = {}
    
    def update(self, symbol: str, price: float, change: float):
        if symbol not in self._price_history:
            self._price_history[symbol] = []
        self._price_history[symbol].append(price)
        
        # Analyze trend
        history = self._price_history[symbol]
        if len(history) >= 3:
            trend = "📊 UPTREND" if history[-1] > history[-2] > history[-3] else "📊 DOWNTREND"
            print(f"  📊 Analyst {self._name}: {trend} detected for {symbol}")
            print(f"     Current: ${price:.2f}, 3-period avg: ${sum(history[-3:])/3:.2f}")


class MobileApp(Observer):
    """Concrete observer - mobile app notification"""
    
    def __init__(self, user_id: str):
        self._user_id = user_id
    
    def update(self, symbol: str, price: float, change: float):
        change_percent = (change / (price - change)) * 100 if (price - change) > 0 else 0
        emoji = "🟢" if change > 0 else "🔴" if change < 0 else "⚪"
        print(f"  📱 Mobile App ({self._user_id}): {emoji} {symbol} ${price:.2f} ({change_percent:+.2f}%)")


class EmailNotifier(Observer):
    """Concrete observer - email notification service"""
    
    def __init__(self, email: str):
        self._email = email
    
    def update(self, symbol: str, price: float, change: float):
        if abs(change) > 1.0:  # Only email for significant changes
            direction = "increased" if change > 0 else "decreased"
            print(f"  📧 Email to {self._email}: {symbol} {direction} by ${abs(change):.2f}")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Observer Pattern - Stock Market Example")
    print("=" * 60)
    print()
    
    # Create stock
    apple_stock = StockPrice("AAPL", 150.00)
    
    # Create observers
    trader1 = Trader("John", threshold=0.03)
    trader2 = Trader("Sarah", threshold=0.05)
    analyst = Analyst("Dr. Smith")
    mobile_app = MobileApp("user123")
    email = EmailNotifier("alerts@example.com")
    
    # Subscribe observers
    print("Setting up observers:")
    print("-" * 60)
    apple_stock.attach(trader1)
    apple_stock.attach(trader2)
    apple_stock.attach(analyst)
    apple_stock.attach(mobile_app)
    apple_stock.attach(email)
    print()
    
    # Simulate price changes
    print("Simulating price changes:")
    print("=" * 60)
    apple_stock.set_price(152.50)
    print()
    
    apple_stock.set_price(148.00)
    print()
    
    apple_stock.set_price(155.00)
    print()
    
    # Unsubscribe one observer
    print("Unsubscribing trader2:")
    print("-" * 60)
    apple_stock.detach(trader2)
    print()
    
    apple_stock.set_price(153.00)
    print()
    
    print("=" * 60)
    print("Key Benefit: Stock doesn't need to know about specific observers.")
    print("Observers can be added/removed dynamically!")
    print("=" * 60)

