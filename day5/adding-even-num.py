#Write your code below this row 👇

total = 0

for n in range(0, 101):
  if n % 2 == 0:
    total += n
    print(total)

print("The sum off all even numbers from 1 to 100 is " + str(total))
