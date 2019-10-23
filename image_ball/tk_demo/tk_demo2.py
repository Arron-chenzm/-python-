import msvcrt
import time

if __name__ == '__main__':
    print("Reading form keybord")
    print("""   i
j  k  l
   m""")
    print('press Q to quit')
    while True:
        ch = msvcrt.getwch()
        print(ch)
        if ch == 'i':
            print('move forward')
        elif ch == 'm':
            print('move back')
        elif ch == 'j':
            print("turn left!")
        elif ch == 'l':
            print("turn right!")
        elif ch == 'u':
            print("turn right!")
        elif ch == 'o':
            print("turn right!")
        elif ch == 'k':
            print("stop motor!")
        elif ch == 'q':
            print("shutdown!")
            break
        elif ord(ch) == 0x3:
            # 这个是ctrl c
            print("shutdown")
            break
        print("Reading form keybord")
        print("""   i
j  k  l
   m""")
        print('press Q or ctrl+c to quit')