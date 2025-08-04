from asyncore import write
import re
import sys
import csv

#view data/show data
def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

#add a data
def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


#update a data
def update(i):
    #save updated data
    def update_newlist(i):
        with open('data.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerows(i)
    
    new_list = []
    phone = i[0]
    
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == phone:
                    fname = i[1]
                    lname = i[2]
                    dob = i[3]
                    age = i[4]
                    gender = i[5]
                    phone = i[6]
                    email = i[7]
                    city = i[8]
                    province = i[9]
                    country = i[10]
                    
                    data = [fname,lname,dob,age,gender,phone,email,city,province,country]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

#remove a data
def remove(i): 
    #save
    def save(j):
        with open('data.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerows(j)
            
    new_list = []
    phone = i
    
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            
            for element in row:
                if element == phone:
                    new_list.remove(row)
    
    save(new_list)

#search a data
def search(i):
    data = []
    phone = i
    
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == phone:
                    data.append(row)
    print(data)
    return data