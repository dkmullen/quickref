types_of_people = 10
x = f"There are {types_of_people} types of people." # the 'f' tells py to format
binary = "binary"
do_not = "don't"
y = f"  Those who know {binary} and those who {do_not}."
z = float(2.6)
exp = 5**3 # 5 to the third
power = 5e3 # Five times (ten to the third) - 'e' can be 'E'
myComplex = 5j # 'j' stands for the imaginary part

print(x)
print(y)
print(y.strip()) # removes whitespace from beginning and/or end
print(len(y))
print(y.upper())
print(y.lower())
print(y.split(' ')) # returns array of substrings split on the seperator
print(y.replace("h", "3"))
print(f'Keep it real, dawg\'s friend, and {do_not} learn {binary}.') #or
print("I like " + binary)
print(z)
print(type(z)) # not 'typeof'
print (binary[0]) #print the char at the zero index
print (binary[1:4]) #print chars 1, 2 and 3 but not 4
print(power)
print(type(power))
print(exp)

""" Sometimes you'll use casting to specify type, using int(), float() or str().
    int(2.7) or int("2.7") rounds down to two.
    float(2) or float("2") becomes 2.0.
    str(2.0) becomes "2.0"
    Even if you cast to a type, it appears you can reassign the var to anything
"""

#print("What's your name?")
# x = input()
# print("Hello, " + x)
# print(f"Nice to see you, {x}")

#Math stuff
print(5**3) # 5 to the third
print(5e3) # Five times (ten to the third) - 'e' can be 'E'
print(12 // 5) # floor division - returns 2, tosses remainder

#Comparison and logical
print(3 == 4) # No ===
print(3 != 4)
print(not(3 == 4)) # the word 'not', not '!'
print(3 == 4 and 4 == 4) # false, and no '&&'
print(3 == 4 or 4 == 4) # true, and no '||'

# Identity operators
set_a = [1, 2, 3]
set_b = [1, 2, 3]
set_c = set_a

print(set_a == set_b) # True, b/c they have the same content
print(set_a is set_b) # False, b/c they are not the same object
print(set_a is set_c) # True, b/c set_c was assigned (=) to be the same object 

# Membership operators
print('ban' in 'Copa cabana')
print('ban' not in 'Cleveland!')
