a = "11"
b = "1"
# a_, b_, c, d = 0, 0, 0, 0
# for i in a[::-1]:
#     a_ = a_ + int(i)*pow(2,c)
#     c = c + 1
# for j in b[::-1]:
#     b_ = b_ + int(j)*pow(2,d)
#     d = d + 1
a, b = int(a, 2), int(b, 2)
res = str(bin(a + b)).replace('0b','')
print(res)