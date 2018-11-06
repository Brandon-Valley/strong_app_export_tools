# ('hi', 4) = 'hi  '
def add_spaces_for_min_length(str, min_length):
#     if len(str) < min_length:
#         return str + ' ' * (1 + min_length - len(str))
#     else:
#         return str

    while(len(str) < min_length):
        str += ' '
    return str


a = '3'
b = '10.4'

print(add_spaces_for_min_length(a, 6) + 'o')
print(add_spaces_for_min_length(b, 6) + 'o')

print(float(a))