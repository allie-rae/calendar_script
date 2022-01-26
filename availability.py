import sys
import json
from pprint import pprint
from datetime import datetime

events_f = open('events.json')
users_f = open('users.json')

events = json.load(events_f)
users = json.load(users_f)

events_f.close()
users_f.close()

def find_availability(str):
  name_arr = str.split(",")
  ids_arr = []
  event_times = []
  find_ids(name_arr, ids_arr)
  find_events(ids_arr, event_times)
  # pprint(event_times)
  remove_events(event_times)
  pprint(event_times)

def remove_events(event_times):
  availability = [
    datetime(2021, 7, 5, 13, 0), 
    datetime(2021, 7, 5, 21, 0), 
    datetime(2021, 7, 6, 13, 0), 
    datetime(2021, 7, 6, 21, 0), 
    datetime(2021, 7, 7, 13, 0), 
    datetime(2021, 7, 7, 21, 0)
    ]
  return availability
  

  

 
def find_ids(names, ids):
  for name in names:
    for user in users:
      if name == user['name']:
        ids.append(user['id'])

def find_events(ids, event_times):
  for id in ids:
    for event in events:
      if id == event['user_id']:
        event_times.append({datetime.fromisoformat(event['start_time']), datetime.fromisoformat(event['end_time'])})




find_availability(sys.argv[1])