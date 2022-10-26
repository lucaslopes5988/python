num_str = input("Enter your number: ")
num_chars = list(num_str)
print(num_chars)

sum = 0
i = 0

while (i < len(num_chars)):
  sum = sum + int(num_chars[i])
  i = i+1
print(sum)