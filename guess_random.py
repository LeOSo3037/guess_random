import random
r = random.randint(1, 100)
count = 0
while True:
	count +=1
	g = input('Please guess a number from 1 to 100\n')
	g = int(g)

	if g == r:
		print('You are correct!!! You guessed', count, 'times!!')
		break

	elif g > 100:
		print('Don\'t enter a number grater than 100!!')

	elif g < 0:
		print('Don\'t enter a number smaller than 0!!')

	else:
		if g > r:
			print('Your guess is LARGER than the answer! You guessed', count, 'times!!')
		if g < r:
			print('Your guess is SMALLER than the answer! You guessed', count, 'times!!')

