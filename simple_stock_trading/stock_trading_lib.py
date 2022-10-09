import random

import matplotlib.pyplot as plt
from random import randint

def generate_random_prices_(max_price=10, length=6):
    prices = [randint(1, max_price) for _ in range(length)]
    return prices

def plot_strategy(prices, buy_day, sell_day):
    buy_price = prices[buy_day]
    sell_price = prices[sell_day]
    profit = sell_price - buy_price

    arrow_length = profit * 0.9
    arrow_head_length = abs(profit * 0.1)
    arrow_head_width = 0.1

    ax = plt.axes()
    plt.plot([buy_day, sell_day], [sell_price, sell_price])
    ax.arrow(buy_day, prices[buy_day], 0, arrow_length, head_width=arrow_head_width, head_length=arrow_head_length, fc='k', ec='k')

    plt.annotate("buy for " + str(buy_day), [buy_day + 0.1, buy_price - 0.35])
    plt.annotate("sell for " + str(sell_day), [sell_day + 0.1, sell_price + 0.35])
    plt.annotate("profit=" + str(profit), [buy_day + 0.1, (buy_price + sell_price) / 2])


def plot_prices(prices):
    plt.plot([x for x in range(len(prices))], prices)
    plt.xlim([-0.1, len(prices) - 0.8])
    plt.ylim([0, max(10, max(prices) + 2)])


def show_strategy(prices, buy_day, sell_day):
    assert 0 <= buy_day <= sell_day < len(prices)
    plot_strategy(prices, buy_day, sell_day)
    plot_prices(prices)

    plt.show()


def show_prices(prices):
    plot_prices(prices)
    plt.show()


def find_best_strategy_(prices):
    buy_day = 0
    max_profit = 0
    max_buy_day = 0
    max_sell_day = 0
    for day in range(len(prices)):
        buy_day_price = prices[buy_day]
        if prices[day] < buy_day_price:
            buy_day = day
            continue
        profit = prices[day] - buy_day_price
        if profit > max_profit:
            max_sell_day = day
            max_profit = profit

    return max_profit, max_buy_day, max_sell_day


def check_strategy(prices, buy_day, sell_day, visualize=True):
    if visualize:
        show_strategy(prices, buy_day, sell_day)

    max_profit, _, _ = find_best_strategy_(prices)
    profit = prices[sell_day] - prices[buy_day]
    if profit < max_profit:
        print("Try again :)")
        return False
    else:
        print("Correct!")
        return True


def check_task_1(buy_day, sell_day):
    stock_prices = [7, 1, 5, 3, 6, 4]
    check_strategy(stock_prices, buy_day, sell_day)

# def check_task_1_5(fun):
#     for _ in range(10):
#         prices = generate_random_prices_(10, 3)

def check_task_2(strategies):
    correct_solution = {
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3)
    }

    for strategy in strategies:
        if strategy not in correct_solution:
            print(strategy, "is an invalid strategy for len(prices) == 4")
            return False

    strategies_set = set(strategies)

    if len(strategies_set) != len(strategies):
        print("You listed some strategy twice!")
        return False

    strategies_left = len(correct_solution) - len(strategies_set)

    if strategies_left > 0:
        print("Try finding", strategies_left, "more strategies!")
        return False

    print("Correct!")
    return True

def task_3_solution(prices_len):
    strategies = []
    for sell_day in range(1, prices_len):
        strategies.append((0, sell_day))
    return strategies


def check_task_3(fun):
    for i in range(100):
        user_solution = fun(i)
        correct_solution = task_3_solution(i)
        if set(user_solution) != set(correct_solution):
            print("for prices_len ==", i)
            print("correct answer is ", correct_solution)
            print("but your answer is", user_solution)
            return False
    print("Correct!")
    return True


def task_4_solution(prices_len, buy_day):
    strategies = []
    for sell_day in range(buy_day + 1, prices_len):
        strategies.append((buy_day, sell_day))
    return strategies


def check_task_4(fun):
    for buy_day in range(100):
        for prices_len in range(buy_day, 100):
            user_solution = fun(prices_len, buy_day)
            correct_solution = task_4_solution(prices_len, buy_day)
            if set(user_solution) != set(correct_solution):
                print("for prices_len ==", prices_len, "buy_day ==", buy_day)
                print("correct answer is ", correct_solution)
                print("but your answer is", user_solution)
                return False
    print("Correct!")
    return True


def task_5_solution(prices_len):
    strategies = []
    for buy_day in range(0, prices_len - 1):
        for sell_day in range(buy_day + 1, prices_len):
            strategies.append((buy_day, sell_day))
    return strategies


def check_task_5(fun):
    for prices_len in range(100):
        user_solution = fun(prices_len)
        correct_solution = task_5_solution(prices_len)
        if set(user_solution) != set(correct_solution):
            print("for prices_len ==", prices_len)
            print("correct answer is ", correct_solution)
            print("but your answer is", user_solution)
            return False
    print("Correct!")
    return True


def check_task_6(fun):
    random.seed(346534)
    max_len = 200
    for prices_len in range(3, max_len):
        prices = generate_random_prices_(20, prices_len)
        user_max_profit, user_best_buy_day, user_best_sell_day = fun(prices)
        max_profit, best_buy_day, best_sell_day = find_best_strategy_(prices)
        if user_max_profit != max_profit:
            print("for prices ==", prices)
            print("max_profit ==", max_profit, "best_buy_day ==",
                  best_buy_day, "best_sell_day ==", best_sell_day)
            show_strategy(prices, best_buy_day, best_sell_day)
            print("but your solution is")
            print("max_profit ==", user_max_profit, "best_buy_day ==",
                  user_best_buy_day, "best_sell_day ==", user_best_sell_day)
            show_strategy(prices, user_best_buy_day, user_best_sell_day)
            return False
        if prices_len % 10 == 0:
            print(str(prices_len * 100 / max_len) + "% checked!")
    print("Correct!")
    return True
