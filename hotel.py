# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:08:48 2022

@author: HORSEMAN
"""

import os
import pathlib as pl
import pickle


class Hotel:
    cName = ''
    cNumber = ''
    cAddress = ''
    cBilling = ''
    cRoomNumber = 000

    def cProfile(self):
        self.cName = input("Customer Name : ")
        self.cNumber = int(input('Customer Mob. Number : '))
        self.cAddress = input("Customer Address : ")
        self.cBilling = input("Billing Type : ")
        print("please wait...Searching Room🏠")
        print("Available Room...")


# creating object of class Hotel
def createNewCustomer():
    hotel = Hotel()
    hotel.cProfile()
    createDB(hotel)

# All customers list
def displayAllCustomer():
    file = pl.Path("customers.data")
    if file.exists():
        openFile = open("customers.data", "rb")
        storeData = pickle.load(openFile)
        openFile.close()

        print("Customers Details....")
        print('---------------------------------------------')
        for data in storeData:

            print('Customer Name : ', data.cName)
            print('Customer Mob. Number: ', data.cNumber)
            print('customer Address : ', data.cAddress)
            print('Billing Type : ', data.cBilling)
            print()
        print('---------------------------------------------')
    else:
        print('No Customer Available....')

# creating database
def createDB(customer):
    file = pl.Path("customers.data")

    if file.exists():
        openFile = open("customers.data", "rb")
        storeData = pickle.load(openFile)
        storeData.append(customer)
        openFile.close()
        os.remove("customers.data")
    else:
        storeData = [customer]
    createFile = open("newCustomer.data", "wb")
    pickle.dump(storeData, createFile)
    createFile.close()
    os.rename("newCustomer.data", "customers.data")
    print("Customer recorded....")

# creating room
def createRoom():
    def create():
        room = {800: "available",
                801: "available",
                802: "available",
                803: "available",
                804: "available",
                805: "available",
                806: "available",
                807: "available",
                808: "available",
                809: "available",
                810: "available"}

        create = open("roomNew.data", "wb")
        pickle.dump(room, create)
        create.close()
        os.rename("roomNew.data", "room.data")
        print("room created.....")

    file = pl.Path("room.data")
    if not file.exists():
        create()

createRoom()
c = ''
while c != '0':
    print('---------------------------------------------')
    print('* : All customers List')
    print('0 : Exit')
    print('1 : New Customer')
    print('---------------------------------------------')
    c = input('Choose option : ')

    if c == '*':
        displayAllCustomer()
    elif c == '1':
        createNewCustomer()
