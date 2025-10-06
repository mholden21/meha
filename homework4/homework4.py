fav_foods=["pancakes", "pesto", "mango", "pistachio", "ice cream"]
print(fav_foods[1])
print(fav_foods[4])
fav_foods.append("chicken")
fav_foods.insert(0,"apple")
fav_foods.remove("pesto")
print(len(fav_foods))

for food in fav_foods:
    upper_food=food.upper()
    print(upper_food)

fav_foods2=fav_foods[0::5]
print(fav_foods2)

if "potato" in fav_foods2:
    print("A potato!")
else:
    print("No potato!")
# error:
#AttributeError: 'builtin_function_or_method' object has no attribute 'upper'
#I originally wrote print.upper(food)
#the .upper needed to apply to the food so I rewrote it to food.upper()
numbers=list(range(20))
def get_first_15(numbers):
    return(numbers[0:16])
step1= get_first_15(numbers)
def get_every_5th(lst):
    return(lst[0::5])
step2=get_every_5th(step1)
def reverse_and_stride(lst):
    lst.reverse()
    return(lst[0:2])
step3=reverse_and_stride(step2)
print(step3)
#error
#TypeError: print() got an unexpected keyword argument 'step2'
#I originally wrote print(step3=reverse_and_stride(step2))
#print was confused by = so I just made a new line with print(step3)
nested_numbers= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(nested_numbers[2])
print(nested_numbers[1][1])
nested_numbers.append([10, 11, 12])
def sum_nested(nested_numbers):
    total=0
    for i in nested_numbers:
        for n in i:
            total+=n
    return total
print(sum_nested(nested_numbers))   


def five_by_five():
    nested=[]
    n=1
    for i in range(5):
        row=[]
        for ii in range(5):
            row.append(n)
            n+=1
        nested.append(row)
    return(nested)
fives=five_by_five()
print(fives)
def replace_threes(fives):
    nested2 = []
    for row in fives:
        row2 = []
        for n in row:
            if n % 3 == 0:
                row2.append("?")
            else:
                row2.append(n)
        nested2.append(row2)
    return(nested2)
print(replace_threes(fives))
fives2=replace_threes(fives)
#error
#AttributeError" 'int' object has no attribute 'replace'
#I wanted to replace n with ?, but there is no function called replace
#I rewrote the function by creating a whole new nested list and appending every single value
def sumnation(fives2):
    total = 0
    for row in fives2:
        for n in row:
            if n != "?":
                total+=n
    return total
print(sumnation(fives2))


ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for key in ages:
    value = ages[key]
    print(f"Name: {key}, Age: {value}")

    
print(five_by_five())