class decimal:     
        
    def decimal_to_base(self,number,base):
            dic={
                10:'A',
                11:'B',
                12:'C',
                13:'D',
                14:'E',
                15:'F',
                16:'G',
                17:"H",
                18:'I',
                19:'J',
                20:'k',
                21:'L',
                22:'M',
                23:'N',
                24:'O',
                25:'P',
                26:'Q',
                27:'R',
                28:'S',
                29:'T',
                30:'U',
                31:'V',
                32:'W',
                33:'X',
                34:'Y',
                35:'Z'
            }
            Result=[]
            while number!=0:
                temp=number%base
                if temp>9:
                    Result.append(dic[temp])
                else:
                    Result.append(temp)
                number=number//base
            Result=Result[::-1]
            ans=""
            for i in Result:
                 ans=ans+str(i)
            return ans
    def str_to_Number(self,number,base):
        dic={
        }
        for i in range(65,65+26):
            dic[chr(i)]=i-55
        for i in range(97,97+26):
              dic[chr(i)]=i-87
        
        result=0
        siz=len(number)-1
        for i in number:
            t=ord(i)
            temp=base**siz
            if ((t>=ord('1')) and (t<=ord('9'))):
                result=result+(temp*(int(i)))
            elif (t>=ord('A') or t>=ord('a')) and (t<=ord('Z') or t<=ord('z')):
                 t2=dic[i]
                 result=result+(temp*t2)
            siz-=1
        return result
      
            
         

          