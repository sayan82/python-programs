class Multiplicationtable:
    def mul(self,n):
        self.i=1
        while(self.i<=10):
            print(n,"x",self.i,"=",self.i*n)
            self.i+=1
s=Multiplicationtable()
n=int(input("Enter a number to print its multiplication table:\n"))
s.mul(n)