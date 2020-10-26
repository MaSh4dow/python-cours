from art import *

def say_hello(name):
    print("Hello " + name)
    print(f"How are you {name} ?")

n = "Kilian"
say_hello(n)
h = art("Hello")
print(h)
print(text2art("Hello", font='block'))
print("Yo", font='block')