#-*- coding: utf-8 -*-


	# 	integer += 1 
	# 	if isItPrime(integer) == True: 
	# 		i += integer
	# 		i += counter
	# 	else:
	# 		i += integer
	# return integer
# a = [[1,2,3],[apple,grape],7,8,9,10]
# for i in a:
# 	print i

# a = [1,2,3,4,5,6,7,8]
# for i in a:

# def star(x):
# 	for i in range (0,x):
# 		for j in range (0,x-i):
# 			print (" ",end="")
# 		for k in range (0, 2 * i + 1):
# 			print ("*",end="")
# 		print ""

# print star(4)

# use helper function to seperate two sections of a star

#     *
#    ***
#   ***** 여기까지 하나

# 	 *** 여기까지 하나 (helper)
#     *

# helper는 range -1하고 function 반대로 쓰면 될듯? like for i in rage (0,x-1)



# s = 'abcda'
# if s[0] == s[-1]:
# 	return True


# def mostFrequentLetters(s):
# 	newstring = ""
# 	maxcounter = 0
# 	maxstring = ""
# 	s = s.lower().replace(" ","")
# 	while len(s) > 0:
# 		for i in range (0,len(s)): # 이걸 for i in s로 가능 range 쓸필요 x
# 			b = s.count(s[i])
# 			if b > maxcounter:
# 				maxcounter = b
# 				maxstring = s[i]
		
# 		newstring += maxstring
# 		s = s.replace( maxstring ,"") # ********
# 		maxcounter = 0
# 		maxstring = ""
# 	return newstring

# print mostFrequentLetters("We attack at dawn")
		
# currentcharacter = s[0]

# gradebook = """
# # ignore blank lines and lines starting with #'s
# wilma,91,93,0
# fred,80,85,90,95,100
# betty,100
# """



# def studentwithhighestavg(gradeBook):
# 	maxAvg = 0
# 	maxAvgName = ""
# 	for sentences in gradeBook.splitlines():
# 		if sentences[0:1] == '#' or sentences[0:1] == "":
# 			continue
# 		z = sentences.split(',')
# 		add = 0
# 		name = ''
# 		for i in range (1,len(z)):
# 			z[i] = int(z[i])
# 			add += z[i] 
# 			name = z[0]
# 		avg = add / len(z[1:])
# 		if avg > maxAvg:
# 			maxAvg = avg
# 			maxAvgName = name
# 	return maxAvg , maxAvgName #be careful of where the return thing is 

		


# myList = [['John, 100,93,92'],['Becky, 98,78,68,70'], ['Karen, 78, 98, 81, 78'], ['Joanne, 98, 78, 81, 85, 80'], ['Liv, 78, 95, 78, 67']]

# def question(myList):
# 	maxAvg = 0
# 	maxAvgName = ''

# 	for i in range (0,len(myList)):
# 		# print i 
# 		# print myList[i][0]
# 		# print type(myList[i])
# 		# print type(myList[i][0])
# 		z = myList[i][0].split(',') #뒤에 있는 [0]은 지금 'john,100,93,92'이걸 말하고있는거임 저거 하나가 one element inside the element
# 		# print len(z[1:])
# 		add = 0
# 		name = ''
# 		for f in range (1,len(z)):
# 			z[f] = int(z[f])
# 			add += z[f] 
# 			name = z[0]
# 		avg = add / len(z[1:])
# 		print avg
# 		if avg > maxAvg:
# 			maxAvg = avg
# 			maxAvgName = name
# 	return maxAvg , maxAvgName 


		

# 	# for i in range (1,)


# print question (myList)



def isPrime(x):
	if x == 1 or x < 0:
		return False
	for i in range (2, x):
		print i 
		if x % i == 0:
			return False
		else:
			return True

print isPrime(39)


def nthPrime(n):
	counter = 0
	integer = 0
	while counter < n:
		integer += 1
		if isPrime(integer) == True:
			counter += 1
		print counter, integer
	return integer

print nthPrime(4)

















