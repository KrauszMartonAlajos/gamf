import os
import math

def elso_A(input):
    fokok = []
    input = input.split("\n")
    for i in input:
        i = i.split(" ")
        tempfok = 0
        if(int(i[0]) < 12):
            tempfok = fokCalc(int(i[0]),int(i[1]))
        else:
            tempfok = fokCalc(int(i[0])-12,int(i[1]))
        fokok.append(tempfok)
    index = maxIndex(fokok)
    mindex = minIndex(fokok)
    print("elso feladat a: ", ':'.join(input[index].split(" ")) ,"\nelso feladat b: ",min(fokok))

    #print("elso feladat a: ", input[0])


def maxIndex(lista):
    max = lista[0]
    maxIndex = 0
    for i in range(len(lista)):
        if lista[i]>max:
            max = lista[i]
            maxIndex = i
    return maxIndex

def minIndex(lista):
    min = lista[0]
    minIndex = 0
    for i in range(len(lista)):
        if lista[i]<min:
            min = lista[i]
            minIndex = i
    return minIndex

def fokCalc(ora,perc):
    percfok = perc * 6
    orafok = ora * 30 + perc*0.5
    fok = abs(orafok - percfok)
    return min(fok,360-fok)

def elso_C(input):
    input = input.split(" ")
    nap = -1
    Ora = 0
    Perc = 0
    index = 0
    while(index<len(input)):
        nap+=1
        for ora in range(24):
            for perc in range(60):
                if(index<len(input)):
                    szog = fokCalc(ora,perc)
                    if(float(input[index]) == szog):
                        index+=1
                        Ora = ora
                        Perc = perc

    print(f'első feladat c: {nap}|{Ora}:{Perc}')
        

def masodik_A(idopontok,dontesek):   
    
    print("masodik feladat a: ", idopontok[0])

def masodik_B(idopontok,dontesek):
    print("masodik feladat b: ", idopontok[0])

def masodik_C(idopontok,dontesek):
    print("masodik feladat c: ", idopontok[0])

def harmadik_A(input):
    lista = szavakforditasa(input)
    elsoQi = 0
    utolsoQi = 0
    for i in range(len(lista)):
        if('Q' in lista[i]):
            elsoQi = i
            break
    for i in range(len(lista)-1,0,-1):
        if('Q' in lista[i]):
            utolsoQi = i
            break

    print("harmadik feladat a:", utolsoQi-elsoQi-1)

def szavakforditasa(input):
    input = input.replace("\n"," ").split(" ")
    szavak = []
    csere = False
    for i in range(len(input)):
        szo = []
        for j in range(0,len(input[i]),2):
            temp = [input[i][j],input[i][j+1]]    
            if(csere):
                csere = not csere
                temp.reverse()
                szo.append(getBetu(temp))
            else:
                csere = not csere
                szo.append(getBetu(temp))
        szavak.append(''.join(szo))
    return szavak

matrix = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "X", "Y", "Z"]
]

def getNum(betu):
    if(betu == "A"):
        return 0
    elif(betu == "E"):
        return 1
    elif(betu == "I"):
        return 2
    elif(betu == "O"):
        return 3
    elif(betu == "U"):
        return 4    

def getBetu(betupar):
    return matrix[getNum(betupar[0])][getNum(betupar[1])]

def harmadik_B(input):
    print("harmadik feladat b: ", input[0])
 
def harmadik_C(input):
    print("harmadik feladat c: ", input[0])   



def faljbeolvasas(filename):
    f = open(filename,"r")
    return f.read()

def main():
    idopontok = faljbeolvasas("idopontok.txt")
    dontesek = faljbeolvasas("dontesek.txt")
    dobasok = faljbeolvasas("dobasok.txt")
    szavak = faljbeolvasas("szavak.txt")
    szogek = faljbeolvasas("szogek.txt")
    szoveg = faljbeolvasas("szoveg.txt")
    szoveg2= faljbeolvasas("szoveg2.txt")
    szoveg3= faljbeolvasas("szoveg3.txt")
    elso_A(idopontok)
    elso_C(szogek)

    masodik_A(idopontok,dontesek)
    masodik_B(idopontok,dontesek)    
    masodik_C(idopontok,dontesek)

    harmadik_A(szoveg)
    harmadik_B(szoveg)    
    harmadik_C(szoveg)
    
main()