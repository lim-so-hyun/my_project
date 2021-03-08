# C:/doit/memo_edit.py
import sys

option = sys.argv[1]

if option == '-a':
     memo = sys.argv[2]
     f = open('memo.txt', 'a')
     f.write(memo)
     f.write('\n')
     f.close()
