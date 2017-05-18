#!/usr/bin/env python
import time
import string
code=[]
dcode=[]
keys=[]

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan



print ' '+G+'           Now you going to Encrypt your text\n '+B+''
time.sleep(1)
print '            This '+W+'ENCRYPTION'+B+' Algorithm is written by'+W+' Manohar singh rajawat\n'
time.sleep(1)

print ' '+W+' 1. Encryption or '+R+' (encipher) \n '+G+' 2. Decrpytion or '+O+' (decipher) '+B+'\n  3. Brute force attack for key  \n'+P+'  4. Attack from word list('+T+' Real Brute Force Attack )\n '+C+''
choice=input("\n  Enter the option 1 or 2 or 3 and 4(easy hacking by manohar)\n  ")
print '\n'

def numbershuffle(z):
   if (z>=0 and z<=26):
     num=z
   else :
     rem=z%26
     num=rem
   return num

def Encryption(c):
   man=ord('%s' % c)
   if (man>=97 and man<=122):
     a=man+num
     if (a>122):
       a=a-122;
       a=96+a;
     char=chr(a)
   else :
     char=c

   check=ord('%s' % char)
   if (check<97 or check>122):
     char=c
   if (char=='#'):
          char=' '
   code.append(char)

def Decryption(d):
   dman=ord('%s' % d)
   if (dman>=97 and dman<=122):
     e=dman-num
     if (e<97):
       e=97-e
       e=123-e
     dchar=chr(e)
   else :
     dchar=d
   
   dcheck=ord('%s' % dchar)
   
   if (dcheck<97 or dcheck>122):
     dchar=d
   if (dchar==' '):
     dchar=' ';
   dcode.append(dchar)




def BruteFor(c,h):
   man=ord('%s' % c)
   num=h
   if (man>=97 and man<=122):
     a=man+num
     if (a>122):
       a=a-122;
       a=96+a;
     char=chr(a)
   else :
     char=c

   check=ord('%s' % char)
   if (check<97 or check>122):
     char=c
   if (char=='#'):
          char=' '
   code.append(char)







def BruteForce(x):
  sofp=len(x) 
  for knum in range(0,26):
    for second in range(0,sofp):
       BruteFor(x[second],knum)
       
    m_string=''.join(code)    
    
    del(code[:])
    
    print m_string
    if (m_string==cipher_text):
      print '\n\n\n'
      print ''+W+' ----------------------------------------------------------------------------- '+P+''
      print ''+P+' ----------------------------------------------------------------------------- '+G+''
      print '  The Brute Force was successfull and now we have the key :) '+W+''
      time.sleep(1)
      print ''+B''
      print "  The key is : %d" % knum
      keys.append(knum)
      time.sleep(1)
      return 1
      
      


def RealBruteForce():
   file=open("/root/Desktop/words.txt","r")
   data=file.readlines()
   file.close()
   length=len(data)
   for mankit in range(0,length):
     data[mankit]=data[mankit].replace('\n','')
   
   
   for kitman in range(0,length):
     simple_text=data[kitman]
     g=BruteForce(simple_text)
     if (g==1):
       print ' '+B+' One KEY has been '+W+'Found'
       time.sleep(2)

   print '\n\n\n'
   print ' '+B+'Now The computer will write The '+W+'Key'+B+' on Monitor\n '+W+''   
   for maapapa in keys:
      print maapapa

if (choice==1):
  print ' '+G+'                           Now Enter the message that you want to encrypt\n\n '+W+''
  time.sleep(1.5);
  string=raw_input("Type the message that you want to Encrypt\n\n");
  size=len(string)
  num=input("\nEnter the number for shuffle the code\n\n");
 
  num=numbershuffle(num)
  
  strint_w=string.replace(' ','')

  for man in range(0,size):
    Encryption(string[man])

  encoded=''.join(code)
  print ' '+R+'                                     The Encrypted code is \n '+B+''
  time.sleep(1)
  print "                                      %s" % encoded


elif (choice==2):
  print ' '+P+'                           Now Enter the message that you want to Decrypt\n '+W+''
  time.sleep(1.5);
  string=raw_input("Type the message that you want to Decrypt\n\n");
  size=len(string)
  num=input("\nEnter the number for shuffle the code\n\n");

  num=numbershuffle(num)  

  strint_w=string.replace(' ','') 

  for man1 in range(0,size):
    Decryption(string[man1])

  decoded=''.join(dcode)
  print ' '+R+'                                     The Decrypted code is \n '+B+''
  time.sleep(1)
  print "                                      %s" % decoded




elif (choice==3):
    time.sleep(1)
    print ' '+R+'                             Now you have to enter only one pair it will automatically detect the key '+B+' \n'
    time.sleep(.1)
    plain_text=raw_input("Enter the plain text \n")
    
    cipher_text=raw_input("Enter the cipher text \n")
    
    BruteForce(plain_text) 

elif (choice==4):
   print ' '+G+'                              This special software is written by manohar singh rajawat and this will use a brute force list '
   print '\n'
   print ''+R+'Now It will use the text file ====> '+W+' /root/Desktop/words.txt '
   time.sleep(1)
   cipher_text=raw_input("\n\nEnter the snoofed(cipher text)\n\n")
   RealBruteForce()
    
else:
  print ' '+W+'you are going wrong plese choose between 1 and 4 '


