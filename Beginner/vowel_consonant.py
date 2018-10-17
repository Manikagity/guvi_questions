ch=input()
if(len(ch)==1):
        if((ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122)):
                if(ch in 'aeiou'):
                        print("vowel")
                else:
                        print("consonant")
        else:
                print("invalid")
else:
        print("invalid")
