class Playr:
  
   def __init__(self,o,h,c) :
       self.o = o
       self.h = h
       self.c=c
       print("bvn",o,"/poo",h,"/c",4)

   def get_poli(self):
       return self.o  
   def setwa(self,a):
        self.h +=a
        print("---",str(self.h))