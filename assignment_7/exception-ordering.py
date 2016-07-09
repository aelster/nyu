#!/usr/local/bin/python3

#def divideAndConquer(argA, argB): return argA / argB if argB == 0: raise ZeroDivisionError("Woops, divided by zero")

def divideAndConquer(argA, argB):
    try:
        return argA / argB;

    except ZeroDivisionError:
        print('Woops, divided by zero')
        return "NAN"      # this will allow the program to keep running
#        raise            # this will print the message and raise the exception causing execution to crash

print( divideAndConquer( 5, 10) )
print( divideAndConquer( 5, 0) )
