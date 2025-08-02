#Grade average
first_score=float(input('What was your grade on the first test?'))
second_score=float(input('What was your grade on the second test?'))

average= (first_score + second_score)/2

if average < 5:
	print(f'Your average was {average}, you failed!\n')
elif average >=5 and average <= 6.9:
	print(f'Your average was {average}, you need to do a retake test!\n')
else:
	print(f'Your average was {average}, you passed!\n')