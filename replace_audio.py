import sys
import os

def main(argv):
    if (len(argv) != 3):
        print("Too few/many arguments.")
        quit()
    if ((not os.path.exists(argv[1])) or (not os.path.exists(argv[2]))):
        print("One of the paths does not exist.")
        quit()
    if (argv[1][-6::]!="uasset" or argv[2][-3::]!="ogg"):
        print("Bad file types..?")
        quit()
    uexpr = open(argv[1][:-6]+"uexp","rb")
    uexpdata = bytearray(uexpr.read())
    uexpr.close()
    
    oggr = open(argv[2],"rb")
    oggdata = bytearray(oggr.read())

    # Find the beginning of the OGG
    i = 0
    while True:
        if (uexpdata[i:i+4] == bytearray(str.encode("OggS"))):
            break
        i = i + 1
        
    print("Found OggS at " + str(i) + "!")
    
    uexpend = uexpdata[len(uexpdata)-0x14:]
    uexpdata = uexpdata[:i]
    uexpdata[i-0x10:i-0x8] = len(oggdata).to_bytes(4,'little') * 2
    uexpdata += oggdata
    uexpdata += uexpend
    
    uexpw = open(argv[1][:-6] + "newuexp","wb")
    uexpw.write(uexpdata)
    uexpw.close()
    
    #uexp replaced, now fix the uasset
    
    uassetr = open(argv[1],"rb")
    uassetdata = bytearray(uassetr.read())
    uassetr.seek(0, os.SEEK_END)
    uassetlen = uassetr.tell()
    uassetr.close()
    
    uassetdata[-0x60:uassetlen-0x60+4] = (len(uexpdata)-4).to_bytes(4,'little')
    uassetw = open(argv[1][:-6] + "newuasset","wb")
    uassetw.write(uassetdata)
    uassetw.close()
    
    print("success?")
    
    


if __name__ == "__main__":
    main(sys.argv)