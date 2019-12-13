import tkinter as tk
import tkinter.messagebox
import Control

top=tk.Tk()
top.title("世界上最完美的英文词典")
#大小

menubar=tk.Menu(top) #创建一个菜单栏
top['menu'] = menubar
queryMenu=tk.Menu(menubar,tearoff=0) #定义一个空的菜单单元
menubar.add_cascade(label='菜单', menu=queryMenu)#装入选项

TopFrame=tk.Frame(top,width=65)                         #用来布局使用

WordEntry=tk.Entry(TopFrame,width=40)                   #创建一个单行文本框
SearchBtn=tk.Button(TopFrame,text="Search",width=15)    #创建一个按钮
modifyFrame=tk.Frame(top,width=65,height=15)   #修改界面布局
addFrame=tk.Frame(top,width=65,height=16)   #添加界面布局
ResultLabel=tk.Label(top,text='Nothing',height=15,width=65,bg='#FFFFDD',justify=tk.LEFT)    #创建一个显示标签

def func1():

    def BtnCallback():                                      #按钮触发回调函数
        words=WordEntry.get()                               #获取文本框中的文本
        sdh=Control.Handle()
        sdh.GetWordLocalInfo(words) 
        out_string=sdh.Result_Formate()
        ResultLabel.configure(text=out_string,anchor=tk.NW)

    SearchBtn.configure(command=BtnCallback)        #设置回调函数
    WordEntry.grid(row=0,column=0)              #布局
    SearchBtn.grid(row=0,column=1)
    TopFrame.grid(row=0,column=0,padx=50)
    ResultLabel.grid(row=1,column=0)
    addFrame.grid_forget()

def func2():

    word=tk.Label(modifyFrame,text="")
    StandardText1=tk.Label(modifyFrame,text="英:")
    StandardEntry1=tk.Entry(modifyFrame,width=40) 
    StandardText2=tk.Label(modifyFrame,text="美:")
    StandardEntry2=tk.Entry(modifyFrame,width=40) 
    ResultText=[]
    ResultEntry=[]
    okk=tk.Button(modifyFrame,text="确定")
    ohno=tk.Button(modifyFrame,text="删除此单词",bg="#C80C0C")
    
    for index in range(5):
        ResultText.append(tk.Label(modifyFrame,text="解释"+str(index+1)))
        ResultEntry.append(tk.Entry(modifyFrame,width=40))
    
    

    def BtnCallback():                                      #按钮触发回调函数
        words=WordEntry.get()                               #获取文本框中的文本
        sdh=Control.Handle()
        sdh.GetWordLocalInfo(words)

        #清空文本框
        StandardEntry1.delete(0,'end')
        StandardEntry2.delete(0,'end')
        for index in range(5):
            ResultEntry[index].delete(0,'end')
        
        if (sdh.result==[]):
            word.configure(text="查询失败")
        else:
            #赋值
            word.configure(text=sdh.keyword)
            StandardEntry1.insert(0,sdh.phonetic[0])
            StandardEntry2.insert(0,sdh.phonetic[1])
            for index in range(len(sdh.result)):
                ResultEntry[index].insert(0,sdh.result[index])

    def Okk():
        a=tkinter.messagebox.askyesno('提示', '要执行此操作吗')   # 返回 Ture 和 False
        if (a==False):
            return
        if (word['text']=="" or word['text']=="查询失败"):
            tkinter.messagebox.showerror('错误','无法删除')
            return
        words=WordEntry.get()
        sdh=Control.Handle()
        sdh.GetWordLocalInfo(words)
        sdh.phonetic=[]
        sdh.result=[]
        sdh.phonetic.append(StandardEntry1.get())
        sdh.phonetic.append(StandardEntry2.get())
        for index in range(5):
            if(ResultEntry==[]):
                break
            else:
                sdh.result.append(ResultEntry[index].get())
        sdh.SaveLocalInfo()
        
        # print(sdh.keyword,sdh.phonetic,sdh.result)

    def Ohno():
        a=tkinter.messagebox.askyesno('提示', '要删除此单词吗')
        if (a==False):
            return
        if (word['text']=="" or word['text']=="查询失败"):
            tkinter.messagebox.showerror('错误','无法删除')
            return
        sdh=Control.Handle()
        sdh.GetWordLocalInfo(word['text'])
        sdh.DeleteWord()

    SearchBtn.configure(command=BtnCallback)        #设置回调函数
    okk.configure(command=Okk)
    ohno.configure(command=Ohno)

    WordEntry.grid(row=0,column=0)              #布局
    SearchBtn.grid(row=0,column=1)

    word.grid(row=0,column=0,columnspan=2)
    StandardText1.grid(row=1,column=0)
    StandardEntry1.grid(row=1,column=1)
    StandardText2.grid(row=2,column=0)
    StandardEntry2.grid(row=2,column=1)
    for index in range(5):
        ResultText[index].grid(row=index+3,column=0)
        ResultEntry[index].grid(row=index+3,column=1)
    okk.grid(row=8,column=0,pady=10)
    ohno.grid(row=8,column=1,pady=10,padx=20,sticky="W")

    TopFrame.grid(row=0,column=0,padx=50)

    modifyFrame.grid(row=1,column=0)
    #ResultLabel.grid(row=1,column=0)
    ResultLabel.grid_forget()
    addFrame.grid_forget()

def func3():
    print("567")
    word=tk.Label(addFrame,text="单词")
    wordEntry=tk.Entry(addFrame,width=40) 
    StandardText1=tk.Label(addFrame,text="英:")
    StandardEntry1=tk.Entry(addFrame,width=40) 
    StandardText2=tk.Label(addFrame,text="美:")
    StandardEntry2=tk.Entry(addFrame,width=40) 
    ResultText=[]
    ResultEntry=[]
    okk=tk.Button(addFrame,text="确定")
    for index in range(5):
        ResultText.append(tk.Label(addFrame,text="解释"+str(index+1)))
        ResultEntry.append(tk.Entry(addFrame,width=40))

    def Okk():
        #print(1234)
        a=tkinter.messagebox.askyesno('提示', '要添加此单词吗')
        if (a==False):
            return
        sdh=Control.Handle()
        sdh.keyword=wordEntry.get()
        sdh.phonetic.append(StandardEntry1.get())
        sdh.phonetic.append(StandardEntry2.get())
        for index in range(5):
            if(ResultEntry==[]):
                break
            else:
                sdh.result.append(ResultEntry[index].get())
        sdh.SaveLocalInfo()


    okk.configure(command=Okk)

    word.grid(row=0,column=0)
    wordEntry.grid(row=0,column=1)
    StandardText1.grid(row=1,column=0)
    StandardEntry1.grid(row=1,column=1)
    StandardText2.grid(row=2,column=0)
    StandardEntry2.grid(row=2,column=1)
    for index in range(5):
        ResultText[index].grid(row=index+3,column=0)
        ResultEntry[index].grid(row=index+3,column=1)
    okk.grid(row=8,column=0,columnspan=2,pady=20)

    addFrame.grid(row=0,column=0,padx=100)

    TopFrame.grid_forget()
    ResultLabel.grid_forget()
    modifyFrame.grid_forget()

queryMenu.add_command(label="查询", command=func1)
queryMenu.add_command(label="修改", command=func2)
queryMenu.add_command(label="添加", command=func3)



func1()


# 进入消息循环
top.mainloop()