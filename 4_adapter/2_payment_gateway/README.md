# Adapter Pattern - Example 2: Payment Gateway

## Problem Description

An e-commerce application needs to integrate multiple payment gateways (Stripe, PayPal, Square) that have different APIs. The Adapter pattern allows the application to use a unified payment interface while working with different gateway implementations.

**Real-world usage**: Used in payment processing systems, cloud service integrations (AWS, Azure, GCP), social media API wrappers, and database drivers (JDBC, ODBC).

## Class Diagram

```
                    ┌─────────────────────┐
                    │   PaymentGateway    │
                    │  (Target)           │
                    ├─────────────────────┤
                    │ + processPayment(   │
                    │        amount)      │
                    │ + refund(           │
                    │        transactionId)│
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │  StripeAdapter  │ │PayPalAdapter│ │SquareAdapter│
    │  (Adapter)      │ │ (Adapter)   │ │ (Adapter)  │
    ├──────────────────┤ ├────────────┤ ├────────────┤
    │ - stripe         │ │ - paypal   │ │ - square   │
    │ + processPayment()│ │ + process() │ │ + process() │
    │ + refund()       │ │ + refund() │ │ + refund() │
    └──────────┬───────┘ └─────┬──────┘ └─────┬──────┘
               │               │              │
    ┌──────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │  StripeAPI      │ │ PayPalAPI  │ │ SquareAPI  │
    │  (Adaptee)      │ │ (Adaptee)  │ │ (Adaptee)  │
    ├──────────────────┤ ├────────────┤ ├────────────┤
    │ + charge()      │ │ + makePayment()│ │ + createPayment()│
    │ + reverseCharge()│ │ + cancelPayment()│ │ + voidPayment()│
    └──────────────────┘ └────────────┘ └────────────┘
```

