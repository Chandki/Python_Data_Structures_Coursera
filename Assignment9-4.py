#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")

try:
    with open(fname) as fh:
        counts = {}
        for line in fh:
            if line.startswith('From '):
                words = line.split()
                if len(words) > 1 and words[1].strip():
                    sender = words[1].strip().lower()
                    counts[sender] = counts.get(sender, 0) + 1
except:
    print("File cannot be opened or read:", fname)
    sys.exit()

if counts:
    max_sender = None
    max_count = 0
    for sender, count in counts.items():
        if count > max_count:
            max_count = count
            max_sender = sender
    print(max_sender,max_count)
else:
    print("No senders found.")