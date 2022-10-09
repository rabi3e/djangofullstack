

class Game:
    def __init__(self):
        while True :
            choice = int(input('''Welcome, Choose a Game :  
                    1 ---->  Odd and Even Numbers 
                    2 ---->  No duplicate
                    3 ---->  from 0 
                    4 ---->  divide
                    5 ---->  divide 0 to 100 
                    ----->>  :  ''') )
            if choice == 1 :
                lt = input("plz enter your LIST : ")
                self.odd_even(lt)
            elif choice == 2 :
                sent = input(" plz Enter your Sentence : ")
                self.noum_words(sent)
            elif choice == 3 :
                x= int(input(" Enter a Number : "))
                self.num_from(x)
            elif choice == 4 :
                x=int(input("First Number :  "))
                y= int(input("2nd Number :  "))
                self.divide(x,y)
            elif choice == 5 :
                x=int(input("First Number :  "))
                y= int(input("2nd Number :  "))
                self.divide_100(x,y)
            else :
                print ( "plz choose a correct Number")
                
            ext= input(" exit  y/n  :  ")   
            if ext == "y" :
                print("bye bye")    
                break
                                        
    def num_from(self,x):
        lis = []
        for i in range(0,x+1) :
            lis.append(i)
            print ( i )    
        print ( lis)
        
    def divide(self,x,y):
        lst=[]
        for i in range(0,y+1) :
            print(i)
            if i%x==0 :
                lst.append(i)
        print(lst)
                    
    def divide_100(self,x,y):
        lst=[]
        for i in range(0,101):
            if i%x==0 and i%y==0 :
                lst.append(i)
        print(lst)         
            
    def odd_even(self,lt) :
        lpai=[]
        limpai=[]
        for i in lt.split( " ") :
            if int(i)%2 == 0 :
                lpai.append(int(i))
            else :
                limpai.append(int(i))
        print(f"list of odd numbers : {limpai}")
        print(f"list of even numbers : {lpai}")
            
    def noum_words(self, sent):
        words = []
        for i in sent.split(" ") :
            if i not in words :
                words.append(i)
        print(' '.join(words))
        
    
g1 = Game()

        
