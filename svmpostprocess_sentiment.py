import sys;

inputfile = sys.argv[1];
outputfile = sys.argv[2];
file1 = open(inputfile, "r");
file2 = open(outputfile, "w");


line = file1.readline();

while(line):
	value = float(line.strip());
	if(value >= 0):
		file2.write("POS" + "\n");
	else:
		file2.write("NEG" + "\n");
	
	line = file1.readline();

file1.close();
file2.close();

