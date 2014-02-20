from sys import argv
#number of arguments must equal to the number of variables
script, filenmae = argv  # set variables (or get filename)

txt = open(filenmae)  # open file
#print a string
print "Here's your file %r:" % filenmae
print txt.read()  # print all strings in the file
txt.close()

print "Type the filenmae again:"  #print the prompt
file_again = raw_input("> ")

txt_again = open(file_again)# open the file

print txt_again.read();#print all strings in the file
txt_again.close()
#print txt_again.read(); #this print will print nothing.