from tkinter import *

#config tela
root = Tk()
root.geometry('400x300+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#fff') #background color

#-------------------------- Functions --------------------------#

#Aqui ficaram as funções do projeto

#-------------------------- Frame 0 / Widgets --------------------------#

frX = LabelFrame(root, background='#fff', text='text', fg="gray", font='Georgia 15')
#X é o numero a ser substiuido pelo numero da sua flame
lb0_frX = Label(frX, text="text", font='Georgia 15')
#Label padronizado
bt0_frX = Button(frX, text="text", font='Georgia 15')
#Botão padronizado
in0_frX = Entry(frX, font='Georgia 15')
#Entrada de dados (input) padronizado

#-------------------------- Frame 1 / Apresentar --------------------------#

frX.grid()
#grid / para mostrar o flame
lb0_frX.grid()
#grid / para mostrar o Label
in0_frX.grid()
#grid / para mostrar a entrada de dados

#-------------------------- Mostrar tela --------------------------#

root.mainloop()