from tkinter import *

root = Tk()
root.geometry('500x470') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#fff') #background color



#-------------------------- Frame 2 --------------------------#

fr2 = LabelFrame(root, background='#fff', text='Dados Pessoais', fg="blue", font='Georgia 12')
fr2.grid(row=0, padx= 15)

#Linha 1
lb0_fr2 = Label(fr2, text="Nome:", font='Georgia 10').grid(row=1, column=0)
in0_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=1, column=1, columnspan=5, sticky=NSEW)

#Linha 2
lb1_fr2 = Label(fr2, text="CPF:", font='Georgia 10').grid(row=2, column=0)
in1_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=2, column=1)

lb2_fr2 = Label(fr2, text="Data Nasc:", font='Georgia 10').grid(row=2, column=2)
in2_fr2 = Entry(fr2, fg='blue', font='Georgia 10', cursor="gobbler").grid(row=2, column=3)

lb3_fr2 = Label(fr2, text="Telefone:", font='Georgia 10').grid(row=2, column=4)
in3_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=2, column=5)

#Linha 3
lb4_fr2 = Label(fr2, text="Rua:", font='Georgia 10').grid(row=3, column=0)
lb4_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=3, column=1, columnspan=3, sticky=NSEW)

lb5_fr2 = Label(fr2, text="  N° da casa:", font='Georgia 10').grid(row=3, column=4)
lb5_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=3, column=5)

#linha 4
lb6_fr2 = Label(fr2, text="Bairro:", font='Georgia 10').grid(row=4, column=0,)
lb6_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=4, column=1)

lb7_fr2 = Label(fr2, text="Cidade:", font='Georgia 10').grid(row=4, column=2)
lb7_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=4, column=3)

lb8_fr2 = Label(fr2, text=" Estado:", font='Georgia 10').grid(row=4, column = 4)
lb8_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=4, column=5)

#-------------------------- Frame 2.1 --------------------------#

fr2_1 = LabelFrame(root, background='#fff', text='Finalize seu cadastro', fg="blue", font='Georgia 12')
fr2_1.grid(row=2, padx= 15, sticky=NSEW)

#Linha 8
bt0_fr1 = Button(fr2_1, text="Gravar Dados", font='Georfia 10').grid(row=8, column=0)
bt1_fr1 = Button(fr2_1, text="Listar Dados", font='Georfia 10').grid(row=8, column=1)

root.mainloop()