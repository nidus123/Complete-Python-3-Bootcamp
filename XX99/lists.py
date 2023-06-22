my_list = [1, 2, 3, 4, 5, 6, "this is a test string full of "]

my_list_with_stuff = ["stuff",1,2.3331, 1/2]


len (my_list)
len (my_list_with_stuff)


my_list_with_stuff[0] = my_list_with_stuff[0].upper()

new_list = my_list[6] + my_list_with_stuff[0]
print (new_list)


my_list_with_stuff.append(5-8)

popped_list = []
popped_list.append(my_list_with_stuff.pop())

print(popped_list)
print(my_list_with_stuff)


new_list1 = ['a', 'e', 'b', 'c', 'd', 't', 'y', 'e', 'r', 'a']
new_list2 = [1,5,67,8,6,2,3,0,9]

new_list1.sort()

new_list1