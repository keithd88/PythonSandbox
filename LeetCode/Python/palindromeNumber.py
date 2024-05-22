"""
:type x: int
:rtype: bool
"""
x = 10258391

int_str = str(x)
len_int = len(int_str) - 1
# print(int_str, len_int)

rev_int = ''
for index, char in enumerate(int_str):
    rev_int += int_str[len_int-index]
    # print(rev_int)
    # print(int_str[index])

print(int_str, rev_int)

# if rev_int == int_str:
#     return True
# else:
#     return False