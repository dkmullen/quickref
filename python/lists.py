# Collections (Arrays):
# Lists - ordered and changable

myList = ["Kurtz", "Willard", "Mr. Clean"]
anotherList = list((23, 45, "Michael Jordan")) # using the constructor
print(myList[1])
myList[2] = "Chef"
print(myList) # Replace an item's value
for i in myList:
    print(i)
print("Willard" in myList)
print (len(myList))
myList.append("Lucas")
myList.insert(2, "The Photo Journalist")
print(myList)
myList.remove('Chef')
print(myList)
myList.pop() # removes the last item (and returns it?)
print(myList)
myList.pop(1) # removes item at index 1 "' ""
print(myList)
del myList[1] # deletes the item at index 1
print(myList)
del myList # delete the list completely
myList = list(("Biff", "Marty", "Elaine")) # using the list constructor
print(myList)
# myList.clear() # Empties, leaving []
# myList.copy() # Returns a copy
print(myList.count("Biff")) # returns count of how many Biffs
print(myList.index('Elaine')) # returns index of 'Elaine'
myList.reverse() # reverses the list, actually returns 'None'
print(myList) 
myList.sort() # sorts the list, actually returns 'None'
print(myList)
newList = [14, "Joker", "Animal", 34]
myList.extend(newList)
print(myList)

# Tuples - ordered and UNchangable
myTuple = (2, 34, "The Tick", "Batmanuel")
anotherTuple = tuple((23, 45, "Michael Jordan")) # using the constructor
print(myTuple)
print(myTuple[2])
for i in myTuple:
    print(i)
if 34 in myTuple:
    print("Yes, 34")
print(len(myTuple))
# del myTuple # Can delete a tuple, but cannot add, remove or reorder items
print(myTuple.count(34))
print(myTuple.index(34))

# Set - Unordered, unindexed. Can add/remove items, not edit. No duplicate members
mySet = {3, 'apples', 'oranges', 'bananas', 23}
anotherSet = set(("Tom", "Dick", "Harry"))
print(mySet)
for i in mySet:
    print(i)
print("orange" in mySet)
mySet.add("apple") # for one item
mySet.update(["pineapple", "mints", 45]) # for many
print(mySet)
print(len(mySet))
mySet.remove('apple') # if specified isn't present, will throw an err
mySet.discard(3) # if not present, will NOT throw an err
print(mySet)
# mySet.pop() #removes last item, but in an unordered set, don't know what that is
# mySet.clear() # empties the set - {}
# del mySet
myCopiedSet = mySet.copy()
print(myCopiedSet)

setA = {"Kurtz", "Willard", "Vietnam", "NVA", "French Plantation Scene"}
setB = {"Joker", "Animal Mother", "Vietnam", "NVA", "Rafterman"}
print(setA.difference(setB)) # ie, setA minus setB
print(setB.difference(setA)) # b minus  a
print(setA.intersection(setB)) # what they have in common
bigSet = setA.union(setB) # Put the two together w/o duplicates
print(bigSet)

# Dictionary: unordered, indexed, changable
myDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
anotherDictionary = dict(brand="Chevy", year="2000") # dict() constructor
print(anotherDictionary)
print(myDictionary)
print(myDictionary["model"]) # accesing the value of a key
print(myDictionary.get("model")) # using the 'get' method
myDictionary["year"] = 2018 # changing a value
for i in myDictionary:
    print(i)            # prints the keys
for i in myDictionary:
    print(myDictionary[i]) # prints the values
for i in myDictionary.values():
    print(i)                # prints the values w/ values function
for x, y in myDictionary.items(): # prints both with items function
    print(x, y)
if "model" in myDictionary:
    print("Yes, model")
print(len(myDictionary))
myDictionary["color"] = "red" # add item
print(myDictionary)
# v = myDictionary.pop('model') # remember that 'pop' removes and returns
# print(v)
# del myDictionary["model']
# del myDictionary
# myDictionary.clear()
myDictionary.popitem() # removes the last (chronologically) inserted item
print(myDictionary)
myDictionary.update(condition="Good", rust="No")
print(myDictionary)
names=("Dennis", "Cindy", "Sarah", "Kiri")
nameDict = dict.fromkeys(names) # makes new dict - each val is None
print(nameDict)
