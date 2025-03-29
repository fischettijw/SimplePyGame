import os; os.system("cls")

from faker import Faker
fake = Faker()
# Faker.seed(0)

def write_txt_file(filename, data):
    file = open(filename, 'a')
    file.write(data + "\n")
    file.close()

    # with open(filename, mode='a', newline='') as file:
    #     file.write(data + "\n")


def read_txt_file(filename):
    file = open(filename, 'r')
    for row in file:
        print(row)  # print(row, end='')
    file.close()

    # with open(filename, mode='r') as file:
    #     for row in file:
    #         print(row)  # print(row, end='')

filename = "students.txt"
students = []

for student in range(3):
    students.append(f"{fake.name_male()} - {fake.state()} - {fake.zipcode()}")
    students.append(f"{fake.name_female()} - {fake.state()} - {fake.zipcode()}")

for student in students:
    write_txt_file(filename, student)

read_txt_file(filename)
