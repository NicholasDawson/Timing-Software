import csv
import time
from string import ascii_letters
import os

acceptable_chars = ascii_letters + '0123456789 '

def get_event_name():
    event_name = input('Enter the name of the event: ')
    for x in event_name:
        if x not in acceptable_chars:
            print('Only use letters, numbers, & spaces!')
            return get_event_name()
    return event_name


def createdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


# --------------------------------------------------------------------
event_name = get_event_name()
number_of_athletes = int(input('Number of athletes participating: '))

createdir('Events')

with open('Events/' + event_name + ' - ' + time.strftime("%m-%d-%Y") + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow([event_name])
    writer.writerow([number_of_athletes])
    writer.writerow(['Bib Number', 'Time'])

print('Event Created!')



