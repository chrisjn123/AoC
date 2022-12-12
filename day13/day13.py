from collections import defaultdict
from time import sleep, time
from queue import PriorityQueue

data = [line.strip() for line in open('input.txt').readlines()]
data_test = [line.strip() for line in open('test.txt').readlines()]

