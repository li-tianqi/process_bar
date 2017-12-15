#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:40:16 2017

@author: victor
"""
import sys

class processBar(object):
    """
    process bar
    """
    
    def __init__(self, bar_len = 40):
        """
        bar_len: length of the bar
        default value is 40 characters
        """
        
        self.bar_len = bar_len
        self.l = 0
        self.L = 1
        self.P = 0
        
    def bar(self, l=None, L=None, P=None, 
            bar_p1=None, bar_p3=None, 
            out=None, R=None):
        """
        bar(): bulid the process bar
        l: current process
        L: total process
        P: current process percentage (0-100)
        bar_p1: first part of the bar
        bar_p3: third part of the bar
        out: the printed content during the process bar
        R: specify the end time of the bar and write a '\n'
        """
        
        if P:
            self.P = P
            self.l = P
            self.L = 100
            bar_p1_def = ''
        elif l and L:
            self.l = l
            self.L = L
            self.P = l*100/L
            bar_p1_def = "%d/%d " % (self.l, self.L)
        else:
            raise ValueError('\033[1;31mMissing parameters!!!\033[0m')
        
        bar_p3_def = " %d%%" % self.P
        
        if bar_p1:
            self.bar_p1 = bar_p1
        else:
            self.bar_p1 = bar_p1_def
            
        if bar_p3:
            self.bar_p3 = bar_p3
        else:
            self.bar_p3 = bar_p3_def
        
        m = int(self.P*self.bar_len/100)
        self.bar_p2 = "|%s|" % (m*"\033[47;7m \033[0m" +
                                (self.bar_len-m)*' ')
            
        #flag = False
        
        if out:
            lenght = self.draw()
            #flag = False
            self.clear_bar(lenght)
            for s in out:
                print(s)
            self.draw()
            #flag = True
        else:
            self.draw()
            #flag = True
        self.r = 0
        if R:
            self.r += 1
            if self.l == self.L and self.r == R:
                sys.stdout.write('\n')
        else:
            if self.l == self.L:
                sys.stdout.write('\n')
            

        
        
    def draw(self):
        """
        draw the bar
        return the total length of the bar for clear
        """
        
        str_b = self.bar_p1+self.bar_p2+self.bar_p3
        sys.stdout.write('\r'+ str_b)
        sys.stdout.flush()
        return len(str_b)
        
    def clear_bar(self, lenght):
        """
        clear the bar with space
        """
        
        sys.stdout.write('\r' + " "*lenght + '\r')
        
        
        
if __name__ == "__main__":
    import time
    bar = processBar()
    N = 30
    print("ready to epoch 0")
    for j in range(3):
        time.sleep(0.5)
        for i in range(N):
            time.sleep(0.1)
            l = i+1
            L = N
            P = (i+1)*100/N
            #bar.bar(l, L)
            bar.bar(l, L, R =4, bar_p1="epoch "+str(j))
        
        out = []
        out1 = "epoch " + str(j) + ' done'
        out.append(out1)
        if j+1<3:
            out2 = "ready to epoch " + str(j+1)
            out.append(out2)
        
        #out = [out1, out2]
        bar.bar(P=P, R=4, out=out, bar_p1='epoch' + str(j))
    bar.clear_bar(60)
    bar.bar(P=P, R = 4, bar_p1="all")
    
    