from email_actions.db import insert_data
from email_actions.utils import search_messages,read_message


def store_emails_to_db(service):
    try:
        query = input("Please Enter the Query: ")
        maxResults = input("Please Enter the Maximum Email to Store: ")
        messages = search_messages(service, query, maxResults)
        sql_values = ""
        for message in messages:
            result = read_message(service, message)
            sql_format = f"('{message.get('id')}','{result.get('from','')}','{result.get('to','')}','{result.get('date','')}','{result.get('subject')}')"
            sql_values = sql_values + ","  +sql_format
        if sql_values:
            insert_data(sql_values[1:])
    except:
        pass


