# A dictionary can contain dictionaries, this is called nested dictionaries.
course = {
    'php': {'duration': '3 Months', 'fees': 15000},
    'java': {'duration': '2 Months', 'fees': 10000},
    'python': {'duration': '2 Months', 'fees': 12000},
}
print("Nested Dictionary is", course)
print("php row is", course['php'])
# course['java']['fees'] = 20000 updating value of fees item in java key
print("java fees is", course['java']['fees'])

print()
for i, j in course.items():
    # print(i, j)
    print(i, j['duration'], j['fees'])
