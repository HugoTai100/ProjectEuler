def check(number):
	number = str(number)
	if number[0] == "1" and number[2] == "2" and number[4] == "3" and number[6] == "4" and number[8] == "5" and number[10] == "6" and number[12] == "7" and number[14] == "8" and number[16] == "9" and number[18] == "0":
		
		return 1
	return 0

for i in range(1010101010,9010101010, 10):
	if check(i*i) == 1:
		print(i*i)
		break