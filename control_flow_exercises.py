print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

#A1a:

def first_five(list_1):
    print(list_1[0:4])

first_five(x)

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
def even(list_2):
    for i in x:
        if i%2 == 0:
            print(i)

even(x)




print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
def even_till_five(list_3):
    for i in x[0:5]:
        if i%2 == 0:
            print(i)

even_till_five(x)
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
def first_letters(list_of_names):
    firstletters = []
    letters = [i[0] for i in list_of_names]
    for letter in letters:
        firstletters.append(letter)
    print(firstletters)

first_letters(names)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
s_index = []
for i in range(0,len(names)):
    s_index.append(names[i].index(" "))
print(s_index)

def sub_list(list_of_name_2):
    s_index = []
    for i in range(0, len(list_of_name_2)):
        s_index.append(list_of_name_2[i].index(" "))
    print(s_index)

sub_list(names)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

first_last = []
for name in names:
    first_last.append(name[0] + name[name.index(" ") + 1])
print(first_last)

def initials(list_of_names_3):
    first_last = []
    for name in list_of_names_3:
        first_last.append(name[0] + name[name.index(" ") + 1])
    print(first_last)

initials(names)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]
# A3a:

new_list = []
for i in range(0,len(list_of_lists)):
    if len(list_of_lists[i]) == len(set(list_of_lists[i])):
        new_list.append(list_of_lists[i])
print(new_list)

def no_duplicates(list_5):
    new_list = []
    for i in range(0, len(list_5)):
        if len(list_5[i]) == len(set(list_5[i])):
            new_list.append(list_5[i])
    print(new_list)

no_duplicates(list_of_lists)
# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

ans = int(input("Enter a value bigger than 100: "))
while ans <= 100:
    print("try again")
    ans = int(input("Enter a value bigger than 100: "))
print(f"Congrats: {ans}")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise


# A4b:

prime = int(input("Enter a value bigger than 100: "))
while prime <= 100:

    print("try again")
    prime = int(input("Enter a value bigger than 100: "))
flag = True
for i in range(2,prime):
    if (prime % i) == 0:
        flag = True
        break


if flag:
    print(f"{prime} is not a prime number")

else:
    print(f"{prime} is a prime number")



