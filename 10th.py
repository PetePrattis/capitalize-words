#!/usr/bin/python
# -*- coding: utf8 -*-


'''
Εργασία απο τον Νίκο Κοντόπουλο Π15056
Άσκηση 10
Γράψτε μία συνάρτηση η οποία παίρνει σαν όρισματα έναν τίτλο και κάποιες
λέξεις οδηγούς. Σκοπός σας είναι χωρίς τη χρήση εξωτερικών βιβλιοθηκών
να επιστρέψετε τον τίτλο σε "title case", όπου τα πρώτα γράμματα των
λέξεων οδηγων δεν γίνονται κεφαλαία, εκτός αν είναι στην πρώτη θέση.
'''




def cap():
    title =raw_input("Give the title you want to capitalize ")
    print title
    #print len(title)

    keyw = raw_input("Give the key words you want to capitalize seperating them with space ")
    print keyw
    #print len(keyw)
        
    #Εδώ μετατρέπω την πρόταση και τις λέξεις κλειδιά σε array με τις λέξεις
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
    #Εδώ μετατρέπω το array με τις capitalized λέξεις σε πρόταση
    print ' '.join(stitle)
  
                    
#Εδώ καλώ την συνάρτηση
cap();

print "Press enter to exit"
raw_input()        






                 



