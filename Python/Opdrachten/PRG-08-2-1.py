from asyncore import loop
import csv
from sqlite3 import Row

with open('myfirst.csv', 'a', newline = "") as file:
    myfile = csv.writer(file)
    myfile.writerow(["firstname","lastname","Jobtitle","Company"])
    noOftimes = int(input("How many times do you want loop:"))
    for i in range (noOftimes):
        firstname = input("Enter firstname:")
        lastname = input("Lastname: ")
        Jobtitle = input("Job title: ")
        Company = input("Company: ")
        myfile.writerow([firstname, lastname, Jobtitle,Company])
    