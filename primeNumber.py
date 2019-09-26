num = 10000

while(1):
    flag = True
    for i in range(2,num):
	if num % i == 0:
	    flag = False
	    break
    if flag == True:
	print(num)
    num += 1
