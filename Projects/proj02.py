__author__ = 'sreeram'
print "This puzzle is favoured by Einstein.You will be asked to enter a three digit number,where hundred's number differs from one's digit by atleast two,The procedure will always yield 1029"
x = raw_input("Give me your number")
if x.isdigit()== True:
    print "For the number:{} the reverse number is:{}".format(x,x[::-1])
    print "The difference between {} and {} is : {} ".format(int(x),int(x[::-1]),int(x[::-1])-int(x))
    print "The reverse difference is {}".format(str(int(x[::-1])-int(x))[::-1])
    print "The sum of {} and {} is {}".format(int(x[::-1])-int(x),str(int(x[::-1])-int(x))[::-1],int(str(int(x[::-1])-int(x))[::-1])+int(x[::-1])-int(x))
else:
    print "Give Valid input"
