list_1 = ["eggs", "bread", "milk"]
list_1.append("chocolate")
print(list_1)

essentials_tuple = ("bread", "eggs")
print(essentials_tuple)

fruit = {"apple", "banana", "cherry"}
print(fruit)

emb_list = [[1,2,3],[4,5,6]]

for item in emb_list:
    print(item)
    for num in item:
        print(num)

dict_data = {1:{"name":"Eren", "course":"data"}, 2:{"name":"Armin", "course":"ba"} }

for item in dict_data.values():
    print(item)
    for key in item.values():
        print(key)

user_prompt = True

while user_prompt:
    age = input("What is your age?: ")
    if age.isdigit():
        if int(age) < 117:
            user_prompt = False
        else:
            print("Please provide digits: ")


print(f"Your age is: {age}")
