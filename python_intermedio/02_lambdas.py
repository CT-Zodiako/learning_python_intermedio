#lambdas

sum_two_values = lambda first_value, secont_value: first_value + secont_value

print(sum_two_values(1,2))



def sum_values(value):
    return lambda first_value,secont_value:first_value+secont_value+value


my_sum= sum_values(5)(2,4)
print(my_sum)


