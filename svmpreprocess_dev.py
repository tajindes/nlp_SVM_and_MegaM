import sys;
import glob;
import os;
import re;

outputfile = sys.argv[2];
file2 = open(outputfile, "w");
fileNames =  glob.glob(sys.argv[1]+'/*.txt');
fileNames.sort();

#documents = 0;
#term_freq = { };
#weight_freq = { };
#contain_dict = { };
#vocabulary = set();
#document_freq = { };

feature_dict = { };
feature_counter = 1 ;
#print ("filenames are", fileNames,"\n");
for name in fileNames:
#	documents = documents + 1;

	path = re.search('/(.+?).[0-9]+.txt', name).group(1);
	index = path.rfind('/');
	index = index+1;

	file1 = open(name, 'r', errors='ignore')
	lines  = file1.readlines()
	str_temp = ' '.join([line.strip() for line in lines]);
	str_temp = re.sub("[^A-Za-z0-9_\s\'\@\$\-]+",'',str_temp);	
#	str_temp = str_temp.lower();
	file1.close();
#	list_array = str_temp.split(" ");
	list_array = str_temp.split();

	term_freq = { };
#	feature_dict= { };
	feature_order = { };
#	print("name is", name);
#	print ("document is:", list_array);
	for item in list_array:		
		if(item not in feature_dict):		
			feature_dict[item] = feature_counter;
#			print("feature counter is :", feature_counter);
			feature_counter = feature_counter + 1;			

		if(item not in feature_order):
			feature_order[item] = feature_dict[item];

		if (item not in term_freq):
			term_freq[item] = 1;
		else:
			term_freq[item] = 1;
#			term_freq[item] = term_freq[item] + 1;

#	print("term frequency is:", term_freq);

	str_str =  "";
	genexp = ((k, feature_order[k]) for k in sorted(feature_order, key=feature_order.get, reverse=False))
	for k,v in genexp:
#		print ("value is: ", v, "term frequency s:", term_freq[k]);
#		print ("str_str is:", str_str);
#		str_dummy = str(v);
		str_str =str_str + str(v) + ":" + str(term_freq[k]) + " ";
	
	term_freq = { };
	feature_order = { };
#	print (str_str);
 
#	for item in list_array:		
	if (path[index:] == "SPAM" or path[index:] == "POS"):
		file2.write("1" + " " + str_str+"\n");
	elif(path[index:]=="HAM" or path[index:] == "NEG"):
		file2.write("-1" + " " + str_str + "\n");
	else:
		file2.write("0" + " " + str_str + "\n");
	str_str = " ";
file2.close();
