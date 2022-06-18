from tkinter import *
from classe_cliente import *
from classe_conta import *
#MODELO CRIADO POR BRENO
root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
root.geometry('750x470') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#8a37cc') #background color
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
#Funções

#Deixar primeiras letras maiusculas - Cadastro Funcionário - in0_fr2
var =StringVar()
def caps(*args):
    var.set(var.get().title())
var.trace("w", caps)

#Deixar primeiras letras maiusculas - Cadastro Usuário - lb7_fr2
var1 =StringVar()
def caps_1(*args):
    var1.set(var1.get().title())
var1.trace("w", caps_1)

#Deixar todas as letras maiusculas - lb8_fr2
var2 =StringVar()
def maiusculo(*args):
    var2.set(var2.get().upper())
var2.trace("w", maiusculo)

#Deixar primeiras letras maiusculas - Cadastro Usuário - lb6_fr2
var3 =StringVar()
def caps_2(*args):
    var3.set(var3.get().title())
var3.trace("w", caps_2)

#Deixar primeiras letras maiusculas - Cadastro Usuário - lb4_fr2
var4 =StringVar()
def caps_3(*args):
    var4.set(var4.get().title())
var4.trace("w", caps_3)

#Deixar primeiras letras maiusculas - Cadastro Usuário - in7_fr3_1
var5 =StringVar()
def caps_4(*args):
    var5.set(var5.get().title())
var5.trace("w", caps_4)

#Deixar todas as letras maiusculas - Cadastro Usuário - in8_fr3_1
var6 =StringVar()
def caps_5(*args):
    var6.set(var6.get().upper())
var6.trace("w", caps_5)

#Deixar as primeiras letras maiusculas - Cadastro Usuário -
var7 =StringVar()
def caps_6(*args):
    var7.set(var7.get().title())
var7.trace("w", caps_6)

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
#CADASTRO FEITO PELO FUNCIONÁRIO
def cpf_funcionario(event=None):
    x=in1_fr2.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    in1_fr2.delete(0, 'end')
    in1_fr2.insert(0, y)
def telefone_funcionario(event=None):
    x=in3_fr2.get().replace('(','').replace(')', '').replace('-', '')[:12]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [0]:
            y+= '(' + x[i]
        elif i in [2]:
            y+= x[i] + ')'
        elif i in [3, 7]:
            y+= x[i] + '-'
        else:
            y+=x[i]
    in3_fr2.delete(0, 'end')
    in3_fr2.insert(0, y)
def data_nasc(event=None):
    x=in2_fr2.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    in2_fr2.delete(0, 'end')
    in2_fr2.insert(0, y)
def dois_digitos_funcionario(event=None):
    x=lb8_fr2.get()[:2]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789':
            y+=x[i]
    lb8_fr2.delete(0, 'end')
    lb8_fr2.insert(0, y)
def numeros_funcionario(event=None):
    x=lb5_fr2.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y+=x[i]
    lb5_fr2.delete(0, 'end')
    lb5_fr2.insert(0, y)

#CADASTRO FEITO PELO USUÁRIO
def cpf_cliente(event=None):
    x=in4_fr3_1.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    in4_fr3_1.delete(0, 'end')
    in4_fr3_1.insert(0, y)
def data_nasc1(event=None):
    x=in3_fr3_1.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    in3_fr3_1.delete(0, 'end')
    in3_fr3_1.insert(0, y)
def telefone_cliente(event=None):
    x=in5_fr3_1.get().replace('(','').replace(')', '').replace('-', '')[:12]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [0]:
            y+= '(' + x[i]
        elif i in [2]:
            y+= x[i] + ')'
        elif i in [3, 7]:
            y+= x[i] + '-'
        else:
            y+=x[i]
    in5_fr3_1.delete(0, 'end')
    in5_fr3_1.insert(0, y)
def dois_digitos_cliente(event=None):
    x=in8_fr3_1.get()[:2]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789':
            y+=x[i]
    in8_fr3_1.delete(0, 'end')
    in8_fr3_1.insert(0, y)
def numeros_cliente(event=None):
    x=in9_fr3_1.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y+=x[i]
    in9_fr3_1.delete(0, 'end')
    in9_fr3_1.insert(0, y)
#Front & Back
def cadastrar_funcionario():
    p1 = Cliente(nome=in0_fr2.get(), cpf=in1_fr2.get(), dataNasc=in2_fr2.get())#, telefone=in3_fr2.get()), uf=lb8_fr2.get(), logradouro=lb4_fr2.get(), numero=lb5_fr2.get(), bairro=lb6_fr2.get(), cidade=lb7_fr2.get(), email=in9_fr2.get(), senha=in10_fr2.get())
    c1 = Conta(p1, num='123-4')
    c1.extrato()
def cadastrar_cliente():
    p1 = Cliente(nome=in2_fr3_1.get(), cpf=in4_fr3_1.get(), dataNasc=in3_fr3_1.get())
    c1 = Conta(p1, num='432-1')
    c1.extrato()



#Salvar os Usuários e Senhas de cada frame

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
lb0_fr0 = Label(fr0, text='Seja Muito Bem-Vindo', font = ("Mongolian Baiti", "32"),bg='#8a37cc', fg='#f5f5f5',).grid(row=0,column=0,columnspan=3, sticky=W,padx=165,ipady=120)
bt0_fr0 = Button(fr0, text='Funcionário', font=('Mongolian Baiti' ,'26', "bold"), bg='#eb8334',fg='#fff', width=10, command= lambda: [fr0.grid_remove(), fr1.grid(row=0, column=0, sticky=NSEW)]).grid(row=1, column=0,columnspan=1, sticky=W, padx=150)
bt1_fr0 = Button(fr0, text='Usuario', font= ('Mongolian Baiti' ,'26', "bold"),bg='#eb8334',fg='#fff',width=8, command= lambda: [fr0.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=1, column=0,columnspan=2,sticky=W, padx=400)
fr0.grid(row=0, column=0, sticky=NSEW)

#Frame 1 - Samuel
#criar janela

fr1 = LabelFrame(bg= '#8a37cc',pady=90)
#criar os widgets
lb0_fr1 = Label(fr1, text='Login do Funcionário', font= ('Mongolian Baiti', '32'),bg='#8a37cc',fg='#f5f5f5').grid(row=0,column=1,sticky=W,padx=180,pady=30)
lb1_fr1 = Label(fr1, text='Usuário:', font=('Mongolian Baiti', '22'),bg='#8a37cc',fg='#f5f5f5').grid(row=1, column=1,sticky=W, padx=45)
lb2_fr1 = Label(fr1, text='Senha:', font=('Mongolian Baiti', "22" ),bg='#8a37cc',fg='#f5f5f5',width=7).grid(row=2, column=1,sticky=W, padx=50)
#--Entrada ---
in0_fr1 = Entry(fr1, font='Arial 18', width=35)
in0_fr1.grid(row=1,column=1,sticky=W,padx=154)
in1_fr1 = Entry(fr1, font='Arial 18', width=35,show="*")
in1_fr1.grid(row=2,column=1,sticky=W,padx=154)
#--Button ---
bt0_fr1 = Button(fr1,text='Entrar', font= ('Mongolian Baiti', "18", "bold") ,width=15,bg='#eb8334', fg='#fff',command= lambda: [in0_fr1.delete(0, 'end'), in1_fr1.delete(0, 'end'), fr1.grid_remove(), fr2.grid(row=0, column=0, pady=50)]).grid(row=4, column=1, sticky=W, padx=155)
bt1_fr1 = Button(fr1, text='Voltar', font=('Mongolian Baiti', "18", "bold"),width=16,bg='#eb8334', fg='#fff', command= lambda: [in0_fr1.delete(0, 'end'), in1_fr1.delete(0, 'end'), fr1.grid_remove(), fr0.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W,padx=380)
bt2_fr1 = Button(fr1, text='👁', font=('Mongolian Baiti', "18", "bold"),bg='#eb8334', fg='#fff').grid(row=2, column=1, padx=620)
#---Configuração do Frame---
#fr1.grid()

#Frame 2 - Breno

#-------------------------- Frame 2 --------------------------#

fr2 = LabelFrame(root, bg="#8a37cc")
#Infos
lb0_fr2 = Label(fr2, text="Bem Vindo a Home Dos Funcionarios", font=("Mongolian Baiti", "32"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=6, padx=50, sticky=W)
lb1_fr2 = Label(fr2, text="BRENO KAUAN", font=("Mongolian Baiti", "20"), background="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, columnspan=6, sticky=W, pady=10,padx=300)
#lb1_fr2 o label acima se possivel é pra ser usado pra mostrar o nome do usuario registrado, ou sej aretirando o nome Breno Depois durante a finalização
lb2_fr2 = Label(fr2, text="Avisos:", font=("Mongolian Baiti", "17", "bold"),background="#8a37cc", fg="#f5f5f5").grid(row=3, column=0,sticky=W,padx=350)
lb3_fr2 = Label(fr2, text="Nenhuma atualização relevante no sistema ", font=("Mongolian Baiti", "15"),background="#8a37cc", fg="#f5f5f5").grid(row=4, column=0, sticky=W,padx=220, pady=10)
#Botões
bt0_fr2 = Button(fr2, text="Logout", font=("Mongolian Baiti", "18", "bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda: [fr2.grid_remove(), fr1.grid(row=0, column=0)] ).grid(row=6, column=0,sticky=W,padx=250,pady=20)
bt1_fr2 = Button(fr2, text="Cadastrar novo cliente", font=("Mongolian Baiti", "18", "bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda:[fr2.grid_remove(), fr2_1.grid(row=0,column=0)] ).grid(row=5,column=0,sticky=W,padx=100)
bt3_fr2 = Button(fr2, text="Excluir usuarios", font=("Mongolian Baiti", "18"," bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda:[fr2.grid_remove(), fr2_2.grid(row=0,column=0)]).grid(row=5, column=0,columnspan=2,sticky=W,padx=400)
#Frame fr2_1
fr2_1 = LabelFrame(root, bg="#8a37cc") #grid(row=0, column=0)
lb0_fr2_1 = Label(fr2_1, text="Faça aqui o cadastro de novos Clientes", font=("Mongolian Baiti", "20"),background="#8a37cc", fg="#f5f5f5").grid(row=0, column=0,sticky=W,pady=60,padx=165)
#Linha 1
lb1_fr2 = Label(fr2_1, text="Nome:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=1, column=0, sticky=W,padx=55)
in0_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), textvariable=var,width=49, bg="#eb8334", fg="#fff")
in0_fr2.grid(row=1, column=0, columnspan=1, sticky=W,padx=122)
#Linha 2
lb2_fr2 = Label(fr2_1, text="CPF:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=2, column=0, sticky=W,padx=71)
in1_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), bg="#eb8334", fg="#fff")
in1_fr2.bind('<KeyRelease>', cpf_funcionario)
in1_fr2.grid(row=2, column=0, sticky=W,padx=122)
lb3_fr2 = Label(fr2_1, text="Data Nasc:", font=("Mongolian Baiti", "16"),background="#8a37cc", fg="#f5f5f5" )
lb3_fr2.grid(row=2, column=0,sticky=W,padx=375)
in2_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"),width=20, bg="#eb8334", fg="#fff", cursor="gobbler")
in2_fr2.bind('<KeyRelease>', data_nasc)
in2_fr2.grid(row=2, column=0, sticky=W,padx=470)
#Linha 3
lb4_fr2 = Label(fr2_1, text="Tel:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column=0, sticky=W,padx=82)
in3_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), bg="#eb8334", fg="#fff")
in3_fr2.bind('<KeyRelease>', telefone_funcionario)
in3_fr2.grid(row=3, column=0, sticky=W,padx=122)
lb5_fr2 = Label(fr2_1, text="Logradouro:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=0, sticky=W,padx=0)
lb4_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"),textvariable=var4, bg="#eb8334", fg="#fff")
lb4_fr2.grid(row=4, column=0, sticky=W,padx=122)
lb6_fr2 = Label(fr2_1, text="N°:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=0,sticky=W,padx=435)
lb5_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), bg="#eb8334", fg="#fff")
lb5_fr2.bind('<KeyRelease>', numeros_funcionario)
lb5_fr2.grid(row=4, column=0,sticky=W,padx=470)
#linha 5
lb7_fr2 = Label(fr2_1, text="Bairro:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=5, column=0, sticky=W,padx=53)
lb6_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), textvariable=var3, bg="#eb8334", fg="#fff")
lb6_fr2.grid(row=5, column=0, sticky=W,padx=122)
lb8_fr2 = Label(fr2_1, text="Cidade:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=5, column=0,sticky=W,padx=395)
lb7_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), textvariable=var1, bg="#eb8334", fg="#fff")
lb7_fr2.grid(row=5, column=0, sticky=W,padx=470)
lb9_fr2 = Label(fr2_1, text="UF:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column = 0,sticky=W,padx=431)
lb8_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), textvariable=var2, bg="#eb8334", fg="#fff")
lb8_fr2.bind('<KeyRelease>', dois_digitos_funcionario)
lb8_fr2.grid(row=3, column=0, sticky=W,padx=470)
lb10_fr2 = Label(fr2_1, text="Email:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=6, column=0, sticky=W,padx=58)
in9_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), bg="#eb8334", fg="#fff")
in9_fr2.grid(row=6, column=0, sticky=W,padx=122)
lb11_fr2 = Label(fr2_1, text="Senha:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=6, column=0,sticky=W,padx=403)
in10_fr2 = Entry(fr2_1, font=("Mongolian Baiti", "16"," bold"), bg="#eb8334", fg="#fff")
in10_fr2.grid(row=6, column=0, sticky=W,padx=470)
# Botões
bt0_fr2 = Button(fr2_1, text="Criar conta ", font=("Mongolian Baiti", "17", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[cadastrar_funcionario(), in0_fr2.delete(0,'end'),in1_fr2.delete(0,'end'),in2_fr2.delete(0,'end'),in3_fr2.delete(0,'end'),lb4_fr2.delete(0,'end'),lb5_fr2.delete(0,'end'),lb6_fr2.delete(0,'end'),lb7_fr2.delete(0,'end'),lb8_fr2.delete(0,'end'),in9_fr2.delete(0,'end'),in10_fr2.delete(0,'end'), fr2_1.grid_remove(), fr2.grid(row=0, column=0)]).grid(row=8, column=0, sticky=W,pady=20,padx=119)
bt1_fr2 = Button(fr2_1, text="Voltar", font=("Mongolian Baiti", "17", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[in0_fr2.delete(0,'end'),in1_fr2.delete(0,'end'),in2_fr2.delete(0,'end'),in3_fr2.delete(0,'end'),lb4_fr2.delete(0,'end'),lb5_fr2.delete(0,'end'),lb6_fr2.delete(0,'end'),lb7_fr2.delete(0,'end'),lb8_fr2.delete(0,'end'),in9_fr2.delete(0,'end'),in10_fr2.delete(0,'end'), fr2_1.grid_remove(), fr2.grid(row=0, column=0)]).grid(row=8, column=0, sticky=W,padx=455)
#bt2_fr2 = Button(fr2_1, text='👁', font=('Mongolian Baiti', "12", "bold"),bg='#eb8334', fg='#fff').grid(row=6, column=0, sticky=W,padx=712)

fr2_2 = LabelFrame(root, bg="#8a37cc",padx = 100)
lb0_fr2_2 = Label(fr2_2, text="Faça aqui a exclusão de usuarios", font=("Mongolian Baiti", "23"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=4, sticky=EW, pady=30)
lb1_fr2_2 = Label(fr2_2, text="Nome do usuario:", font=("Mongolian Baiti", "13"),background="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, sticky=EW)
in0_fr2 = Entry(fr2_2, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff", width=30)
in0_fr2.grid(row=2, column=1, columnspan=2, sticky=W)
lb2_fr2_2 = Label(fr2_2, text="Confirme sua senha:", font=("Mongolian Baiti", "13"),background="#8a37cc", fg="#f5f5f5").grid(row=3, column=0, sticky=EW)
in1_fr2 = Entry(fr2_2, font=("Mongolian Baiti", "11"," bold"), bg="#eb8334", fg="#fff", width=30,show="*")
in1_fr2.grid(row=3, column=1, columnspan=2, sticky=W)
# Botões
bt0_fr2 = Button(fr2_2, text="Deletar conta ", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff", command= lambda:[in0_fr2.delete(0,'end'),in1_fr2.delete(0,'end'), fr2_2.grid_remove(), fr2.grid(row=0,column=0)]).grid(row=4, column=0,columnspan=2, sticky=W, pady=60, padx=30) #Pura Gambiarra e ta tudo bem
bt1_fr2 = Button(fr2_2, text="Voltar", font=("Mongolian Baiti", "11", "bold"), height=2,width=15, bg="#eb8334", fg="#fff", command= lambda:[in0_fr2.delete(0,'end'),in1_fr2.delete(0,'end'), fr2_2.grid_remove(), fr2.grid(row=0,column=0)]).grid(row=4, column=1, sticky=W, padx=50)
#grid(row=0, column=0,pady=50, padx=150)
#Frame 3 - Felipe
#criando janela
fr3 = LabelFrame(root, text='Login / Cadastro',font=('Mongolian Baiti', '17'), bg='#8a37cc',fg='#f5f5f5',pady=30)
fr3_1 = LabelFrame(root, text='Cadastro',font=('Mongolian Baiti', '17'), bg='#8a37cc',fg='#f5f5f5')
#criando widgets
#lb0_fr3 = Label(fr3, text='Bem Vindo ao Dellux', font='Arial 20', background='#10929c', foreground='#f5f5f5').grid(row=0, column=0, sticky=NSEW)
#lb1_fr3 = Label(fr3, text='O que deseja fazer?', font='Arial 20', background='#10929c', foreground='#f5f5f5').grid(row=1, column=0, sticky=NSEW)
lb2_fr3 = Label(fr3, text='Usuário:', font=('Mongolian Baiti', '23'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0, sticky=W,padx=128)
lb3_fr3 = Label(fr3, text='Senha:', font=('Mongolian Baiti', '23'), bg='#8a37cc', fg='#f5f5f5').grid(row=3, column=0, sticky=W,padx=149)
in0_fr3 = Entry(fr3,text='', font='Arial 20', bg='#fff')
in0_fr3.grid(row=2, column=0,sticky=W,padx=240)
in1_fr3 = Entry(fr3,text='', font='Arial 20', bg='#fff',show="*")
in1_fr3.grid(row=3, column=0,sticky=W,padx=240,pady=10)
#widgets j2
lb4_fr3_1 = Label(fr3_1, text='Bem vindo a área de cadastro', font=('Mongolian Baiti', '22'), bg='#8a37cc', fg='#f5f5f5').grid(row=0, column=0,sticky=W, padx=193,pady=20)
lb5_fr3_1 = Label(fr3_1, text='Nome:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=1, column=0,sticky=W, padx=67)
lb6_fr3_1 = Label(fr3_1, text='Data de Nasc:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0,sticky=W)
lb7_fr3_1 = Label(fr3_1, text='CPF:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0,sticky=W, padx=441)
lb8_fr3_1 = Label(fr3_1, text='Telefone:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=3, column=0,sticky=W, padx=400)
lb9_fr3_1 = Label(fr3_1, text='Endereço:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=3, column=0,sticky=W,padx=35)
lb10_fr3_1 = Label(fr3_1, text='Cidade:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=4, column=0,sticky=W,padx=56)
lb11_fr3_1 = Label(fr3_1, text='UF:',font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=4, column=0,sticky=W, padx=453)
lb12_fr3_1 = Label(fr3_1, text='N°:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=5, column=0,sticky=W, padx=457)
lb13_fr3_1 = Label(fr3_1, text='Email:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=5, column=0,sticky=W,padx=66)
in2_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),textvariable=var ,width=50, bg='#f5f5f5')
in2_fr3_1.grid(row=1, column=0, sticky=W,padx=132) #NOME OK
in3_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),width=22, bg='#f5f5f5')
in3_fr3_1.bind('<KeyRelease>', data_nasc1)
in3_fr3_1.grid(row=2, column=0, sticky=W,padx=132) #DATA NASC OK
in4_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), bg='#f5f5f5')
in4_fr3_1.bind('<KeyRelease>', cpf_cliente)
in4_fr3_1.grid(row=2, column=0, sticky=W,padx=492) #CPF OK
in5_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), bg='#f5f5f5')
in5_fr3_1.bind('<KeyRelease>', telefone_cliente)
in5_fr3_1.grid(row=3, column=0, sticky=W,padx=492) #TELEFONE OK
in6_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), textvariable=var7,width=22, bg='#f5f5f5')
in6_fr3_1.grid(row=3, column=0, sticky=W,padx=132) #LOGRADOURO
in7_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), textvariable=var5,width=22,bg='#f5f5f5')
in7_fr3_1.grid(row=4, column=0, sticky=W,padx=132) #CIDADE
in8_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),textvariable=var6, bg='#f5f5f5')
in8_fr3_1.bind('<KeyRelease>', dois_digitos_cliente)
in8_fr3_1.grid(row=4, column=0, sticky=W,padx=492) #UF OK
in9_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'), bg='#f5f5f5')
in9_fr3_1.bind('<KeyRelease>', numeros_cliente)
in9_fr3_1.grid(row=5, column=0, sticky=W,padx=492) #Nº OK
in10_fr3_1 = Entry(fr3_1, text='', font= ('Arial 16'),width=22, bg='#f5f5f5')
in10_fr3_1.grid(row=5, column=0, sticky=W,padx=132) #EMAIL
#botões
bt0_fr3 = Button(fr3, text='Login', font = ('Mongolian Baiti', '20', 'bold' ) , bg='#eb8334', fg='#f5f5f5',width=13, command= lambda:[in0_fr3.delete(0, 'end'), in1_fr3.delete(0, 'end'), fr3.grid_remove(), fr4.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=30,pady=10)
bt1_fr3 = Button(fr3, text='Cadastrar', font = ('Mongolian Baiti', "20", 'bold' ) , bg='#eb8334', fg='#f5f5f5',width=13, command= lambda:[in0_fr3.delete(0, 'end'), in1_fr3.delete(0, 'end'), fr3.grid_remove(), fr3_1.grid(row=0, column=0)] ).grid(row=4, column=0, sticky=W,padx=265)
bt2_fr3 = Button(fr3, text='Voltar', font = ('Mongolian Baiti', "20", 'bold') , bg='#eb8334', fg='#f5f5f5',width=13 , command= lambda:[in0_fr3.delete(0, 'end'), in1_fr3.delete(0, 'end'), fr3.grid_remove(), fr0.grid(row=0, column=0)]).grid(row=4, column=0, sticky=E,padx=50)
bt3_fr3_1 = Button(fr3_1, text='Salvar', font = ('Mongolian Baiti', '19', 'bold' ), width= 18, bg='#eb8334', fg='#f5f5f5', command= lambda:[cadastrar_cliente(),in2_fr3_1.delete(0, 'end'),in3_fr3_1.delete(0, 'end'),in4_fr3_1.delete(0, 'end'),in5_fr3_1.delete(0, 'end'),in6_fr3_1.delete(0, 'end'),in7_fr3_1.delete(0, 'end'),in8_fr3_1.delete(0, 'end'),in9_fr3_1.delete(0, 'end'),in10_fr3_1.delete(0, 'end'),fr3_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=6, column=0,sticky=W,padx=130,pady=15)
bt4_fr3_1 = Button(fr3_1, text='Voltar', font = ('Mongolian Baiti', '19', 'bold' ), width=18, bg='#eb8334', fg='#f5f5f5', command= lambda:[in2_fr3_1.delete(0, 'end'),in3_fr3_1.delete(0, 'end'),in4_fr3_1.delete(0, 'end'),in5_fr3_1.delete(0, 'end'),in6_fr3_1.delete(0, 'end'),in7_fr3_1.delete(0, 'end'),in8_fr3_1.delete(0, 'end'),in9_fr3_1.delete(0, 'end'),in10_fr3_1.delete(0, 'end'),fr3_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=6, column=0, sticky=W,padx=460)

#Frame 4 - Ewerson
fr4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Usuário', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4 = Label(fr4, text='Ewerson Ribeiro Brandina', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4 = Label(fr4, text='Número da Conta', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=2)
lb1_fr4 = Label(fr4, text='R$ 0.0', font='Arial 20',padx=5, pady=10, bg='#49A').grid(row=1, column=0, sticky=W)
bt2_fr4 = Button(fr4, text='Depósito', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_1.grid(row=0, column=1)]).grid(row=2, column=0, sticky=W)
bt3_fr4 = Button(fr4, text='Saque', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_2.grid(row=0, column=1)]).grid(row=3, column=0, sticky=W)
bt4_fr4 = Button(fr4, text='Transferência', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_3.grid(row=0, column=1)]).grid(row=4, column=0, sticky=W)
bt5_fr4 = Button(fr4, text='Extrato', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_4.grid(row=0, column=1)]).grid(row=5, column=0, sticky=W)
bt6_fr4 = Button(fr4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=14, command= lambda:[fr4.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=7, column=2, sticky=E)
#Frame 4_1 - Ewerson
fr4_1 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Depósito', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_1 = Label(fr4_1, text='Valor a Ser Depositado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#49A')
in0_fr4_1.bind("<KeyRelease>", deposito)
in0_fr4_1.grid(row=0, column=1)
lb1_fr4_1 = Label(fr4_1, text='Senha', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=1, column=0, sticky=E)
in1_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#49A',show="*")
in1_fr4_1.grid(row=1, column=1)
bt2_fr4_1 = Button(fr4_1, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_1 = Label(fr4_1, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=38).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_1 = Button(fr4_1, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [in0_fr4_1.delete(0, 'end'), in1_fr4_1.delete(0, 'end'), fr4_1.grid_remove(), fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_1 = Button(fr4_1, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda:[in0_fr4_1.delete(0, 'end'), in1_fr4_1.delete(0, 'end'), fr4_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W)
#Frame 4_2 - Ewerson
fr4_2 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Saque', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_2 = Label(fr4_2, text='Valor a Ser Sacado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_2 = Entry(fr4_2,font='Arial 20', bg='#49A')
in0_fr4_2.bind('<KeyRelease>', saque)
in0_fr4_2.grid(row=0, column=1)
in1_fr4_2 = Entry(fr4_2, font='Arial 20', bg='#49A',show="*")
in1_fr4_2.grid(row=1, column=1)
bt2_fr4_2 = Button(fr4_2, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_2 = Label(fr4_2, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_2 = Button(fr4_2, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [in0_fr4_2.delete(0, 'end'), in1_fr4_2.delete(0, 'end'), fr4_2.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_2 = Button(fr4_2, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [in0_fr4_2.delete(0, 'end'), in1_fr4_2.delete(0, 'end'), fr4_2.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W)
#Frame 4_3 - Ewerson
fr4_3 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Transferência', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_3 = Label(fr4_3, text='Valor a Ser Transferido', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_3 = Entry(fr4_3,font='Arial 20', bg='#49A')
in0_fr4_3.bind('<KeyRelease>', transferencia)
in0_fr4_3.grid(row=0, column=1)
in1_fr4_3 = Entry(fr4_3, font='Arial 20', bg='#49A',show="*")
in1_fr4_3.grid(row=1, column=1)
bt2_fr4_3 = Button(fr4_3, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_3 = Label(fr4_3, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_3 = Button(fr4_3, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [in0_fr4_3.delete(0, 'end'), in1_fr4_3.delete(0, 'end'), fr4_3.grid_remove(), fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_3 = Button(fr4_3, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda:[in0_fr4_3.delete(0, 'end'), in1_fr4_3.delete(0, 'end'), fr4_3.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W)
#Frame 4_4 - Ewerson
fr4_4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Extrato', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_4 = Label(fr4_4, text='PERIODO', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_4 = Entry(fr4_4,font='Arial 20', bg='#49A')
in0_fr4_4.bind('<KeyRelease>', extrato)
in0_fr4_4.grid(row=0, column=1)
in0_fr4_4.insert(0, 'MM/AAAA')
in1_fr4_4 = Entry(fr4_4, font='Arial 20', bg='#49A',show="*")
in1_fr4_4.grid(row=1, column=1)
bt2_fr4_4 = Button(fr4_4, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_4 = Label(fr4_4, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=27).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_4 = Button(fr4_4, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [in0_fr4_4.delete(0, 'end'), in1_fr4_4.delete(0, 'end'), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_4 = Button(fr4_4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda:[in0_fr4_4.delete(0, 'end'), in1_fr4_4.delete(0, 'end'), fr4_4.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W)
#Looping para tudo
root.mainloop()