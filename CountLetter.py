def count_letter(text):
    #initializing variables to count upper and lower case letters 
    upper_case = 0
    lower_case = 0
    #using for loop to check and count letters
    for char in text:
        #isupper() and islower() method used to check the upper and lower case
        #Iterration in text will check if letter is upper count +1 
        #If not upper then check for lower 
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1

    return upper_case , lower_case

sample_text = "I am Studying"

upper_case , lower_case = count_letter(sample_text)

print("Upper case numbers: ",upper_case)
print("lower case numbers: ", lower_case)
#counting all letters
def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1

    return letters
sample_text = "I am Studying"
letters = count_letter(sample_text)
print("Total letters are: ", letters)
