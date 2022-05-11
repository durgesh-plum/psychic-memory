import csv

def open_file(file_name):
    try:
        csvfile = open(file_name, newline =' ')
        user_details = csv.reader(csvfile, delimiter=',')
        return user_details
    except FileNotFoundError:
        print("file not found")



def transform_user_details(csv_file_name):

        new_user_data = []
        with open("user_details.csv", newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

        for user in user_details:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[4])
            new_user_data.append(transformation)
        return new_user_data

def create_new_csv(old_data="user_details.csv", new_file_name = "new_user_details.csv"):
    new_user_data = transform_user_details(old_data)
    new_file = open(new_file_name, "w")


    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_csv()






  #  iterable_csv = iter(csvreader)
   # next(iterable_csv)

    #for row in csvreader:
 #       print(row[0])
#

  #  print(list(csvreader))
