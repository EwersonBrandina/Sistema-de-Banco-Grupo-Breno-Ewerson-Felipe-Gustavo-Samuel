
from __future__ import nested_scopes
from tkinter import *
from tkinter import font
from tkinter.ttk import Style
from turtle import width
#MODELO CRIADO POR BRENO
root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
root.geometry('750x470') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#8a37cc') #background color
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
#Funções
#Deixar primeiras letras maiusculas
var =StringVar()
def caps(*args):
    var.set(var.get().title())
var.trace("w", caps)
#Tratar a Entrada de Valores em R$
def deposito(event=None):
    x = in0_fr4_1.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    in0_fr4_1.delete(0, 'end')
    in0_fr4_1.insert(0, y)
def saque(event=None):
    x = in0_fr4_2.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    in0_fr4_2.delete(0, 'end')
    in0_fr4_2.insert(0, y)
def transferencia(event=None):
    x = in0_fr4_3.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    in0_fr4_3.delete(0, 'end')
    in0_fr4_3.insert(0, y)
def extrato(event=None):
    x = in0_fr4_4.get().replace('/', '').replace('--','')[:12]
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1, 7]:
            y += x[i] + '/'
        elif i in [5]:
            y += x[i] + '--'
        else:
            y += x[i]
    in0_fr4_4.delete(0, 'end')
    in0_fr4_4.insert(0, y)
#Salvar os Usuários e Senhas de cada frame
def usuario_fr1(event=None):
    x_fr1 = in0_fr1.get()
    in0_fr1.delete(0, 'end')
    in0_fr1.insert(0, x_fr1)
    print(x_fr1)
def senha_fr1(event=None):
    y_fr1 = in1_fr1.get()
    in1_fr1.delete(0, 'end')
    in1_fr1.insert(0, y_fr1)
    print(y_fr1)
def senha_fr2_1(event=None):
    y_fr1_1 = in10_fr2.get()
    in10_fr2.delete(0, 'end')
    in10_fr2.insert(0, y_fr1_1)
    print(y_fr1_1)
def senha_fr2_2(event=None):
    y_fr2_2 = in1_fr2.get()
    in1_fr2.delete(0, 'end')
    in1_fr2.insert(0, y_fr2_2)
    print(y_fr2_2)
def senha_fr3(event=None):
    y_fr3 = in1_fr3.get()
    in1_fr3.delete(0, 'end')
    in1_fr3.insert(0, y_fr3)
    print(y_fr3)
def senha_fr4_1(event=None):
    y_fr4_1 = in1_fr4_1.get()
    in1_fr4_1.delete(0, 'end')
    in1_fr4_1.insert(0, y_fr4_1)
    print(y_fr4_1)
def senha_fr4_2(event=None):
    y_fr4_2 = in1_fr4_2.get()
    in1_fr4_2.delete(0, 'end')
    in1_fr4_2.insert(0, y_fr4_2)
    print(y_fr4_2)
def senha_fr4_3(event=None):
    y_fr4_3 = in1_fr4_3.get()
    in1_fr4_3.delete(0, 'end')
    in1_fr4_3.insert(0, y_fr4_3)
    print(y_fr4_3)
def senha_fr4_4(event=None):
    y_fr4_4 = in1_fr4_4.get()
    in1_fr4_4.delete(0, 'end')
    in1_fr4_4.insert(0, y_fr4_4)
    print(y_fr4_4)

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

#INÍCIO DO CÓDIGO
#Frame 0 - Gustavo

fr0 = LabelFrame (bg='#8a37cc')
lb0_fr0 = Label(fr0, text='Seja Muito Bem-Vindo', font = ("Mongolian Baiti", "32"),bg='#8a37cc', fg='#f5f5f5',).grid(row=0,column=0, sticky=W,padx=170,ipady=60)
lb1_fr0 = Label(fr0, text='Bem Vindo ao Dellux', font='Arial 26', bg='#8a37cc', fg='#f5f5f5').grid(row=1, column=0, sticky=W,ipadx=210)
bt0_fr0 = Button(fr0, text='Funcionário', font=('Mongolian Baiti' ,'26', "bold"), bg='#eb8334',fg='#fff', width=10, command= lambda: [fr0.grid_remove(), fr1.grid(row=0, column=0, sticky=NSEW)]).grid(row=2, column=0,columnspan=1, sticky=W, padx=165,pady=70)
bt1_fr0 = Button(fr0, text='Usuario', font= ('Mongolian Baiti' ,'26', "bold"),bg='#eb8334',fg='#fff',width=8, command= lambda: [fr0.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=2, column=0,columnspan=2,sticky=W, padx=415)
fr0.grid(row=0, column=0, sticky=NSEW)

#Frame 1 - Samuel
#criar janela

fr1 = LabelFrame(bg= '#8a37cc',pady=90)
#criar os widgets
lb0_fr1 = Label(fr1, text='Login do Funcionário', font= ('Mongolian Baiti', '32'),bg='#8a37cc',fg='#f5f5f5').grid(row=0,column=1,sticky=W,padx=180,pady=30)
lb1_fr1 = Label(fr1, text='Usuário:', font=('Mongolian Baiti', '22'),bg='#8a37cc',fg='#f5f5f5').grid(row=1, column=1,sticky=W, padx=45)
lb2_fr1 = Label(fr1, text='Senha:', font=('Mongolian Baiti', "22" ),bg='#8a37cc',fg='#f5f5f5',width=7).grid(row=2, column=1,sticky=W, padx=50)
#--Entrada ---
in0_fr1 = Entry(fr1, font= 'Arial 18', width=35)
in0_fr1.bind('<KeyRelease>', usuario_fr1)
in0_fr1.grid(row=1,column=1,sticky=W,padx=154)
in1_fr1 = Entry(fr1, font='Arial 18', width=35,show="*")
in1_fr1.bind('<KeyRelease>', senha_fr1)
in1_fr1.grid(row=2,column=1,sticky=W,padx=154)
#--Button ---
bt0_fr1 = Button(fr1,text='Entrar', font= ('Mongolian Baiti', "18", "bold") ,width=15,bg='#eb8334', fg='#fff', command= lambda: [in0_fr1.delete(0, 'end'), in1_fr1.delete(0, 'end'), fr1.grid_remove(), fr2.grid(row=0, column=0, pady=50)]).grid(row=4, column=1, sticky=W, padx=155)
bt1_fr1 = Button(fr1, text='Voltar', font=('Mongolian Baiti', "18", "bold"),width=16,bg='#eb8334', fg='#fff', command= lambda: [in0_fr1.delete(0, 'end'), in1_fr1.delete(0, 'end'), fr1.grid_remove(), fr0.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W,padx=380)
bt2_fr1 = Button(fr1, text='👁', font=('Mongolian Baiti', "18", "bold"),bg='#eb8334', fg='#fff').grid(row=2, column=1, padx=620)
#---Configuração do Frame---
#fr1.grid()

#Frame 2 - Breno

#-------------------------- Frame 2 --------------------------#

fr2 = LabelFrame(root, bg="#8a37cc")
# Infos
lb0_fr2 = Label(fr2, text="Bem Vindo a Home Dos Funcionarios", font=("Mongolian Baiti", "32"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=6, padx=50, sticky=W)
lb1_fr2 = Label(fr2, text="BRENO KAUAN", font=("Mongolian Baiti", "20"), background="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, columnspan=6, sticky=W, pady=10,padx=300)
#lb1_fr2 o label acima se possivel é pra ser usado pra mostrar o nome do usuario registrado, ou sej aretirando o nome Breno Depois durante a finalização
lb2_fr2 = Label(fr2, text="Avisos:", font=("Mongolian Baiti", "17", "bold"),background="#8a37cc", fg="#f5f5f5").grid(row=3, column=0,sticky=W,padx=350)
lb3_fr2 = Label(fr2, text="Nenhuma atualização relevante no sistema ", font=("Mongolian Baiti", "15"),background="#8a37cc", fg="#f5f5f5").grid(row=4, column=0, sticky=W,padx=220, pady=10)
# Botões
bt0_fr2 = Button(fr2, text="Logout", font=("Mongolian Baiti", "18", "bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda: [fr2.grid_remove(), fr1.grid(row=0, column=0)] ).grid(row=6, column=0,sticky=W,padx=250,pady=20)
bt1_fr2 = Button(fr2, text="Cadastrar novo cliente", font=("Mongolian Baiti", "18", "bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda:[fr2.grid_remove(), fr2_1.grid(row=0,column=0)] ).grid(row=5,column=0,sticky=W,padx=100)
bt3_fr2 = Button(fr2, text="Excluir usuarios", font=("Mongolian Baiti", "18"," bold"), height=2,width=20, bg="#eb8334", fg="#fff").grid(row=5, column=0,columnspan=2,sticky=W,padx=400)
#Frame fr2_1
fr2_1 = LabelFrame(root, bg="#8a37cc") #grid(row=0, column=0)
lb0_fr2_1 = Label(fr2_1, text="Faça aqui o cadastro de novos Clientes", font=("Mongolian Baiti", "20"),background="#8a37cc", fg="#f5f5f5").grid(row=0, column=0,sticky=W,pady=60,padx=165)
#Linha 1
lb1_fr2 = Label(fr2_1, text="Nome:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=1, column=0, sticky=W,padx=55)
in0_fr2 = Entry(fr2_1, font=('Arial 17'),width=47, bg="#f5f5f5").grid(row=1, column=0, columnspan=1, sticky=W,padx=122)
#Linha 2
lb2_fr2 = Label(fr2_1, text="CPF:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=2, column=0, sticky=W,padx=71)
in1_fr2 = Entry(fr2_1, font=('Arial 17'),width=19, bg='#f5f5f5').grid(row=2, column=0, sticky=W,padx=122)
lb3_fr2 = Label(fr2_1, text="Data Nasc:", font=("Mongolian Baiti", "16"),background="#8a37cc", fg="#f5f5f5" ).grid(row=2, column=0,sticky=W,padx=375)
in2_fr2 = Entry(fr2_1, font=('Arial 17'),width=20, bg='#f5f5f5', cursor="gobbler").grid(row=2, column=0, sticky=W,padx=473)
#Linha 3
lb4_fr2 = Label(fr2_1, text="Tel:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column=0, sticky=W,padx=82)
in3_fr2 = Entry(fr2_1, font=('Arial 17'),width=19, bg='#f5f5f5').grid(row=3, column=0, sticky=W,padx=122)
lb5_fr2 = Label(fr2_1, text="Logradouro:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=0, sticky=W,padx=0)
lb4_fr2 = Entry(fr2_1, font=('Arial 17'),width=19, bg='#f5f5f5').grid(row=4, column=0, sticky=W,padx=122)
lb6_fr2 = Label(fr2_1, text="N°:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=0,sticky=W,padx=435)
lb5_fr2 = Entry(fr2_1, font=('Arial 17'), bg='#f5f5f5').grid(row=4, column=0,sticky=W,padx=473)
#linha 5
lb7_fr2 = Label(fr2_1, text="Bairro:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=5, column=0, sticky=W,padx=53)
lb6_fr2 = Entry(fr2_1, font=('Arial 17'),width=19, bg='#f5f5f5').grid(row=5, column=0, sticky=W,padx=122)
lb8_fr2 = Label(fr2_1, text="Cidade:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=5, column=0,sticky=W,padx=395)
lb7_fr2 = Entry(fr2_1, font=('Arial 17'), bg='#f5f5f5').grid(row=5, column=0, sticky=W,padx=473)
lb9_fr2 = Label(fr2_1, text="UF:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column = 0,sticky=W,padx=431)
lb8_fr2 = Entry(fr2_1, font=('Arial 17'), bg='#f5f5f5').grid(row=3, column=0, sticky=W,padx=473)
lb10_fr2 = Label(fr2_1, text="Email:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=6, column=0, sticky=W,padx=58)
in9_fr2 = Entry(fr2_1, font=('Arial 17'),width=19, bg='#f5f5f5').grid(row=6, column=0, sticky=W,padx=122)
lb11_fr2 = Label(fr2_1, text="Senha:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=6, column=0,sticky=W,padx=403)
in10_fr2 = Entry(fr2_1, font=('Arial 17'), bg='#f5f5f5',show="*").grid(row=6, column=0, sticky=W,padx=473)
# Botões
bt0_fr2 = Button(fr2_1, text="Criar conta ", font=("Mongolian Baiti", "17", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[fr2_1.grid_remove(), fr2.grid(row=0, column=0)]).grid(row=8, column=0, sticky=W,pady=20,padx=119)
bt1_fr2 = Button(fr2_1, text="Voltar", font=("Mongolian Baiti", "17", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[fr2_1.grid_remove(), fr2.grid(row=0, column=0)]).grid(row=8, column=0, sticky=W,padx=455)
#bt2_fr2 = Button(fr2_1, text='👁', font=('Mongolian Baiti', "12", "bold"),bg='#eb8334', fg='#fff').grid(row=6, column=0, sticky=W,padx=712)
#grid(row=0, column=0, pady=50)
#Frame 2_2
fr2_2 = LabelFrame(root, bg="#8a37cc") #grid(row=0, column=0,pady=50, padx=150)
lb0_fr2_2 = Label(fr2_2, text="Faça aqui a exclusão de usuarios", font=("Mongolian Baiti", "23"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=5, sticky=E, pady=30)
lb1_fr2_2 = Label(fr2_2, text="Nome do usuario:", font=("Mongolian Baiti", "13"),background="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, sticky=E)
in0_fr2 = Entry(fr2_2, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff", width=30).grid(row=2, column=1, columnspan=2, sticky=EW)
lb2_fr2_2 = Label(fr2_2, text="Confirme sua senha:", font=("Mongolian Baiti", "13"),background="#8a37cc", fg="#f5f5f5").grid(row=3, column=0, sticky=E)
in1_fr2 = Entry(fr2_2, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff",show="*")
in1_fr2.bind('<KeyRelease>', senha_fr2_2)
in1_fr2.grid(row=3, column=1, columnspan=2, sticky=EW)
# Botões
bt0_fr2 = Button(fr2_2, text="Deletar conta ", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff", command= lambda:[fr2_2.grid_remove(), fr2.grid(row=0, column=0)]).grid(row=4, column=0,columnspan=2, sticky=W, pady=60, padx=190) #Pura Gambiarra e ta tudo bem
bt1_fr2 = Button(fr2_2, text="Voltar", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff", command= lambda:[fr2_2.grid_remove(), fr2.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W, padx=50)

#Frame 3 - Felipe
#criando janela
fr3 = LabelFrame(root, text='Login / Cadastro',font=('Mongolian Baiti', '17'), bg='#8a37cc',fg='#f5f5f5',pady=30)
fr3_1 = LabelFrame(root, text='Cadastro',font=('Mongolian Baiti', '17'), bg='#8a37cc',fg='#f5f5f5')
#criando widgets
#lb0_fr3 = Label(fr3, text='Bem Vindo ao Dellux', font='Arial 20', bg='#8a37cc', fg='#f5f5f5').grid(row=0, column=0, sticky=W)
#lb1_fr3 = Label(fr3, text='O que deseja fazer?', font='Arial 20', bg='#8a37cc', fg='#f5f5f5').grid(row=1, column=0, sticky=W)
lb2_fr3 = Label(fr3, text='Usuário:', font=('Mongolian Baiti', '23'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0, sticky=W,padx=128)
lb3_fr3 = Label(fr3, text='Senha:', font=('Mongolian Baiti', '23'), bg='#8a37cc', fg='#f5f5f5').grid(row=3, column=0, sticky=W,padx=149)
in0_fr3 = Entry(fr3,text='', font='Arial 20', bg='#fff').grid(row=2, column=0,sticky=W,padx=240)
in1_fr3 = Entry(fr3,text='', font='Arial 20', bg='#fff',show="*")
in1_fr3.bind('<KeyRelease>', senha_fr3)
in1_fr3.grid(row=3, column=0,sticky=W,padx=240,pady=10)
#widgets j2
lb4_fr3_1 = Label(fr3_1, text='Bem vindo a área de cadastro', font=('Mongolian Baiti', '22'), bg='#8a37cc', fg='#f5f5f5').grid(row=0, column=0,sticky=W, padx=193,pady=20)
lb5_fr3_1 = Label(fr3_1, text='Nome:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=1, column=0,sticky=W, padx=67)
lb6_fr3_1 = Label(fr3_1, text='Data de Nasc:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0,sticky=W)
lb7_fr3_1 = Label(fr3_1, text='CPF:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0,sticky=W, padx=441)
lb8_fr3_1 = Label(fr3_1, text='Telefone:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=3, column=0,sticky=W, padx=400)
lb9_fr3_1 = Label(fr3_1, text='Endereço:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=3, column=0,sticky=W,padx=35)
lb10_fr3_1 = Label(fr3_1, text='Cidade:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=4, column=0,sticky=W,padx=58)
lb11_fr3_1 = Label(fr3_1, text='UF:',font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=4, column=0,sticky=W, padx=453)
lb12_fr3_1 = Label(fr3_1, text='N°:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=5, column=0,sticky=W, padx=457)
lb13_fr3_1 = Label(fr3_1, text='Email:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=5, column=0,sticky=W,padx=68)
in2_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),width=50, bg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=132)
in3_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),width=22, bg='#f5f5f5').grid(row=2, column=0, sticky=W,padx=132)
in4_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), bg='#f5f5f5').grid(row=2, column=0, sticky=W,padx=492)
in5_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), bg='#f5f5f5').grid(row=3, column=0, sticky=W,padx=492)
in6_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),width=22, bg='#f5f5f5').grid(row=3, column=0, sticky=W,padx=132)
in7_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),width=22,bg='#f5f5f5').grid(row=4, column=0, sticky=W,padx=132)
in8_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), bg='#f5f5f5').grid(row=4, column=0, sticky=W,padx=492)
in9_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), bg='#f5f5f5').grid(row=5, column=0, sticky=W,padx=492)
in10_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),width=22, bg='#f5f5f5').grid(row=5, column=0, sticky=W,padx=132)
#botões
bt0_fr3 = Button(fr3, text='Login', font = ('Mongolian Baiti', '20', 'bold' ) , bg='#eb8334', fg='#f5f5f5',width=13, command= lambda:[fr3.grid_remove(), fr4.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=30,pady=10)
bt1_fr3 = Button(fr3, text='Cadastrar', font = ('Mongolian Baiti', "20", 'bold' ) , bg='#eb8334', fg='#f5f5f5',width=13, command= lambda:[fr3.grid_remove(), fr3_1.grid(row=0, column=0)] ).grid(row=4, column=0, sticky=W,padx=265)
bt2_fr3 = Button(fr3, text='Voltar', font = ('Mongolian Baiti', "20", 'bold') , bg='#eb8334', fg='#f5f5f5',width=13 , command= lambda:[fr3.grid_remove(), fr0.grid(row=0, column=0)]).grid(row=4, column=0, sticky=E,padx=50)
#bt5_fr3 = Button(fr3, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff').grid(row=3, column=0, sticky=E,padx=180,pady=7)
bt3_fr3_1 = Button(fr3_1, text='Salvar', font = ('Mongolian Baiti', '19', 'bold' ), width= 18, bg='#eb8334', fg='#f5f5f5', command= lambda:[fr3_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=6, column=0,sticky=W,padx=130,pady=15)
bt4_fr3_1 = Button(fr3_1, text='Voltar', font = ('Mongolian Baiti', '19', 'bold' ), width=18, bg='#eb8334', fg='#f5f5f5', command= lambda:[fr3_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=6, column=0, sticky=W,padx=460) 
#frames
#fr3.grid()
#fr3_1.grid(padx=5)

#Frame 4 - Ewerson
fr4 = LabelFrame(root, padx=10, pady=5, bg='#8a37cc', text='Usuário', font='Arial 25',fg='#f5f5f5', borderwidth=1, relief="sunken", width=5)
lb0_fr4 = Label(fr4, text='Ewerson Ribeiro Brandina', font='Arial 20',padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5').grid(row=0, column=0 , sticky=W)
lb0_1_fr4 = Label(fr4, text='Número da Conta', font='Arial 20',padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5').grid(row=0, column=2)
lb1_fr4 = Label(fr4, text='R$ 0.0', font='Arial 20',padx=5, pady=10, bg='#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W)
bt2_fr4 = Button(fr4, text='Depósito', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [fr4.grid_remove(), fr4_1.grid(row=0, column=1)]).grid(row=2, column=0, sticky=W,pady=5)
bt3_fr4 = Button(fr4, text='Saque', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [fr4.grid_remove(), fr4_2.grid(row=0, column=1)]).grid(row=3, column=0, sticky=W,pady=5)
bt4_fr4 = Button(fr4, text='Transferência', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [fr4.grid_remove(), fr4_3.grid(row=0, column=1)]).grid(row=4, column=0, sticky=W,pady=5)
bt5_fr4 = Button(fr4, text='Extrato', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [fr4.grid_remove(), fr4_4.grid(row=0, column=1)]).grid(row=5, column=0, sticky=W,pady=5)
bt6_fr4 = Button(fr4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=14, command= lambda:[fr4.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=7, column=2, sticky=E)
#fr4.grid(row=0, column=0, sticky=NSEW)
#Frame 4_1 - Ewerson
fr4_1 = LabelFrame(root, pady=5, bg= '#8a37cc', text='Depósito',fg='#f5f5f5', font=('Mongolian Baiti', "19" ), borderwidth=1, relief="sunken",width=150)
lb0_fr4_1 = Label(fr4_1, text='Valor a Ser Depositado:',bg='#8a37cc',fg='#f5f5f5', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0).grid(row=0, column=0 , sticky=W,padx=25)
in0_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#f5f5f5')
in0_fr4_1.bind("<KeyRelease>", deposito)
in0_fr4_1.grid(row=0, column=0,sticky=W,padx=280)
lb1_fr4_1 = Label(fr4_1, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=203)
in1_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#f5f5f5',show="*")
in1_fr4_1.bind('<KeyRelease>', senha_fr4_1)
in1_fr4_1.grid(row=1, column=0,sticky=W,padx=280)
bt2_fr4_1 = Button(fr4_1, text='Confirmar', font=('Mongolian Baiti', '19', 'bold'),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=19).grid(row=2, column=0, sticky=W,padx=282,pady=5)
lb3_fr4_1 = Label(fr4_1, text='Mensagem de Confirmação', fg='#f5f5f5',font=('Mongolian Baiti', "17" ),padx=5, pady=0, bg= '#8a37cc',width=38).grid(row=3, column=0, columnspan=3, sticky=W,padx=175)
bt4_fr4_1 = Button(fr4_1, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=15, command= lambda: [fr4_1.grid_remove(), fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=W,padx=190,pady=5)
bt4_1_fr4_1 = Button(fr4_1, text='Logout', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda:[fr4_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=450)
#bt5_fr4_1 = Button(fr4_1, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff').grid(row=1, column=0, sticky=W,padx=588,pady=5)
#fr4_1.grid()
#Frame 4_2 - Ewerson
fr4_2 = LabelFrame(root, pady=5, bg= '#8a37cc',fg='#f5f5f5', text='Saque', font=('Mongolian Baiti', "22" ), borderwidth=1, relief="sunken", width=150)
lb0_fr4_2 = Label(fr4_2, text='Valor a Ser Sacado:', font=('Mongolian Baiti', "17", "bold" ),padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5').grid(row=0, column=0 , sticky=W,padx=67)
in0_fr4_2 = Entry(fr4_2,font='Arial 20', bg='#f5f5f5')
in0_fr4_2.bind('<KeyRelease>', saque)
in0_fr4_2.grid(row=0, column=0,sticky=W,padx=280)
lb1_fr4_2 = Label(fr4_2, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=203)
in1_fr4_2 = Entry(fr4_2, font='Arial 20', bg='#f5f5f5',show="*")
in1_fr4_2.bind('<KeyRelease>', senha_fr4_2)
in1_fr4_2.grid(row=1, column=0,sticky=W,padx=280)
bt2_fr4_2 = Button(fr4_2, text='Confirmar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=19).grid(row=2, column=0, sticky=W,padx=282,pady=5)
lb3_fr4_2 = Label(fr4_2, text='Mensagem de Confirmação', font=('Mongolian Baiti', "17" ),padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5',width=31).grid(row=3, column=0, columnspan=3, sticky=W,padx=220)
bt4_fr4_2 = Button(fr4_2, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=15, command= lambda: [fr4_2.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=W,padx=190,pady=5)
bt4_1_fr4_2 = Button(fr4_2, text='Logout', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=15, command= lambda:[fr4_2.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=450)
#bt5_fr4_2 = Button(fr4_2, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff').grid(row=1, column=0, sticky=W,padx=588,pady=5)
#fr4_2.grid()
#Frame 4_3 - Ewerson
fr4_3 = LabelFrame(root, pady=5, bg= '#8a37cc',fg='#f5f5f5', text='Transferência', font=('Mongolian Baiti', "22" ), borderwidth=1, relief="sunken", width=150)
lb0_fr4_3 = Label(fr4_3, text='Valor a Ser Transferido:',padx=5, pady=0, font=('Mongolian Baiti', "17", "bold" ),bg='#8a37cc',fg='#f5f5f5').grid(row=0, column=0 , sticky=W,padx=21)
in0_fr4_3 = Entry(fr4_3,font='Arial 20', bg='#f5f5f5')
in0_fr4_3.bind('<KeyRelease>', transferencia)
in0_fr4_3.grid(row=0, column=0, sticky=W,padx=280)
lb1_fr4_3 = Label(fr4_3, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=203)
in1_fr4_3 = Entry(fr4_3, font='Arial 20', bg='#f5f5f5',show="*")
in1_fr4_3.bind('<KeyRelease>', senha_fr4_3)
in1_fr4_3.grid(row=1, column=0, sticky=W,padx=280)
bt2_fr4_3 = Button(fr4_3, text='Confirmar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=19).grid(row=2, column=0, sticky=W, padx=282,pady=5)
lb3_fr4_3 = Label(fr4_3, text='Mensagem de Confirmação', font=('Mongolian Baiti', "17" ),padx=5, pady=0,  bg= '#8a37cc',fg='#f5f5f5',width=31).grid(row=3, column=0, columnspan=3, sticky=W,padx=220)
bt4_fr4_3 = Button(fr4_3, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0,  bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda: [fr4_3.grid_remove(), fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=W,padx=190,pady=5)
bt4_1_fr4_3 = Button(fr4_3, text='Logout', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda:[fr4_3.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=450)
#bt5_fr4_3 = Button(fr4_3, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff').grid(row=1, column=0, sticky=W,padx=588,pady=5)
#fr4_3.grid()
#Frame 4_4 - Ewerson
fr4_4 = LabelFrame(root, pady=5, bg= '#8a37cc',fg='#f5f5f5', text='Extrato', font=('Mongolian Baiti', "22" ), borderwidth=1, relief="sunken", width=150)
lb0_fr4_4 = Label(fr4_4, text='Periodo:', font=('Mongolian Baiti', "17", "bold" ),bg='#8a37cc',fg='#f5f5f5',padx=5, pady=0).grid(row=0, column=0 , sticky=W,padx=185)
in0_fr4_4 = Entry(fr4_4,font='Arial 20', bg='#f5f5f5')
in0_fr4_4.bind('<KeyRelease>', extrato)
in0_fr4_4.grid(row=0, column=0, sticky=W,padx=280)
in0_fr4_4.insert(0, 'MM/AA')
lb1_fr4_4 = Label(fr4_4, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=203)
in1_fr4_4 = Entry(fr4_4, font='Arial 20', bg='#f5f5f5',show="*")
in1_fr4_4.bind('<KeyRelease>', senha_fr4_4)
in1_fr4_4.grid(row=1, column=0,sticky=W,padx=280)
bt2_fr4_4 = Button(fr4_4, text='Confirmar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=19).grid(row=2, column=0, sticky=W, padx=282,pady=5)
lb3_fr4_4 = Label(fr4_4, text='Mensagem de Confirmação',  font=('Mongolian Baiti', "17" ),padx=5, pady=0,  bg= '#8a37cc',fg='#f5f5f5',width=31).grid(row=3, column=0, columnspan=3, sticky=W,padx=220)
bt4_fr4_4 = Button(fr4_4, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0,  bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda: [fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=W,padx=190,pady=5)
bt4_1_fr4_4 = Button(fr4_4, text='Logout', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda:[fr4_4.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=450)
bt5_fr4_4 = Button(fr4_4, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff').grid(row=1, column=0, sticky=W,padx=588,pady=5)
#fr4_4.grid()

#Looping para tudo
root.mainloop()