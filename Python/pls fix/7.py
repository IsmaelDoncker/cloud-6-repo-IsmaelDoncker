'''
The output should be:
['Dog', 'Cat', 'Fly']
'''
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = ['Dog', 'Cat', 'Fly']

for animal in ln:
	if len(animal) == 3:
		short_names.append(animal)
	short_names = ['Dog', 'Cat', 'Fly']

print(short_names)