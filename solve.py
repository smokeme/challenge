################################################################
#
#    Generate string with a set value of ASCII digit total
#    ./solve.py 15 1190
#
#    * Found valid key: WbLlqHw5K4m224L
#    We would need to use it three times for each of the if statements
#    Once for a 5 character 377 ascii total
#    Once for a 3 character 225 ascii total
#    Once for a 7 character 519 ascii total
#    Then we comine them together into a single key 
#    Like the following AAAAA-BBB-CCCCCCC
#
################################################################
import sys
import random

def check_param(param):
    total = 0
    for letter in param:
        total += ord(letter)
    return total

def solve(characters,maximum):
    key = ""
    while True:
        key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHSJKLMNPQRSTUVWXYZ1234567890")
        total = check_param(key)
        if total > int(maximum):
            key = ""
        if total == int(maximum) and len(key) == int(characters):
            print('Found valid key: ' + str(key))
            exit()
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {0} <number of character> <maximum ascii>'.format(sys.argv[0]))
        exit()
    number = sys.argv[1]
    maximum = sys.argv[2]
    solve(number,maximum)
    

