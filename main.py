from tkinter import *
# from tkinter import tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import scrolledtext



class Main:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Number System")
        self.root.iconbitmap(r"Full_Stack_Number_System/Images/logo.ico")
        
        title_ibl=Label(self.root,text="NUMBER-SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(root,bd=2)
        main_frame.place(x=0,y=50,width=1600,height=1000)
        
        
        #-----------------------------------------left lable frame---------------------------------------------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,text="BASE-CONVERTER",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=10,width=900,height=1000)
        INN_frame=LabelFrame(Left_frame,bd=2,bg="light green",relief=RIDGE,font=("times new roman",12,"bold"))
        INN_frame.place(x=20,y=10,width=860,height=680)
        # ==============================================
        
        img0=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Full_Stack_Number_System\Images\Number.jpg")
        img0=img0.resize((840,270))
        self.photoimg0=ImageTk.PhotoImage(img0)
        
        f_lbl=Label(INN_frame,image=self.photoimg0)
        f_lbl.place(x=10,y=500,width=840,height=170)
        
        img00=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Full_Stack_Number_System\Images\logo.ico")
        img00=img00.resize((80,80))
        self.photoimg00=ImageTk.PhotoImage(img00)
        
        f_lbl=Label(INN_frame,image=self.photoimg00)
        f_lbl.place(x=380,y=30)
        
        number=Label(INN_frame,width="15",height=2,text="Enter Number",font=("times new roman",15,"bold"),bg="white")
        number.place(x=70,y=190)
        
        # number_lable=Label(INN_frame,text="Number",font=("times new roman",12,"bold"),bg="white")
        # number_lable.grid(row=0,column=0,padx=10,pady=2,sticky=W)
        number_entry=ttk.Entry(INN_frame,width="20",font=("times new roman",30,"bold"))
        number_entry.place(x=330,y=190)
        
        
        number_combo=ttk.Combobox(INN_frame,font=("times new roman",30,"bold"),width=2,state="readonly")
        number_combo['values']=("10","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35")
        number_combo.current(0)
        number_combo.place(x=730,y=190)
        
        # ==============================================
        
        
        number1=Label(INN_frame,width="15",height=2,text="Result",font=("times new roman",15,"bold"),bg="white")
        number1.place(x=70,y=300)
        
        # number1_lable=Label(INN_frame,text="Number1",font=("times new roman",12,"bold"),bg="white")
        # number1_lable.grid(row=0,column=0,padx=10,pady=2,sticky=W)
        number1_entry=ttk.Entry(INN_frame,width=20,font=("times new roman",30,"bold"))
        number1_entry.place(x=330,y=300)
        
        
        number1_combo=ttk.Combobox(INN_frame,font=("times new roman",30,"bold"),width=2,state="readonly")
        number1_combo['values']=("10","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35")
        number1_combo.current(0)
        number1_combo.place(x=730,y=300)
        
        # Button
        
        Submit=Button(INN_frame,text="Submit",width=20,font=("times new roman",20,"bold"),bg="red",fg="white")
        Submit.place(x=330,y=400,width=150,height=50)
             
        
        
        # =============================RIGHT LABLE FRAME===================
        Right_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,text="About Me",font=("times new roman",12,"bold"))
        Right_frame.place(x=935,y=10,width=580,height=1000)
        
        img1=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Full_Stack_Number_System\Images\RANVEER.jpeg")
        img1=img1.resize((250,250))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(Right_frame,image=self.photoimg1)
        f_lbl.place(x=180,y=30,width=250,height=250)
        
        
        R6=Label(Right_frame,text="Ranveer Kumar",font=(" ",25,"bold"),bg="white",fg="red")
        R6.place(x=180,y=290)
        
        Right1_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        Right1_frame.place(x=10,y=350,width=560,height=250)
        
        R7=Label(Right1_frame,text="A dedicated  Python  developer, brings a wealth  of expertise to the ",font=(" ",13,"bold"),bg="white",fg="black")
        R7.place(x=10,y=20)
        R8=Label(Right1_frame,text="Realm of full-stack development.His commitment to crafting efficient",font=(" ",13,"bold"),bg="white",fg="black")
        R8.place(x=10,y=50)
        R8=Label(Right1_frame,text="A elegant  solutions is evident in his meticulous approach to coding.",font=(" ",13,"bold"),bg="white",fg="black")
        R8.place(x=10,y=80)
        R8=Label(Right1_frame,text="With a keen eye  for detail  and a passion  for clean  code, Renveer ",font=(" ",13,"bold"),bg="white",fg="black")
        R8.place(x=10,y=110)
        R9=Label(Right1_frame,text="transforms   complex   challenges  into   streamlined   applications.  ",font=(" ",13,"bold"),bg="white",fg="black")
        R9.place(x=10,y=140)
        R10=Label(Right1_frame,text="Constantly  evolving  alongside  Python  dynamic  ecosystem, he  ",font=(" ",13,"bold"),bg="white",fg="black")
        R10.place(x=10,y=170)
        R11=Label(Right1_frame,text="remains at the  forefront  of innovation. ",font=(" ",13,"bold"),bg="white",fg="black")
        R11.place(x=130,y=200)
        # Futter
        
        img2=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Full_Stack_Number_System\Images\git.png")
        img2=img2.resize((40,40))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lb2=Label(Right_frame,image=self.photoimg2)
        f_lb2.place(x=100,y=630,width=40,height=40)
        
        
        
        img3=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Full_Stack_Number_System\Images\facebook.png")
        img3=img3.resize((40,40))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lb3=Label(Right_frame,image=self.photoimg3)
        f_lb3.place(x=200,y=630,width=40,height=40)
        
        
        
        img4=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Full_Stack_Number_System\Images\insta.png")
        img4=img4.resize((40,40))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        f_lb4=Label(Right_frame,image=self.photoimg4)
        f_lb4.place(x=300,y=630,width=40,height=40)
        
        img5=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Full_Stack_Number_System\Images\linkidin.png")
        img5=img5.resize((40,40))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        f_lb5=Label(Right_frame,image=self.photoimg5)
        f_lb5.place(x=400,y=630,width=40,height=40)
        
        
        
        
        
        

        




if __name__=="__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()
    root.mainloop()
    