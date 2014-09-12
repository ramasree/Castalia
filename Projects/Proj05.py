__author__ = 'sreeram'
# Program to calculate a simple calculator


def operation(Exp_0,Exp_2,Exp_1):
    Exp[0]=Exp_0
    Exp[2]=Exp_2
    if Exp[1] == '+':
        print Exp[0]
        print Exp[2]
        print Exp_1, '= {}'.format(float(Exp[0])+float(Exp[2]))
    elif Exp[1] == '-':
        print Exp_1, '= {}'.format(str((float(Exp[0])-float(Exp[2]))))
    elif Exp[1] == '*':
        print Exp_1, '= {}'.format(str((float(Exp[0])*float(Exp[2]))))
    elif Exp[1] == '/':
        if float(Exp[2])!= '0':
            print Exp_1, '= {}'.format(str((float(Exp[0])/float(Exp[2]))))
        else:
            print "Error"
    else:
        print "Enter valid Operator +,-,*,/"



while(1):
    Exp_1 = raw_input("Enter the input in format(Operand Operator Operand)")
    Exp = Exp_1.split()
    if len(Exp) == 3:
        if Exp[0].isdigit() == True & Exp[2].isdigit() == True:
            Exp_2 = Exp[2]
            E0 = Exp[0]
            operation(E0,Exp_2, Exp_1)
            if ((Exp[1] =='+')|(Exp[1] == '-')|(Exp[1] == '*')|(Exp[1] == '/')):
                y = raw_input("Do you want to contine:y/n")
                if y == 'y':
                    pass
                elif y == 'Y':
                    pass
                elif y == 'Yes':
                    pass
                elif y == 'YES':
                    pass
                elif y == 'n':
                    break
            else:
                pass
        elif Exp[0].find(".") == True & Exp[2].find(".") == True:
            Exp_0= Exp[0]
            Exp_2= Exp[2]
            Exp_0 =float(Exp_0)
            Exp_2 =float(Exp_2)
            operation(Exp_0,Exp_2,Exp_1)
            if (Exp[1] =='+') | (Exp[1] == '-') | (Exp[1] == '*')| (Exp[1] == '/'):
                y = raw_input("Do you want to contine:y/n")
                if y == 'y':
                    pass
                elif y == 'Y':
                    pass
                elif y == 'Yes':
                    pass
                elif y == 'YES':
                    pass
                elif y == 'n':
                    break

        else:
            print "Operands are invalid"
    else:
        pass


















