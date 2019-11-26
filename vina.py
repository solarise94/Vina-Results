import linecache
from sys import argv
import os 

input_file_path = argv[1]
output_file = argv[2]

def getline(the_file_path,line_number):
    if line_number < 1:
        return ''
    for cur_line_number, line in enumerate(open(the_file_path,'rU')):
        if cur_line_number == line_number-1:
            return line
    return ''

def readID(input_file):
    Line = linecache.getline(input_file,4)
    sep = Line.split()
    return sep[3]

def readEnergy(input_file):
    Line = linecache.getline(input_file,2)
    sep = Line.split()
    return sep[2]

def judgeFile(input_file):
    if linecache.getline(input_file,1) == '':
        return False
    else:
        return True

filelist = os.listdir(input_file_path)
outfile = open(output_file,'w')
outfile.write("ID\tEnergy\n") # header

for i in range(0,len(filelist)):
    path = os.path.join(input_file_path,filelist[i])
    if os.path.isfile(path):
        if judgeFile(path):
            ID = readID(path)
            Energy = readEnergy(path)
            print(f"{ID}\t{Energy}")
            outfile.write(f"{ID}\t{Energy}\n")
        else:
            pass
    else:
        pass
outfile.close()
