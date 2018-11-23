from collections import Counter
import csv

import matplotlib.pyplot as plt

def read_csv(filename):
    jobs = []
    ages = []

    with open(filename) as my_file:
        reader = csv.reader(my_file)
        next(reader)
        for row in reader:
            jobs.append(row[5])
            ages.append(row[3])

    return jobs, ages

jobs, ages = read_csv('insert exciting file containing ages and jobs here')

def get_age_count(ages):
    c = Counter(ages)
    ages = c.most_common()
    return ages

def get_job_count(jobs):
    c = Counter(jobs)
    jobs = c.most_common()
    return jobs

def show_ages(ages):
    print('Age\tFrequency')
    for age in ages:
        print(f'{age[0]}\t\t{age[1]}')

def show_jobs(jobs):
    print('Job\tFrequency')
    for job in jobs:
        print(f'{job[0]}\t\t{job[1]}')

show_ages(get_age_count(ages))
show_jobs(get_job_count(jobs))



