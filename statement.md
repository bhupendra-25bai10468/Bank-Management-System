# Project Statement

## 1. Problem Statement
The primary challenge in developing basic management systems is ensuring **data persistence and integrity** without relying on complex, external database infrastructure (like MySQL or PostgreSQL) for simple applications. This project addresses the need for a reliable, console-based solution to manage customer bank accounts where data must be safely stored and retrieved across multiple sessions using standard Python tools.

## 2. Objectives
* To design and implement a **modular and clean** console application for bank account management.
* To effectively utilize Python's `json` library for durable, non-volatile data storage.
* To demonstrate the implementation of core banking functionalities, including **CRUD operations** for accounts and detailed **transaction logging**[cite: 29].
* To integrate essential non-functional requirements such as **error handling** and input validation for a robust user experience.

## 3. Scope of the Project
This project focuses on the back-end logic of account management.
* **Included:** Staff user authentication, customer account creation and deletion, balance management, transaction logging (deposit/withdrawal), and customer data retrieval.
* **Excluded (Future Enhancements):** Advanced features like interest calculation, account transfers between customers, graphical user interfaces (GUI), and network security.

## 4. Target Users
The primary target users are:
1.  **Bank Staff/Administrators:** Individuals responsible for managing customer accounts (e.g., creating accounts, processing transactions, viewing records).
2.  **Students/Developers:** The system serves as a practical, easy-to-understand model for applying concepts of data structures, algorithms, and file handling in Python.

## 5. High-Level Features
* Staff Login and Registration.
* Customer Account Creation (`create_account`).
* Fund Withdrawal and Deposit (`handle_transaction`).
* Account Information Lookup (`display_customer_details`).
* Full Transaction History Report (`display_transaction_details`).
