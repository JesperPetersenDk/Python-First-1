print("for in")
for i in [0, 1, 2, 3]:
    print(i)

v = 4
print("Range 4")
for i in range(v):
    print(i)


print("Enumerate")
for idx, value in enumerate(range(8,0,-1)):
    print(idx, value)

print("Apply (Tal information)")
def apply(plus, min):
    result = plus + min
    print(result)

apply(100, -20)

print("Crew list")
def hire_crew(*sailors):
    for sailor in sailors:
        print('- ' + sailor)

hire_crew('Mads', 'Jesper', 'Sofie', 'Jonas')

#Lambda funtion
#1
print("First Lambda")
print((lambda x: x + 1)(2))

#2
print("two")
add_one = lambda x: x + 2
print(add_one(4))

print("three")
high_ord_func = lambda x, func: x + func(x)
x = high_ord_func(5, lambda x: x*x)
print(x)

print("Filter + lambda")
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list) 

other_list = list(map(lambda x: x*2, li))
print(other_list)

print("Random")
import random
for idxx in range(0,10):
    dice = random.choice(li)
    print(idxx, dice)

