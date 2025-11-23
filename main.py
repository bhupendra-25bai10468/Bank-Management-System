import datetime as dt
import account_manager as am
import transaction_manager as tl
from data_manager import initialize_data

USER_DATA, CUSTOMER_DATA = initialize_data()
LOGGED_IN_USER = None

am.USER_DATA = USER_DATA
am.CUSTOMER_DATA = CUSTOMER_DATA
tl.CUSTOMER_DATA = CUSTOMER_DATA

def main_menu():
    global LOGGED_IN_USER
    while True:
        print(f'\n================ BANK OPERATIONS MENU (User: {LOGGED_IN_USER}) ================')
        print('1. CREATE BANK ACCOUNT')
        print('2. TRANSACTION (Withdraw/Deposit)')
        print('3. CUSTOMER DETAILS')
        print('4. TRANSACTION DETAILS')
        print('5. DELETE ACCOUNT')
        print('6. LOGOUT')
        print('==============================================================================')
        
        try:
            n = int(input('Enter your CHOICE: '))
            print()
            
            if n == 1:
                am.create_account(CUSTOMER_DATA)
            elif n == 2:
                tl.handle_transaction(CUSTOMER_DATA)
            elif n == 3:
                am.display_customer_details(CUSTOMER_DATA)
            elif n == 4:
                tl.display_transaction_details(CUSTOMER_DATA)
            elif n == 5:
                am.delete_account(CUSTOMER_DATA)
            elif n == 6:
                LOGGED_IN_USER = None
                print('\nLOGGED OUT. Returning to startup menu.')
                break
            else:
                print('Invalid choice. Please enter a valid number between 1 and 6.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def startup_menu():
    print('====================== WELCOME TO BANK OF PYTHON =======================')
    print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('\n1. REGISTER')
    print('2. LOGIN')
    print('3. EXIT PROGRAM')
    print('========================================================================')
    
    try:
        n = int(input('Enter your choice: '))
        print()
        
        if n == 1:
            am.register_user(USER_DATA)
        elif n == 2:
            logged_in = am.login_user(USER_DATA)
            if logged_in:
                global LOGGED_IN_USER
                LOGGED_IN_USER = logged_in
                main_menu()
        elif n == 3:
            print('\nExiting Program. Goodbye!')
            return False
        else:
            print('Invalid choice.')
            
    except ValueError:
        print('Invalid input. Please enter a number.')
    return True

# --- Main Execution ---
if __name__ == '__main__':
    while startup_menu():
        pass
