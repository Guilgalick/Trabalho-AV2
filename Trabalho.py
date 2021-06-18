import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import sqlite3
import tkinter.messagebox as msg

app=Tk()
app.title("Sistema de reconhecimento de aluno")
width=700
height=400
app.config(bg="#6666ff")
sc_width = app.winfo_screenmmwidth()
sc_height =app.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
app.geometry("%dx%d+%d+%d" % (width, height, x, y))

aluno=StringVar()
disciplina=StringVar()
av1=StringVar()
av2=StringVar()
avd=StringVar()
av3=StringVar()
avds=StringVar()
id=None
updateWindow = None
newWindow = None

def db():
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS Cadastro (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               aluno TEXT, disciplina TEXT, av1 FLOAT, av2 FLOAT, avd FLOAT,av3 FLOAT,avds FLOAT) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM Cadastro ORDER BY aluno")
    fetch = cursor.fetchall() #pega todos os itens que o cursor ta recebendo do banco fetch=dados data=dados
    for data in fetch:
        tree.insert('', 'end', values=(data))#ordena como vai ficar no treeview
    cursor.close()
    conn.close()

def submit():  
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    query = """ INSERT INTO Cadastro (aluno, disciplina, av1, av2, avd, av3, avds) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(query, (str(aluno.get()), str(disciplina.get()), str(av1.get()), str(av2.get()), str(avd.get()), str(av3.get()), str(avds.get())))
    conn.commit()
    cursor.execute("SELECT * FROM Cadastro ORDER BY aluno")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    aluno.set("")
    disciplina.set("")
    av1.set("")
    av2.set("")
    avd.set("")
    av3.set("")
    avds.set("")

def update():
    tree.delete(*tree.get_children())
    conn=sqlite3.connect("registros.db")
    cursor=conn.cursor()
    cursor.execute("""UPDATE Cadastro SET aluno = ?, disciplina = ?, av1 = ?, av2 = ?, avd = ?, av3=?, avds=? WHERE id = ?""",
                      (str(aluno.get()), str(disciplina.get()), float(av1.get()), float(av2.get()), float(avd.get()), float(av3.get()), float(avds.get())))
    conn.commit()
    cursor.execute("SELECT * FROM Cadastro ORDER BY nome")
    fetch=cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    aluno.set("")
    disciplina.set("")
    av1.set("")
    av2.set("")
    avd.set("")
    av3.set("")
    avds.set("")

def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo['values']
    id = selectedItem[0]
    aluno.set("")
    disciplina.set("")
    av1.set("")
    av2.set("")
    avd.set("")
    av3.set("")  
    avds.set("")
    aluno.set(selectedItem[1])
    disciplina.set(selectedItem[2])
    av1.set(selectedItem[3])
    av2.set(selectedItem[4])
    avd.set(selectedItem[5])
    av3.set(selectedItem[6])
    avds.set(selectedItem[7])    
 
    updateWindow=Toplevel()
    updateWindow.title("**** ATUALIZANDO CADASTRO ****")
    formTitulo=Frame(updateWindow)
    formTitulo.pack(side=TOP)
    formCadastro=Frame(updateWindow)
    formCadastro.pack(side=TOP, pady=10)
    largura = 400
    altura = 300
    largura_screen = app.winfo_screenwidth()
    altura_screen = app.winfo_screenheight()
    posx = (largura_screen/2) - (largura/2)
    posy = (altura_screen/2) - (altura_screen/2)
    updateWindow.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


    lbl_title=Label(formTitulo, text="Atualizando cadastros", font=('arial', 18), bg='gray', width=280)
    lbl_title.pack(fill=X)
    lbl_aluno=Label(formTitulo, text="Nome", font=('arial', 12))
    lbl_aluno.grid(row=0, sticky=W)
    lbl_disciplina=Label(formTitulo, text="Disciplina", font=('arial', 12))
    lbl_disciplina.grid(row=1, sticky=W)
    lbl_av1=Label(formTitulo, text="Av1", font=('arial', 12))
    lbl_av1.grid(row=2, sticky=W)
    lbl_av2=Label(formTitulo, text="Av2", font=('arial', 12))
    lbl_av2.grid(row=3, sticky=W)
    lbl_avd=Label(formTitulo, text="AvD", font=('arial', 12))
    lbl_avd.grid(row=4, sticky=W)
    lbl_av3=Label(formTitulo, text="Av3", font=('arial', 12))
    lbl_av3.grid(row=5, sticky=W)
    lbl_avds=Label(formTitulo, text="AvDS", font=('arial', 12))
    lbl_avds.grid(row=6, sticky=W)


    alunoEntry = Entry(formCadastro, textvariable=aluno, font=('arial', 12))
    alunoEntry.grid(row=0, column=1)
    disciplinaEntry = Entry(formCadastro, textvariable=disciplina, font=('arial', 12))
    disciplinaEntry.grid(row=1, column=1)
    av1Entry = Entry(formCadastro, textvariable=av1, font=('arial', 12))
    av1Entry.grid(row=2, column=1)
    av2Entry = Entry(formCadastro, textvariable=av2, font=('arial', 12))
    av2Entry.grid(row=3, column=1)
    avdEntry = Entry(formCadastro, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=4, column=1)
    av3Entry = Entry(formCadastro, textvariable=av3, font=('arial', 12))
    av3Entry.grid(row=5, column=1)
    avdsEntry = Entry(formCadastro, textvariable=avds, font=('arial', 12))
    avdsEntry.grid(row=6, column=1)

    bttn_updatecom = Button(formCadastro, text="Atualizar",
                            width=50, command=update)
    bttn_updatecom.grid(row=6, columnspan=2, pady=10)

   
def delete():
    if not tree.selection():
        resultado = msg.showwarning('', 'Por favor, selecione o item na lista', icon='warning')
    else:
        resultado = msg.askquestion('', 'Tem certeza que deseja deletar o contato?')
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("registros.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'Cadastro' WHERE id = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()
       
def inserirData():
    global newWindow
    aluno.set("")
    disciplina.set("")  
    av1.set("")  
    av2.set("")  
    avd.set("")
    av3.set("")
    avds.set("")



 

    newWindow = Toplevel()
    newWindow.title("**** ATUALIZANDO CONTATO *****")
    formTitulo = Frame(newWindow)
    formTitulo.pack(side=TOP)
    formCadastro = Frame(newWindow)
    formCadastro.pack(side=TOP, pady=10)
    width=400
    height=300
    newWindow.config(bg="gray")
    sc_width = newWindow.winfo_screenmmwidth() #em relação a largura da tela
    sc_height = newWindow.winfo_screenheight() #em relação a altura da tela
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))


    #---------- LABELS - CADASTRAR ------------
    lbl_title = Label(formTitulo, text="Cadastrando contatos", font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X) #preenchimento do item
    lbl_aluno=Label(formCadastro, text='Aluno', font=('arial', 12))
    lbl_aluno.grid(row=0, sticky=W)
    lbl_disciplina = Label(formCadastro, text='Disciplina', font=('arial', 12))
    lbl_disciplina.grid(row=1, sticky=W) #sticky = preso a um ponto
    lbl_AV1 = Label(formCadastro, text='Av1', font=('arial', 12))
    lbl_AV1.grid(row=2, sticky=W) #sticky = preso a um ponto
    lbl_AV2= Label(formCadastro, text='Av2', font=('arial', 12))
    lbl_AV2.grid(row=3, sticky=W) #sticky = preso a um ponto
    lbl_AVD= Label(formCadastro, text='AvD', font=('arial', 12))
    lbl_AVD.grid(row=4, sticky=W) #sticky = preso a um ponto
    lbl_AV3 = Label(formCadastro, text='Av3', font=('arial', 12))
    lbl_AV3.grid(row=5, sticky=W) #sticky = preso a um ponto
    lbl_AVDS = Label(formCadastro, text='AvDS', font=('arial', 12))
    lbl_AVDS.grid(row=6, sticky=W) #sticky = preso a um ponto

    # ----------- ENTRY - CADASTRAR ------------
    alunoEntry = Entry(formCadastro, textvariable=aluno, font=('arial', 12))
    alunoEntry.grid(row=0, column=1)
    disciplinaEntry = Entry(formCadastro, textvariable=disciplina, font=('arial', 12))
    disciplinaEntry.grid(row=1, column=1)
    AV1Entry = Entry(formCadastro, textvariable=av1, font=('arial', 12))
    AV1Entry.grid(row=2, column=1)
    AV2Entry = Entry(formCadastro, textvariable=av2, font=('arial', 12))
    AV2Entry.grid(row=3, column=1)
    AVDEntry = Entry(formCadastro, textvariable=avd, font=('arial', 12))
    AVDEntry.grid(row=4, column=1)
    AV3Entry = Entry(formCadastro, textvariable=av3, font=('arial', 12))
    AV3Entry.grid(row=5, column=1)
    AVDSEntry = Entry(formCadastro, textvariable=avds, font=('arial', 12))
    AVDSEntry.grid(row=6, column=1)
    # ----------- BOTÂO - CADASTRAR ------------
    bttn_submitcom=Button(formCadastro, text="Cadastrar", width=50, command=submit)
    bttn_submitcom.grid(row=7, columnspan=2, pady=10)

# ---------------- FRAME PRINCIPAL -----------------

top = Frame(app, width=500, bd=1, relief=SOLID) #usado pro titulo
top.pack(side=TOP)        #pack vai dentro do grid            
mid=Frame(app, width=500, bg="#6666ff")
mid.pack(side=TOP)
midleft=Frame(mid, width=100)
midleft.pack(side=LEFT, pady=10)
midleftPadding =Frame(mid, width=350, bg="#6666ff")
midleftPadding.pack(side=LEFT)
midright=Frame(mid, width=100)
midright.pack(side=RIGHT, pady=10)
bottom=Frame(app, width=500)
bottom.pack(side=BOTTOM)
tableMargin=Frame(app, width=500)
tableMargin.pack(side=TOP)

# ------------- LABELS PRINCIPAL ---------------
lbl_title=Label(top, text="SISTEMA DE GERENCIAMENTO DE CONTATOS", font=('arial', 18), width=500)
lbl_title.pack(fill=X) #preencher todo um eixo: exemplo fill=x preenche todo eixo x

lbl_alterar=Label(bottom, text="Para alterar clique duas vezes no contato desejado.", font=('arial', 12), width=200)
lbl_alterar.pack(fill=X)

# ----------------- BUTTONS PRINCIPAL -----------------
bttn_add=Button(midleft, text="INSERIR", bg="royal blue", command=inserirData)
bttn_add.pack()
bttn_delete = Button(midright, text="Deletar", bg="OrangeRed2", command=delete)
bttn_delete.pack(side=RIGHT)

# ----------------- TREEVIEW PRINCIPAL -----------------
#treeview da tela principal
#scrollbarx tem que declarar com s minusculo
ScrollbarX=Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY=Scrollbar(tableMargin, orient=VERTICAL)

tree=ttk.Treeview(tableMargin, column=("ID", "Aluno", "Disciplina", "Av1", "Av2", "AvD", "Av3", "AvDS"),
                  height=400, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand=ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Aluno", text="Aluno", anchor=W)
tree.heading("Disciplina", text="Disciplina", anchor=W)
tree.heading("Av1", text="Av1", anchor=W)
tree.heading("Av2", text="Av2", anchor=W)
tree.heading("AvD", text="AvD", anchor=W)
tree.heading("Av3", text="Av3", anchor=W)
tree.heading("AvDS", text="AvDS", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=50)
tree.column('#6', stretch=NO, minwidth=0, width=50)
tree.column('#7', stretch=NO, minwidth=0, width=50)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)


# --------- MENU - PRINCIPAL ---------------
menu_bar = Menu(app)
app.config(menu=menu_bar)

# adicionar itens
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Criar novo", command=inserirData)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=app.destroy)

menuSobre = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Sobre", menu=menuSobre)
menuSobre.add_command(label="Info")


if __name__ == '__main__':
    db()
    app.mainloop()