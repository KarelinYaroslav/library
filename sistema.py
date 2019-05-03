class sistema:
    b=''
    k=0
    def inversia(self,x):
        for i in x:
            if i=='1':
                self.b+='0'
            else:
                self.b+='1'
        return self.b
    def si10(self,x,y):
        self.k=int(x,y)
        return self.k
    
    
        

            
