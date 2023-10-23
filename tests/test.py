from email_actions.utils import (
    search_messages, 
    read_message,
    mark_as_read,
    mark_as_unread,
    delete_messages
)
from email_actions.api import gmail_authenticate

service = gmail_authenticate()

def test_search_messages():
    messages = search_messages(service,'', 20)
    assert len(messages) == 20

def test_read_message():
    message = search_messages(service,'', 1)
    response = read_message(service, message[0])
    assert response.get('from')
    assert response.get('to')
    assert response.get('subject')
    assert response.get('date')


def test_mark_as_read():
    message = search_messages(service,'', 1)
    response = mark_as_read([message[0].get('id')])
    assert response.status_code == 204

def test_mark_as_unread():
    message = search_messages(service,'', 1)
    response = mark_as_unread([message[0].get('id')])
    assert response.status_code == 204

def test_delete_messages():
    message = search_messages(service,'', 1)
    response = delete_messages([message[0].get('id')])
    assert response.status_code == 204

# search_messages
# read_message
# mark_as_read
# mark_as_unread
# delete_messages