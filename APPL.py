from tkinter import *
import os
import time
print('APPL v1.0')
command = ''
def execute(cmmd):
    if cmmd == 'say':
        data1 = input('  message: ')
        print(f'\n{data1}\n')
    elif cmmd == 'math':
        data1 = input('  first number: ')
        data2 = input('  second number: ')
        data3 = input('  operation: ')
        if data3 == '+':
            print(f'\n{float(data1) + float(data2)}\n')
        elif data3 == '-':
            print(f'\n{float(data1) - float(data2)}\n')
        elif data3 == '*':
            print(f'\n{float(data1) * float(data2)}\n')
        elif data3 == '/':
            print(f'\n{float(data1) / float(data2)}\n')
        else:
            print('\nProblem: Please use a valid operator! (+, -, *, /)\n')

    elif cmmd == 'help':
        print('\nsay = repeats a message\nmath = preforms a math problem\n')


    else:
        print('\nProblem: Your command was not understood! Type :help for assistance!\n')



while True:
    command = input(':')
    execute(command)
    lastcmmd = command



