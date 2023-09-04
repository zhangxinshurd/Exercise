import re


with open('file_to_read.txt',"r",encoding='utf-8')  as test:
	i=0
	words=[]
	for line in test:
		line=line.replace(',',' ')
		line=line.strip()
		wo=line.split(' ')
		words.extend(wo)
	
	for word in words:
		if word=='terrible':
			i+=1
	print("The number of occurrences of terrible is %d"%i)

with open('file_to_read.txt',"r",encoding='utf-8')  as test:
	file_data=test.read()
	replaced_text = re.sub('terrible', lambda m: 'terrible' if m.start() % 2 == 0 else 'pathetic', file_data)
	replaced_text = re.sub('terrible', lambda m: 'terrible' if m.start() % 2 == 1 else 'marvellous', replaced_text)
	print(replaced_text)



with open('result.txt',"w",encoding="utf-8") as f:
    f.write(replaced_text)

