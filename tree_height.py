# python3

import sys
import threading
import numpy
import os

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    height = [0] * n
    for up in range(n):
        distance = get_distance(up, parents, height)
        if distance > max_height:
            max_height = distance
    return max_height

def get_distance(up, parents, height):

    if height[up] != 0:
        return height[up]
    if parents[up] == -1:
        height[up] = 1
    else:
        height[up] = get_distance(parents[up], parents, height) + 1
        return height[up]

def main():
    # implement input form keyboard and from files
    text = input().strip()
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    if text == 'I':
        n = int(input("Elementu skaits: "))
        parents = numpy.asarray(list(map(int,input("Vertibas: ").strip().split())))
    elif text == 'F':
        name = input("Faila nosaukums: ")
        if 'a' in name:
            print("Nepareizs nosaukums")
            return
        file_path = os.path.join(os.getcwd(), 'test', name)
        with open(file_path, 'r') as f:
            n = int(f.readline().strip())
            parents = numpy.asarray(list(map(int, f.readline().strip().split())))
    else:
        print("Nepareiza ievade")
        return

    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    max_height = compute_height(n, parents)
    print(max_height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))