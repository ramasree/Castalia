__author__ = 'sreeram'
#Program to play mastermind game

#input the key for playing mastermind game
key= raw_input("Enter the 4 digit key:")
guess_times = 0
guess_count = 0
guess_Chance = 12
number = ""
clue = ""

while guess_times<=12:

# Entering the value to break the key
    guess_key = raw_input("Break the Key ")

# Checking guessed key is a digit or not
    if guess_key.isdigit() == True:
        len_1 = len(guess_key)
        if len_1 == 4:
            for i in range(len_1):
                guess_count = guess_key.count(guess_key[i])
                print "Count is{}".format(guess_count)
                if guess_count !=1:
                    print "Error:The values are repeated"
                    break
                else:
                    print "The key values are perfect"
                    break
            for i,j in zip(guess_key,key):
                if guess_key==key:
                    print "Congrats!!!,You won the game,Key{}".format(key)
                    exit()
                elif guess_count ==1:
                    if i == j:
                        print "The number {} is in correct position {}".format(i,guess_key.index(i)+1)
                    else:
                        for k in range(len_1):
                            for i,j in zip(guess_key,key):
                                if guess_key[k]== j:
                                    print "The number {} in incorrect position{}".format(j,guess_key.index(j)+1)
                                    break
                                else:
                                    pass
                else:
                    pass

            print "Wrong Key,\nHistorical value is {}\nYou have {} times of chance".format(guess_key,guess_Chance)
            guess_Chance-=1

            if guess_times==12:
                print"You Lose\n Key is : {}".format(key)
                exit()
            guess_times+=1

        else:
            print "Please enter four key value"

    else:
        print "Entered key value is not a number"











