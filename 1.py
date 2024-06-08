for i in range(10, 0, -1):
    print ("I ate", i, "bananas")
    
    
nie = 0

while nie < 5:
    print ("Skończyły mi się bananas")
    nie = nie + 1
    
fruit = ['apple', 'pineapple', 'water arbuz']

print ("ale nie skonczyly mi sie", fruit[0],"s")

fruit[0] = "pear"

print ("I prefer", fruit[0],"s")

for dupa in fruit:
    print ("nie masz bananasow, tylko masz", dupa)
    
name = input("What is your name?")
print("Hello", name)

r = input("ile razy napisac abca????????")
ilo = 0
while ilo < int(r):
    ilo += 1
    print ("abca")
    
    
a = "5"
b = 4

c = int(a) + b  

print (c)  

read_only_fruit = ('fajny fruit', 'orangarańcza', 'straw berry')

for owoc in read_only_fruit:
    print (owoc)

print('Now we get an error.')
read_only_fruit[0] = 'apple'