import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

 
"""
// In Progress

import configparser

def get_config(file_name) -> dict:
    config = configparser.ConfigParser()
    config.read(file_name)
    return config

"""

def get_data(file_name) -> list:
    result = []
    with open(f"./Input/{file_name}", 'r') as file:
        data = file.readlines()
        result = [list(map(float, line.strip().split())) for line in data]
        return result


def calculate(data):
    array_x = [element[0] for element in data]
    array_y = [element[1] for element in data]

    x_avg = sum(array_x) / len(array_x)
    y_avg = sum(array_y) / len(array_y)

    x_squares_avg = sum([x**2 for x in array_x]) / len(array_x)

    xy_avg = sum([x*y for x, y in zip(array_x, array_y)]) / len(array_x)

    k = (xy_avg - (x_avg * y_avg)) / (x_squares_avg - (x_avg ** 2))
    b = y_avg - k * x_avg

    result = {
        'k': k,
        'b': b,
        "array_x": array_x,
        "array_y": array_y
    }

    return result


def make_plot(file_name: str, data: dict):

    # Get data
    array_x = data["array_x"]
    array_y = data["array_y"]
    k = data['k']
    b = data['b']


    scale_coefficient  = 1.05

    # Set domain of definition
    x1_limit = -b / k
    x2_limit = scale_coefficient * (max(array_y) - b) / k

    # Get (X, Y)
    X = np.linspace(x1_limit, x2_limit, 100)
    Y = k*X + b

    fig, ax = plt.subplots()

    # Show Grid
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.tight_layout()

    # Draw axes
    ax.axhline(linewidth=1.5, y=0, color='k')
    ax.axvline(linewidth=1.5, x=0, color='k')

    #plt.xticks(np.arange(np.min(Y), np.max(Y)+1, 2.0))
    #plt.yticks(np.arange(0, np.max(X)+1, 1.0))

    #ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    # Draw Graph
    plt.plot(X, Y, 'b', label=f"y = kx + b")

    # Draw points
    plt.plot(array_x, array_y, 'k+', markersize=10)

    # Show legend
    plt.legend(title=f"k = {k:.2f}, b = {b:.2f}")

    # Save graph to file, then show picture to user
    plt.savefig(f'./Output/{file_name[:-4]}.png')
    plt.show()