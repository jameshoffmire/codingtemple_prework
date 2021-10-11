from math import inf

#Q1

def hello_name(user_name):
    print('hello ' + user_name + '!')

#Q2

def odd100():
    for i in range(1,101):
        print(i*2-1)

#Q3

def max_num_in_list(a_list):
    max_num = -inf
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

def is_a_leap_year(a_year):
    return (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list),max(a_list)+1))