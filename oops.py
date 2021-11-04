'''class student:    
	name="abc"    
	def abc():        	
		print('student abc')
student.abc()
a=student.abc()
print(a)'''

def max1(l):
    c=l[0]
    for i in l:
        if c < i:
            c=i
    return c
n=int(input())
