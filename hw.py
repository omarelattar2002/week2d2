# "Example" -> 3
# "Hello World" -> 3
# "Brian" -> 2
# "This is a longer response" -> 8
count=0

vowels='aeiouAEIOU'

username=input("what is your name ")

for x in range(len(username)):
    if username[x] in vowels:
        count += 1

print(f"Hello {username} you {count} amount of vowels in your name")

















# Hint: Use help(str) to see methods on string object
names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']
# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Output - ['Connor', 'Connor', 'Connor', 'Evan', 'Evan', 'Kevin']


for name in names1:
    if len(name) < 4:
        names1.remove(name)
print(names1.title())
#I tried to capitilize it but it wouldn't work





