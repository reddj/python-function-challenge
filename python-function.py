#1
def sum_to(num):
  sum = 0
  for i in range(num + 1):
    sum += i
  print(str(num) + " : " + str(sum))

sum_to(6)

#2
def largest(ls):
  largest = 0
  for num in ls:
    if num > largest:
      largest = num
  print(str(largest))


largest([10, 4, 2, 231, 91, 54])

#3
def occurances(one, two):
	occur = 0
	for i in one:
		if(i == two):
			occur += 1
	print(str(occur))


occurances('fleep floop', 'fe')