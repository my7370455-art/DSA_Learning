#judge two strings are equal or not, without influence of upper/lower case and space
def equal_strings(str1, str2):
    #remove space and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    #compare the two strings
    return str1 == str2

str1 = input()
str2 = input()
if equal_strings(str1, str2):
    print("YES")
else:
    print("NO")