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
print((lambda x: x + 1)(2))

#2
add_one = lambda x: x + 2
print(add_one(4))

