from functools import reduce, lru_cache


# Find the unique number in a list, with cache        
@lru_cache
def find_unique_listcached(arr):
    dic_numbers={}
    for number in arr:
        if number not in dic_numbers: dic_numbers[number]=1
        else: dic_numbers[number]+=1
    for x, y in dic_numbers.items():
        if y ==1: return x   
        
  
'''
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
Example(Input => Output):
35231 => [1,3,2,5,3]

'''
#
#
def digitize_reverse(n):
    list=[]
    for num in reversed(str(n)):
        list.append(int(num))
    return list


'''
Essentially, rearrange the digits to create the highest possible number.
Input: 145263 Output: 654321
'''
def descending_order(num):
    numbers = list(str(num))
    numbers.sort(reverse=True)
    return int(''.join(numbers))
        
 
        
        
        