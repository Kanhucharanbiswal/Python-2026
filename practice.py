for i in range(1, 11):
    print(i)

#Check if a number is even or odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Find factorial of a number
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)

#Check prime number
num = 13
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#Find largest number in a list
numbers = [10, 45, 67, 23]
print(max(numbers))

#Count vowels in a string
text = "data science"
count = 0
for char in text:
    if char in "aeiou":
        count += 1
print(count)

#Remove duplicates from list
numbers = [1, 2, 2, 3, 4, 4]
unique = list(set(numbers))
print(unique)

#Find sum of list elements
numbers = [10, 20, 30]
print(sum(numbers))

#Swap two numbers
a = 5
b = 10
a, b = b, a
print(a, b)
