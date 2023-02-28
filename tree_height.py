# python3

import sys
import threading
import numpy
import os


def compute_height(n, parents):
    max_height = 0
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
    text = input().strip().upper()
    if text == 'I':
        n = int(input("Elementu skaits: "))
        parents = list(map(int, input("Vertibas: ").strip().split()))
    elif text == 'F':
        name = input("Faila nosaukums: ")
        if 'a' in name:
            print("Nepareizs nosaukums")
            return
        file_path = os.path.join(os.getcwd(), 'test', name)
        with open(file_path, 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    else:
        print("Nepareiza ievade")
        return

    max_height = compute_height(n, parents)
    print(max_height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()