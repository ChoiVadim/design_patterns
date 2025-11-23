"""
Decorator Pattern - Coffee Shop Example
Real-world usage: GUI frameworks, I/O streams, middleware, text formatting
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    """Component interface for beverages"""
    
    @abstractmethod
    def get_description(self) -> str:
        """Return beverage description"""
        pass
    
    @abstractmethod
    def get_cost(self) -> float:
        """Return beverage cost"""
        pass


class Espresso(Beverage):
    """Concrete component - base coffee"""
    
    def get_description(self) -> str:
        return "Espresso"
    
    def get_cost(self) -> float:
        return 2.50


class BeverageDecorator(Beverage):
    """Base decorator class"""
    
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def get_cost(self) -> float:
        pass


class MilkDecorator(BeverageDecorator):
    """Decorator for adding milk"""
    
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Milk"
    
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.50


class SugarDecorator(BeverageDecorator):
    """Decorator for adding sugar"""
    
    def __init__(self, beverage: Beverage, teaspoons: int = 1):
        super().__init__(beverage)
        self._teaspoons = teaspoons
    
    def get_description(self) -> str:
        return self._beverage.get_description() + f", {self._teaspoons} tsp Sugar"
    
    def get_cost(self) -> float:
        return self._beverage.get_cost() + (0.10 * self._teaspoons)


class WhipDecorator(BeverageDecorator):
    """Decorator for adding whipped cream"""
    
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Whipped Cream"
    
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.75


class CaramelDecorator(BeverageDecorator):
    """Decorator for adding caramel syrup"""
    
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramel"
    
    def get_cost(self) -> float:
        return self._beverage.get_cost() + 0.60


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Decorator Pattern - Coffee Shop Example")
    print("=" * 60)
    print()
    
    # Simple espresso
    print("1. Simple Espresso:")
    print("-" * 60)
    coffee1 = Espresso()
    print(f"Description: {coffee1.get_description()}")
    print(f"Cost: ${coffee1.get_cost():.2f}")
    print()
    
    # Espresso with milk and sugar
    print("2. Espresso with Milk and Sugar:")
    print("-" * 60)
    coffee2 = SugarDecorator(MilkDecorator(Espresso()), teaspoons=2)
    print(f"Description: {coffee2.get_description()}")
    print(f"Cost: ${coffee2.get_cost():.2f}")
    print()
    
    # Espresso with all add-ons
    print("3. Espresso with All Add-ons:")
    print("-" * 60)
    coffee3 = CaramelDecorator(
        WhipDecorator(
            SugarDecorator(
                MilkDecorator(Espresso()), 
                teaspoons=1
            )
        )
    )
    print(f"Description: {coffee3.get_description()}")
    print(f"Cost: ${coffee3.get_cost():.2f}")
    print()
    
    # Complex order
    print("4. Custom Order (Espresso + Milk + 3 Sugar + Whip):")
    print("-" * 60)
    coffee4 = WhipDecorator(
        SugarDecorator(
            MilkDecorator(Espresso()),
            teaspoons=3
        )
    )
    print(f"Description: {coffee4.get_description()}")
    print(f"Cost: ${coffee4.get_cost():.2f}")
    print()
    
    print("=" * 60)
    print("Key Benefit: Can combine decorators dynamically without")
    print("creating classes for every possible combination!")
    print("=" * 60)

