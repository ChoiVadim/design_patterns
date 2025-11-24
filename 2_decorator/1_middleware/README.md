# Decorator Pattern - Example 1: Middleware

## Problem Description

In web development, we often need to process HTTP requests with cross-cutting concerns like logging, authentication, data validation, and caching. Adding this logic directly into the core request handler violates the Single Responsibility Principle and makes the code hard to maintain. The Decorator pattern (often called "Middleware" in this context) allows us to wrap the request handler with layers of additional behavior.

**Real-world usage**: Web frameworks (Django, Flask, Express.js), RPC frameworks (gRPC interceptors), and message queues (Celery task hooks).

## Class Diagram

```
                    ┌─────────────────────┐
                    │       Handler       │
                    │     (Component)     │
                    ├─────────────────────┤
                    │ + handle_request()  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │                             │
    ┌───────────▼──────┐          ┌───────────▼──────────┐
    │  RequestHandler  │          │      Middleware      │
    │    (Concrete)    │          │     (Decorator)      │
    ├──────────────────┤          ├──────────────────────┤
    │ + handle_request()│         │ - handler            │
    └──────────────────┘          │ + handle_request()   │
                                  └──────────┬───────────┘
                                             │
                    ┌────────────────────────┼─────────────────────────┐
                    │                        │                         │
        ┌───────────▼──────┐         ┌───────▼────────┐        ┌───────▼────────┐
        │ LoggingMiddleware│         │ AuthMiddleware │        │ CacheMiddleware│
        ├──────────────────┤         ├────────────────┤        ├────────────────┤
        │ + handle_request()│        │ + handle_request()│     │ + handle_request()│
        └──────────────────┘         └────────────────┘        └────────────────┘
```

## How to run
```bash
python3 example.py
```
