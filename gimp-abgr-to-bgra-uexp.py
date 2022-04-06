import sys

def main(argv):
    try:
        file = open(argv[1],"rb")
    except:
        print("No file as second argument or unable to open.")
        quit()
    
    file.seek(0,2)
    length = file.tell()
    file.seek(0,0)
    
    data = file.read()
    if(data[0:3].decode('utf-8') != 'DDS'):
        print("File is not a DDS file.")
        quit()
    data = bytearray(data[0x80::])
    
    i=0
    while(i < length-0x80):
        save = data[i]
        data[i] = data[i+2]
        data[i+2] = save
        i += 4
    try:
        wrfile = open(argv[1][:len(argv[1])-3]+"data","wb")
    except:
        print("UMMMMMM?!??!?!")
        print(argv[1][:len(argv[1])-3])
        quit()
    wrfile.write(data)
if __name__ == "__main__":
	main(sys.argv)