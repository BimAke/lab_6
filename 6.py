import datetime
def subtract_days_from_current_date(days):
    current_date = datetime.date.today()
    new_date = current_date - datetime.timedelta(days=days)
    return new_date
new_date = subtract_days_from_current_date(5)
print("Current date:", datetime.date.today())
print("New date:", new_date)
#2
import datetime
def print_dates():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)
print_dates()
#3
from datetime import datetime
def drop_microseconds(date):
    date_without_microseconds = date.replace(microsecond=0)
    return date_without_microseconds
date_with_microseconds = datetime(2022, 1, 1, 12, 30, 45, 123456)
date_without_microseconds = drop_microseconds(date_with_microseconds)
print("Date without microseconds:", date_without_microseconds)

#4
def date_difference(date1, date2):
    date1_obj = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2_obj = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    difference = (date2_obj - date1_obj).total_seconds()
    return difference
date1 = "2022-01-01 00:00:00"
date2 = "2022-01-02 12:00:00"

#1
def square_generator(N):
    for i in range(1, N+1):
        yield i**2
N = 5
squares = square_generator(N)
for square in squares:
    print(square)

#2
def even_generator(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input("Enter a number: "))
even_numbers = even_generator(n)
print(','.join(map(str, even_numbers)))

#3
def divisible_generator(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter number: "))
divisible_numbers = divisible_generator(n)
print(','.join(map(str, divisible_numbers)))

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
square_numbers = squares(a, b)
for number in square_numbers:
    print(number)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i
n = int(input("Enter a number: "))
countdown_numbers = countdown(n)
for number in countdown_numbers:
    print(number)

#1 
import math
degrees = float(input("Input degree: "))
radians = degrees * (math.pi/180)
print("Output radian:", radians)

#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = (base1 + base2) * height / 2
print("Area:", area)


#3
num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", area)

#4
