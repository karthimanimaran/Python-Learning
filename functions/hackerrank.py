#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    word = sentence.split(" ")
    result = ""
    word.reverse()
    result = [w.swapcase() for w in word]
    return ' '.join(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys



class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_coins):
        self.num_items = num_items
        self.item_coins = item_coins
    def buy(self, num_items,num_coins):
        if (self.num_items < num_items):
            return "Not enough items in the machine"
        total_money = num_items * self.item_coins
        if (num_coins < total_money):
            return "Not enough coins"
        else :
            change = num_coins - (num_items*self.item_coins)
            self.num_items = self.num_items - num_items
            return change
        
        
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
