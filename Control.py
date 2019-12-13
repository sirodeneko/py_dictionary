import DB

class Handle:
    
    keyword=''
    phonetic=[]
    result=[]

    def __init__(self):
        
        self.db_obj=DB.Sqlopen()       #链接数据库

    def GetWordLocalInfo(self,words):
        # 单词
        self.keyword=''
        # 英标
        self.phonetic=[]
        # 解释
        self.result=[]
        
        
        word_list=self.db_obj.GetWord(words)            #数据库查询
        
        if(word_list==[]):
            return -1
        # 返回为列表，只有一个元素，故word_list[0]取出至word_result
        word_result=word_list[0]
        
        self.keyword=word_result[1]
        for index in range(2):
            if(word_result[2+index]!=None):
                self.phonetic.append(word_result[2+index])
            else:
                break
                
        for index in range(5):
            if(word_result[4+index]!=None):
                self.result.append(word_result[4+index])
            else:
                break
                
        return 0
        
    def SaveLocalInfo(self):
        self.db_obj.UpWord(self.keyword,self.phonetic,self.result)
                    
    def Result_Formate(self):
        if(self.result==[]):        
            return '查询无结果'
        f_string="%s\n" %(self.keyword)
        f_string=f_string+("英:%s\t美:%s" %(self.phonetic[0],self.phonetic[1]))

        if(len(self.result)):
            f_string=f_string+"\n解释:\n"
            for index in range(len(self.result)):
                f_string=f_string+("\t%d: %s\n" %(index+1,self.result[index]))
        return f_string
    
    def DeleteWord(self):
        self.db_obj.DelWord(self.keyword)
        
