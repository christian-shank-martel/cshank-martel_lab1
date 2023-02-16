#!/usr/bin/env python3
#Author: christian shank-martel
#Date:feb 15th 2023
#Program: Lab1.py

from datetime import date

def age_finder(born):
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
 
    return age

def Helloworld():
    print("hello world!")

if __name__ == '__main__':
    year_born = int(input("What year were you born?: "))
    month_born = int(input("What month were you born?: "))
    day_born = int(input("What day were you born?: "))
    age = age_finder(date(year_born,month_born,day_born))
    print("\nyou are ",age," years old")

    Helloworld()
