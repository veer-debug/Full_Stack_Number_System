from tkinter import *
# from tkinter import tk
import webbrowser
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Main:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("DEVLOPER")
        
        title_ibl=Label(self.root,text="CALCULATOR",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(root,bd=2)
        main_frame.place(x=0,y=50,width=1600,height=1000)
        
        
        #-----------------------------------------left lable frame---------------------------------------------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,text="BASE-CONVERTER",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=10,width=900,height=1000)
        INN_frame=LabelFrame(Left_frame,bd=2,bg="light green",relief=RIDGE,font=("times new roman",12,"bold"))
        INN_frame.place(x=20,y=10,width=860,height=680)
        
        number=Label(INN_frame,width="20",height=2,text="Enter Number",font=("times new roman",12,"bold"),bg="white")
        number.grid(row=0,column=0,padx=10,pady=20,sticky=W)
        
        # Numbers=Label(INN_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        # Numbers.grid(row=0,column=1,padx=10,pady=2,sticky=W)
        student_entry=ttk.Entry(INN_frame,width=20,font=("times new roman",27,"bold"))
        student_entry.grid(row=0,column=1,padx=8,pady=2,sticky=W)
        
        number_combo=ttk.Combobox(INN_frame,height=1000,font=("times new roman",12,"bold"),width=5,state="readonly")
        number_combo['values']=("Male","Female","Other")
        number_combo.current(0)
        number_combo.grid(row=0,column=2,padx=10,sticky=W)
        
        
        
        # =============================RIGHT LABLE FRAME===================
        Right_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,text="DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=935,y=10,width=580,height=1000)
        
        
        
        
        
        
        
        

        




if __name__=="__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()
    root.mainloop()
    