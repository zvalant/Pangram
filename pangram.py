def pangram(string):
    str_set = [] # create an empty list and make all char lower case to prevent duplicates
    string.lower()
    for char in string: # for loop that will add to list if is lower and not already in list
        if char.islower() and char not in str_set:
            str_set.append(char)
        print(str_set)
    return len(str_set) == 26  # boolean will check to see if length is equal to total letters in alphabet

