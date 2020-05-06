import random

def IsValid(Expression):
    try:
        int(Expression)
        return True
    except:
        return False

def AddSpaces(Expression):
    SpaceRamover = Expression.split(" ")
    Expression = ""

    for i in range(len(SpaceRamover)):
        Expression += SpaceRamover[i]
    Position = 0

    while True:
        while True:
            Position += 1
            if Position >= len(Expression):
                break
            if IsValid(Expression[(Position - 1):(Position + 1)]) == False:
                break

        if Position >= len(Expression):
            break

        Expression = Expression[:Position] + " " + Expression[(Position):]
        Position += 1

    return Expression

def Roll(a):
    sum = random.randint(1, a)
    return sum

def Calc(Expression):
    ExpressionList = Expression.split(" ")
    Positon = 0
    FinalList = []
    FinalSum = 0

    while True:

        if IsValid(ExpressionList[Positon]) == True:

            if len(ExpressionList) == Positon + 1 or IsValid(ExpressionList[Positon + 1]) == True:

                FinalList.append(ExpressionList[Positon])
                FinalSum += int(ExpressionList[Positon])
            elif ExpressionList[Positon + 1] == "d" or ExpressionList[Positon + 1] == "D" and IsValid(ExpressionList[Positon + 2]) == False:
                return False
            elif ExpressionList[Positon + 1] == "d" or ExpressionList[Positon + 1] == "D" and IsValid(ExpressionList[Positon + 2]) == True:

                for i in range (int(ExpressionList[Positon])):

                    Calc = Roll((int(ExpressionList[Positon + 2])))
                    FinalList.append(str(Calc))
                    FinalSum += int(Calc)

                Positon += 2

            else:
                return False
        else:
            return False

        Positon += 1
        if Positon == len(ExpressionList) == Positon:
            break

    return FinalList, FinalSum

def Main(Expression):
    Expression = str(Expression)
    Expression = Expression[5:]
    Expression = AddSpaces(Expression)
    Expression = Calc(Expression)
    return Expression

Main()
