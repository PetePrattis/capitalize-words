#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
A program which accepts as an input a sentence and some key words 
and then returns the sentence with the key words capitalized.
'''

#goal is not to use any imported libraries


def cap():
    title =raw_input("Give the title you want to capitalize ")
    print title
    #print len(title)

    keyw = raw_input("Give the key words you want to capitalize seperating them with space ")
    print keyw
    #print len(keyw)
        
    #make the sentence and the key words into two arrays of words
    stitle = title.split()
    skeyw = keyw.split()
    

    #print len(title.split())
    x =len(title.split())
    #print len(keyw.split())
    y =len(keyw.split())

    
    for i in range(0,x):
        for j in range(0,y):
            if stitle[i]==skeyw[j]:
                stitle[i]=stitle[i].title()

    print "This is the capitalized sentence"
    #convert array with capitalized letters into a string
    print ' '.join(stitle)
  
#main                    
#call the function
cap();

print "Press enter to exit"
raw_input()        

