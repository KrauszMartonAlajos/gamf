import os
import math

def elso_A(input):
    # for i in range(len(input)):
    #     print(input[i])
    #print(input)
    hosszak = []
    betuk = []
    mostani1 = input[0]
    mostani2 = ""
    hossz=0
    for i in range(len(input)):
        karakter = input[i]
        #print(karakter)
        hossz+=1
        if mostani1 == "":
            mostani1 = karakter
        elif mostani2 == "" and mostani1 != karakter:
            mostani2 = karakter
        elif mostani1 != karakter and mostani2 != karakter and mostani2 != "":
            hosszak.append(hossz)
            lista = [mostani1,mostani2]
            lista.sort()
            betuk.append(lista)
            #print(lista[0]+lista[1]+str(hossz))
            mostani1 = ""
            mostani2 = ""
            hossz = 0
    index= maxIndex(hosszak)
    print("első feladat a: ",betuk[index][0]+betuk[index][1]+str(hosszak[index]))

def maxIndex(lista):
    max = lista[0]
    maxIndex = 0
    for i in range(len(lista)):
        if lista[i]>max:
            max = lista[i]
            maxIndex = i
    return maxIndex


#aabaabbaaabb ccc         l1[0] ba l1[1] cc
#                       l2[0] 10 l2[1] 3

#i i+1 --+-->  i+1 i+2
#2+6             2+4

def elso_B(input):
    abcCounter = 0
    for i in range(len(input)):
        karakter = input[i]
        if karakter == "a":
            for j in range(i,len(input)):
                if input[j] == "b":
                    for k in range(j,len(input)):
                        if input[k] == "c":
                            abcCounter+=1
    print("elso feladat b: " ,abcCounter)
                            

def elso_C(input):
    x = 0
    y = 0
    for i in range(len(input)):
        if input[i] == "a":
            y += 1
        elif input[i] == "b":
            x += 1
        elif input[i] == "c":
            y -= 1
        elif input[i] == "d":
            x -= 1
    #print(x,y)
    distance = math.sqrt(x**2 + y**2)
    print("elso feladat c: " , round(distance))

def masodik_A(input):
    formazott = input.replace("\n"," ").replace("\t"," ").split(" ")
    popolandok = []
    joszavak = []
    for i in range(len(formazott)):
        if formazott[i] == "":
            popolandok.append(i-len(popolandok))
    for i in range(len(popolandok)):
        formazott.pop(popolandok[i])      

    for i in range(len(formazott)):
        if len(formazott[i]) == len(set(formazott[i])):
            joszavak.append(formazott[i])

    maxlengthszo = joszavak[0]
    for i in range(len(joszavak)):       
        if len(joszavak[i]) > len(maxlengthszo):
            maxlengthszo = joszavak[i]

    print("masodik feladat a: " ,maxlengthszo)

def masodik_B(input):
    formazott = input.replace("\n"," ").replace("\t"," ").split(" ")
    popolandok = []
    for i in range(len(formazott)):
        if formazott[i] == "":
            popolandok.append(i-len(popolandok))
    for i in range(len(popolandok)):
        formazott.pop(popolandok[i])      

    legnagyobb = 0
    hossz = 0
    for i in range(len(formazott)):

        if formazott[i] =="AZ" or formazott[i] =="A" and hossz >0:
            if legnagyobb<hossz:
                legnagyobb = hossz
            hossz = 0
        if hossz>0:
            #print(formazott[i])
            #print(len(formazott[i])+1)
            hossz += len(formazott[i])+1
        if formazott[i] =="AZ" or formazott[i] =="A" and hossz == 0:
            hossz+=1
    print("masodik feladat b: " ,legnagyobb)

def masodik_C(input):
    formazott = input.replace("\n"," ").replace("\t"," ").split(" ")
    popolandok = []
    joszavak = []
    for i in range(len(formazott)):
        if formazott[i] == "":
            popolandok.append(i-len(popolandok))
    for i in range(len(popolandok)):
        formazott.pop(popolandok[i])    

    for i in range(len(formazott)):
        if len(formazott[i]) >= 2:
            if formazott[i] == formazott[i][::-1]:
                joszavak.append(formazott[i])

    print("masodik feladat c: ",len(joszavak))


def faljbeolvasas(filename):
    f = open(filename,"r")
    return f.read()


def main():
    elsoInput = faljbeolvasas("karsor.txt")
    masodikInput = faljbeolvasas("szoveg.txt")
    harmadikInput = faljbeolvasas("terkep.txt")
    elso_A(elsoInput)
    elso_B(elsoInput)
    elso_C(elsoInput)

    masodik_A(masodikInput)
    masodik_B(masodikInput)    
    masodik_C(masodikInput)
main()