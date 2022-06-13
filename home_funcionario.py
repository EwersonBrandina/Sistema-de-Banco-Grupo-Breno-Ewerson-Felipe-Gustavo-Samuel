from tkinter import *

#config tela
root = Tk()
root.geometry('400x300+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#fff') #background color

#-------------------------- Functions --------------------------#

#Aqui ficaram as funções do projeto

#-------------------------- Frame 2 / Widgets --------------------------#

fr2 = LabelFrame(root, background='#fff', text='Cadastro de fúncionarios', fg="gray", font='Georgia 15')

lb0_fr2 = Label(fr2, text="Insira a seguir todos os dados requisitados para cadastro", font='Georgia 10')

#nome
lb1_fr2 = Label(fr2, text="Nome:", font='Georgia 15')
in0_frX = Entry(fr2, font='Georgia 15')

#cpf
lb2_fr2 = Label(fr2, text="CPF:")
in1_frX = Entry(fr2, font='Georgia 15')

#telefoneu
lb3_fr2 = Label(fr2, text="Telefone:")
in2_frX = Entry(fr2, font='Georgia 15')

#data de nascimento
lb4_fr2 = Label(fr2, text="Data de Nasc:")
in3_frX = Entry(fr2, font='Georgia 15')

#endereço 
lb5_fr2 = Label(fr2, text="Endereço:")
in4_frX = Entry(fr2, font='Georgia 15')

#cidade
lb6_fr2 = Label(fr2, text="Cidade:")
in5_frX = Entry(fr2, font='Georgia 15')

#numero da casa
lb7_fr2 = Label(fr2, text="N°:")
in6_frX = Entry(fr2, font='Georgia 15')

#Conclusão do formulario
bt0_frX = Button(fr2, text="Salvar dados", font='Georgia 15')
bt1_frX = Button(fr2, text="Voltar", font='Georgia 15')

#-------------------------- Frame 2 / Apresentar --------------------------#

fr2.grid()

#Linha 0 
lb0_fr2.grid(row=0, column=0)

#linha 1 
lb1_fr2.grid()
lb2_fr2.grid()
lb3_fr2.grid()
lb4_fr2.grid()
lb5_fr2.grid()
lb6_fr2.grid()
lb7_fr2.grid()

#-------------------------- Mostrar tela --------------------------#

root.mainloop()