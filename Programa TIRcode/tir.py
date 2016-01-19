#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Escuela Superior de Cómputo
import Tkinter
import math as m
import ImageTk
def van(i,f,tir,n):
	sum=0.0
	for x in range(0, len(f)):
		sum+= (f[x]/(m.pow((1+tir),(x+1))))
 	van = sum - i
	print "\nvp: "+str(van)+ "\t [TIR:" + str(tir*100)+"]"
 	return van
def tir():
	print "TIR 1.0"
	flujosEfectivoaux=flujosEVar.get()
	inv=InversionVar.get()
	flujosEfectivo=[]
	flujosEfectivo = map(float, flujosEfectivoaux.split())
	i = float(inv)
	print "\n\nAproximando TIR..."
	c=0.0
	d=0.0
	vana=0.0
	vanb=0.0
	for y in range(0, 100):
		vana=van(i,flujosEfectivo,y*0.01,len(flujosEfectivo))
		vanb=van(i,flujosEfectivo,(y+1)*0.01,len(flujosEfectivo))		
		if vana*vanb<0 :
			print "\nDiferencia encontrada\n"
			c=y*0.01
			d=(y+1)*0.01
			break
	ftir=0.0
	ftir=(c +((vana)/(vana-vanb))*(d-c))*100
	tirc=Tkinter.StringVar
	text = "Tir aproximada correctamente: \t ["+str(ftir)+"%]"
	etiqueta.config(text=text, width=100)
	etiqueta.update_idletasks()
root = Tkinter.Tk()
root.geometry("1150x300+50+50")
root.title("TIR 1.0")
frame = Tkinter.Frame(root)
frame.pack()
canvas = Tkinter.Canvas(frame, width=1366, height=100)
canvas.pack()
photoimage = ImageTk.PhotoImage(file="header.png")
canvas.create_image(500,50, image=photoimage)
flujosEVar=Tkinter.StringVar()
flujos = Tkinter.Entry(root,width=100,font=("Roboto", 11),relief="flat",textvariable=flujosEVar)
flujos.pack()
flujos.insert(0, "Ingrese flujos de efectivo: -800000 400000 400000 400000 400000 400000 400000 400000 400000 400000 400000 400000 3200000")
InversionVar=Tkinter.StringVar()
inversion = Tkinter.Entry(root,width=20,font=("Roboto", 13),relief="flat",textvariable=InversionVar)
inversion.pack()
inversion.insert(0, "Inversión : 3500000")
b = Tkinter.Button(root, text="Calcular TIR", width=10,relief="groove",command=tir)
b.pack()
etiqueta = Tkinter.Label(root, textvariable="", width=50, height=50, anchor="center",font=("Roboto", 13))
etiqueta.pack()
root.mainloop()
