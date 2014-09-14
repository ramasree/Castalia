__author__ = 'sreeram'
#Program to add,delete,score an indel into the string


#function for adding indel
def add_indel(indx,Len_1,Len_2,str_chnge):

#Addition for string 1
    if str_chnge == 1:
        for i in range(Len_1):
            if i == indx:
                print "First sequence is :{} ".format(Str_1[:i] + "-"+ Str_1[i:])
                print "Second sequence is:{}".format(Str_2)
            elif indx > Len_1:
                Len_new = (indx - Len_1)+1
                Str_new1 = Str_1
                for k in range(0, Len_new):
                    Str_new1= Str_new1[:] + "-"
                print "First sequence is :{} ".format(Str_new1)
                print "Second sequence is:{}".format(Str_2)
                indx = Len_1

#Addition for string 2

    elif str_chnge == 2:
        for j in range(Len_2):
            if j == indx:
                print "First sequence is{}".format(Str_1)
                print "Second sequence is{}" .format(Str_2[:j]+"-"+Str_2[j:])
            elif indx > Len_2:
               Len_new = (indx - Len_2)+1
               Str_new2 = Str_2
               for k in range(0, Len_new):
                   Str_new2= Str_new2[:] + "-"
               print "First sequence is:{}".format(Str_1)
               print "Second sequence is :{} ".format(Str_new2)
               indx = Len_2
    else:
        pass

#function for deleting an indel
def del_indel(indx,Len_1,Len_2,str_chnge):
    Str_new1 = Str_1
    Str_new2 = Str_2

#deletion for string 1

    if str_chnge == 1:
        for i in range(Len_1):
            if i == indx:
                if Str_new1[i] == "-":
                    print "First sequence is:{}".format(Str_new1[:i]+Str_new1[(i+1):])
                    print "Second sequence is :{}".format(Str_new2)
                else:
                    print "Not an indel"
            elif indx>Len_1:
                Len_new = (indx - Len_1)+1
                Str_new1 = Str_1
                for k in range(0, Len_new):
                    if Str_new1[indx] == "-":
                        print "First sequence is:{}".format(Str_new1[0:indx])
                    else:
                        print "Not an indel"
                print "First sequence is :{} ".format(Str_new1)
                print "Second sequence is:{}".format(Str_2)
                indx = Len_1


  #deletion for string 2
    elif str_chnge == 2:
        for i in range(Len_2):
            if i == indx:
                if Str_new2[i] == "-":
                    print "First sequence is :{}".format(Str_new1)
                    print "Second sequence is:{}".format(Str_new2[:i]+Str_new2[(i+1):])
                else:
                    print "Not an indel"

            elif indx>Len_2:
                Len_new = (indx - Len_2)+1
                Str_new2 = Str_2
                for k in range(0, Len_new):
                    if Str_new2[indx] == "-":
                        print "First sequence is:{}".format(Str_new2[0:indx])
                    else:
                        print "Not an indel"
                print "First sequence is:{}".format(Str_2)
                print "Second sequence is :{} ".format(Str_new2)
                indx = Len_2


#function for scoring an indel
def score_indel(Len_1,Len_2,str_chnge):
    Str_new1 = Str_1
    Str_new2 = Str_2
    Str_new4 =''
    Str_new5 =''
    similarity = 0
    dissimilarity =0


#score for string 1
    if (str_chnge == 1)|(str_chnge == 2):
        print Len_1
        print Len_2
        if Len_1==Len_2:
            for i,j in zip(Str_new1,Str_new2):
                if i==j:
                    Str_new4 += i.lower()
                    Str_new5 += j.lower()
                    similarity+=1
                else:
                    Str_new4 += i.upper()
                    Str_new5 += j.upper()
                    dissimilarity+=1

            print "The first sequence is : {}".format(Str_new4)
            print "The second sequence is : {}".format(Str_new5)
            print "The similarity is:{}".format(similarity)
            print "The dissimilarity is :{}".format(dissimilarity)

        elif Len_1!=Len_2:
            if Len_1>Len_2:
                Len_new = Len_1 - Len_2
                for k in range(Len_new):
                    Str_new2 = Str_new2 + "-"

                for i,j in zip(Str_new1,Str_new2):
                    if i==j:
                        Str_new4 += i.lower()
                        Str_new5 += j.lower()
                        similarity+=1
                    else:
                        Str_new4 += i.upper()
                        Str_new5 += j.upper()
                        dissimilarity+=1

                print "The first sequence is : {}".format(Str_new4)
                print "The second sequence is : {}".format(Str_new5)
                print "The similarity is:{}".format(similarity)
                print "The dissimilarity is :{}".format(dissimilarity)

            elif Len_2>Len_1:
                Len_new = Len_2 - Len_1
                for k in range(Len_new):
                    Str_new1 =Str_new1 + "-"
                for i,j in zip(Str_new1,Str_new2):
                    if i==j:
                        Str_new4 += i.lower()
                        Str_new5 += j.lower()
                        similarity+=1
                    else:
                        Str_new4 += i.upper()
                        Str_new5 += j.upper()
                        dissimilarity+=1

                print "The first sequence is : {}".format(Str_new4)
                print "The second sequence is : {}".format(Str_new5)
                print "The similarity is:{}".format(similarity)
                print "The dissimilarity is :{}".format(dissimilarity)




Str_1 = raw_input("Enter the 1st string:")
Str_2 = raw_input("Enter the 2nd string:")
Str_new1 = Str_1
Str_new2 = Str_2

while 1:
    print "Please select the below commands:\n 'a' for adding an indel \n 'd' for deleting an indel \n 's' for score an indel \n 'q'for quit"
    sel_cmd = raw_input("Select a command :")
    str_chnge = raw_input("Enter the sring to change:1 or 2")
    Len_1 = len(Str_1)
    Len_2 = len(Str_2)


    #For string 1

    if str_chnge.isdigit() == True:

        str_chnge = int(str_chnge)

    #Adding an indel for string1
        if sel_cmd == 'a':
            indx = raw_input("Index at which you wish to place the indel:")
            if indx.isdigit()==True:
                indx = int(indx)
                if indx >= Len_1:
                    add_indel(indx,Len_1,Len_2,str_chnge)
                else:
                    add_indel(indx,Len_1,Len_2,str_chnge)
            else:
                print "Enter valid index"

    #deleting an indel for string 1
        elif sel_cmd == 'd':
            indx = raw_input("Index at which you wish to place the indel:")
            if indx.isdigit() == True:
                indx =int(indx)
                if indx  >=Len_1:
                     del_indel(indx,Len_1,Len_2,str_chnge)
                else:
                    del_indel(indx,Len_1,Len_2,str_chnge)
            else:
                print "Enter valid index"

    #scoring an indel for string 1
        elif sel_cmd == 's':
            Len_1 = int(Len_1)
            Len_2 = int(Len_2)
            score_indel(Len_1,Len_2,str_chnge)

        #quiting from program
        elif sel_cmd == 'q':
            break
        else:
            pass

    # For string 2

        str_chnge = int(str_chnge)


    #Adding an indel for string 2
        if sel_cmd == 'a':
            indx = raw_input("Index at which you wish to place the indel:")
            if indx.isdigit()==True:
                indx =int(indx)
                if indx>=Len_2:
                    add_indel(indx,Len_1,Len_2,str_chnge)
                else:
                    add_indel(indx,Str_1,Str_2,str_chnge)
            else:
                print "Enter valid index"

    #Deleting an indel for string 2

        elif sel_cmd == 'd':
            indx = raw_input("Index at which you wish to place the indel:")
            if indx.isdigit() == True:
                indx =int(indx)
                if indx>=Len_2:
                     del_indel(indx,Len_1,Len_2,str_chnge)
                else:
                    del_indel(indx,Len_1,Len_2,str_chnge)
            else:
                print "Enter valid index"


    #Scoring an indel for string 2

        elif sel_cmd == 's':
            Len_1 = int(Len_1)
            Len_2 = int(Len_2)
            score_indel(Len_1,Len_2,str_chnge)


    #Quiting from program

        elif sel_cmd == 'q':
            break
        else:
            pass

    #For incorrect strings
    else:
        pass














