print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def integer(n):
    list_1 = []
    for i in range(1,n):
        if n%i == 0:
            list_1.append(i)

    return list_1

print(integer(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:
def factor(f, n):
    if (n%f==0) or (f%n==0):
        return True
    else:
        return False

print(factor(17,7))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def letter_bet(letter):
        return(alphabet.index(letter))

print(letter_bet("f"))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def letter_id(p_name):
    empty = ""
    for i in p_name:
        empty += str(letter_bet(i))

    return empty

print(letter_id("hello"))

#letter_id("durgesh")

print("\nQ2c\n")

# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def function_1(p_name):
    empty = ""
    for i in p_name:
        empty += str(letter_bet(i))

    final_id_2 = sum(int(i) for i in empty)

    print(int(empty) - int(final_id_2))


function_1("bob")

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime_number(x):
    if x == 0:
        return False
    elif x == 1:
        return False
    elif x == 2:
        return True
    for n in range(3, x - 1):
        if x % n == 0:
            return False
    return True



print(prime_number(2))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def no_error(x = input("Enter number")):

    while x.isdigit() == False:
        x = input("Enter number: ")
    if x == 0:
        return False
    elif x == 1:
        return False
    elif x == 2:
        return True
    for n in range(3, x - 1):
        if x % n == 0:
            return False
    return True


print(no_error())


# -------------------------------------------------------------------------------------- #



