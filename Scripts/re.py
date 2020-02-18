#!/usr/bin/python


def balanceoPar(listaCar):
    parentesisI = [] #Inicial
    parentesisF = [] #Final
    for i in range(0,len(listaCar)):
        l = listaCar[i]
        if l == "(":
            parentesisI = parentesisI + ["("]
        else:
            if l == ")":
                parentesisF = parentesisF  + [")"]
            else:
                return(parentesisI, parentesisF)
    if len(parentesisI)==len(parentesisF):
        return True
    else:
        return False



# print(balanceoPar("()("))

def generadorTel(name):
    num = []
    for i in range(len(name)):
        caracter = name[i]
        if caracter == "a" or caracter == "b" or caracter == "c": 
            num.append(2)
        elif caracter == "d" or caracter == "e" or caracter == "f": 
            num.append(3)
        elif caracter == "g" or caracter == "h" or caracter == "i": 
            num.append(4)
        elif caracter == "j" or caracter == "k" or caracter == "l": 
            num.append(5)
        elif caracter == "m" or caracter == "n" or caracter == "o": 
            num.append(6)
        elif caracter == "p" or caracter == "q" or caracter == "r" or caracter == "s": 
            num.append(7)
        elif caracter == "t" or caracter == "u" or caracter == "v": 
            num.append(8)
        elif caracter == "w" or caracter == "x" or caracter == "y" or caracter == "z": 
            num.append(9)
    return num 
    
# print(generadorTel("adrian"))


def functionRepe(arreglo, numero, cantidad):
    veces = 0
    for i in range(len(arreglo)):
        a = arreglo[i]
        if a == numero:
            veces = veces + 1
    
    if veces >= cantidad:
        print("True")
    else: 
        print("False")

arr = [1,2,2,4,5,5,5,6,7,7,8,8]
# functionRepe(arr, 2, 2)

def mayorDiferencia(arreglo): 
    maxNum = max(arreglo)
    minNum = min(arreglo)
    result = maxNum - minNum
    print(result)

# mayorDiferencia([ 28, 16, 28, 11, 14, 26, 23, 25, 17, 3, 22, 23, 23, 10 ])

# myarr = [ 28, 16, 28, 11, 14, 26, 23, 25, 17, 3, 22, 23, 23, 10 ]
# orderArr = sorted(myarr)
# print(orderArr)

def mismaDiferencia(arreglo): 
    oa = sorted(arreglo)
    num1 = oa[0]
    num2 = oa[1]
    dife = num2 - num1
    ini = 0
    fin = 2
    newArr = []
    for i in range(len(oa) - 1):
        newValue = oa[ini:fin]
        newArr.append(newValue[1] - newValue[0])
        ini = ini + 1
        fin = fin + 1
    for i in range(len(newArr)):
        if(newArr[i] == dife):
            result = "True"
        else: 
            result = "False"
    return result
print(mismaDiferencia([ 44, 37, 30, 23]))



routes = [                                            
  ["pbc", "sfo", "plane", 8],
  ["pbc", "mex", "bus", 2],
  ["pbc", "mex", "plane", 5],
  ["pbc", "mty", "plane", 2],
  ["pbc", "mty", "bus", 12],
  ["pbc", "tij", "bus", 33],
  ["pbc", "tij", "plane", 7],
  ["mex", "mty", "plane", 2],
  ["mex", "mty", "bus", 12],
  ["tij", "sfo", "bus", 13],
  ["tij", "sfo", "plane", 10],
  ["mex", "sfo", "plane", 4],
  ["mty", "sfo", "bus", 43],
  ["mty", "sfo", "plane", 5]
];

def plansFromATob(a, b):
    trips = []
    result = []
    for route in routes: 
        if(route[0] == a and route[1] == b): 
            result.append([route]) 
        elif (route[0] == a):
            for trip in routes:
                if trip[0] == route[1] and trip[1] == b:
                    result.append([route, trip])
                for trip2 in routes:
                    if route[1] == trip[0] and trip[1] == trip2[0] and trip2[1] == b:
                        result.append([route, trip, trip2])
                    
            
                    
    for path in result:
        print(path)
    
# plansFromATob("pbc", "sfo")



# 
# Your previous JavaScript content is preserved below:
# 
# var routes = [                                            
#   ["pbc", "sfo", "plane", 8],
#   ["pbc", "mex", "bus", 2],
#   ["pbc", "mex", "plane", 5],
#   ["pbc", "mty", "plane", 2],
#   ["pbc", "mty", "bus", 12],
#   ["pbc", "tij", "bus", 33],
#   ["pbc", "tij", "plane", 7],
#   ["mex", "mty", "plane", 2],
#   ["mex", "mty", "bus", 12],
#   ["tij", "sfo", "bus", 13],
#   ["tij", "sfo", "plane", 10],
#   ["mex", "sfo", "plane", 4],
#   ["mty", "sfo", "bus", 43],
#   ["mty", "sfo", "plane", 5]
# ];
# 
# // Find out many ways to go from one place to another
# 
# function plansFromATob(a, b) {
#   if (routes) {
#     
#   }
#   
# };
# 
# plansFromATob("pbc", "sfo");
# 
# //
# // [{ 
# //   route:   [ ["pbc -> mex -> bus"], [ "mex -> sfo -> plane" ] ],
# //   duration: 6 
# // }]
# //
# 

