x = "Jesper"

def myfun():
    x = "Kasper"
    print("Hej med dig, " + x)

myfun()

print("Hej " + x)

x = "Jonas"
def myfun2():
    global x
    x = "Google"

myfun2()

print("Hej " + x)