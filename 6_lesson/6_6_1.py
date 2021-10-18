import sys

if __name__ == '__main__':
    vals = list(map(int,sys.argv[1:]))
    with open('bakery.csv') as f:
        text = f.readline()
        if len(vals) == 2:
            for line in text[vals[0]-1:vals[1]]:
                print(line.strip())
        elif len(vals) ==1:
            for line in text[vals[0]-1:]:
                print(line.strip())
        else:
            for line in text:
                print(line.strip())
    exit()