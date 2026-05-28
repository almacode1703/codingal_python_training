# 1. Odd and Even numbers using List Comprehension

num = int(input("Enter a number: "))

odd_list = [i for i in range(1, num + 1) if i % 2 != 0]
even_list = [i for i in range(1, num + 1) if i % 2 == 0]

print("Odd Numbers List :", odd_list)
print("Even Numbers List :", even_list)


# 2. Capitalize first letter of fruits

fruits = ["apple", "banana", "mango", "orange", "grapes"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("\nOriginal Fruits List :", fruits)
print("Updated Fruits List :", updated_fruits)