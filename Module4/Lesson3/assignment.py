test_dict = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}

print("Test Dictionary:")
print(test_dict)

value = int(input("Enter the value to check frequency: "))

count = 0

for v in test_dict.values():
    if v == value:
        count += 1

print("Frequency of value", value, "is =", count)