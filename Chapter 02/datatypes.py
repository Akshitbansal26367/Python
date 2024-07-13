a = 10
print(a, type(a))
a = 20.5
print(a, type(a))
a = 4 + 2j
print(a, type(a))

w = "welcome to wscube tech"
print(w, type(w))

w = '''
welcome 
    to 
        wscubetech'''
print(w, type(w))

l1 = [10, 20, "hello"]
print(l1, type(l1))
l1[1] = 40
print(l1, type(l1))

t = (10, 20, "hello")
print(t, type(t))

# important for interview --> Tuple must contain more than 1 value in the brackets.
# t1 = (50) is similar to t1 = 50

d = {
    'name': 'Pradeep',
    'course_name': 'Python'
}
print(d, type(d))

s = {10, 20, 10, 30}
print(s, type(s))
