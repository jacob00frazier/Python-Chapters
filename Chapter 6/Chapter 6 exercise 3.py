''' 
Encapsulate this code in a function named count, and generalize it so that it accepts the string and
the letter as arguments.
'''
 
def count():
	word = input("Enter a word:")
	letter = input("Enter a letter in that word:")
	index = 0
	for i in word:
		if i == letter:
			index = index +1
	print(index)
count()


