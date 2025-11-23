# Strategy Pattern - Example 1: Payment Processing

## Problem Description

In an e-commerce application, customers need to pay using different payment methods (Credit Card, PayPal, Cryptocurrency). The payment processing logic varies significantly between methods, but the interface should be consistent. Without the Strategy pattern, we'd have complex if-else chains that become hard to maintain as new payment methods are added.

**Real-world usage**: Used in payment gateways like Stripe, PayPal SDKs, e-commerce platforms (Shopify, WooCommerce), and financial apps.

## Class Diagram

```
                    ┌─────────────────────┐
                    │  PaymentStrategy    │
                    │  (Interface)        │
                    ├─────────────────────┤
                    │ + pay(amount)       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌────▼──────┐ ┌────▼──────────┐
    │ CreditCardPayment│ │PayPalPayment│ │CryptoPayment │
    ├──────────────────┤ ├────────────┤ ├──────────────┤
    │ + pay(amount)    │ │ + pay(...) │ │ + pay(...)   │
    └──────────────────┘ └────────────┘ └──────────────┘
                │              │              │
                └──────────────┼──────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  PaymentProcessor   │
                    ├─────────────────────┤
                    │ - strategy          │
                    │ + setStrategy()     │
                    │ + processPayment()  │
                    └─────────────────────┘
```

