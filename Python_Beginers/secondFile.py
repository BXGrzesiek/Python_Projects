#!/bin/python3

def test(N):
#   in range?
    if  range(1,100):
#   Number in range!
        if N % 2 == 0:
        #   Even number
            if N in range(2, 6):
            #   in range?
                print ('1Not Weird')
            elif N in range(6, 21):
            #   in range?
                print ('Weird')
            elif N >= 21:
                print ('2Not Weird')
        else:
        #   Odd number
            print ('Weird')

    else:
#   out of range
        print('endOfLife')
        
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
test(N)