__author__ = 'sreeram'
#program to print the latin square
Order = raw_input("Please Enter the order of square:")
First_num = raw_input("Please input the top left number:")
#To check order and First numbers are integers
if Order.isdigit() == True & First_num.isdigit() == True:
    Order = int(Order)
    First_num = int(First_num)
    if First_num > Order:
        print "Error"
    else:
        for i in range(0, Order):
            for j in range(0, Order):
                if First_num < Order:
                    print First_num,
                    First_num += 1
                else:
                    print First_num,
                    First_num = 1
            print "\n"
            First_num += 1

            if First_num < Order:
                pass
            elif First_num == Order:
                pass
            else:
                First_num = 1



else:
    print "Invalid Input"
