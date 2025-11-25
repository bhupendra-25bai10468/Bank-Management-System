# Bank Management System

## Overview

This is a modular, console-based Bank Management System developed in Python. The application simulates essential operations in a banking environment, providing secure authentication, customer account management, transaction processing, error handling, and persistent data storage using JSON files.

## Problem Statement

The project demonstrates core banking operations without using an external database, focusing on practical file I/O, modular programming, and thorough input validation.

## Features

- Secure staff registration and login
- Customer account creation, viewing, and deletion
- Deposit and withdrawal processing with balance checks
- Detailed transaction history per account
- Persistent data using JSON files
- User-friendly, menu-driven console interface

## Functional Requirements

- Staff registration and 4-digit password login
- CRUD operations for customer accounts
- Deposit and withdrawal transactions
- Customer details viewing
- Transaction logs for every account
- Account deletion

## Non-Functional Requirements

- **Reliability:** Data persists between runs via JSON files
- **Error Handling:** Input validation for all critical fields
- **Usability:** Simple menu navigation flow
- **Maintainability:** Modular code layout for future enhancements

## System Architecture

Three-tier modular design:
- **Presentation:** `mainapp.py` (UI and menu flow)
- **Business Logic:** `accountmanager.py` (auth/CRUD), `transactionmanager.py` (transactions/reports)
- **Data Access:** `datamanager.py` (JSON file I/O)
- **Data Storage:** `userdata.json`, `customerdata.json`
  

## Design Diagrams

- **Use Case Diagram:** Shows main user flows (register, login, manage accounts, perform transactions)
- **Workflow Diagram:** Visualizes menu choices and program logic
- **Sequence Diagram:** Describes the steps during deposit/withdrawal transactions
- **Class/Component Diagram:** Highlights code modules and relationships
- **ER Diagram:** Shows tables (users, customers, transactions)


## Installation

1. Install Python 3.x
2. Clone this repository:
git clone https://github.com/bhupendra-25bai10468/Bank-Management-System.git
3. Navigate to the project folder and run:
python mainapp.py

## Instructions for Testing

- Register a staff user and log in
- Create a customer account, verify addition
- Perform valid and invalid deposits/withdrawals
- View customer details and transaction logs
- Exit and restart the program to verify data persistence
- Delete accounts to test removal


## Future Enhancements

- Interest calculation for savings accounts
- Account-to-account transfers
- Upgrade interface with a simple GUI (Tkinter/PyQt)
- Enhanced password security (hashing/encryption)

## References

- [Python 3 Documentation](https://docs.python.org/3)
- Real Python Tutorials
- VITyarthi Project Guidelines
- Course resources

