import json
from email_actions.utils import mark_as_read,mark_as_unread,delete_messages
from email_actions.db import get_data
from dateutil import parser



sql_translate_dict = {
    "any" : "or" ,
    "all" : "and" ,
    "contains": "like",
    "equals" : "=",
    "lesser_than" : "<",
    "greater_than" : ">",
    "not_equals_to" : "!="
}

action_dict = {
    "mark_as_read" : mark_as_read,
    "mark_as_unread" : mark_as_unread,
    "delete_message": delete_messages
}

def email_actions_by_rules():

    try:
        with open("rules.json", "rb") as rules:
            rules = json.load(rules)
            rule_predicate = rules.get("rule_predicate")
            rule_predicate = sql_translate_dict.get(rule_predicate)
            conditions = rules.get("conditions", [])
            actions = rules.get("actions")

            sql_query =""
            n = len(conditions)
            for i, condition in enumerate(conditions):
                field = condition.get('field')
                predicate = condition.get('predicate')
                predicate = sql_translate_dict.get(predicate)
                value = condition.get('value')

                
                #Change to Contain Format
                if predicate == 'like':
                    value = '%' + value + '%'
                #Change to Date Format
                if field =='created_at':
                    value = str(parser.parse(value))

                if not value.isnumeric():
                    value = F"'{value}'"
                
                curr_query = f" {field} {predicate} {value}"
                if i == n-1:
                    sql_query = sql_query + curr_query
                else:
                    sql_query = sql_query + curr_query + rule_predicate
            
            message_ids = [q[0] for q in get_data(sql_query)]

            action_function = action_dict.get(actions)
            action_function(message_ids)
            print("Action Completed as per rules")
    except:
        pass
