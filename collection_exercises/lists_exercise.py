# mylist=[1,2,3,4,5]
# print(type(mylist))
# print(mylist[0])
# print(len(mylist))
# mylist.append(6)
# print(mylist)

# mylist.remove(3)
# print(mylist)
# mylist.pop()
# print(mylist)
# mylist.pop(2)
# print(mylist)
# del mylist[0]
# print(mylist)
# mylist.clear()
# print(mylist)

fruits=["apple","banana","cherry"]
# fruits.append("orange")
# print(fruits)
# print(fruits[1])

# mylist.extend(fruits)
# print(mylist)

#list comprehension
new_list=[]
for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)
    
new_list=[x for x in fruits if "a" in x]
print(new_list)

ranging_list=[x for x in range(11)]
print(ranging_list)


print(ranging_list[0:5])
print(ranging_list[5:])
print(ranging_list[:])