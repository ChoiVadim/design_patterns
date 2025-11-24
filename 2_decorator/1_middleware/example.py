"""
Decorator Pattern - Middleware Example
Real-world usage: Web frameworks (Django/Flask/Express) for request processing, Logging, Authentication, Caching
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class Handler(ABC):
    """Component interface for Request Handler"""

    @abstractmethod
    def handle_request(self, request: Dict[str, Any]) -> None:
        pass


class RequestHandler(Handler):
    """Concrete Component - The core request handler"""

    def handle_request(self, request: Dict[str, Any]) -> None:
        print(f"Processing request for path: {request.get('path')}")
        print("  -> Core logic executed (Database query, Business logic, etc.)")
        print("  -> Response generated: 200 OK")


class Middleware(Handler):
    """Base Decorator - Middleware"""

    def __init__(self, handler: Handler):
        self._handler = handler

    @abstractmethod
    def handle_request(self, request: Dict[str, Any]) -> None:
        pass


class LoggingMiddleware(Middleware):
    """Decorator for logging requests"""

    def handle_request(self, request: Dict[str, Any]) -> None:
        print(f"[LOG] Incoming request: {request}")
        self._handler.handle_request(request)
        print(f"[LOG] Request finished for: {request.get('path')}")


class AuthMiddleware(Middleware):
    """Decorator for authentication"""

    def handle_request(self, request: Dict[str, Any]) -> None:
        if request.get("is_authenticated"):
            print("[AUTH] User is authenticated. Proceeding...")
            self._handler.handle_request(request)
        else:
            print("[AUTH] Authentication FAILED! Request blocked.")
            print("  -> Response generated: 401 Unauthorized")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Decorator Pattern - Middleware Example")
    print("=" * 60)
    print()

    # Core application handler
    app = RequestHandler()

    # 1. Simple Request (No Middleware)
    print("1. Direct Request (No Middleware):")
    print("-" * 60)
    request1 = {"path": "/home", "user": "guest", "is_authenticated": True}
    app.handle_request(request1)
    print()

    # 2. Request with Logging
    print("2. Request with Logging:")
    print("-" * 60)
    logged_app = LoggingMiddleware(app)
    request2 = {"path": "/about", "user": "guest", "is_authenticated": True}
    logged_app.handle_request(request2)
    print()

    # 3. Request with Authentication and Logging
    print("3. Request with Auth + Logging:")
    print("-" * 60)
    secure_app = AuthMiddleware(LoggingMiddleware(app))
    
    # Valid request
    print("Case A: Valid User")
    request3 = {"path": "/dashboard", "user": "admin", "is_authenticated": True}
    secure_app.handle_request(request3)
    print()

    # Invalid request
    print("Case B: Invalid User")
    request4 = {"path": "/dashboard", "user": "hacker", "is_authenticated": False}
    secure_app.handle_request(request4)
    print()

    print("=" * 60)
    print("Key Benefit: We can wrap the core handler with any number of")
    print("middleware layers (Auth, Logging, Caching) dynamically!")
    print("=" * 60)
