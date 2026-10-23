#sets: unordered 
set1 = {"apple", "banana", "cherry"}
print(type(set1))
print(len(set1))
set2={1,2,3,4,5}
print(type(set2))
print(len(set2))
fruit_list=["apple","banana","cherry"]
# set3=set(fruit_list)
set2.update(fruit_list)
print(set2)
fruit_list.remove("banana")
print(fruit_list)

set2.remove("banana")
print(set2)

set2.discard("banana")
print("Discard Result:", set2)

set2.pop()
print(set2)

# set2.clear()
# print(set2)

del set2
print(set2)