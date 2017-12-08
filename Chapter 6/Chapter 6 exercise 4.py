'''
There is a string method called count that is similar to the function in the previous exercise.
Read the documentation of this method at https://docs.python.org/3.5/library/stdtypes.html#string-methods 
and write an invocation that counts the number of times the letter a occurs in "banana".
'''

def count():
	word = input("Enter a word:")
	letter = input("Enter a letter in that word:")
	index = word.count(letter)
	
	print(index)

count()
