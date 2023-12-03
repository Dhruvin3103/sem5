# # # append()-appends element to list
# # print("append() function")
# # list1 = [10, 20, 30]
# # print("Original list:", list1)
# # list1.append(50)
# # print("List After Appending 50:", list1)
# # # extend()- extends by adding on with new list
# # print("extend() function")
# # list1 = [10, 20, 30]
# # print("Original list:", list1)
# # list2 = [222, 333]
# # list1.extend(list2)
# # print("After extending to list2, the original list is : ", list1)
# # # insert() – inserts element at particular location
# # print("insert() function")
# # list1 = [10, 20, 30]
# # print("Original list:", list1)
# # list1.insert(2, 15)
# # print("List After Appending 15:", list1)
# # # pop()- pops element from list
# # print("pop() function")
# # list1 = [10, 20, 30]
# # print("Original list:", list1)
# # list1.pop(2)
# # print("List after poping from index 2:", list1)
# # # copy()-copies a list
# # print("copy() function")
# # list1 = [10, 20, 30]
# # print("Original list:", list1)
# # list2 = list1.copy()
# # print("Copied list is:", list2)
# # # clear()-clears the list
# # print("Clear() function")
# # list1 = [10, 20, 30]
# # print("Original list:", list1)
# # list2 = list1.clear()
# # print("List after clearing:", list2)

# tuple1 = (10, 20, 30, 50, 50, 70, 90, 80, 100)
# print("Original tuple:", tuple1)
# # len()- length of tuple
# print("len() function")
# print("The length of tuple is:",len(tuple1))
# # count()-repetation of element in tuple
# print("count() function")
# print("The count of 50 in tuple is:",tuple1.count(50))
# # index()- gives index of element in tuple
# print("Index() function")
# print("The index of 80 in tuple is:", tuple1.index(80))
# # sort()-sorts the elements in tuple
# print("sort() function")
# print("The sorted tuple is:", sorted(tuple1))
# # min()- gives minimum element of tuple
# print("min() function")
# print("The minimum element of tuple is:", min(tuple1))
# # max()- gives maximum element of tuple
# print("max() function")
# print("The maximum element of tuple is:", max(tuple1))
# # sum()-gives sum of elements in tuple
# print("sum() function")
# print("The sum of elements in tuple is:", sum(tuple1))
# set1 = {'a','b', 'c', 'd', 'e'}
# print("Original set is:", set1)
# # add()- adds element to set
# set1.add('f')
# print("add() function")
# print("Set after adding 'f'", set1)
# # discard() – discards element from set
# set1.discard('e')
# print("discard() function")
# print("Set after discarding/Updating 'e': ",set1)
# # remove() – removes element from set
# set1.remove('a')
# print("remove() function")
# print("Set after removing 'a':", set1)
# # pop()- pops element from the set
# set1.pop()
# print("pop() function")
# print("Set after poping elements:", set1)
# # clear()-clears the set
# set1.clear()
# print("clear() function")
# print("Set after clearing:",set1)
dict1 = {'1': 'One','2':'Two','3':'Three'}
print("Original dictionary:", dict1)
# copy()- copies the dictionary
dict2 = dict1.copy()
print("Copied Dictionary :",dict2)
# fromkeys() – gives details from dictionary
seq = ('1', '2', '3')
print("fromkeys() method")
print(dict1.fromkeys(seq, None))
# clear()- clears the dictionary
dict1.clear()
print("clear() function")
print("The dictionary after clearing it:", dict1)
