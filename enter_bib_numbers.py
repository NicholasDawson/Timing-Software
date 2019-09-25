import csv
from shutil import move
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

with open(event_file, 'r', newline='') as source:
    reader = list(csv.reader(source))
    with open('temp.csv', 'a', newline='') as new:
        writer = csv.writer(new)
        for x in range(3):
            writer.writerow(reader[x])

        print('Enter each bib number from fastest to slowest...')
        for x in range(int(reader[1][0])):
            bib = input('Bib: ')
            writer.writerow([bib, reader[x+3][1]])

move('temp.csv', event_file)
print('All Bibs Entered!')
print('Open the event file to view the results!')
print('Feel free to add more columns of data as you wish.')



