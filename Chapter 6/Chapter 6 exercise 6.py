'''
Read the documentation of the string methods at
https://docs.python.org/3.5/library/stdtypes.html#string-methods
You might want to experiment with some of them to make sure you understand 
how they work. strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. 
For example, in find(sub[, start[, end]]), the brackets indicate 
optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
'''

def replace():
    word = input("enter a word: ")
    letter = input("What letter do you want to replace: ") 
    new_letter = input("What letter do you want to replace it with: ")
    new_word = word.replace(letter, new_letter)
    print(new_word)
	
replace()


