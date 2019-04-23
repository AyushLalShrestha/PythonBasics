
def main():
 infile = open("calmBlue.jpg", "rb")
 outfile = open("copy.jpg", "wb")

 bufferSize = 10000
 buffer = infile.read(bufferSize)
 while len(buffer):
    outfile.write(buffer)
    print(".", end=' ')
    buffer = infile.read(bufferSize)
 print("Done")

if __name__ == '__main__':
    main()