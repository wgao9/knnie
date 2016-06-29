import numpy.random as nr
import knnie 

def main():
	x = nr.normal(0,1,[1000,1])
	y = nr.normal(0,1,[1000,1])
	z = nr.normal(0,1,[1000,1])
	print "I(X;Y) = ", knnie.kraskov_mi(x,y)
	print "I(X;Y) = ", knnie.revised_mi(x,y)
	print "I(X;Y;Z) = ", knnie.kraskov_multi_mi(x,y,z)
	print "I(X;Y;Z) = ", knnie.revised_multi_mi(x,y,z)

if __name__ == '__main__':
	main()


