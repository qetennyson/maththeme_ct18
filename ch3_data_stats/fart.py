from collections import Counter
import csv

def read_csv(filename):
    farters = []
    non_farters = []
    maybe_farters = []

    with open(filename) as my_file:
        reader = csv.reader(my_file)
        next(reader)
        for row in reader:
            if row[2].lower() == 'yes':
                farters.append(row[0])
            elif row[2].lower() == 'maybe':
                maybe_farters.append(row[0])
            else:
                non_farters.append(row[0])

    return farters, maybe_farters, non_farters

farters, maybe_farters, non_farters = read_csv('fart.csv')
print(farters)
print(maybe_farters)
print(non_farters)

def show_farters(farters, maybe_farters, non_farters):
    print('Farters')
    for animal in farters:
        print(f'{animal}')
    print('\n\n')
    print('Maybe Farters')
    for animal in maybe_farters:
        print(f'{animal}')
    print('\n\n')
    print('Non-Farters')
    for animal in non_farters:
        print(f'{animal}')
    print('\n\n')
show_farters(farters, maybe_farters, non_farters)