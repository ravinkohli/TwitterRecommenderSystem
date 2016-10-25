with open('Replace.txt', 'r') as document:
   Replace = {}
   for line in document:
       line = line.split(',',1)
       if not line:  # empty line
           continue
       Replace[line[0]] = line[1][:-1]

with open('Dismiss.txt', 'r') as document:
   Dismiss = {}
   for line in document:
       line = line.split(',',1)
       if not line:  # empty line
           continue
       print(line[1])
       #Dismiss[line[0]] = line[1][:-1]

# Two dictionaries created, Replace and Dismiss

file = open('Tweets_PrePOS.txt','w')

with open('Tweets_PreSlang.txt','r') as doc:
   for line in doc:
       file.write('\n')
       line = line.replace(',',' ').split()
       part = []
       for y in line:
           if Dismiss.get(y, "NO") == "NO":
               replacement = Replace.get(y, y)
               part.append(replacement)
               text = ' '.join(part)
       file.write(text)
