"""
Template Method Pattern - Recipe System Example
Real-world usage: Frameworks, build systems, data processing pipelines, algorithms
"""

from abc import ABC, abstractmethod


class Recipe(ABC):
    """Abstract class defining the template method"""
    
    def prepare_recipe(self):
        """Template method - defines the algorithm skeleton"""
        print(f"\n🍳 Preparing {self.get_name()}...")
        print("-" * 60)
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
        print(f"✅ {self.get_name()} is ready!")
    
    def boil_water(self):
        """Common step - can be overridden if needed"""
        print("1. Boiling water...")
    
    @abstractmethod
    def brew(self):
        """Abstract step - must be implemented by subclasses"""
        pass
    
    def pour_in_cup(self):
        """Common step - can be overridden if needed"""
        print("3. Pouring into cup...")
    
    @abstractmethod
    def add_condiments(self):
        """Abstract step - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Get recipe name"""
        pass


class CoffeeRecipe(Recipe):
    """Concrete implementation - Coffee recipe"""
    
    def brew(self):
        print("2. Dripping coffee through filter...")
    
    def add_condiments(self):
        print("4. Adding sugar and milk...")
    
    def get_name(self) -> str:
        return "Coffee"


class TeaRecipe(Recipe):
    """Concrete implementation - Tea recipe"""
    
    def brew(self):
        print("2. Steeping the tea...")
    
    def add_condiments(self):
        print("4. Adding lemon...")
    
    def get_name(self) -> str:
        return "Tea"


class SoupRecipe(Recipe):
    """Concrete implementation - Soup recipe"""
    
    def boil_water(self):
        print("1. Boiling water in a pot...")
    
    def brew(self):
        print("2. Adding vegetables and cooking...")
    
    def pour_in_cup(self):
        print("3. Pouring soup into bowl...")
    
    def add_condiments(self):
        print("4. Adding salt, pepper, and herbs...")
    
    def get_name(self) -> str:
        return "Vegetable Soup"


class LatteRecipe(Recipe):
    """Concrete implementation - Latte recipe"""
    
    def brew(self):
        print("2. Brewing espresso...")
        print("   Steaming milk...")
    
    def add_condiments(self):
        print("4. Adding steamed milk foam...")
        print("   Creating latte art...")
    
    def get_name(self) -> str:
        return "Latte"


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Template Method Pattern - Recipe System Example")
    print("=" * 60)
    
    # Prepare different recipes
    recipes = [
        CoffeeRecipe(),
        TeaRecipe(),
        SoupRecipe(),
        LatteRecipe()
    ]
    
    for recipe in recipes:
        recipe.prepare_recipe()
        print()
    
    print("=" * 60)
    print("Key Benefit: Algorithm structure is defined once in the")
    print("base class, but specific steps can be customized by subclasses!")
    print("=" * 60)

