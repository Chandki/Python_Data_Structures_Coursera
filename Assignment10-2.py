#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

filename = input("Enter the filename: ")
try:
    fhand = open(filename)
    hours = dict()
    for line in fhand:
        if line.startswith("From "):
            words = line.split()
            time = words[5]
            hour = time.split(":")[0]
            hours[hour] = hours.get(hour, 0) + 1
    sorted_counts=sorted(hours.items())
    for hour, count in sorted_counts:
        print(hour, count)
        
            
except:
    print("File not found")
    exit()
