from tkinter import *
import sqlite3

def save_database(Name,E_id,Mobile,F_name,Gender,Address,Lan_1,Lan_2):
    conn = sqlite3.connect(r'D:\projects\Employee_Management\database.db')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO emp_info(name,email_id,mobile,f_name,gender,\
        address) VALUES(?,?,?,?,?,?)',(Name,E_id,Mobile,F_name,Gender,Address))
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    

def validate_input(new_value):
    valid = new_value .isdigit() and len(new_value) <= 10
    return valid


def save():
    name=e1.get()
    e_id=e2.get()
    mobile=e3.get()
    f_name=e4.get()
    g=v.get()
    if g==1:
        gender="Male"
    else:
        gender="Female"
        
    address=Add.get("1.0",END)
    
    if lan1.get():
        lan_1="Hindi"
    else:
        lan_1=""
    if lan2.get():
        lan_2="English"
    else:
        lan_2=""
    
    save_database(name,e_id,mobile,f_name,gender,address,lan_1,lan_2) 
    

m=Tk()
m.geometry('500x500')
m.title('Employee_Management')
m.configure(background='#BABFB6')
menu=Menu(m)
validate = m.register(validate_input)

m.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Edit')
filemenu.add_separator()
filemenu.add_command(label='exit',command=m.destroy)
helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
filemenu.add_command(label='About')

l1=Label(m,text="Name : ",bg='#BABFB6')
l2=Label(m,text="Email Id  : ",bg='#BABFB6')
l3=Label(m,text="Mobile  : ",bg='#BABFB6')
l4=Label(m,text="Father_Name: ",bg='#BABFB6')

l1.grid(row = 0, column = 0, sticky = NW)
l2.grid(row = 1, column = 0, sticky = NW)
l3.grid(row = 2, column = 0, sticky = NW)
l4.grid(row = 3, column = 0, sticky = NW)
f2=Frame(m)
f2.grid(row=0,column=1,sticky=NW)
e1=Entry(f2,bg='#CFE8F3')
f3=Frame(m)
f3.grid(row=1,column=1,sticky=NW)
e2=Entry(f3,bg='#CFE8F3')
f4=Frame(m)
f4.grid(row=2,column=1,sticky=NW)
e3=Entry(f4,bg='#CFE8F3',validate="key", validatecommand=(validate, "%P"))
f5=Frame(m)
f5.grid(row=3,column=1,sticky=NW)              
e4=Entry(f5,bg='#CFE8F3')
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)

l5=Label(m,text="Gender : ",bg='#BABFB6')#.grid(row=8)
l5.grid(row=4,column=0,sticky=NW)
f1=Frame(m)
f1.grid(row=4,column=1,sticky=NW)
v=IntVar()
Radiobutton(f1,text="Male",variable=v,value=1,bg='#BABFB6').grid(row=4,column=1,sticky=W)
Radiobutton(f1,text="Female",variable=v,value=2,bg='#BABFB6').grid(row=4,column=2,sticky=W)
#radiobutton(m,text="Others",variable=v,value=3).pack(anchor=W)
f0=Frame(m)
f0.grid(row=5,column=0,sticky=NW)
l6=Label(f0,text="Address : ",bg='#BABFB6')
l6.grid(row=5,column=0,sticky=NW)
Add=Text(m,height=5,width=25,fg='black',bg='#CFE8F3')
Add.grid(row=5,column=1,sticky=W)
Label(m,text="Language : ",bg='#BABFB6').grid(row=6,sticky=NW)
lan1=IntVar()
f1=Frame(m)
f1.grid(row=6,column=1,sticky=W)
C1=Checkbutton(f1,text='Hindi',variable=lan1,bg='#BABFB6')
lan2=IntVar()
C2=Checkbutton(f1,text='English',variable=lan2,bg='#BABFB6')
C1.grid(row=6,column=1)
C2.grid(row=6,column=2)
frame=Frame(m)
frame.grid(row=8,column=1,sticky=S)


button=Button(frame,text='SAVE',width=12,height=2,fg='black',bg='#BABFB6',command=save)\
.grid(row=8,column=2,sticky=S)
button=Button(frame,text='SEARCH',width=12,height=2,fg='black',bg='#BABFB6')\
.grid(row=8,column=3,sticky=S)

m.mainloop()