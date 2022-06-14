from tkinter import *
#MODELO CRIADO POR BRENO
root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
#root.geometry('%dx%d+0+0' % (largura, altura)) # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#fff') #background color
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1, pad=3)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
#NSEW
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
fr1 = Frame(root, bg='green')
lb0_fr1 = Label(fr1, text='Login do Funcionario', font='Arial 22',bg='green')
lb1_fr1 = Label(fr1, text='Usuario:', font="Arial 20",bg='green')
lb2_fr1 = Label(fr1, text='Senha:', font="Arial 20",bg='green')
#--Entrada ---
int0_fr1 = Entry(fr1, font='Arial 18', width=35)
int1_fr1 = Entry(fr1, font='Arial 18', width=35)
#--Button ---
tb0_fr1 = Button(fr1,text='Entrar', font="Arial 20",width=15,bg='black', fg='white')
tb1_fr1 = Button(fr1, text='Voltar', font="Arial 20",width=15,bg='black', fg='white')
#---Configuração do Frame---
fr1.grid()
#organizar os widgets
#---Frame 1---w
lb0_fr1.grid(row=0,column=1,sticky=W,padx=150)
lb1_fr1.grid(row=1, column=1,sticky=W, padx=5)
lb2_fr1.grid(row=2, column=1,sticky=W, padx=5)
#--Entrada --
int0_fr1.grid(row=1,column=1,sticky=W,padx=110)
int1_fr1.grid(row=2,column=1,sticky=W,padx=110)
#---Butoon Função---
tb0_fr1.grid(row=4, column=1, sticky=W, padx=55)
tb1_fr1.grid(row=4, column=1, sticky=E,padx=110)
#executar a janel4

#Frame 2 - Breno

#Frame 3 - Felipe

#Frame 4 - Ewerson
fr4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Usuário', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4 = Label(fr4, text='Ewerson Ribeiro Brandina', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4 = Label(fr4, text='Número da Conta', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=2)
lb1_fr4 = Label(fr4, text='R$ 0.0', font='Arial 20',padx=5, pady=10, bg='#49A').grid(row=1, column=0, sticky=W)
bt2_fr4 = Button(fr4, text='Depósito', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_1.grid(row=0, column=1)]).grid(row=2, column=0, sticky=W)
bt3_fr4 = Button(fr4, text='Saque', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_2.grid(row=0, column=1)]).grid(row=3, column=0, sticky=W)
bt4_fr4 = Button(fr4, text='Transferência', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_3.grid(row=0, column=1)]).grid(row=4, column=0, sticky=W)
bt5_fr4 = Button(fr4, text='Extrato', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_4.grid(row=0, column=1)]).grid(row=4, column=0, sticky=W)
bt6_fr4 = Button(fr4, text='Pix', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=6, column=0, sticky=W)
bt7_fr4 = Button(fr4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=14).grid(row=7, column=2, sticky=E)
fr4.grid()
#Frame 4_1 - Ewerson
fr4_1 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Depósito', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_1 = Label(fr4_1, text='Valor a Ser Depositado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_1 = Entry(fr4_1,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_1 = Button(fr4_1, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_1 = Label(fr4_1, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=38).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_1 = Button(fr4_1, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=1)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_1 = Button(fr4_1, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_1.grid()
#Frame 4_2 - Ewerson
fr4_2 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Saque', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_2 = Label(fr4_2, text='Valor a Ser Sacado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_2 = Entry(fr4_2,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_2 = Entry(fr4_2, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_2 = Button(fr4_2, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_2 = Label(fr4_2, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_2 = Button(fr4_2, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=0, sticky=E)
bt4_1_fr4_2 = Button(fr4_2, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_2.grid()
#Frame 4_3 - Ewerson
fr4_3 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Transferência', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_3 = Label(fr4_3, text='Valor a Ser Transferido', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_3 = Entry(fr4_3,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_3 = Entry(fr4_3, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_3 = Button(fr4_3, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_3 = Label(fr4_3, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_3 = Button(fr4_3, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=0, sticky=E)
bt4_1_fr4_3 = Button(fr4_3, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_3.grid()
#Frame 4_4 - Ewerson
fr4_4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Extrato', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_4 = Label(fr4_4, text='PERIODO', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_4 = Entry(fr4_4,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_4 = Entry(fr4_4, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_4 = Button(fr4_4, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_4 = Label(fr4_4, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=27).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_4 = Button(fr4_4, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=0, sticky=E)
bt4_1_fr4_4 = Button(fr4_4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_3.grid()















#Looping para tudo
root.mainloop()
