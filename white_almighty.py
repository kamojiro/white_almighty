#import sys
#input = sys.stdin.readline
from tiles import tiles

def main():
    t = tiles()
    while True:
        t.display_hands()
        input("Please input something")
        t.display_answer()
if __name__ == '__main__':
    main()
