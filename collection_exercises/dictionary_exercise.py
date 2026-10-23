#dictionary:ordered,
dictionary = {
    "name": "John",
    "age": 30,
    "age":31,
    "city": "New York"
}
print(type(dictionary))
print(len(dictionary))
print(dictionary["name"])
print(dictionary["age"])

new_dictionary = {
    "name": "John",
    "age": 30,
    "age":31,
    "city": "New York",
    "colors": ["red", "green", "blue"]
}
print(new_dictionary)
new_dictionary["name"] = "kawthar"
print(new_dictionary)
new_dictionary["country"] = "USA"
print(new_dictionary)
new_dictionary.update({"age": 32, "city": "Los Angeles"})
print(new_dictionary)

del new_dictionary["age"]
print(new_dictionary)

new_dictionary.clear()
print(new_dictionary)

