def utf16_value(my_string):
    my_list = list(my_string)
    number_list = []
    for char in my_list:
        number_list.append(ord(char))
    return sum(number_list)

# These examples should all print True
print(utf16_value('Four score'))
print(utf16_value('Launch School'))
print(utf16_value('a'))
print(utf16_value(''))



