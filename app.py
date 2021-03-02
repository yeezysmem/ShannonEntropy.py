import numpy as np
from math import log2
import collections
import math
import io
from collections import Counter
import pickle
import os
 
FILENAME = "inputUA100.txt"

def fileEntropy():
    with  io.open(FILENAME,encoding='utf-8') as f:
        a = np.array(list(f.read())) #заносим данные в с файла в массив
        _, cnt = np.unique(a, return_counts=True) #_ это все символы в файле сtn это статистика появления символа
        p = cnt/np.sum(cnt) #вероятность появления символа 
        P = -1*(p * np.log2(p)) #ентропия посимвольно
        H = -np.sum(p * np.log2(p)) #общая ентропия

        print("Entropy is: '{0}'".format(H))
        print("Entropy of each symbol: '{0}'".format(P))
        print("Probability of each symbol: '{0}',probability: {2} => {1}".format(p,cnt,_)) 
 
def countChar():
    with open(FILENAME) as infile:
        lines=0
        words=0
        characters=0
        for line in infile:
            wordslist=line.split()
            lines=lines+1
            words=words+len(wordslist)
            characters += sum(len(word) for word in wordslist)
    print("Lines: '{0}'".format(lines))
    print("Words: '{0}'".format(words))
    print("Characters: '{0}'".format(characters))

def main():
    fileSize = os.path.getsize(FILENAME)
    print( "File size in bytes: {0}".format(fileSize) ) 
    print( "What do you want to do: 1 - change txt file, 2 - Entropy, 3 - find out information about a file" )
    type1 = int(input())
    if type1 == 1:
        st = open(FILENAME, "w")  
        a = input("Enter text: ")  
        st.write(a)  
        print("your text is saved in a file '{0}'".format(FILENAME))
        st.close()  
    if type1 == 2:
        print( "Entropy your file is:" )
        print(fileEntropy())  
    if type1 == 3:
        countChar()
    # if type1 == 4:
    #     print(char_frequency("zhdanov daniil alexeyevich")) 
main()
