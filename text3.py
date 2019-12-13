import tkinter as tk
 
g_font = ("Monaco", 12)
 
 
class ShowFrame(object):
    '''
    show frame
    '''
 
    def __init__(self, master=None):
        self.root = master
        self.create_frame()
 
    def create_frame(self):
        '''
        create main frame
        '''
        self.frm = tk.Frame(self.root)
        self.frm.pack(fill="both", expand=1)
 
        self.frm_choose = tk.LabelFrame(self.frm) 
        self.frm_choose.pack(fill="both", expand=1, padx=2, side=tk.TOP)
 
        self.frm_show = tk.LabelFrame(self.frm) 
        self.frm_show.pack(fill="both", expand=1, padx=2, side=tk.BOTTOM)
 
        self.create_frm_choose()
        self.create_frm_show()
 
    def create_frm_choose(self):
        '''
        create frame choose
        '''
        self.choose_info_lst = ["Button0", "Button1", "Button2", "Button3"]
        self.choose_btn_lst = list()
        for index, value in enumerate(self.choose_info_lst):
            temp_btn = tk.Button(self.frm_choose,
                                 anchor="w",
                                 text=value,
                                 font=g_font)
            temp_btn.bind('<Button-1>', self.btn_click)
            temp_btn.pack(fill="both", expand=1, padx=2, pady=2, side=tk.LEFT)
            self.choose_btn_lst.append(temp_btn)
 
    def create_frm_show(self):
        '''
        create frame show
        '''
        self.show_label_0 = tk.Label(self.frm_show, text="Button0", font=g_font)
        self.show_label_0.pack(fill="both", expand=1, padx=2, pady=2)
 
        self.show_label_1 = tk.Label(self.frm_show, text="Button1", font=g_font)
        self.show_label_1.pack_forget()
 
        self.show_label_2 = tk.Label(self.frm_show, text="Button2", font=g_font)
        self.show_label_2.pack_forget()
 
        self.show_label_3 = tk.Label(self.frm_show, text="Button3", font=g_font)
        self.show_label_3.pack_forget()
 
    def btn_click(self, event=None):
        '''
        choose frm
        '''
        btn_text = event.widget['text']
        if btn_text == "Button0":
            self.show_label_0.pack(fill="both", expand=1, padx=2, pady=2)
            self.show_label_1.pack_forget()
            self.show_label_2.pack_forget()
            self.show_label_3.pack_forget()
        elif btn_text == "Button1":
            self.show_label_0.pack_forget()
            self.show_label_1.pack(fill="both", expand=1, padx=2, pady=2)
            self.show_label_2.pack_forget()
            self.show_label_3.pack_forget()
        elif btn_text == "Button2":
            self.show_label_0.pack_forget()
            self.show_label_1.pack_forget()
            self.show_label_2.pack(fill="both", expand=1, padx=2, pady=2)
            self.show_label_3.pack_forget()
        elif btn_text == "Button3":
            self.show_label_0.pack_forget()
            self.show_label_1.pack_forget()
            self.show_label_2.pack_forget()
            self.show_label_3.pack(fill="both", expand=1, padx=2, pady=2)
 
if __name__ == "__main__":
    '''
    main loop
    '''
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry()
 
    app = ShowFrame(root)
    app.frm.pack(fill="both", expand=1)
    root.mainloop()