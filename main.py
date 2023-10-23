from email_actions.email_fetch import store_emails_to_db, search_messages
from email_actions.api import gmail_authenticate
from email_actions.db import insert_data,table_creation
from email_actions.email_process import email_actions_by_rules

def user_input(service):
    print("Please Enter the Numberic Input for Email Actions")
    option = input("""
    1. To Initialize DB Schemas
    2. To Store Emails in DB
    3. To Process Email based on Rules
    """)
    
    if option == '1':
        table_creation()
    elif option == '2':
        #Script Based on GMAIL API
        store_emails_to_db(service)
    elif option == '3':
        #Script Based on REST API
        email_actions_by_rules()


if __name__ == "__main__":
    service = gmail_authenticate()
    user_input(service)
    # while True:
    #     user_input(service)