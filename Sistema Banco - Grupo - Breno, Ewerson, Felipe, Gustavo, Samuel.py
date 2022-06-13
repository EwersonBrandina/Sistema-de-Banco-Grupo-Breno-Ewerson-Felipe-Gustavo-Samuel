from tkinter import *
#MODELO CRIADO POR BRENO
root = Tk()
root.geometry('400x300+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
root.config(background='#fff') #background color

#-------------------------- Functions --------------------------#

#Aqui ficaram as funções do projeto

#-------------------------- Frame 0 / Widgets --------------------------#

#frX = LabelFrame(root, background='#fff', text='text', fg="gray", font='Georgia 15')
# X é o numero a ser substiuido pelo numero da sua flame

#lb0_frX = Label(frX, text="text", font='Georgia 15')
#Label padronizado
#bt0_frX = Button(frX, text="text", font='Georgia 15')
#Botão padronizado
#in0_frX = Entry(frX, font='Georgia 15')
#Entrada de dados (input) padronizado

#-------------------------- Frame 1 / Apresentar --------------------------#

#frX.grid()
#grid / para mostrar o flame
#lb0_frX.grid()
#grid / para mostrar o Label
#in0_frX.grid()
#grid / para mostrar a entrada de dados

#-------------------------- Mostrar tela --------------------------#

#root.mainloop()

#INÍCIO DO CÓDIGO
#Frame 0 - Gustavo

#Frame 1 - Samuel
fr1 = Frame(root)

lb0_fr1 = Label(fr1, text='Usuario:', font="Arial 20")
lb1_fr1 = Label(fr1, text='Senha:', font="Arial 20")

fr1.grid()

lb0_fr1.grid(row=0, column=2,sticky=W, padx=5)
lb1_fr1.grid(row=1, column=2,sticky=W, padx=5)
#Frame 2 - Breno

#Frame 3 - Felipe

#Frame 4 - Ewerson

fr4 = LabelFrame(root, padx=10, pady=10, bg='#49A', text='Usuário', font='Arial 25', borderwidth=1, relief="sunken")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

lb0_fr4 = Label(fr4, text='Início', font='Arial 20')
lb0_fr4.grid(row=0, column=0)

fr4.grid()

root.mainloop()