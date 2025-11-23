## 🌟 Bank Management System
**Simple Console-Based Bank Management System**

## 📖 Overview of the Project
This project is a console-based Bank Management System developed in Python. It is designed to simulate the core operations of a small banking environment, allowing users (bank staff) to register, log in, create new customer accounts, manage deposits, withdrawals, and transaction details.

The system emphasizes **data persistence** by storing all user and customer information (including transaction history) in local JSON files, eliminating the need for a separate database (like MySQL) and ensuring data integrity between program runs.

## ✨ Features
* **Secure Authentication:** User registration and 4-digit password login.
* **Account CRUD:** Create, read (view details), and delete customer bank accounts.
* **Transaction Handling:** Process withdrawals and deposits with balance validation.
* **Reporting:** View current customer details and a detailed history of all transactions for any account.
* **Data Persistence:** All customer and transaction data is stored in `customer_data.json` and `user_data.json`.

## 🛠️ Technologies/Tools Used
* **Core Language:** Python 3.x
* **Data Handling:** `json` module for persistent data storage.
* **Utilities:** `datetime` and `os` modules.
* **Version Control:** Git

## 🚀 Steps to Install & Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone (https://github.com/bhupendra-25bai10468/Bank-Management-System)
    cd bank_management_system
    ```

2.  **Save the Code:**
    Ensure your Python code is saved as a single file named `bank_management_system.py` in the root directory.

3.  **Run the System:**
    Execute the Python file from your terminal:
    ```bash
    python bank_management_system.py
    ```

4.  **Start Interaction:**
    Follow the on-screen prompts:
    * Start by choosing **1. REGISTER** to create a staff user account.
    * Then, choose **2. LOGIN** to access the main bank operations menu.

## 🧪 Instructions for Testing
To test the core functionality, perform the following steps:

1.  **Account Creation (Test CRUD: Create):** Create a new account and verify that the initial deposit is correctly recorded.
2.  **Deposit (Test Transaction):** Add an amount and use option 3 (Customer Details) to verify the balance has increased.
3.  **Withdrawal (Test Transaction & Error Handling):** Attempt a withdrawal.
    * Test a valid withdrawal.
    * Test an invalid withdrawal amount (greater than the balance) to confirm the **insufficient funds** error message.
4.  **Transaction History (Test Reporting):** Use option 4 (Transaction Details) to view the history and confirm all deposits and withdrawals are logged correctly.
5.  **Data Persistence (Test Reliability):** Run the program, perform a transaction, then quit (option 6), and restart the program. Log in and verify that the balance and transaction history are unchanged.
