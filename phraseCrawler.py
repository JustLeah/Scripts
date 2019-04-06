import pprint
import sys
pp = pprint.PrettyPrinter(indent=4)
output = False

if len(sys.argv) == 1:
    print("Please specifiy the file to read and optionally the output file e.g. python phraseCrawler.py textfile.txt output.txt")
    quit()

if len(sys.argv) == 3:
    output = True

try:
    #Read the textfile and create the structure
    book = open(sys.argv[1], "r")
    bookText = book.read().replace('\r', ' ').replace('\n', ' ').split(' ')
    book.close()
except:
    print("This file does not exist")
    quit()


#Initilise vars which are used
strings = {}
start = 0
length = len(bookText)

#Create the data structures
for i in range(0, length):
    strings[i] = []

#First add all the unique words to the structure
for word in bookText:
    if word not in strings[0]:
        strings[0].append(word)


#Recursive function which will create the final output
def getStrings(book, length, start):

    combine = 1

    if start + combine > length:
        return strings

    while start + combine <= length:
        wordsToCombine = 0

        for i in range(combine, length - start):
            combined = []

            while wordsToCombine <= i:
                combined.append(book[start + wordsToCombine])
                wordsToCombine += 1

            s = ' '
            if output:
                string = s.join(combined)
            else:
                string = str(combine) + ": " + s.join(combined)

            if(len(combined) == combine + 1 and string not in strings[combine - 1]):
                strings[combine].append(string)

        combine += 1

    return getStrings(bookText, length, start + 1)


#Create the output via the recurisve function
strings = getStrings(bookText, length, start)

#Write the output to the desired file or just print it if one isn't specified
if output:
    writeTo = open(sys.argv[2], 'w+')
    for key in strings:
        for phrase in strings[key]:
            writeTo.write("%s\n" % phrase)
    writeTo.close()
else:
    pp.pprint(strings)