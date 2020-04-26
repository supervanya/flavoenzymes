from pathlib import Path
import os
CURRENT_DIR = os.path.dirname(__file__)
p = Path('/home/antoine/pathlib/setup.py')
p.relative_to('/home/antoine')


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)



x = 'global, unchanged!'
def change(y):
    global x
    x = y
change('global, --changed!')

x = [1,2]
def change(y):
    x = y
print(x)
change(3)
print(x)