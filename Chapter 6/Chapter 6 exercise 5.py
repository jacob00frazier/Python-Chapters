'''
Take the following Python code that stores a string:`
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
'''

string = 'X-DSPAM-Confidence:0.8475'
colon = string.find(":")
new_string = str(string[colon+1:])
final_string = float(new_string) 

print(final_string)
