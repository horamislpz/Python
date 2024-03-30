list_a = ['olive', 'palm', 'coconut']
print(list_a)

list_b = [8, 6, 7, 5, 3, 0, 8]
print(list_b)

list_c = ['Abidjan', 14.2, [1, 2, None], 'Zagreb']
print(list_c)

empty_list_1 = []
empty_list_2 = list()


# Indexing and slicing

phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[1])

phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[-1])

phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[1:4])

phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[:3])
print(phrase[3:])

my_list = ['Macduff', 'Malcolm', 'Duncan', 'Banquo']
my_list[2] = 'Macbeth'
print(my_list)

my_list = ['Macduff', 'Malcolm', 'Macbeth', 'Banquo']
my_list[1:3] = [1, 2, 3, 4]
print(my_list)

# List operations
num_list = [1, 2, 3]
char_list = ['a', 'b', 'c']
num_list + char_list

list_a = ['a', 'b', 'c']
list_a * 2 #But they cannot be subtracted or divided. 

num_list = [2, 4, 6]
print(5 in num_list)
print(5 not in num_list)




