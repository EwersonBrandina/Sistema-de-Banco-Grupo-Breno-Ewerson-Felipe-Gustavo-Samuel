from tkinter import *

root = Tk()
root.geometry('750x470') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#8a37cc') #background color

#-------------------------- Functions --------------------------#

#Aqui ficaram as funções do projeto

#-------------------------- Frame 2.1 / Widgets --------------------------#

fr2_2 = LabelFrame(root, bg="#8a37cc").grid(row=0, column=0,pady=50, padx=150)

lb0_fr2_2 = Label(fr2_2, text="Faça aqui a exclusão de usuarios", font=("Mongolian Baiti", "23"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=5, sticky=E, pady=30)

lb1_fr2_2 = Label(fr2_2, text="Nome do usuario:", font=("Mongolian Baiti", "13"),background="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, sticky=E)
in0_fr2 = Entry(fr2_2, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff", width=30).grid(row=2, column=1, columnspan=2, sticky=EW)

lb2_fr2_2 = Label(fr2_2, text="Confirme sua senha:", font=("Mongolian Baiti", "13"),background="#8a37cc", fg="#f5f5f5").grid(row=3, column=0, sticky=E)
in1_fr2 = Entry(fr2_2, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff").grid(row=3, column=1, columnspan=2, sticky=EW)


# Botões
bt0_fr2 = Button(fr2_2, text="Deletar conta ", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff").grid(row=4, column=0,columnspan=2, sticky=W, pady=60, padx=190) #Pura Gambiarra e ta tudo bem
bt1_fr2 = Button(fr2_2, text="Voltar", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff").grid(row=4, column=1, sticky=W, padx=50)




root.mainloop()