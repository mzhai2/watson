import sys
import os
import glob

if __name__ == "__main__":
    choices = []
    target = sys.argv[1]
    for d in glob.glob(os.path.join(target, '*/')):
        dirname = os.path.basename(os.path.dirname(d))
        if len(dirname) > 3:
            if dirname[:3] == 'sim':
                choices.append(dirname)
    
    for i, choice in enumerate(choices):
        print('{} {}'.format(i, choice))

    while(True):
        i = input('Type in the number?')
        try:
            i = int(i)
            if i in range(len(choices)):
                print(choices[i][3:])
                sys.exit()
        except ValueError:
            continue