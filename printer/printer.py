import sys
def print_to_log(args):
    temp = sys.stdout
    sys.stdout = open('log.txt','a')
    print(args)
    sys.stdout = temp
