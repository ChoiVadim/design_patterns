"""
State Pattern - Vending Machine Example
Real-world usage: Game development, workflow engines, order processing, TCP states, UI state
"""

from abc import ABC, abstractmethod
from typing import Dict


class VendingState(ABC):
    """State interface"""
    
    @abstractmethod
    def insert_money(self, machine, amount: float):
        """Insert money into machine"""
        pass
    
    @abstractmethod
    def eject_money(self, machine):
        """Eject money from machine"""
        pass
    
    @abstractmethod
    def select_product(self, machine, product: str):
        """Select a product"""
        pass
    
    @abstractmethod
    def dispense(self, machine):
        """Dispense product"""
        pass


class NoMoneyState(VendingState):
    """State when no money is inserted"""
    
    def insert_money(self, machine, amount: float):
        print(f"💰 Inserted ${amount:.2f}")
        machine.add_money(amount)
        machine.set_state(HasMoneyState())
    
    def eject_money(self, machine):
        print("❌ No money to eject")
    
    def select_product(self, machine, product: str):
        print("❌ Please insert money first")
    
    def dispense(self, machine):
        print("❌ Please insert money first")


class HasMoneyState(VendingState):
    """State when money is inserted"""
    
    def insert_money(self, machine, amount: float):
        print(f"💰 Inserted additional ${amount:.2f}")
        machine.add_money(amount)
    
    def eject_money(self, machine):
        money = machine.get_money()
        print(f"💰 Ejecting ${money:.2f}")
        machine.set_money(0)
        machine.set_state(NoMoneyState())
    
    def select_product(self, machine, product: str):
        price = machine.get_product_price(product)
        if price is None:
            print(f"❌ Product '{product}' not available")
            return
        
        if machine.get_money() >= price:
            print(f"✅ Selected {product} (${price:.2f})")
            machine.set_selected_product(product)
            machine.set_state(SoldState())
        else:
            needed = price - machine.get_money()
            print(f"❌ Insufficient funds. Need ${needed:.2f} more")
    
    def dispense(self, machine):
        print("❌ Please select a product first")


class SoldState(VendingState):
    """State when product is sold"""
    
    def insert_money(self, machine, amount: float):
        print("⏳ Please wait, processing your order...")
    
    def eject_money(self, machine):
        print("⏳ Cannot eject money, product already selected")
    
    def select_product(self, machine, product: str):
        print("⏳ Please wait, processing your order...")
    
    def dispense(self, machine):
        product = machine.get_selected_product()
        price = machine.get_product_price(product)
        money = machine.get_money()
        
        if machine.has_product(product):
            print(f"🎉 Dispensing {product}...")
            machine.remove_product(product)
            change = money - price
            if change > 0:
                print(f"💰 Returning change: ${change:.2f}")
            machine.set_money(0)
            machine.set_selected_product(None)
            machine.set_state(NoMoneyState())
        else:
            print(f"❌ {product} is out of stock")
            machine.set_state(NoMoneyState())


class SoldOutState(VendingState):
    """State when machine is out of products"""
    
    def insert_money(self, machine, amount: float):
        print("❌ Machine is out of products")
    
    def eject_money(self, machine):
        money = machine.get_money()
        if money > 0:
            print(f"💰 Ejecting ${money:.2f}")
            machine.set_money(0)
        machine.set_state(NoMoneyState())
    
    def select_product(self, machine, product: str):
        print("❌ Machine is out of products")
    
    def dispense(self, machine):
        print("❌ Machine is out of products")


class VendingMachine:
    """Context class that uses states"""
    
    def __init__(self):
        self._state = NoMoneyState()
        self._money = 0.0
        self._selected_product = None
        self._products: Dict[str, Dict[str, any]] = {
            "Coke": {"price": 1.50, "stock": 5},
            "Pepsi": {"price": 1.50, "stock": 3},
            "Chips": {"price": 2.00, "stock": 4},
            "Candy": {"price": 1.00, "stock": 0}  # Out of stock
        }
    
    def set_state(self, state: VendingState):
        """Change state"""
        self._state = state
    
    def get_state(self) -> VendingState:
        """Get current state"""
        return self._state
    
    def add_money(self, amount: float):
        """Add money"""
        self._money += amount
    
    def set_money(self, amount: float):
        """Set money"""
        self._money = amount
    
    def get_money(self) -> float:
        """Get current money"""
        return self._money
    
    def set_selected_product(self, product: str):
        """Set selected product"""
        self._selected_product = product
    
    def get_selected_product(self) -> str:
        """Get selected product"""
        return self._selected_product
    
    def get_product_price(self, product: str) -> float:
        """Get product price"""
        if product in self._products:
            return self._products[product]["price"]
        return None
    
    def has_product(self, product: str) -> bool:
        """Check if product is available"""
        if product in self._products:
            return self._products[product]["stock"] > 0
        return False
    
    def remove_product(self, product: str):
        """Remove one product from stock"""
        if product in self._products:
            self._products[product]["stock"] -= 1
    
    def insert_money(self, amount: float):
        """Insert money"""
        self._state.insert_money(self, amount)
    
    def eject_money(self):
        """Eject money"""
        self._state.eject_money(self)
    
    def select_product(self, product: str):
        """Select product"""
        self._state.select_product(self, product)
    
    def dispense(self):
        """Dispense product"""
        self._state.dispense(self)
    
    def show_status(self):
        """Show machine status"""
        print(f"\n📊 Machine Status:")
        print(f"   State: {self._state.__class__.__name__}")
        print(f"   Money: ${self._money:.2f}")
        print(f"   Selected: {self._selected_product or 'None'}")
        print(f"   Products:")
        for product, info in self._products.items():
            print(f"     - {product}: ${info['price']:.2f} (Stock: {info['stock']})")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("State Pattern - Vending Machine Example")
    print("=" * 60)
    print()
    
    machine = VendingMachine()
    machine.show_status()
    
    # Try to select without money
    print("\n1. Attempting to select product without money:")
    print("-" * 60)
    machine.select_product("Coke")
    print()
    
    # Insert money
    print("2. Inserting money:")
    print("-" * 60)
    machine.insert_money(2.00)
    machine.show_status()
    print()
    
    # Select product
    print("3. Selecting product:")
    print("-" * 60)
    machine.select_product("Coke")
    machine.show_status()
    print()
    
    # Dispense
    print("4. Dispensing product:")
    print("-" * 60)
    machine.dispense()
    machine.show_status()
    print()
    
    # Try another purchase
    print("5. Another purchase:")
    print("-" * 60)
    machine.insert_money(1.50)
    machine.select_product("Pepsi")
    machine.dispense()
    machine.show_status()
    print()
    
    # Try out of stock product
    print("6. Attempting to buy out-of-stock product:")
    print("-" * 60)
    machine.insert_money(1.00)
    machine.select_product("Candy")
    machine.dispense()
    machine.show_status()
    print()
    
    # Insufficient funds
    print("7. Insufficient funds scenario:")
    print("-" * 60)
    machine.insert_money(1.00)
    machine.select_product("Chips")  # Costs $2.00
    machine.show_status()
    print()
    
    print("=" * 60)
    print("Key Benefit: State-specific behavior is encapsulated in")
    print("separate classes, making state management clear and maintainable!")
    print("=" * 60)

