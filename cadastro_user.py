from tkinter import *

root = Tk()
root.geometry('900x250') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#8a37cc') #background color

#-------------------------- Functions --------------------------#

#Aqui ficaram as funções do projeto

#-------------------------- Frame 2.1 / Widgets --------------------------#

fr2_1 = LabelFrame(root, text="Banco Dellux", bg="green").grid(row=0, column=0, pady=15)

# lb0_fr2_1 = Label(fr2_1, text="Faça aqui o cadastro de novos Clientes", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=6, padx=200, pady=15)

#Linha 1
lb1_fr2 = Label(fr2_1, text="Nome:", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=1, column=0)
in0_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=1, column=1, columnspan=5, sticky=EW)

#Linha 2
lb2_fr2 = Label(fr2_1, text="Cpf:", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=2, column=0)
in1_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=2, column=1, sticky=EW)

lb3_fr2 = Label(fr2_1, text="Data Nasc:", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=2, column=2)
in2_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff", cursor="gobbler").grid(row=2, column=3, sticky=EW)

#Linha 3

lb4_fr2 = Label(fr2_1, text="Tel:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=2, column=4)
in3_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=2, column=5, sticky=EW)

lb5_fr2 = Label(fr2_1, text="Logradouro:", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column=0)
lb4_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=3, column=1, columnspan=3, sticky=EW)

lb6_fr2 = Label(fr2_1, text="N°:", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column=4)
lb5_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=3, column=5,sticky=EW)

#linha 4
lb7_fr2 = Label(fr2_1, text="Bairro", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=0,)
lb6_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=4, column=1, sticky=EW)

lb8_fr2 = Label(fr2_1, text="Cidade:", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=2)
lb7_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=4, column=3, sticky=EW)

lb9_fr2 = Label(fr2_1, text="UF:", font=("Mongolian Baiti", "12"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column = 4)
lb8_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=4, column=5, sticky=EW)

# Botões
bt0_fr2 = Button(fr2_1, text="Criar conta ", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff").grid(row=5, column=0, sticky=EW, pady= 30)

bt1_fr2 = Button(fr2_1, text="Voltar", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff").grid(row=5, column=1, sticky=EW)


#Anotações

# Falta adicionar o LB0 ao layout, colocar uma margin nos botões, e mudar as cores dos labels para outra tonalidade


#-------------------------- Mostrar tela --------------------------#

root.mainloop()