import os
import sys
import re

path = "C:\Users\Dell\Documents\GitHub\Homework_4.1-4\dz 4-1.txt"

def total_salary(path):
    total = 0
    average = 0
    i = 0

    with open(path, "r") as fh:
        lines = fh.readlines()
        for line in lines:
            payment = line.find(r"\d")
            i = i + 1
            total = total + payment
        print (total)
        average = total / i
        print (average)


if __name__ == "__main__":
    total_salary()