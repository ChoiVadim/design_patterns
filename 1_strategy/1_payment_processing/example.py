"""
Strategy Pattern - Payment Processing Example
Real-world usage: E-commerce platforms, payment gateways, financial apps
"""

from abc import ABC, abstractmethod
from typing import Dict


class PaymentStrategy(ABC):
    """Strategy interface for payment methods"""
    
    @abstractmethod
    def pay(self, amount: float) -> Dict[str, any]:
        """Process payment and return result"""
        pass


class CreditCardPayment(PaymentStrategy):
    """Credit card payment strategy"""
    
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount: float) -> Dict[str, any]:
        print(f"Processing credit card payment of ${amount:.2f}")
        print(f"Card: ****{self.card_number[-4:]}")
        # Simulate payment processing
        return {
            "status": "success",
            "method": "credit_card",
            "amount": amount,
            "transaction_id": f"CC-{hash(self.card_number) % 10000}"
        }


class PayPalPayment(PaymentStrategy):
    """PayPal payment strategy"""
    
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> Dict[str, any]:
        print(f"Processing PayPal payment of ${amount:.2f}")
        print(f"PayPal account: {self.email}")
        # Simulate PayPal API call
        return {
            "status": "success",
            "method": "paypal",
            "amount": amount,
            "transaction_id": f"PP-{hash(self.email) % 10000}"
        }


class CryptoPayment(PaymentStrategy):
    """Cryptocurrency payment strategy"""
    
    def __init__(self, wallet_address: str, currency: str = "BTC"):
        self.wallet_address = wallet_address
        self.currency = currency
    
    def pay(self, amount: float) -> Dict[str, any]:
        print(f"Processing {self.currency} payment of ${amount:.2f}")
        print(f"Wallet: {self.wallet_address[:10]}...{self.wallet_address[-10:]}")
        # Simulate blockchain transaction
        return {
            "status": "success",
            "method": "crypto",
            "currency": self.currency,
            "amount": amount,
            "transaction_id": f"CRYPTO-{hash(self.wallet_address) % 10000}"
        }


class PaymentProcessor:
    """Context class that uses payment strategies"""
    
    def __init__(self, strategy: PaymentStrategy = None):
        self._strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        """Change payment strategy at runtime"""
        self._strategy = strategy
    
    def process_payment(self, amount: float) -> Dict[str, any]:
        """Process payment using current strategy"""
        if not self._strategy:
            raise ValueError("No payment strategy set")
        return self._strategy.pay(amount)


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Strategy Pattern - Payment Processing Example")
    print("=" * 60)
    print()
    
    processor = PaymentProcessor()
    
    # Process payment with credit card
    print("1. Credit Card Payment:")
    print("-" * 60)
    processor.set_strategy(CreditCardPayment("4532-1234-5678-9010", "123"))
    result1 = processor.process_payment(99.99)
    print(f"Result: {result1}")
    print()
    
    # Switch to PayPal
    print("2. PayPal Payment:")
    print("-" * 60)
    processor.set_strategy(PayPalPayment("customer@example.com"))
    result2 = processor.process_payment(149.50)
    print(f"Result: {result2}")
    print()
    
    # Switch to cryptocurrency
    print("3. Cryptocurrency Payment:")
    print("-" * 60)
    processor.set_strategy(CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "BTC"))
    result3 = processor.process_payment(200.00)
    print(f"Result: {result3}")
    print()
    
    print("=" * 60)
    print("Key Benefit: Can switch payment methods at runtime")
    print("without modifying the PaymentProcessor class!")
    print("=" * 60)

