''' Everything we've done up to this point has been interesting,
but relatively useless from a visualization standpoint. '''
import random
from collections import Counter

movie_ratings = [random.randint(1,5) for i in range(101)]

def get_freq_table(nums):
    table = Counter(nums)
    print('Number\tFrequency')
    for number in table.most_common():
        print('{0}\t\t{1}'.format(number[0], number[1]))

get_freq_table(movie_ratings)
