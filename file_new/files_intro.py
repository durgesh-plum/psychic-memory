try:
    file = open("../orders.txt")
except FileNotFoundError as errmsg:
    print("There is an error")
    print(errmsg)
    raise

def open_print_file(file):
    try:
        with open(file,"r") as open_file:
            for line in open_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File was not Found")
        raise
    finally:
        print("Execution complete")


def write_to_file(file, order_item):
    try:
        with open(file,"w") as open_file:
            open_file.write(order_item + '\n')
    except FileNotFoundError:
        print("File not Found")

def append_file(file, order_item):
    try:
        with open(file,"a") as append_file:
            append_file.write(order_item + '\n')
    except FileNotFoundError:
        print("File not Found")




open_print_file("../orders.txt")
write_to_file("../orders.txt", "nuggets")
write_to_file("../orders.txt", "bread")
write_to_file("../orders.txt", "juice")
#write_to_file("orders.txt", "ice cream")

append_file("../orders.txt", "nuggets")
append_file("../orders.txt", "beer")

