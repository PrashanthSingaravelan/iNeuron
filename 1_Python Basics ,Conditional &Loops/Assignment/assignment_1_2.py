first_name = "Prashanth"
last_name = "S"

str1 = []
for i in range(1, len(first_name) + 1):
    str1.append(first_name[-i])

str1.append(" ")

for i in range(1, len(last_name) + 1):
    str1.append(last_name[-i])

print("".join(str1))
