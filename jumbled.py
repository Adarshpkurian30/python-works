# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:48:02 2024

@author: adars
"""
import random
def choose():
    words=['rainbow','computer','science','programming','mathematics']
    choice1=random.choice(words)
    return choice1
def jumbled(word):
    word1="".join(random.sample(word,len(word)))
    return word1
def thank(playername1,playername2,pp1,pp2):
    print('thanks for playing,',playername1,'&',playername2)

def play():
    pp1=0
    pp2=0
    playername1=input('enter name of first player')
    playername2=input('enter the neme of 2nd player')
    turn=0
    int c
    while(c==1):
        picked_word=choose()
        qn=jumbled(picked_word)
        print(qn)
        if(turn%2==0):
            print(playername1,'this is your turn ')
            ans=input('what is on your mind')
            if(ans==picked_word):
                pp1=pp1+1
                print('your ans is right! your score becomes ',pp1)
            else:
                print('your ans is wrong!! better luck next time...the correct ans is',picked_word)
            c = int(input('Press 1 to continue and 0 to quit: ')) 
            if(c==0):
                thank(playername1,playername2,pp1,pp2)
                break
            else:
                  picked_word=choose()
                  qn=jumbled(picked_word)
                  print(qn)   
                  print(playername2,'this is your turn ')
                  ans=input('what is on your mind')
                  if(ans==picked_word):
                     pp2=pp2+1
                     print('your ans is right! your score becomes ',pp1)
                  else:
                     print('your ans is wrong!! better luck next time...the correct ans is',picked_word)
                  c =int(input('press 1 to continue and 0 to quit'))
                  if(c==0):
                     thank(playername1,playername2,pp1,pp2)
                     break
        turn=turn+1
play()
         
         