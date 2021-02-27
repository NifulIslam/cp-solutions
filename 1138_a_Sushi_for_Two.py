
class Sushi:
    def __init__(self, sushi_list, length):
        self.sushi_list= sushi_list
        self.length= length
    def max_part(self):
        max_cont=0
        leng_func=0
        first_cont,leng_func=self.contiguous(leng_func)
        secont_cont=0
        while(leng_func< length):
            secont_cont, leng_func=self.contiguous(leng_func)
            
            if(max_cont< 2*(min(first_cont, secont_cont))):
                max_cont= 2*(min(first_cont, secont_cont))
            first_cont=secont_cont
            
        return max_cont
        
    def contiguous(self,index):
        serial=0
        indexes=index
        try:
            for i in range(index,self.length):
                if(self.sushi_list[i]!=self.sushi_list[i+1]):
                    return serial+1, indexes+1
                    
                    break
                serial+=1
                indexes+=1
        except IndexError:
            return serial+1, indexes+1
            
            

length=int(input())                
sushi_l= list(map(int , input().split()))
s= Sushi  (sushi_l, length)
print(s.max_part())
                
