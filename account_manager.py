import datetime as dt
from data_manager import update_user_data, update_customer_data

USER_DATA = {}
CUSTOMER_DATA = {}

def register_user(user_data):
    print('=========== 1. REGISTER ==========')
    while True:
        username = input('Enter a Username: ').strip()
        if not username:
            print('Username cannot be empty.')
            continue
        if username in user_data:
            print('Username already exists.')
        else:
            break
            
    while True:
        pswd = input('Enter a 4 DIGIT Password: ').strip()
        if len(pswd) == 4 and pswd.isdigit():
            break
        else:
            print('Password must be exactly 4 digits.')
            
    user_data[username] = pswd
    update_user_data(user_data)
    print('\nUSER created successfully! Please log in.')

def login_user(user_data):
    print('========== 2. LOGIN ==========')
    username = input('Enter your Username: ').strip()
    password = input('Enter your 4 DIGIT Password: ').strip()

    if username in user_data and user_data[username] == password:
        return username
    else:
        print('\nInvalid username or password.')
        return None

# --- Account CRUD (Create/Read/Delete) ---

def create_account(customer_data):
    print('========== 1. CREATE BANK ACCOUNT ==========')
    while True:
        acc_no = input('Enter your ACCOUNT NUMBER (5 digits): ').strip()
        if len(acc_no) != 5 or not acc_no.isdigit():
             print('Account number must be 5 digits.')
             continue
        if acc_no in customer_data:
            print('Account Number already exists.')
        else:
            break
            
    acc_name = input('Enter your ACCOUNT NAME: ').strip()
    ph_no = input('Enter your PHONE NUMBER: ').strip()
    address = input('Enter your place: ').strip()
    
    while True:
        try:
            cr_amt = float(input('Enter your initial deposit amount (Min 500): '))
            if cr_amt < 500:
                print('Initial deposit must be at least 500.')
                continue
            break
        except ValueError:
            print('Invalid amount.')

    customer_data[acc_no] = {
        'acc_name': acc_name,
        'ph_no': ph_no,
        'address': address,
        'cr_amt': cr_amt,
        'transactions': []
    }
    update_customer_data(customer_data)
    print('\nAccount Created Successfully!!!!!')

def display_customer_details(customer_data):
    print('========== 3. CUSTOMER DETAILS ==========')
    acc_no = input('Enter your account number: ').strip()
    
    if acc_no in customer_data:
        account = customer_data[acc_no]
        print('\n========== Account Details ==========')
        print(f'ACCOUNT NO: {acc_no}')
        print(f'ACCOUNT NAME: {account["acc_name"]}')
        print(f'PHONE NUMBER: {account["ph_no"]}')
        print(f'ADDRESS: {account["address"]}')
        print(f'CURRENT BALANCE: {account["cr_amt"]:.2f}\n')
    else:
        print('\nInvalid Account number.')

def delete_account(customer_data):
    print('========== 5. DELETE ACCOUNT ==========')
    acc_no = input('Enter the account number to DELETE: ').strip()
    
    if acc_no in customer_data:
        del customer_data[acc_no]
        update_customer_data(customer_data)
        print('\nACCOUNT DELETED SUCCESSFULLY!!!')
    else:
        print('\nInvalid Account Number. Deletion failed.') 
