import random
print ("Random Integer:", random.randint(1,100))
print ("Random float:", random.random())
fruits = ["Apple", "Banana", "Mango"]
print ("Random fruits:",random.choice(fruits))
random.shuffle(fruits)
print("Shuffled List:", fruits)