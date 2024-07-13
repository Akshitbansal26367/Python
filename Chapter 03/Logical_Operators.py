"""and
or
not"""

p = 70
print(p >= 48)  # true
print(p < 60)  # false
print(48 <= p < 60)  # print(p >= 48 and p < 60) false

s1 = 32
s2 = 90
s3 = 22
print(s1 < 35 or s2 < 35 or s3 < 35)  # true
print(not s1 < 35)  # false
