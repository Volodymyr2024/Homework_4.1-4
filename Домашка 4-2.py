import os
import sys
import re

path = "C:\Users\Dell\Documents\GitHub\Homework_4.1-4\dz 4-2.txt"

def get_cats_info(path):
    cats_info = []

    with open(path, "r") as fh:
        lines = fh.readlines()
        for line in lines:
            cat_line = line.removesuffix("\n").split(",")
            cat_info = {"id": cat_line[0], "name": cat_line[1], "age": cat_line[2]}
            cats_info.append(cat_info)
        return cats_info
        

if __name__ == "__main__":
    get_cats_info()

