'''Mean and median '''
# Calculating the mean is quite easy.
# The mean of any set of values is its sum divided by the length of the list.

def calc_mean(nums):
    return sum(nums)/len(nums)

grades = [75, 44, 82, 64, 57, 88, 92, 95, 75, 32, 90, 80, 78, 83]
mean = calc_mean(grades)
print(f'The average grade on the final is {mean:.2f}')

# The median is found by first sorting a list of values, then finding either:
# The value in the middle of an odd length list.
# The mean of the two values in an the middle of an even length list.

# We'll create a discrete variable to hold the length of our list.
# In statistics this is commonly expressed as constant N.
def calc_median(nums):
    N = len(nums)
    nums = sorted(nums)

    if N % 2 == 0:
        middle_index_one = N/2
        middle_index_two = (N/2) + 1

        m1 = int(middle_index_one) - 1 # lists begin at index 0, so we accomodate for that here
        m2 = int(middle_index_two) - 1
        median = (nums[m1] + nums[m2])/2
    else:
        middle = (N+1)/2
        m = int(middle) - 1
        median = nums[m]

    return median

median = calc_median(grades)
print(f'The median grade on the final is {median:.2f}')



