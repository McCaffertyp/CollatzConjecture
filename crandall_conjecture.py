import sys
import matplotlib.pyplot as HarryPlotter
from typing import List

import helpers

# Crandall Conjecture problem is a graphing problem.
# This problem analyzes a pattern based off only positive integers.
# For odd positive integers: 3x + 1, and for even positive integers: x / 2.
# The premise is that all graphs following this pattern eventually come back to 1.


def cc_odd_func(x: int) -> int:
    return (3 * x) + 1


def cc_odd_func_adjusted(x: int) -> int:
    return int(((3 * x) + 1) / 2)


def cc_even_func(x: int) -> int:
    return int(x / 2)


def get_plot_points(x: int) -> List[int]:
    plot_points: List[int] = [x]
    while x > 1:
        if helpers.is_odd(x):
            x = cc_odd_func(x)
        else:
            x = cc_even_func(x)
        plot_points.append(x)
    # print("For original value = {0}, value_storage = {1}".format(og_x, plot_points))
    return plot_points


def get_plot_points_adjusted(x: int) -> List[int]:
    plot_points: List[int] = [x]
    while x > 1:
        if helpers.is_odd(x):
            x = cc_odd_func_adjusted(x)
        else:
            x = cc_even_func(x)
        plot_points.append(x)
    # print("For original value = {0}, value_storage = {1}".format(og_x, plot_points))
    return plot_points


def plot_graph(plot_points: List[int], plot_points_adjusted: List[int] = None):
    plot_point_count_increment = [i for i in range(1, (len(plot_points) + 1))]
    HarryPlotter.plot(
        plot_point_count_increment, plot_points, color="blue", linestyle="--",
        linewidth=2, marker="o", markerfacecolor="white", markersize=4, label="CC_OG"
    )
    for i in range(0, len(plot_points)):
        x_loc = plot_point_count_increment[i]
        y_loc = plot_points[i]
        HarryPlotter.text(x_loc, y_loc, "{0}".format(y_loc))

    if plot_points_adjusted is not None:
        plot_points_adjusted_count_increment = [i for i in range(1, (len(plot_points_adjusted) + 1))]
        HarryPlotter.plot(
            plot_points_adjusted_count_increment, plot_points_adjusted, color="orange", linestyle="--",
            linewidth=2, marker="o", markerfacecolor="white", markersize=4, label="CC_ADJ"
        )
        for i in range(0, len(plot_points_adjusted)):
            x_loc = plot_point_count_increment[i]
            y_loc = plot_points_adjusted[i]
            HarryPlotter.text(x_loc, y_loc, "{0}".format(y_loc))

    HarryPlotter.xlabel("Plot Increment")
    HarryPlotter.ylabel("Plot Points")
    HarryPlotter.title("Crandall Conjecture Graphing")
    HarryPlotter.show()


def run():
    print("=================================================")
    print("Starting program for Crandall Conjecture analysis")
    print("=================================================")

    int_start = 1
    int_end = sys.maxsize
    # int_end = 5000
    # int_start = int_end - 1
    f2p_nums = []
    for i in range(int_start, int_end):
        if helpers.is_p2f(i):
            f2p_nums.append(i)

    print(f2p_nums)

    # num = 85
    # plot_points_og = get_plot_points(num)
    # plot_points_adjusted = get_plot_points_adjusted(num)
    # plot_graph(plot_points_og, plot_points_adjusted)

    # num2 = 2096
    # plot_points_og = get_plot_points(num2)
    # plot_points_adjusted = get_plot_points_adjusted(num2)
    # plot_graph(plot_points_og, plot_points_adjusted)


run()
