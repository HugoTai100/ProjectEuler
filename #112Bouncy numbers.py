"""Bouncy numbers
Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
# return 0 if decreasing,1 if increasng, 2 if bouncy
def test(number):
	number = list(str(number))
	for i in range(len(number)):
		number[i] = int(number[i])
	sum = 0
	for i in range(len(number)-2):
		if number[i] <= number[i + 1] <= number[i + 2]:
			sum += 1
		elif number[i] >= number[i + 1] >= number[i + 2]:
			sum -= 1
		
	if -sum == len(number) - 2:
		return 0
	elif sum == len(number) - 2:
		return 1
	else:
		return 2
print(test(10101))
total = 0
number = 100
for i in range(100,1000000):
	if test(i) == 2:
		total += 1
	if total  == i * 0.90:
		print(i, total)
		break 

print(i)





