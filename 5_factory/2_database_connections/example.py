"""
Factory Pattern - Database Connections Example
Real-world usage: ORM frameworks, connection pools, migration tools, enterprise apps
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Any


class DatabaseType(Enum):
    """Database types"""
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"


# Product interface
class DatabaseConnection(ABC):
    """Abstract database connection"""
    
    @abstractmethod
    def connect(self) -> bool:
        """Establish database connection"""
        pass
    
    @abstractmethod
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """Execute a query"""
        pass
    
    @abstractmethod
    def close(self) -> bool:
        """Close the connection"""
        pass
    
    @abstractmethod
    def get_database_type(self) -> str:
        """Get database type"""
        pass


# Concrete products
class MySQLConnection(DatabaseConnection):
    """MySQL database connection"""
    
    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password
        self._connected = False
    
    def connect(self) -> bool:
        print(f"🔌 Connecting to MySQL at {self._host}:{self._port}")
        print(f"   Database: {self._database}, User: {self._user}")
        # Simulate connection
        self._connected = True
        print("✅ MySQL connection established")
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        if not self._connected:
            raise ConnectionError("Not connected to database")
        print(f"📊 Executing MySQL query: {query}")
        # Simulate query execution
        return [
            {"id": 1, "name": "John", "email": "john@example.com"},
            {"id": 2, "name": "Jane", "email": "jane@example.com"}
        ]
    
    def close(self) -> bool:
        if self._connected:
            print("🔌 Closing MySQL connection")
            self._connected = False
            return True
        return False
    
    def get_database_type(self) -> str:
        return "MySQL"


class PostgreSQLConnection(DatabaseConnection):
    """PostgreSQL database connection"""
    
    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password
        self._connected = False
    
    def connect(self) -> bool:
        print(f"🔌 Connecting to PostgreSQL at {self._host}:{self._port}")
        print(f"   Database: {self._database}, User: {self._user}")
        # Simulate connection
        self._connected = True
        print("✅ PostgreSQL connection established")
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        if not self._connected:
            raise ConnectionError("Not connected to database")
        print(f"📊 Executing PostgreSQL query: {query}")
        # Simulate query execution
        return [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ]
    
    def close(self) -> bool:
        if self._connected:
            print("🔌 Closing PostgreSQL connection")
            self._connected = False
            return True
        return False
    
    def get_database_type(self) -> str:
        return "PostgreSQL"


class MongoDBConnection(DatabaseConnection):
    """MongoDB database connection"""
    
    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password
        self._connected = False
    
    def connect(self) -> bool:
        print(f"🔌 Connecting to MongoDB at {self._host}:{self._port}")
        print(f"   Database: {self._database}, User: {self._user}")
        # Simulate connection
        self._connected = True
        print("✅ MongoDB connection established")
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        if not self._connected:
            raise ConnectionError("Not connected to database")
        print(f"📊 Executing MongoDB query: {query}")
        # Simulate query execution (MongoDB uses different syntax)
        return [
            {"_id": "507f1f77bcf86cd799439011", "name": "Charlie", "email": "charlie@example.com"},
            {"_id": "507f191e810c19729de860ea", "name": "Diana", "email": "diana@example.com"}
        ]
    
    def close(self) -> bool:
        if self._connected:
            print("🔌 Closing MongoDB connection")
            self._connected = False
            return True
        return False
    
    def get_database_type(self) -> str:
        return "MongoDB"


# Factory class
class DatabaseFactory:
    """Factory for creating database connections"""
    
    @staticmethod
    def create_connection(
        db_type: DatabaseType,
        host: str,
        port: int,
        database: str,
        user: str,
        password: str
    ) -> DatabaseConnection:
        """Factory method to create appropriate database connection"""
        if db_type == DatabaseType.MYSQL:
            return MySQLConnection(host, port, database, user, password)
        elif db_type == DatabaseType.POSTGRESQL:
            return PostgreSQLConnection(host, port, database, user, password)
        elif db_type == DatabaseType.MONGODB:
            return MongoDBConnection(host, port, database, user, password)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")


# Application class
class DatabaseManager:
    """Application that uses database factory"""
    
    def __init__(self, db_type: DatabaseType, connection_config: Dict[str, Any]):
        self._connection = DatabaseFactory.create_connection(
            db_type,
            connection_config["host"],
            connection_config["port"],
            connection_config["database"],
            connection_config["user"],
            connection_config["password"]
        )
    
    def run_query(self, query: str):
        """Run a query using the connection"""
        self._connection.connect()
        try:
            results = self._connection.execute_query(query)
            print(f"📋 Results from {self._connection.get_database_type()}:")
            for row in results:
                print(f"   {row}")
        finally:
            self._connection.close()


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Factory Pattern - Database Connections Example")
    print("=" * 60)
    print()
    
    # MySQL connection
    print("1. MySQL Connection:")
    print("-" * 60)
    mysql_config = {
        "host": "localhost",
        "port": 3306,
        "database": "mydb",
        "user": "root",
        "password": "password123"
    }
    mysql_manager = DatabaseManager(DatabaseType.MYSQL, mysql_config)
    mysql_manager.run_query("SELECT * FROM users LIMIT 2")
    print()
    
    # PostgreSQL connection
    print("2. PostgreSQL Connection:")
    print("-" * 60)
    postgres_config = {
        "host": "localhost",
        "port": 5432,
        "database": "mydb",
        "user": "postgres",
        "password": "password123"
    }
    postgres_manager = DatabaseManager(DatabaseType.POSTGRESQL, postgres_config)
    postgres_manager.run_query("SELECT * FROM users LIMIT 2")
    print()
    
    # MongoDB connection
    print("3. MongoDB Connection:")
    print("-" * 60)
    mongo_config = {
        "host": "localhost",
        "port": 27017,
        "database": "mydb",
        "user": "admin",
        "password": "password123"
    }
    mongo_manager = DatabaseManager(DatabaseType.MONGODB, mongo_config)
    mongo_manager.run_query("db.users.find().limit(2)")
    print()
    
    print("=" * 60)
    print("Key Benefit: Application doesn't need to know how to create")
    print("specific database connections - factory handles it!")
    print("=" * 60)

