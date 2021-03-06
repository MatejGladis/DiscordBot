# Created by Matko
import random


# Function IsValid checks if the entered input is number
def IsValid(Expression):
    try:
        int(Expression)
        return True
    except:
        return False


# Function AddSpaces isolate numbers and characters form each other
def AddSpaces(Expression):

    #plus checker
    for i in range(len(Expression)):
        if i > 1 and IsValid(Expression[i]) == True and Expression[i-1] == " ":
            a = 0
            for j in range (i):
                if Expression[i-j] == "+" or Expression[i-j] == "d" or Expression[i-j] == "D":
                    a=1
                if Expression[i-j] != "+" and Expression[i-j] != "d" and Expression[i-j] != "D" and Expression[i-j] != "D" and Expression[i-j] != " " and a == 0 and j != 0:
                    return False

    # SpaceRamover creates ramoves spaces for the Expression in for i cyclus
    SpaceRamover = Expression.split(" ")
    Expression = ""

    for i in range(len(SpaceRamover)):
        Expression += SpaceRamover[i]

    Position = 0

    # While isolate numbers and characters form each other
    while True:
        # This while works while it find first nonnumber character
        while True:
            Position += 1
            if Position >= len(Expression):
                break
            if IsValid(Expression[(Position - 1):(Position + 1)]) == False:
                break

        if Position >= len(Expression):
            break

        # This adds space between characters
        Expression = Expression[:Position] + " " + Expression[(Position):]
        Position += 1

    return Expression


# random roll
def Roll(a):
    sum = random.randint(1, a)
    return sum


# Write each roll and final sum of rolls
def Calc(Expression):
    ExpressionList = Expression.split(" ")
    Positon = 0
    FinalList = []
    FinalSum = 0

    while True:

        if IsValid(ExpressionList[Positon]) == True:

            # for + or -
            if len(ExpressionList) == Positon + 1 or IsValid(ExpressionList[Positon + 1]) == True:

                FinalList.append(ExpressionList[Positon])
                FinalSum += int(ExpressionList[Positon])

            # for dices
            #elif ExpressionList[Positon + 1] == "d" or ExpressionList[Positon + 1] == "D" and IsValid(ExpressionList[Positon + 2]) == False:
                #return False
            elif ExpressionList[Positon + 1] == "d" or ExpressionList[Positon + 1] == "D" and IsValid(ExpressionList[Positon + 2]) == True:

                for i in range(int(ExpressionList[Positon])):
                    Calc = Roll((int(ExpressionList[Positon + 2])))
                    FinalList.append(str(Calc))
                    FinalSum += int(Calc)

                Positon += 2

            elif ExpressionList[Positon+1] == "+" and IsValid(ExpressionList[Positon + 2]) == False and ExpressionList[Positon + 2] != "d" and ExpressionList[Positon + 2] != "D":
                return False

            elif ExpressionList[Positon+1] == "+" and IsValid(ExpressionList[Positon + 2]) == True or ExpressionList[Positon + 2] == "d" or ExpressionList[Positon + 2] == "D":
                FinalList.append(ExpressionList[Positon])
                FinalSum += int(ExpressionList[Positon])
                Positon += 1

            else:
                return False

        elif ExpressionList[Positon] == "d" and len(ExpressionList) != Positon + 1:
            if IsValid(ExpressionList[Positon + 1]) == True:
                Calc = Roll((int(ExpressionList[Positon + 1])))
                FinalList.append(str(Calc))
                FinalSum += int(Calc)
                Positon += 1
            else:
                return False

        else:
            return False

        Positon += 1
        if Positon == len(ExpressionList) == Positon:
            break

    return FinalList, FinalSum


#Core of the program
def Main(Expression):
    Expression = str(Expression)
    Expression = AddSpaces(Expression)
    if Expression == False:
        return False
    Expression = Calc(Expression)
    return Expression
