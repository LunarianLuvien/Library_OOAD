# OOAD Course Project - Basic Library Management System

## Project Overview
This project is a basic library management system developed as part of an Object-Oriented Analysis and Design (OOAD) course. The system is designed using Domain-Driven Design (DDD) principles to ensure that the implementation closely aligns with the domain complexities and requirements of library management.

## Key Features
- **Registration:** Users can register in the system, creating their own accounts to manage their interactions with the library.
- **Borrowing:** Registered users can borrow books from the library. The system tracks borrowed books, due dates, and manages the return process.

## Technologies Used
- **Flask:** A micro web framework written in Python, used to build the web interface for the library system. Flask is chosen for its simplicity and flexibility, allowing for quick development and easy integration with other components.
- **SQLAlchemy:** An SQL toolkit and Object-Relational Mapping (ORM) system for Python. It provides a high-level interface to common database operations, making it easier to manage database transactions in Pythonic fashion. It supports various database systems and simplifies database manipulation.

## Design Approach
The system is designed using domain-driven design, a methodology that emphasizes the importance of basing the design on the real-world business domain. This approach ensures that the system functionality aligns closely with the needs of users and library management practices, promoting a more intuitive and effective system.

## Implementation Details
- **User Interface:** Simple and user-friendly web interfaces for different types of users (e.g., librarians and borrowers).
- **Database Design:** Utilizing SQLAlchemy, the database schema is designed to efficiently handle operations like book searches, borrowings, and returns.

## Conclusion
This OOAD course project aims to provide a practical implementation of a library management system, demonstrating the application of domain-driven design principles using modern software development tools and frameworks like Flask and SQLAlchemy.
