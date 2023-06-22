# def strcounter(s):  #O(N^2)
#     print(set(s))
#     for sym in set(s):
#         counter = 0
#         for sub_s in s:
#             if sym == sub_s:
#                 counter += 1
#         print(sym, '-', counter)

# # strcounter('abbbcd')

# def strcounter2(s):   #O(N+M)  => O(2*N)  => O(N)
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sym] = syms_counter.get(sym, 0) + 1

#     for sym, count in syms_counter.items():
#         print(sym, '-', count)

# strcounter2('aabccc')

def palindrome(s): 
    return s[::-1] == s 

s = input("enter word: ") 
print( 'True' if palindrome(s) else "False")
