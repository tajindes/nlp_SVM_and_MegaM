import sys;
import glob;
import os;
import re;

outputfile = sys.argv[2];
file2 = open(outputfile, "w");
fileNames =  glob.glob(sys.argv[1]+'/*.txt');
#fileNames.sort();

feature_dict = { };
feature_counter = 1 ;
for name in fileNames:
	#print(name);
	path = re.search('/(.+?).[0-9]+.txt', name).group(1);
	index = path.rfind('/');
	index = index+1;

	file1 = open(name, 'r', errors='ignore')
	lines  = file1.readlines()

	str_temp = ' '.join([line.strip() for line in lines]);
	
#	print("before", str_temp);

	str_temp = re.sub('[^A-Za-z0-9_\s-]+','',str_temp);

#	print ("after", str_temp);
#	print("new" , str_new);
	file1.close();

	if (path[index:] == "SPAM" or path[index:] == "POS"):
		file2.write("1" + " " + str_temp +"\n");
	elif(path[index:]=="HAM" or path[index:] == "NEG"):
#	else:
		file2.write("0" + " " + str_temp + "\n");
	else:
		file2.write("1" + " " + str_temp + "\n");

#	str_str = " ";
file2.close();
