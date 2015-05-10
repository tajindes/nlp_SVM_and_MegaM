import sys;

inputfile = sys.argv[1];
file1 = open(inputfile, "r");
outputfile = sys.argv[2];
file2 = open(outputfile, "w");

line = file1.readline();
while(line):
	
	line = file1.readline();	
	str_temp = line[:1];
#	print("class nuber is :", str_temp);
	try:
		value = float(str_temp);
	except ValueError:
		value = 0.0;	
	
	if(value >= 0.5):
		file2.write("POS" + "\n" );
	else:
		file2.write("NEG" + "\n" );

file1.close();
file2.close();
