# Factory Pattern - Example 2: Database Connections

## Problem Description

An application needs to connect to different database types (MySQL, PostgreSQL, MongoDB) based on configuration. The Factory pattern encapsulates database connection creation logic, allowing the application to work with any database without knowing the specific connection implementation.

**Real-world usage**: Used in ORM frameworks (Hibernate, SQLAlchemy), connection pooling libraries, database migration tools, and enterprise applications with multiple database backends.

## Class Diagram

```
                    ┌─────────────────────┐
                    │  DatabaseFactory     │
                    │  (Factory)          │
                    ├─────────────────────┤
                    │ + createConnection( │
                    │        dbType)      │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  DatabaseConnection │
                    │  (Product)          │
                    ├─────────────────────┤
                    │ + connect()         │
                    │ + executeQuery()    │
                    │ + close()           │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │  MySQLConnection │ │PostgreSQL  │ │MongoDB    │
    │                  │ │Connection  │ │Connection │
    ├──────────────────┤ ├────────────┤ ├───────────┤
    │ + connect()      │ │ + connect()│ │ + connect()│
    │ + executeQuery() │ │ + execute()│ │ + find()   │
    │ + close()        │ │ + close() │ │ + close()  │
    └──────────────────┘ └────────────┘ └───────────┘
```

