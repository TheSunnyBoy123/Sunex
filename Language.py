vars = []
values = []
varType = []

def Input(vars, values, varType):
    toDo = input("|->")
    userInput = toDo.split()
    if(len(userInput) == 0):
        print("***Null value - Unknown to Sunex")
    elif (userInput[0] != "print"):  
        if len(userInput) == 1:
            if(userInput[0] not in vars):
                print("***Unknown variable introduced")   
            elif(userInput[0] in vars):
                print(values[vars.index(userInput[0])])   
        elif (len(userInput) < 4):
            print("***Parameters missing")
            Input(vars, values, varType)                           
        elif (userInput[2] == "="):                                   #checking if we really are setting a value
            if(userInput[0] == "str") or (userInput[0] == "int"):   #checking if var type was provided
                if (userInput[0] == "int"):
                    try:
                        x = int(userInput[3])
                        vars.append(userInput[1])                       
                        varType.append(userInput[0])
                        values.append(userInput[3])
                    except ValueError:
                        print("VarType Error:", userInput[3], "is not a value that can be used with variable type - int")
                if (userInput[1] not in vars):                 #checking if we haven't received this var yet 
                    vars.append(userInput[1])                       #adding to system
                    varType.append(userInput[0])
                    values.append(userInput[3])
                    holder = len(vars)
            else:
                print("Unknown variable type for Sunex")
        else:
            print("Sunex doesn't recognise this")
    Input(vars, values, varType)


def editValue(vars, values, holder):
    pass

def addValues(vars, values, holder):
    pass
def printValue(vars, values, holder):
    pass

def settingValue(vars, values):
    pass


Input(vars, values, varType)

