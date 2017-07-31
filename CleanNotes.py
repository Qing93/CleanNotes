# -*- coding: utf-8 -*
import os
import re

def CleanNotes(filename):
    f = open(filename, 'r+')
    f.seek(0)
    line = f.readlines()
    for l in line:
        for i in range(len(l)):
            if l[i] == '#':
                b = l[:i] #截取‘#’前面的字符串
                num1 = b.count('\'')
                num2 = b.count('\"')
                if (num1 % 2 or num2 % 2) == 0:
                    l = l[:i] + '\n'
                    break
        f.write(l)
    f.close()

if __name__=="__main__":
    CleanNotes(file1.py)
