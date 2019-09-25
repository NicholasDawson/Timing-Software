from time import time
import csv
from tkinter.filedialog import askopenfilename
from tkinter import Tk


def load_event():
    Tk().withdraw()
    event_file = askopenfilename(title='Choose your event file')
    if event_file[-3:] == 'csv':
        return event_file
    elif event_file == '':
        exit()
    else:
        print('Invalid File Type, Choose CSV!')
        return load_event()


event_file = load_event()
number_of_racers = 0

with open(event_file, 'r', newline='') as event:
    reader = csv.reader(event)
    number_of_racers = int(list(reader)[1][0])

wait_for_start = input('Press "Enter" to start race...')
start_time = time()

print('-' * 15)
print('Race Started!')
print('-' * 15)
print('Press "Enter" to record each athletes time...')

with open(event_file, 'a', newline='') as event:
    writer = csv.writer(event)
    for x in range(number_of_racers):
        wait_for_athlete = input()
        athlete_time = time()
        writer.writerow(['', athlete_time - start_time])
        print('Athlete ' + str(x + 1) + ' Completed!')

print('-' * 15)
print('Race Complete!')

