import tkinter,glob,os,sys,shutil
from tkinter import *
from tkinter import messagebox
top=Tk()
top.title("File Manager")
top.geometry("415x365")
Count=Label(top,text="Number of Files",font="Helvetica 12 bold").grid(row=0,column=0)
l1=Label(top,text="Enter File Type:").grid(row=1,column=0)
e1=Entry(top)
e1.grid(row=2,column=0)
e1.focus_set()
l2=Label(top,text="Enter Directory:").grid(row=3,column=0)
e2=Entry(top)
e2.grid(row=4,column=0)
e2.focus_set()

def Coun():
	type=e1.get()
	dir=e2.get()
	type1='*.'+type
	counter=len(glob.glob1(dir,type1))
	messagebox.showinfo("Number of files",str(counter)+" files are present")
B= tkinter.Button(top,text="Calculate",command=Coun).grid(row=6,column=0)


Delete=Label(top,text="Delete a File",font="Helvetica 12 bold").grid(row=0,column=1)
l3=Label(top,text="Enter File Directory:").grid(row=1,column=1)
e3=Entry(top)
e3.grid(row=2,column=1)
e3.focus_set()
l4=Label(top,text="Enter File Name:").grid(row=3,column=1)
e4=Entry(top)
e4.grid(row=4,column=1)
e4.focus_set()

def Del():
	type=e3.get()
	dir=e4.get()
	file=type+"/"+dir
	if(os.path.isfile(file)):
		os.remove(file)
		messagebox.showinfo("File Deleted","File Successfully Deleted")
	else:
		messagebox.showinfo("Error!","File Not Present in Directory")
B= tkinter.Button(top,text="Delete",command=Del).grid(row=6,column=1)



Rename=Label(top,text="Rename a File",font="Helvetica 12 bold").grid(row=0,column=2)
l5=Label(top,text="Enter File Directory:").grid(row=1,column=2)
e5=Entry(top)
e5.grid(row=2,column=2)
e5.focus_set()
l6=Label(top,text="Enter File Name:").grid(row=3,column=2)
e6=Entry(top)
e6.grid(row=4,column=2)
e6.focus_set()
l7=Label(top,text="Enter New Name:").grid(row=5,column=2)
e7=Entry(top)
e7.grid(row=6,column=2)
e7.focus_set()

def Ren():
	type=e5.get()
	dir=e6.get()
	new=e7.get()
	file=type+"/"+dir
	if(os.path.isfile(file)):
		os.chdir(type)
		os.rename(dir,new)
		messagebox.showinfo("File Renamed","File Successfully Renamed")
	else:
		messagebox.showinfo("Error!","File Not Present in Directory")
B= tkinter.Button(top,text="Rename",command=Ren).grid(row=7,column=2)




Create=Label(top,text="Create a Text File",font="Helvetica 12 bold").grid(row=8,column=0)
l8=Label(top,text="Enter File Directory:").grid(row=9,column=0)
e8=Entry(top)
e8.grid(row=10,column=0)
e8.focus_set()
l9=Label(top,text="Enter File Name:").grid(row=11,column=0)
e9=Entry(top)
e9.grid(row=12,column=0)
e9.focus_set()
l10=Label(top,text="Enter Data:").grid(row=13,column=0)
e10=Entry(top)
e10.grid(row=14,column=0)
e10.focus_set()

def Crea():
	type=e8.get()
	dir=e9.get()
	new=e10.get()
	filename=dir+".txt"
	os.chdir(type)
	file=open(filename,"w")
	file.write(new)
	file.close()
	messagebox.showinfo("File Created","File Created Successfully")
B= tkinter.Button(top,text="Create",command=Crea).grid(row=15,column=0)



Copy=Label(top,text="Copy/Paste a File",font="Helvetica 12 bold").grid(row=8,column=1)
l11=Label(top,text="Enter File Directory:").grid(row=9,column=1)
e11=Entry(top)
e11.grid(row=10,column=1)
e11.focus_set()
l12=Label(top,text="Enter File Name:").grid(row=11,column=1)
e12=Entry(top)
e12.grid(row=12,column=1)
e12.focus_set()
l13=Label(top,text="Enter Directory to Copy:").grid(row=13,column=1)
e13=Entry(top)
e13.grid(row=14,column=1)
e13.focus_set()

def Cop():
	type=e11.get()
	dir=e12.get()
	new=e13.get()
	filename=type+"/"+dir
	shutil.copy(filename,new)
	messagebox.showinfo("File Copied","File Copied Successfully")
B= tkinter.Button(top,text="Copy",command=Cop).grid(row=15,column=1)



Move=Label(top,text="Move a File",font="Helvetica 12 bold").grid(row=8,column=2)
l14=Label(top,text="Enter File Directory:").grid(row=9,column=2)
e14=Entry(top)
e14.grid(row=10,column=2)
e14.focus_set()
l15=Label(top,text="Enter File Name:").grid(row=11,column=2)
e15=Entry(top)
e15.grid(row=12,column=2)
e15.focus_set()
l16=Label(top,text="Enter Directory to Move:").grid(row=13,column=2)
e16=Entry(top)
e16.grid(row=14,column=2)
e16.focus_set()

def Mov():
	type=e14.get()
	dir=e15.get()
	new=e16.get()
	filename=type+"/"+dir
	shutil.move(filename,new)
	messagebox.showinfo("File Moved","File Moved Successfully")
B= tkinter.Button(top,text="Move",command=Mov).grid(row=15,column=2)

mainloop()
