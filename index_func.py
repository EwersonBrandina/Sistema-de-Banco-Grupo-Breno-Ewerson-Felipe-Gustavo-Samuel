from tkinter import *

root = Tk()
root.geometry('770x300') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#8a37cc') #background color

#-------------------------- Functions --------------------------#


#-------------------------- Home funcionario Frame 2 --------------------------#

fr2 = LabelFrame(root, text="Banco Dellux", bg="green").grid(row=0, column=0, pady=15)

# Infos

lb0_fr2 = Label(fr2, text="Bem vindo a home dos funcionarios", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=6, padx=200, sticky=EW)

lb1_fr2 = Label(fr2, text="BRENO KAUAN", font=("Mongolian Baiti", "17"), background="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, columnspan=6, sticky=EW, pady=10)
#lb1_fr2 o label acima se possivel é pra ser usado pra mostrar o nome do usuario registrado, ou sej aretirando o nome Breno Depois durante a finalização

lb2_fr2 = Label(fr2, text="Avisos:", font=("Mongolian Baiti", "14", "bold"),background="#8a37cc", fg="#f5f5f5").grid(row=3, column=0, columnspan=6,)

lb3_fr2 = Label(fr2, text="Nenhuma atualização relevante no sistema ", font=("Mongolian Baiti", "10"),background="#8a37cc", fg="#f5f5f5").grid(row=4, column=0, columnspan=6, sticky=EW, pady=10)

# Botões
bt0_fr2 = Button(fr2, text="Logout do sistema ", font=("Mongolian Baiti", "11", "bold"), height=2,width=24, bg="#eb8334", fg="#fff").grid(row=5, column=1, columnspan=2, sticky=EW, pady=30)

bt1_fr2 = Button(fr2, text="Cadastrar novo cliente", font=("Mongolian Baiti", "11", "bold"), height=2, bg="#eb8334", fg="#fff").grid(row=5, column=3, sticky=EW)

bt3_fr2 = Button(fr2, text="Verificar usuarios", font=("Mongolian Baiti", "11"," bold"), height=2, bg="#eb8334", fg="#fff").grid(row=5, column=4, sticky=EW)

#-------------------------- Mostrar tela --------------------------#

root.mainloop()