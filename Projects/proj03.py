__author__ = 'sreeram'
# The program to compute and display information for a utility company
#calculating amount of money billed to customerend customer

def meter_value_difference(Begg_read, End_read):
    if (End_read > Begg_read):
        useage_value = (End_read - Begg_read) / 10.0
    else:
        useage_value = float((999999999 - Begg_read + End_read + 1) / 10.0)
    return useage_value

#infinite loop
while (1):
    cust_code = raw_input("Enter the customer code")
    Begg_read = raw_input("Enter beggining meter reading")
    End_read = raw_input("Enter end meter reading")
    #calling meter difference
    #Amount payment for Reidential cutomers
    if Begg_read.isdigit() == True & End_read.isdigit() == True:
        value = meter_value_difference(float(Begg_read), float(End_read))
        if cust_code == 'r':
            amount_payment = 5.00+(value*0.0005)
            print "Beginning meter reading:{}\nEnd meter reading:{}\ngallons of water used{}\nAmount to be paid{}".format(Begg_read,End_read,value,amount_payment)
        #Amount payment for commercial customers
        elif cust_code == 'c':
            if value <= 4000000000:
                amount_payment = 1000
                print "Beginning meter reading:{}\nEnd meter reading:{}\ngallons of water used{}\nAmount to be paid{}".format(
                    Begg_read, End_read, value, amount_payment)
            else:
                amount_payment = (1000 + (value-4000000000) * 0.00025)
                print "Beginning meter reading:{}\nEnd meter reading:{}\ngallons of water used{}\nAmount to be paid{}".format(
                    Begg_read, End_read, value, amount_payment)
        #Amount payment for industrial customers
        elif cust_code == 'i':
            if value <= 4000000000:
                amount_payment = 1000
                print "Beginning meter reading:{}\nEnd meter reading:{}\ngallons of water used{}\nAmount to be paid{}".format(
                    Begg_read, End_read, value, amount_payment)
            elif (4000000000 <= value) & (10000000000 >= value):
                amount_payment = 2000
                print "Beginning meter reading:{}\nEnd meter reading:{}\ngallons of water used{}\nAmount to be paid{}".format(
                    Begg_read, End_read, value, amount_payment)
            else:
                amount_payment = float(2000 + (value-10000000000) * 0.00025)
                print "Beginning meter reading:{}\nEnd meter reading:{}\ngallons of water used{}\nAmount to be paid{}".format(
                    Begg_read, End_read, value, amount_payment)
        else:
            break

    else:
        print "Error"

















