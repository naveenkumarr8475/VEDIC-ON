from tkinter import *

def product():
    n1=int(num1.get())
    n2=int(num2.get())
    if 100>n1>90 and 100>n2>90:
        t1=Label(root,text="when both numbers are above  90 and below 100 "+"\n"+
        "the two numbers are "+str(n1)+"  and   "+str(n2)+"\n"+
        "calculate their differences from hundred and note the numbers  "+str(100-n1)+"  "+str(100-n2)+"\n"+
        "multiply those numbers  'A'="+str((100-n1)*(100-n2))+"\n"+
        "now interchange their differences from hundred and subtract them from the numbers  "+str(n1)+"-"+str(100-n2)+
        " "+str(n2)+"-"+str(100-n1)+"  =  "+str(n1-(100-n2))+"  ='B'"+"\n"+
        "the product of the numbers is 'BA'  ="+str(n1*n2)+"\n",font=("",12))
        t1.place(relx=0.1,rely=0.4)
    elif n1<100 and n2<100 and(n1+n2)%10==0 and n1//10==n2//10:
        t2=Label(root,text="when the digits in tenth place are equal and the digit in ones place adds upto ten"+"\n"+
        str(n1//10)+"=="+str(n2//10)+"  and  "+str(n1%10)+"  +  "+str(n2%10)+" = "+str((n1%10)+(n2%10))+"\n"+
        "add +1 to digit in tenth place  "+str(n1//10)+"  +1"+"  =  "+str((n1//10)+1)+"\n"+
        "multiply the above numbers  "+str(n1//10)+" and "+str((n1//10)+1)+"  =  "+str((n1//10)*((n1//10)+1))+"  ='A'"+"\n"+
        "multiply the numbers in the ones place  "+str(n1%10)+"  X  "+str(n2%10)+"  =  "+str((n1%10)*(n2%10))+"  ='B'"+"\n"+
        "the product of the numbers is  'AB'  ="+str(n1*n2)+"\n",padx=100,font=("",12))
        t2.place(relx=0.1,rely=0.4)
    elif n1-n2== 2 or n2-n1==2:
        t3=Label(root,text="when the digits are consecutive odd or even numbers  "+"\n"+
        "find the number between the consecutive number  "+"  >>>  "+str((n1+n2)/2)+"\n"+
        "square the obtained number  "+str(((n1+n2)/2)**2)+"\n"+
        "subtract 1 from the obtained square   "+str(((n1+n2)/2)**2)+"   -   "+"1"+"\n"+
        "the product of the numbers is  "+str(n1*n2)+"\n",padx=170,pady=20,font=("",12))
        t3.place(relx=0.1,rely=0.4)
    #elif:
    else:
        last1=Label(root,text="the product of the number is  "+str(n1*n2)+"\n"+
        "sorry for the inconvience caused due insufficient modules to determine"+"\n"+
        "the tricks in vedic math ,we couldnt provide u the steps to the answer arrived"+"\n"+
        "Wait for an update.see u soon",padx=120,pady=30,font=("",12))
        last1.place(relx=0.1,rely=0.4)


def squaring():
    n3=int(num3.get())
    a=(n3//100)
    b=(n3%100)//10
    c=n3%100
    if (n3)%10==5:
        t1=Label(boot,text="when the number ends with digit 5"+"\n"+
        "the given number is  "+str(n3)+"\n"+
        "remove the rightmost digit in the given number  "+str(n3)+"  >>>  "+str(n3//10)+"\n"+
        "now add +1 to the obtained number "+str(n3//10)+" +1 "+"  >>>  "+str((n3//10)+1)+"\n"+
        "multiply the above numbers  'A'=  "+str((n3//10)*((n3//10)+1))+"\n"+
        "square the rightmost digit  'B'=  "+str(n3%10)+"  >>>  "+str((n3%10)**2)+"\n"+
        "the square of the number is  AB=  "+str(n3**2),padx=200,pady=50,font=("",12))
        t1.place(relx=0.05,rely=0.4)
    elif (n3)%10==1:
        t2=Label(boot,text="when the number ends with digit 1"+"\n"+
        "the given number is   "+str(n3)+"\n"+
        "subtract one from the given number  "+str(n3)+"  -1  "+"  >>>  "+str(n3-1)+"\n"+
        "square the obtained number  "+str(n3-1)+"  >>>  "+str((n3-1)**2)+"\n"+
        "multiply the obtained number by 2  "+str(n3-1)+"  >>>>  "+str((n3-1)*2)+"\n"+
        "add the above numbers and add +1 to it  "+str((n3-1)**2)+"  +  "+(str((n3-1)*2))+" + 1 "+"  >>>  "+str(n3**2)+"\n"+
        "the square of the number is  AB=  "+str(n3**2),padx=200,pady=50,font=("",12))
        t2.place(relx=0.05,rely=0.4)
    elif n3 in range(101,1000) and (b==0 or b==1):
        t3=Label(boot,text="when the given number is 3 digit number and the middle digit is '0'or'1'  "+"\n"+
        "the given number is  "+str(n3)+"\n"+
        "considering the left most digit and squaring it.  'A'=  "+str(a)+"  >>>  "+str(a**2)+"\n"+
        "considering the last two digits square them  "+str(c)+"  >>>  "+str(c**2)+"\n"+
        "condider only last two digits of the above number  'B'=  "+str((c**2)%100)+"\n"+
        "leftmost digit 'C'=  "+str((c**2)//100)+"\n"+
        "multiply the first digit and the last two digit nd double it and add 'C'  'D'=  "+str(a)+" X "+str(c)+"  X 2  + "+str((c**2)//100)+"  =  "+str((a*c*2)+((c**2)//100))+"\n"+
        "now jion the numbers in ADB format  "+str(n3**2),pady=30,font=("",12))
        t3.place(relx=0.1,rely=0.4)
    else:
        last2=Label(boot,text="the square of the number is  "+str(n3**2)+"\n"+
        "sorry for the inconvience caused due insufficient modules to determine"+"\n"+
        "the tricks in vedic math ,we couldnt provide u the steps to the answer arrived"+"\n"+
        "Wait for an update.see u soon",padx=120,pady=50,font=("",12))
        last2.place(relx=0.1,rely=0.4)
        
main=Tk()
main.title("VEDIC--ON")
main.geometry("500x500+0+0")
main.configure(bg="BLACK")
lbl=Label(main,text="VEDIC--ON",font=("algerian",50),bg="black",fg="orange")
lbl.place(anchor=N,relx=0.5,rely=0.21)
lbl=Label(main,text="re-glorify the CIVILIZATION",font=("algerian",12),bg="black",fg="white")
lbl.place(anchor=N,relx=0.5,rely=0.35)
lbl=Label(main,text="A VEDIC TUTOR ND CALCULATOR",font=("ALGERIAN",8),bg="black",fg="WHITE")
lbl.place(anchor=N,relx=0.5,rely=0.39)
name1=Entry(main,bg="gold",fg="indigo")
name1.place(anchor=N,relx=0.5,rely=0.45)
name1.insert(0,"FIRST NAME")
name2=Entry(main,bg="silver",fg="indigo")
name2.place(anchor=N,relx=0.5,rely=0.5)
name2.insert(0,"LAST NAME")
entry=Entry(main,bg="aqua",fg="indigo")
entry.place(anchor=N,relx=0.5,rely=0.55)
entry.insert(0,"mODuLeS")

def choose():
    ch1=entry.get()
    ch=ch1.lower()
    if ch=="multiplication":
        def dele1():
            num1.delete(0,END)
        def dele2():
            num2.delete(0,END)
        def dele3():
            dele1()
            dele2()
        global num1
        global num2
        global root
        root=Tk()
        root.title("MULTIPLICATION")
        root.geometry("900x600-0+0")
        root.configure(bg="gold")
        num1=Entry(root,width=15,bg="aqua",fg="purple")
        num1.pack()
        num2=Entry(root,width=15,bg="aqua",fg="purple")
        num2.pack()
        del1=Button(root,text="CLEAR",command=dele3,activebackground="red")
        del1.pack()
        ans1=Button(root,text="MULTIPLY",bg="red",activebackground="green",command=product)
        ans1.pack()
        root.mainloop()
    if ch=="squares":
        def dele4():
            num3.delete(0,END)
        global num3
        global boot
        boot=Tk()
        boot.title("SQUARING")
        boot.geometry("900x600-0+0")
        boot.configure(bg="aqua")
        num3=Entry(boot,width=15,bg="gold",fg="indigo")
        num3.pack()
        del2=Button(boot,text="CLEAR",command=dele4,activebackground="red")
        del2.pack()
        ans2=Button(boot,text="SQUARE",bg="red",activebackground="green",command=squaring)
        ans2.pack()
        boot.mainloop()
    else:
        name=(name1.get()).upper()+"  "+(name2.get()).upper()
        end=Label(main,text="invalid input\ntry again  "+name,bg="red",fg="black",font=("chiler",18))
        end.place(anchor=N,relx=0.5,rely=0.7)

button=Button(main,text="ENTER",font=("ggg",8),command=choose,bg="red",activebackground="green").place(anchor=N,relx=0.5,rely=0.6)


main.mainloop()
