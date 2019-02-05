# Conditions

a=32
b=44
c=55
if a == b:
    print("a == b")
elif a > b:
    print("a > b")
else:
    print("a < b")

if a > b: print('yes') # one liner if statement
print("Yo") if a > b else print("Sup") # one-liner if/else

# One-liner if/else with three conditions
print('Gee') if a > b else print ("hmm") if a == b else print("This")

# And don't forget:
if a > b or a > c: # or use 'and' but not '&&' or '||'
    print:("The horror!")

# while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # means 'skip this one'
    if i == 5:
        break
    print(i)

# for loop
greeting = 'Hello, there. Nice to see ya.'
for i in greeting:
    if i == 'e':
        continue
    print(i)

for i in range(6): # range is 0-5
    print(i)

for i in range(2, 6): # range is 2-5
    print(i)

for i in range(2, 18, 3): # range is 2-18, incremented by 3
    print(i)
