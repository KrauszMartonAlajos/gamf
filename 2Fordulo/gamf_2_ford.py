import os
import math

def elso_A(input):
    print("elso feladat a: ", input[0])

def elso_B(input):
    print("elso feladat b: ", input[0])

def elso_C(input):
    print("elso feladat c: ", input[0]) 

def masodik_A(input):   
    print("masodik feladat a: ", input[0])

def masodik_B(input):
    print("masodik feladat b: ", input[0])

def masodik_C(input):
    print("masodik feladat c: ", input[0])

def harmadik_A(input):
    print("harmadik feladat a: ", input[0])

def harmadik_B(input):
    print("harmadik feladat b: ", input[0])
 
def harmadik_C(input):
    print("harmadik feladat c: ", input[0])   



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

    harmadik_A(harmadikInput)
    harmadik_B(harmadikInput)    
    harmadik_C(harmadikInput)
    
main()