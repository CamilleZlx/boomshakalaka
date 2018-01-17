import os

def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    for root, subdirs, files in os.walk(dir):
        for name in files:
            for ext in exts:
                if (name.endswith(ext)):
                    file.write(name + "\n")
                    break
        if (not recursion):
            break

def Test():
    dir = "C:\\Users\\Camille\\Desktop\\facelle"
    outfile = "binaries.txt"
    wildcard = ".xls"
    file = open(outfile, "w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, file, wildcard, 0)
    file.close()
Test()