import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("MDBA.db")

#variables
rootB=None

def date_up():
    global b1,b2
    b1 = P_id.get()
    b2 = dd.get()
    conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
    conn.commit()
    tkinter.messagebox.showinfo("COVID FACILITY DATABASE SYSTEM", "DISCHARGE DATE UPDATED")

def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = sqlite3.connect("MDBA.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = treat_2.get(tkinter.ACTIVE)
    b5 = cost_t.get()
    b6 = med.get(tkinter.ACTIVE)
    b7 = med_q.get(tkinter.ACTIVE)
    b8 = price.get()
    conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (b1, b3, b4, b5,))
    conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
    conn.commit()
    tkinter.messagebox.showinfo("COVID FACILITY DATABASE SYSTEM", "BILLING DATA SAVED")

def calci():
    global b1
    conn = sqlite3.connect("MDBA.db")
    u=conn.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?",(b1,) )
    conn.commit()
    for ii in u:
        pp=tkinter.Label(rootB,text="TOTAL AMOUNT OUTSTANDING",fg='red',font = ("Recursive", 11, "bold"))
        pp.place(x="200", y='260')
        uu=tkinter.Label(rootB,text=ii[0],font = ("Recursive", 11, "bold"))
        uu.place(x="230",y='290')

L1=None
L2=None
L3=None
L4=None

def exitt():
    rootB.destroy()

def BILLING():
    global rootB,L1,treat1,P_id,dd,cost,med,med_q,price,treat_1,treat_2,cost_t,j,jj,jjj,jjjj,L2,L3,L4
    rootB=tkinter.Tk()
    rootB.geometry("600x350")
    rootB.title("BILLING SYSTEM")
    head=tkinter.Label(rootB,text="PATIENT BILL",font = ("Recursive", 11, "bold"),fg='grey')
    head.place(x=100,y=10)
    id = tkinter.Label(rootB, text="PATIENT ID",font = ("Recursive", 11, "bold"))
    id.place(x=20, y=60)
    P_id = tkinter.Entry(rootB,font = ("Recursive", 11, "bold"))
    P_id.place(x=180, y=60)
    dd_l = tkinter.Label(rootB, text="DATE DISCHARGED",font = ("Recursive", 11, "bold"))
    dd_l.place(x=20, y=100)
    dd = tkinter.Entry(rootB,font = ("Recursive", 11, "bold"))
    dd.place(x=180, y=100)
    ddp=tkinter.Button(rootB,text="UPDATE DISCHARGE DATE",command=date_up,font = ("Recursive", 9, "bold"))
    ddp.place(x=400,y=100)
    treat = tkinter.Label(rootB, text="SELECT TREATMENT",font = ("Recursive", 11, "bold"))
    treat.place(x=20, y=140)
    L1 = ["CONSULATION","SURGERY","LAB TEST"]
    treat_1= tkinter.Listbox(rootB, width=15, height=1, selectmode='SINGLE', exportselection=0,font = ("Recursive", 11, "bold"))
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.place(x=180,y=140)
    treat_c = tkinter.Label(rootB, text="CODE",font = ("Recursive", 11, "bold"))
    treat_c.place(x=350, y=140)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = tkinter.Listbox(rootB, width=6, height=1, selectmode='SINGLE', exportselection=0,font = ("Recursive", 11, "bold"))
    for jj in L2:
        treat_2.insert(tkinter.END, jj)
    treat_2.place(x=400, y=140)
    costl= tkinter.Label(rootB, text="COST",font = ("Recursive", 11, "bold"))
    costl.place(x=450, y=140)
    cost_t = tkinter.Entry(rootB,width=5,font = ("Recursive", 11, "bold"))
    cost_t.place(x=500, y=140)
    med1 = tkinter.Label(rootB, text="SELECT MEDICINE",font = ("Recursive", 11, "bold"))
    med1.place(x=20, y=180)
    L3 = ["NEURAL", "FANEKPLUS", "DISPRIN","DOLO+","BANDAGE","DIGENE"]
    med = tkinter.Listbox(rootB, width=15, height=1, selectmode='SINGLE', exportselection=0,font = ("Recursive", 11, "bold"))
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.place(x=180, y=180)
    med_ql = tkinter.Label(rootB, text="No.#",font = ("Recursive", 11, "bold"))
    med_ql.place(x=350, y=180)
    L4 = [1,2,3,4,5,6,7,8,9,10]
    med_q = tkinter.Listbox(rootB, width=4, height=1, selectmode='SINGLE', exportselection=0,font = ("Recursive", 11, "bold"))
    for jjjj in L4:
        med_q.insert(tkinter.END, jjjj)
    med_q.place(x=400, y=180)
    pricel = tkinter.Label(rootB, text="PRICE ",font = ("Recursive", 11, "bold"))
    pricel.place(x=450, y=180)
    price = tkinter.Entry(rootB, width=5,font = ("Recursive", 11, "bold"))
    price.place(x=500, y=180)
    b1=tkinter.Button(rootB,text="GENERATE BILL",command=calci,font = ("Recursive", 9, "bold"))
    b1.place(x="200",y="230")
    b2 = tkinter.Button(rootB, text="UPDATE DATA", command=up,font = ("Recursive", 9, "bold"))
    b2.place(x="100", y="230")
    ee=tkinter.Button(rootB,text="EXIT",command=exitt,font = ("Recursive", 9, "bold"))
    ee.place(x='310',y='230')
    rootB.mainloop()
