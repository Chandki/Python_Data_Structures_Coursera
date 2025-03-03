#Dictionaries -Part3 - 10/10/2020
#Counting Pattern
counts = dict()
print ('Enter a line of text:')	
line=input('')
words = line.split()    
print ('Words:', words)
print ('Counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print ('Counts', counts)

#Looping through Dictionaries
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print (key, counts[key])

#Retrieving lists of Keys and Values
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print (list(jjj))
print (jjj.keys())
print (jjj.values())    
print (jjj.items())

#Two Iteration Variables
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}  
for aaa,bbb in jjj.items():
    print (aaa, bbb)
