nums = [23,21,82,14,19]
print(nums)

print(nums[0])

names=['keer','kuku','nav']

print(names)

mil = [nums, names]

print(mil)

nums.insert(2,77)
print(nums) #inserts inbetween

nums.remove(14)
print(nums) #Removes the value

nums.pop(1)
print(nums) #pops out the index of 1

nums.pop()
print(nums)  #when not specified index,it pops out the last element FILO(first in last out)

#to delete multiple values
del nums[2:]
print(nums)

#to add multiple values
nums.extend([29,12,13,14,36])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

a= nums.sort()
print(a)

####TUPLES IS NOT MUTABLE (LIST IS MUTABLE)

tup= (21,36,24,13)
print(tup)
print(tup[1])

#tup[1] = 33 #tuples don't support item assignment

set = {23,13,14,13,76}

print(set) #only once 13 came ,no proper seqeuncing, no index

#set is same as list,tuple but not support sequence and duplicates
