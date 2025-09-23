def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("Meha")
def area_of_circle(number):
    print((number**2)*3.14)
area_of_circle(1)
def subtract(a, b):
    return(a-b)
def multiply(a, b):
    return(a*b)
def divide(a, b):
    return(a/b)
def max_min_temp(temperatures):
    min_temp=min(temperatures)
    max_temp=max(temperatures)
    return max_temp, min_temp
today_temps=[46,74,90,89]
print(max_min_temp(today_temps))
def is_weekend(day_number):
    if day_number == 6 or 7:
        return "True"
    else:
        return "False"
print(is_weekend(6))
def fuel_efficiency(miles, gallons):
    return(miles/gallons)
print(fuel_efficiency(80,5))
def power(x, y):
    answer = 1
    for _ in range(abs(y)):
        answer *= x
    return answer
print(power(4,3))
def maximum(number_list):
    max_value=number_list[0]
    for numbers in number_list[1:]:
        if numbers > max_value:
            max_value=numbers
    return max_value
print(maximum([2, 1, 4, 3, 7]))
def minimum(number_list):
    min_value=number_list[0]
    for numbers in number_list:
        if numbers < min_value:
            min_value=numbers
    return min_value
print(minimum([2, 1, 4, 9]))
def maximum2(number_list):
    max_value=number_list[0]
    i=1
    while i < len(number_list):
        if number_list[i]>max_value:
            max_value = number_list[i]
        i+=1
    return max_value
print(maximum2([4,5,3,9,2]))
def minimum2(number_list):
    min_value=number_list[0]
    i=1
    while i < len(number_list):
        if number_list[i]<min_value:
            min_value=number_list[i]
        i += 1
    return min_value
print(minimum2([3,4,9,2,10]))
def sum_of_digits(number):
    sum=0
    while number > 0:
        sum += number % 10
        number //=10
    return sum
print(sum_of_digits(4209))

result = maximum([3, 9, 8, 1, 5])
print(f"The result of Max Loops without the for function (6.2.1) with the list being [3, 9, 8, 1, 5] is {result}")



    






      
        


        


    

    
    
    
    
