import datetime as dt
from data_manager import update_customer_data

CUSTOMER_DATA = {}

def handle_transaction(customer_data):
    print('========== 2. TRANSACTION ==========')
    acc_no = input('Enter Your Account Number: ').strip()

    if acc_no not in customer_data:
        print('\nAccount Number Invalid. Sorry, try again later.')
        return

    account = customer_data[acc_no]
    
    print('\n1. WITHDRAW AMOUNT\n2. ADD AMOUNT')
    try:
        choice = int(input('Enter your CHOICE: '))
    except ValueError:
        print('\nInvalid choice.')
        return

    if choice == 1:
        #withdrawl
        while True:
            try:
                amt = float(input('Enter withdrawal amount: '))
                if amt <= 0:
                    print('Amount must be positive.')
                    continue
                if amt > account['cr_amt']: 
                    print(f"Insufficient funds. Current balance: {account['cr_amt']:.2f}")
                    continue
                break
            except ValueError:
                print('Invalid amount.')
                
        account['cr_amt'] -= amt

        transaction = {
            'date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': 'Withdrawal',
            'amount': amt,
            'new_balance': account['cr_amt']
        }
        account['transactions'].append(transaction)
        print('\nWithdrawal successful. Account Updated Successfully!!!')

    elif choice == 2:
        # Deposit
        while True:
            try:
                amt = float(input('Enter amount to be added: '))
                if amt <= 0:
                    print('Amount must be positive.')
                    continue
                break
            except ValueError:
                print('Invalid amount.')
                
        account['cr_amt'] += amt
        
        # Log transaction
        transaction = {
            'date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': 'Deposit',
            'amount': amt,
            'new_balance': account['cr_amt']
        }
        account['transactions'].append(transaction)
        print('\nDeposit successful. Account Updated Successfully!!!')
    
    else:
        print('Invalid choice.')
        
    update_customer_data(customer_data)

def display_transaction_details(customer_data):
    print('--- 4. TRANSACTION DETAILS ---')
    acc_no = input('Enter your account number: ').strip()
    
    if acc_no in customer_data:
        transactions = customer_data[acc_no].get('transactions', [])
        
        if not transactions:
            print('\nNo transactions found for this account.')
            return

        print('\n========== Transaction History ==========')
        for i, tx in enumerate(transactions):
            print(f'-- Transaction {i+1} --')
            print(f'DATE: {tx["date"]}')
            print(f'TYPE: {tx["type"]}')
            print(f'AMOUNT: {tx["amount"]:.2f}')
            print(f'NEW BALANCE: {tx["new_balance"]:.2f}')
            print('=======================================')
        
    else:
        print('\nInvalid Account number.')
        
