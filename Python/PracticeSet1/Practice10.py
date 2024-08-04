# check for list is palindrome or not

lists = [1,2,3,2,1]
print("original lists ", lists)
lists1 = lists.copy()

#reverse duplicate lists
lists1.reverse()
print("reverse lists ", lists1)

if(lists == lists1):
    print("lists is palindrome")
else:
    print("lists is not palindrome")
    

# palindrome for characters 
list1 = ["m", "a", "n", "m"]

# copy lists
copy_lists = list1.copy()
#reverse lists
copy_lists.reverse()

# compare both the lists
if(list1 == copy_lists):
    print("list is palindrome ")
else:
    print("lists is not palindrome")
    
