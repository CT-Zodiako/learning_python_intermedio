from functools import reduce
#higher order functions

def sum_one(value):
    return value+1

def sum_two_values_and_one(firts_value, secont_value, f_sum):
    return f_sum(firts_value + secont_value)

print(sum_two_values_and_one(5,2, sum_one))


#closures

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)

print(add_closure(5))

print(sum_ten(5)(1))

#built_in higher order functions

numbers = [2,5,40,10,21,30]
#map

def multiply(number):
    return number*2

map(multiply,numbers)

print(list(map(multiply,numbers)))
print(list(map(lambda numbers:numbers*2, numbers)))

#filter
def filter_greater_that_ten(number):
    if number>10:
        return True
    else:
        return False

print(list(filter( filter_greater_that_ten, numbers)))
print(list(filter( lambda number: number<10, numbers)))

#reduce
def sum_two_values(first_values,second_value):
    return first_values + second_value

print(reduce(sum_two_values,numbers))

