from dateutil import parser
import requests
import pickle
import json


def search_messages(service, query='', maxResults=20):
    try:
        result = service.users().messages().list(userId='me',q=query,maxResults=maxResults).execute()
        messages = [ ]
        if 'messages' in result:
            messages.extend(result['messages'])
        return messages
    except:
        pass


def read_message(service, message):
    try:
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()

        payload = msg['payload']
        headers = payload.get("headers")
        result = {}
        if headers:
            # this section prints email basic info 
            for header in headers:
                name = header.get("name")
                value = header.get("value")
                if name.lower() == 'from':
                    # we store the From address
                    result["from"] = value
                if name.lower() == "to":
                    # we store the To address
                    result["to"] = value
                if name.lower() == "subject":
                    result["subject"] = value.replace("'","")
                if name.lower() == "date":
                    result["date"] = parser.parse(value)
                    # we store the date when the message was sent
        return result
    except:
        pass

def get_url_for_messages(user_id='me'):
    url = f"https://gmail.googleapis.com/gmail/v1/users/{user_id}/messages/"
    return url

def access_token():
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)
        return f"Bearer {creds.token}"

def mark_as_read(message_ids):
    try:
        url = get_url_for_messages() + 'batchModify'
        headers = {
            'content-type': 'application/json',
            'Authorization': access_token()
        }
        payload = {
            'ids': message_ids,
            'removeLabelIds': ['UNREAD']
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response
    
    except:
        pass

def mark_as_unread(message_ids):
    try:
        url = get_url_for_messages() + 'batchModify'
        headers = {
            'content-type': 'application/json',
            'Authorization': access_token()
        }
        payload = {
            'ids': message_ids,
            'addLabelIds': ['UNREAD']
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response
    except:
        pass

def delete_messages(message_ids):
    try:
        url = get_url_for_messages() + 'batchDelete'
        headers = {
            'content-type': 'application/json',
            'Authorization': access_token()
        }
        payload = {
            'ids': message_ids
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response
    except:
        pass


