import sys

if __name__ == '__main__':
    sys.stdout.write(
        f"{''.join([chr((x << 0x1) >> 0x1) for x in [0x68,0x65,0x6c,0x6c,0x6f,0x20,0x45,0x69,0x64,0x50,0x20,0x32,0x30,0x32,0x34,0x21]])} :){chr(0x0a)}")
