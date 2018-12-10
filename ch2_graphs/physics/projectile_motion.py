import matplotlib.pyplot as plt
import math

#TODO: Research math principles for this problem.

''' There is no built-in function for creating ranges
of floats, so we'll make our own!'''
def float_range(start, final, increment):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

''' Draw the trajectory of an object in projectile motion'''

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def draw_trajectory(u, theta):

    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2*u*math.sin(theta)/g

    # Find time intervals
    intervals = float_range(0, t_flight, 0.001)

    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x, y)

def user_velocities():
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print("Invalid input.")
    else:
        draw_trajectory(u, theta)
        plt.show()

def test_velocities():

    u_list = [20, 40, 60]
    theta = 45

    for u in u_list:
        draw_trajectory(u, theta)

    plt.legend(['20', '40', '60'])
    plt.show()

# user entry

if __name__ == '__main__':
    cmd = input("1. User Velocities \n"
                "2. Test Velocities\n")
    if cmd == '1':
        user_velocities()
    else:
        test_velocities()

