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
    print("elso feladat a: ", ':'.join(input[index].split(" ")))

    kulonbsegek = []
    for i in range (len(fokok)-1):
        kulonbsegek.append(abs(fokok[i]-fokok[i+1]))
    print("elso feladat b: ",min(kulonbsegek))


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
        
player = 1
players = ["alfa","beta","gamma"]
playerDobasok = [[],[],[]]
korok = 1
Teljeskorok = 0
legnagyobbPoker = 0
parok = 0
winner = ''
gammaFullKor = 0

def masodik(dobasok,dontesek):   
    i = 0
    lehetoDobasok = 5
    currDobasok = []
    global player
    global players
    global playerDobasok
    global Teljeskorok
    global korok
    global legnagyobbPoker
    global parok
    global winner
    while(i<len(dobasok)):
        valasztott = 0
        lehetosegek = []
        valasztasok = []
        for j in range(lehetoDobasok):
            lehetosegek.append(dobasok[i+j])
            valasztasok.append(dontesek[i+j])
            if(dontesek[i+j] == '1'):
                valasztott += 1
                currDobasok.append(dobasok[i+j])
        i+=lehetoDobasok
        lehetoDobasok-=valasztott
        if(lehetoDobasok == 0):
            dobasRendez(currDobasok)
            if(len(playerDobasok[player-1])==7):
                winner = players[player-1]
                break
            currDobasok = []
            lehetoDobasok = 5
            korok += 1
            if(player != 3):
                player += 1
            else:
                Teljeskorok += 1
                player = 1
            
            
    print(f'masodik feladat a: {Teljeskorok}')
    print(f'masodik feladat b: {winner}')
    print(f'masodik feladat c: {gammaFullKor}')
    print(f'masodik feladat d: {legnagyobbPoker}')
    print(f'masodik feladat e: {parok}')

# -1 = semmi
#  1 = 1 pár pl:11234
#  2 = 2 pár pl:11223
#  3 = terc pl:11123
#  4 = full pl:11122 NEM SZÁMOLHATÓ TERC KÉNT
#  5 = póker pl:11112 NEM SZÁMOLHATÓ 2 PÁR KÉNT
#  6 = kissor pl:12345
#  7 = nagysor pl:23456

def mitDobott(dobas):
    dobottak = [0,0,0,0,0,0]
    global legnagyobbPoker
    global parok
    global player 
    global gammaFullKor
    global korok
    for szam in dobas:
        dobottak[int(szam)-1] += 1
    
    rendezettDobottak = dobottak.copy()
    rendezettDobottak.sort()

    if(rendezettDobottak == [0,0,0,0,1,4]):
        poker = maxIndex(dobottak)+1
        if(poker > legnagyobbPoker):
            legnagyobbPoker = poker
        return 5 
    elif(rendezettDobottak == [0,0,0,0,2,3]):
        if(player == 3 and gammaFullKor == 0):
            gammaFullKor = korok
        return 4 
    elif(rendezettDobottak == [0,0,0,1,1,3]):
        return 3 
    elif(rendezettDobottak == [0,0,0,1,2,2]):
        parok += 1
        return 2 
    elif(rendezettDobottak == [0,0,1,1,1,2]):
        parok += 1
        return 1
    elif(dobottak == [1,1,1,1,1,0]):
        return 6
    elif(dobottak == [0,1,1,1,1,1]):
        return 7
    else:
        return -1

def dobasRendez(dobas):
    global playerDobasok
    global player
    ertek = mitDobott(dobas)
    if(ertek > 0):
        if(ertek not in playerDobasok[player-1]):
            playerDobasok[player-1].append(ertek)

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
    betuk = []
    szoveg = []
    for i in range(len(input)):
        if(input[i] in 'AEIOU'):
            betuk.append(input[i])
            if(len(betuk)==2):
                getBetu(betuk)
                szoveg.append(getBetu(betuk))
                betuk = []
    print("harmadik feladat b:", ''.join(szoveg))

codeMatrix = [
    ["AA", "AE", "AI", "AO", "AU"],
    ["EA", "EE", "EI", "EO", "EU"],
    ["IA", "IE", "II", "IO", "IU"],
    ["OA", "OE", "OI", "OO", "OU"],
    ["UA", "UE", "UI", "UO", "UU"]
]

def getCode(betu):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == betu):
                return codeMatrix[i][j]

def harmadik_C(input,szavak):
    valasz = ""
    szavak = szavak.replace("\n"," ").split(" ")
    szavakmgh = szavak.copy()
    for i in range(len(szavakmgh)):
        mghk = ""
        for j in range(len(szavakmgh[i])):
            if(szavakmgh[i][j] in 'AEIOU'): 
                mghk += szavakmgh[i][j]
        szavakmgh[i] = mghk
    # print(szavakmgh)
    codes = []
    for i in range(len(input)):
        codes.append(getCode(input[i]))
    # print(codes)
    for i in range(len(codes)):
        for j in range(len(szavakmgh)):
            if(codes[i] == szavakmgh[j]):
                valasz += szavak[j]+" "
                break
    print("harmadik feladat c:",valasz)   



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

    masodik(dobasok,dontesek)

    harmadik_A(szoveg)
    harmadik_B(szoveg2)    
    harmadik_C(szoveg3,szavak)
    
main()