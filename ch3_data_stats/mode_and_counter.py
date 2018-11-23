''' Finding the mode of a list of value, and building a frequency table with Counter'''
from collections import Counter
import random

# Counter is a powerful tool.
movie_ratings_s = [1, 2, 3, 3, 4, 4, 4, 5, 5]
c = Counter(movie_ratings_s)
print(c.most_common())

def calc_mode(nums):
    c = Counter(nums)
    mode = c.most_common(1)
    return mode[0][0]

if __name__ == '__main__':
    # Using a list comprehension because I'm tired of writing random lists of integers at this point!
    movie_ratings = [random.randint(1,5) for i in range(1, 101)]
    print(movie_ratings)
    mode = calc_mode(movie_ratings)
    print(f'The mode of the movie ratings list is {mode}')

# However, we have a problem if we've got multiple values that appear the "mode" number of times.
# Let's handle that

def calc_all_modes(nums):

    c = Counter(nums)
    num_freq = c.most_common()
    print(num_freq)
    # We're only interested in the numbers that appears the MOST amount of times, not the mostly most or sort of most.
    max_count = num_freq[0][1] # now we have a variable representing the highest possible count.

    modes = []
    for num in num_freq:
        if num[1] == max_count:
            modes.append(num[0]) # only if value has a count == to the max_count will we append to modes

    return modes

movie_ratings_2 = [random.randint(1,5) for i in range(1, 101)]
modes = calc_all_modes(movie_ratings_2)
print(modes)

