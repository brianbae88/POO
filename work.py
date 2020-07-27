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

gradebook = """
# ignore blank lines and lines starting with #'s
wilma,91,93,0
fred,80,85,90,95,100
betty,100
"""

def studentwithhighestavg(gradeBook):
	maxAvg = 0
	maxAvgName = ""
	for sentences in gradeBook.splitlines():
		if sentences[0:1] == '#' or sentences[0:1] == "":
			continue
		z = sentences.split(',')
		add = 0
		name = ''
		for i in range (1,len(z)):
			z[i] = int(z[i])
			add += z[i] 
			name = z[0]
		avg = add / len(z[1:])
		if avg > maxAvg:
			maxAvg = avg
			maxAvgName = name
		return maxAvg , maxAvgName


		


	
#여기서 이 z list를 int로 다 바꾼 다음 z[0:]까지 더하고 그 len(z)만큼 나누면 avg가 나올 수 있을거같다. notes 3에 해놓은거 처럼 maxavg = a 고 c 가 variable b가 int가 된 z
	

#근데 만약에 z를 라인별로 할수있었으면 더 좋을듯. 라인별로 split?? 


	
		# print a
	
		# for a in z:
		# 	a = int(a)
		# 	print a 

		# for b in len(z):
		# 	print b
		# print z
		# print max(z)
		# for avg in z:
		# 	avg = int(avg)
		# 	print avg
		





print studentwithhighestavg(gradebook)




















