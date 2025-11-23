"""
Adapter Pattern - Payment Gateway Example
Real-world usage: Payment processing, cloud services, API integrations, database drivers
"""

from abc import ABC, abstractmethod
from typing import Dict
import random


class PaymentGateway(ABC):
    """Target interface for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> Dict[str, any]:
        """Process a payment"""
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str, amount: float = None) -> Dict[str, any]:
        """Refund a payment"""
        pass


# Adaptee classes (third-party payment APIs with different interfaces)
class StripeAPI:
    """Stripe payment API - different interface"""
    
    def charge(self, amount_cents: int, currency: str) -> Dict[str, any]:
        """Stripe uses cents, not dollars"""
        transaction_id = f"ch_stripe_{random.randint(10000, 99999)}"
        print(f"💳 Stripe: Charging {amount_cents/100:.2f} {currency}")
        return {
            "id": transaction_id,
            "amount": amount_cents,
            "currency": currency,
            "status": "succeeded"
        }
    
    def reverse_charge(self, charge_id: str) -> Dict[str, any]:
        print(f"💳 Stripe: Reversing charge {charge_id}")
        return {
            "id": f"ref_{charge_id}",
            "status": "refunded"
        }


class PayPalAPI:
    """PayPal payment API - different interface"""
    
    def make_payment(self, amount: float, currency_code: str) -> Dict[str, any]:
        """PayPal uses different parameter names"""
        payment_id = f"PAYPAL-{random.randint(100000, 999999)}"
        print(f"💳 PayPal: Processing payment of {amount} {currency_code}")
        return {
            "paymentId": payment_id,
            "state": "approved",
            "amount": amount,
            "currency": currency_code
        }
    
    def cancel_payment(self, payment_id: str) -> Dict[str, any]:
        print(f"💳 PayPal: Cancelling payment {payment_id}")
        return {
            "paymentId": payment_id,
            "state": "refunded"
        }


class SquareAPI:
    """Square payment API - different interface"""
    
    def create_payment(self, amount_money: Dict[str, any]) -> Dict[str, any]:
        """Square uses amount_money object"""
        payment_id = f"sq_{random.randint(1000000, 9999999)}"
        amount = amount_money["amount"] / 100  # Convert from cents
        currency = amount_money["currency"]
        print(f"💳 Square: Creating payment of {amount} {currency}")
        return {
            "payment_id": payment_id,
            "status": "COMPLETED",
            "amount_money": amount_money
        }
    
    def void_payment(self, payment_id: str) -> Dict[str, any]:
        print(f"💳 Square: Voiding payment {payment_id}")
        return {
            "payment_id": payment_id,
            "status": "VOIDED"
        }


# Adapter classes
class StripeAdapter(PaymentGateway):
    """Adapter for Stripe API"""
    
    def __init__(self, api_key: str):
        self._stripe = StripeAPI()
        self._api_key = api_key
    
    def process_payment(self, amount: float, currency: str = "USD") -> Dict[str, any]:
        # Convert dollars to cents for Stripe
        amount_cents = int(amount * 100)
        result = self._stripe.charge(amount_cents, currency)
        # Convert back to standard format
        return {
            "transaction_id": result["id"],
            "amount": result["amount"] / 100,
            "currency": result["currency"],
            "status": result["status"],
            "gateway": "stripe"
        }
    
    def refund(self, transaction_id: str, amount: float = None) -> Dict[str, any]:
        result = self._stripe.reverse_charge(transaction_id)
        return {
            "refund_id": result["id"],
            "transaction_id": transaction_id,
            "status": result["status"],
            "gateway": "stripe"
        }


class PayPalAdapter(PaymentGateway):
    """Adapter for PayPal API"""
    
    def __init__(self, client_id: str, secret: str):
        self._paypal = PayPalAPI()
        self._client_id = client_id
        self._secret = secret
    
    def process_payment(self, amount: float, currency: str = "USD") -> Dict[str, any]:
        result = self._paypal.make_payment(amount, currency)
        # Convert to standard format
        return {
            "transaction_id": result["paymentId"],
            "amount": result["amount"],
            "currency": result["currency"],
            "status": result["state"],
            "gateway": "paypal"
        }
    
    def refund(self, transaction_id: str, amount: float = None) -> Dict[str, any]:
        result = self._paypal.cancel_payment(transaction_id)
        return {
            "refund_id": result["paymentId"],
            "transaction_id": transaction_id,
            "status": result["state"],
            "gateway": "paypal"
        }


class SquareAdapter(PaymentGateway):
    """Adapter for Square API"""
    
    def __init__(self, access_token: str):
        self._square = SquareAPI()
        self._access_token = access_token
    
    def process_payment(self, amount: float, currency: str = "USD") -> Dict[str, any]:
        # Convert to Square's format
        amount_money = {
            "amount": int(amount * 100),  # Convert to cents
            "currency": currency
        }
        result = self._square.create_payment(amount_money)
        # Convert to standard format
        return {
            "transaction_id": result["payment_id"],
            "amount": result["amount_money"]["amount"] / 100,
            "currency": result["amount_money"]["currency"],
            "status": result["status"].lower(),
            "gateway": "square"
        }
    
    def refund(self, transaction_id: str, amount: float = None) -> Dict[str, any]:
        result = self._square.void_payment(transaction_id)
        return {
            "refund_id": result["payment_id"],
            "transaction_id": transaction_id,
            "status": result["status"].lower(),
            "gateway": "square"
        }


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Adapter Pattern - Payment Gateway Example")
    print("=" * 60)
    print()
    
    # Create adapters for different payment gateways
    stripe = StripeAdapter("sk_test_12345")
    paypal = PayPalAdapter("client_id_123", "secret_456")
    square = SquareAdapter("sq_access_token_789")
    
    # Process payments using unified interface
    print("Processing payments through different gateways:")
    print("=" * 60)
    
    # Stripe payment
    print("\n1. Stripe Payment:")
    print("-" * 60)
    result1 = stripe.process_payment(99.99, "USD")
    print(f"Result: {result1}")
    
    # PayPal payment
    print("\n2. PayPal Payment:")
    print("-" * 60)
    result2 = paypal.process_payment(149.50, "USD")
    print(f"Result: {result2}")
    
    # Square payment
    print("\n3. Square Payment:")
    print("-" * 60)
    result3 = square.process_payment(75.00, "USD")
    print(f"Result: {result3}")
    
    # Process refunds
    print("\nProcessing refunds:")
    print("=" * 60)
    
    print("\n4. Stripe Refund:")
    print("-" * 60)
    refund1 = stripe.refund(result1["transaction_id"])
    print(f"Result: {refund1}")
    
    print("\n5. PayPal Refund:")
    print("-" * 60)
    refund2 = paypal.refund(result2["transaction_id"])
    print(f"Result: {refund2}")
    
    print()
    print("=" * 60)
    print("Key Benefit: Can use different payment APIs (Stripe, PayPal,")
    print("Square) through a unified PaymentGateway interface!")
    print("=" * 60)

