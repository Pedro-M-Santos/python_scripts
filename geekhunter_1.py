

testcases = raw_input()
numbers = raw_input().split()
print numbers

for turns in range(int(testcases)):
	for i in range(1,int(numbers[turns])+1,1):
		if ((i%3==0) and (i%5==0)):
			i = "FizzBuzz"
		elif (i%5==0):
			i = "Buzz"
		elif (i%3==0):
			i = "Fizz"
		print i
