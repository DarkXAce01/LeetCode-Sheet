class Solution:
    


    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def per(first,second):
            ads = []
            for i in range(0,len(first)):
                for j in range(0,len(second)):
                    op = first[i]+second[j]
                    ads.append(op)                 
            return ads
        
        asn2=[]
        if len(digits) == 1:
            asn2 = [i for i in numpad[digits]]
       
        if len(digits)==2:
            asn2 = per(numpad[digits[0]],numpad[digits[1]])
        if len(digits)==3:
            ans = per(numpad[digits[0]],numpad[digits[1]])
            asn2 = per(ans,numpad[digits[2]])
        if len(digits)==4:
            ans = per(numpad[digits[0]],numpad[digits[1]])
            asn3 = per(ans,numpad[digits[2]])
            asn2 = per(asn3, numpad[digits[3]])
            
        fin = asn2
        return fin
        
            
        
        
        
        
    
    
    
        
            