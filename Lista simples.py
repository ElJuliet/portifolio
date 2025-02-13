#Ideia, fazer um sistema simples que tenha as adap dele e as permanentes e sempre que ele apagar ou resetar ele
#perde todas
from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkinter import ttk
from tkinter import messagebox
root =Tk()
#Deus abençoe a pobre alma que tentara entender o que eu escrevi
class Back():
 top_inst = None
 positivo=None
 negativo=None
 def conect(self):
  try:
   self.conn = mysql.connector.connect(
    host="Ip",
    user="",
    password="",
    database="",
    port= ""
     )
   if self.conn.is_connected():
    self.cursor = self.conn.cursor()
  except Error as e:
   print(f"Erro ao conectar ao MySQL: {e}")
  
 def desconect(self):
    self.conn.close()
 
 def add_adap2(self):
  self.conect()
  self.conect2()
  self.itemselec = self.listaPerm.selection()
  self.item = self.listaPerm.item(self.itemselec)
  self.a_id,self.a_origem, self.a_nivel, self.a_detalhes = self.item["values"]
  self.cursor.execute("""
        INSERT INTO  adapt (  origem, nivel, detalhes)
        VALUES ( %s,%s,%s)
    """, ( self.a_origem, self.a_nivel, self.a_detalhes))
  self.cursor_perm.execute("DELETE FROM perm2 WHERE  origem = %s AND nivel = %s AND detalhes = %s", (self.a_origem,self.a_nivel,self.a_detalhes))
 
  self.conn.commit()
  self.conn_perm.commit()
  self.desconect()
  self.select2()
  self.select()
 def add_adap(self):
    self.a_origem = self.o_origem.get()
    self.a_nivel = self.o_final
    self.a_detalhes = self.detalhes.get("1.0", END).strip()
    self.conect()
    self.cursor.execute("""
    INSERT INTO adapt (origem, nivel, detalhes)
    VALUES (%s, %s, %s)
""", (self.a_origem, self.a_nivel, self.a_detalhes))

    
    self.conn.commit()
    self.desconect()
    self.select()
    self.j_limpar()
 def select(self):
    self.listaAtuais.delete(*self.listaAtuais.get_children())
    self.conect()
    #Adiconar nivel dps
    self.cursor.execute("SELECT id, origem, nivel, detalhes FROM adapt")
    lista = self.cursor.fetchall()
    for item in lista:
       self.item_id= item
       self.listaAtuais.insert("",END, values=item);self.iid=self.item_id
    self.desconect()
 def editar_item(self):
  self.itemselec=self.listaAtuais.selection()
  self.item=self.listaAtuais.item(self.itemselec)
  self.valor=self.item["values"]
  Back.positivo=1
  self.j_criar()
 def salvar_item(self):
  self.conect()
  self.nivel()
  Back.positivo=None  
  self.a_origem = self.o_origem.get()
  self.a_nivel = self.o_final
  self.a_detalhes = self.detalhes.get("1.0", END).strip()
  self.a_id = self.valor[0]

  self.cursor.execute("""
            UPDATE adapt
            SET origem = %s, nivel = %s, detalhes =%s WHERE id=%s
        """, (self.a_origem,self.a_nivel,self.a_detalhes,self.a_id))

  Back.top_inst = None 
 
  self.conn.commit() 
  self.desconect()
  self.select()
  self.top.destroy()
 def ver_item(self):

  self.itemselec = self.listaAtuais.selection()
  self.item = self.listaAtuais.item(self.itemselec)
  self.valor = self.item["values"]

  self.frame1 = Canvas(self.root)
  self.frame1.configure(background="#1f1e1d")
  self.frame1.place(relx=0.4, rely=0.01, relwidth=0.95, relheight=0.75)

  self.frame2=Label(self.frame1,text="ORIGEM",font=("Arial",8)).place(relx=0.01, rely=0.1, relwidth=0.10, relheight=0.06)
  self.frame2=Label(self.frame1,text=self.valor[1]).place(relx=0.12, rely=0.1, relwidth=0.40, relheight=0.06)

  self.frame2=Label(self.frame1,text="Nivel").place(relx=0.01, rely=0.20, relwidth=0.10, relheight=0.06)
  self.frame2=Label(self.frame1,text= self.valor[2]).place(relx=0.12, rely=0.20, relwidth=0.10, relheight=0.06)

  self.frame2=Label(self.frame1,text="Detalhes:").place(relx=0.20, rely=0.30, relwidth=0.20, relheight=0.08)
  self.frame3=Text(self.frame1,font=("Arial", 10))
  self.frame3.place(relx=0.07, rely=0.40, relwidth=0.5, relheight=0.5)
  self.frame3.insert(1.0,self.valor[3])
  self.frame3.config(state="disabled")
  self.frame1.create_text(150, 20,text="Teste", font=("Sigilos Regular",20),fill="red")
 
  self.b_voltar=Button(self.frame1,text="Voltar",command=self.frame1.destroy)
  self.b_voltar.place(relx=0.0, rely=0.94, relwidth=0.3, relheight=0.06)
  self.b_voltar.configure(background="#5e9943")

  self.b_voltar2=Button(self.frame1,text="Promover",command=self.criar_perm)
  self.b_voltar2.place(relx=0.35, rely=0.94, relwidth=0.3, relheight=0.06)
  self.b_voltar2.configure(background="#2430b5")
 def deletar_item(self):
  self.itemselec=self.listaAtuais.selection()
  self.item=self.listaAtuais.item(self.itemselec)
  self.a_id,self.a_origem,self.a_nivel,self.a_detalhes = self.item["values"]
  self.conect()
  self.cursor.execute("""
    DELETE FROM adapt WHERE origem = %s AND nivel = %s AND detalhes = %s
""", (self.a_origem, self.a_nivel, self.a_detalhes))

  self.conn.commit()
  self.desconect()
  self.listaAtuais.delete(self.itemselec)

 def nivel(self):
    if self.teste1.get()==1:
     self.o_final="P"
     
    if self.teste2.get()==1:
     self.o_final="M"
   
    if self.teste3.get()==1:
     self.o_final="E"
 def j_limpar(self):
     self.o_origem.delete(0,END)
     self.detalhes.delete(1.0,END) 
 def minimenu(self,event):
  
  context_menu = Menu(root, tearoff=0)
  context_menu.add_command(label="Ver Detalhes",command=self.ver_item)
  context_menu.add_command(label="Editar",command=self.editar_item)
  context_menu.add_command(label="Excluir",command=self.deletar_item)
  context_menu.tk_popup(event.x_root, event.y_root)
 def perm_menu(self):
  p_menu = Menu(root, tearoff=1)
  root.config(menu=p_menu)
  p_menu.add_cascade(label="Atuais",command=self.__init__)
  p_menu.add_cascade(label="Permanente",command=self.permanente) 

 def j_criar(self): 
    if Back.top_inst is None:
     self.top = Toplevel()
     #iniciador da janela de criar
     self.j_config()
     self.entrys()
     Back.top_inst = 0
     self.top.protocol("WM_DELETE_WINDOW", self.on_close)
 def on_close(self):
    Back.top_inst = None  # Redefine a variável de classe ao fechar a janela
    self.top.destroy()
 def j_config(self):
     self.top.title("Criar")
     self.top.geometry("350x600")
     self.label_1=Label(self.top)
     self.label_1.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)
     self.label_1.configure(background="#7042d4")
     self.top.resizable(False,False)
 def entrys(self):  
      
     #ORIGEM
     self.origem = Label(self.label_1,text="Origem")
     self.origem.place(relx=0.01, rely=0.01, relheight=0.09, relwidth=0.15)
     self.o_origem = Entry(self.label_1,font=("Arial",13))
     self.o_origem.place(relx=0.17, rely=0.01, relheight=0.09, relwidth=0.65)
     if Back.positivo == 1:
        self.o_origem.insert(0,self.valor[1])

        
     #NIVEL
     self.o_final=""
     self.teste1=IntVar()
     self.teste2=IntVar()
     self.teste3=IntVar()
     self.o_nivel = Label(self.label_1,text="NIvel")
     self.o_nivel.place(relx=0.01, rely=0.12, relheight=0.09, relwidth=0.15)
     self.o_nivel1=Checkbutton(self.label_1,text="Pequeno", variable=self.teste1,onvalue=1,offvalue=0,command=self.nivel)
     self.o_nivel2=Checkbutton(self.label_1,text="Medio", variable=self.teste2,onvalue=1,offvalue=0,command=self.nivel)
     self.o_nivel3=Checkbutton(self.label_1,text="Extremo", variable=self.teste3,onvalue=1,offvalue=0,command=self.nivel)
     self.o_nivel1.place(relx=0.18, rely=0.15, relheight=0.05, relwidth=0.19)
     self.o_nivel2.place(relx=0.38, rely=0.15, relheight=0.05, relwidth=0.19)
     self.o_nivel3.place(relx=0.58, rely=0.15, relheight=0.05, relwidth=0.19)

     if Back.positivo == 1:
      if self.valor[2]== "P":
        self.teste1.set(1)
      elif self.valor[2]== "M":
        self.teste2.set(1)
      elif self.valor[2]== "E":
        self.teste3.set(1)

     #DETALHES
     self.d_detales = Label(self.label_1,text="Detalhes", font=("Arial Bold",28))
     self.d_detales.place(relx=0.30, rely=0.25, relheight=0.07, relwidth=0.45)
     self.detalhes = Text(self.label_1,width=50,font=("Arial Bold",12))
     self.detalhes.place(relx=0.02, rely=0.35, relheight=0.50, relwidth=0.95)
     if Back.positivo == 1:
      self.detalhes.insert(1.0,self.valor[3])

      
     #Finalizar
    
      if Back.negativo==1 and Back.positivo==1:
       self.final = Button(self.label_1,text="Finalizar", font=("Arial Bold",26),command=self.salvar_itemP)
       self.final.place(relx=0.01, rely=0.90, relheight=0.1, relwidth=0.45)
       self.final.configure(background="#4786ba")

      elif Back.positivo == 1 and Back.negativo== None:
       self.final = Button(self.label_1,text="Finalizar", font=("Arial Bold",26),command=self.salvar_item)
       self.final.place(relx=0.01, rely=0.90, relheight=0.1, relwidth=0.45)
       self.final.configure(background="#4786ba")

     elif Back.positivo == None:
       self.final = Button(self.label_1,text="Finalizar", font=("Arial Bold",26),command=self.add_adap)
       self.final.place(relx=0.01, rely=0.90, relheight=0.1, relwidth=0.45)
       self.final.configure(background="#4786ba")

     #Limpar
     self.limpar = Button(self.label_1,text="Limpar", font=("Arial Bold",20),command=self.j_limpar)
     self.limpar.place(relx=0.7, rely=0.90, relheight=0.1, relwidth=0.30)
     self.limpar.configure(background="#8f6b40")

 def permanente(self):
  self.root=root
  self.root.geometry("450x600")
  self.root.title("Adaptar")
  self.root.resizable(True,True)
  self.root.maxsize(width=500, height=710)
  self.inicial=Frame(self.root)
  self.inicial.configure(background="#540c3d")
  self.inicial.place(relx=0.0 ,rely=0.0, relheight=1, relwidth=1)
  self.listaP()
  self.select2()
 def minimenu2(self,event):
  context_menu = Menu(root, tearoff=0)
  context_menu.add_command(label="Ver Detalhes",command=self.ver_itemP)
  context_menu.add_command(label="Editar",command=self.editar_itemP)
  context_menu.add_command(label="Excluir",command=self.deletar_itemP)
  context_menu.tk_popup(event.x_root, event.y_root)

 def criar_perm(self):
  self.conect()
  self.conect2()
  self.itemselec = self.listaAtuais.selection()
  self.item = self.listaAtuais.item(self.itemselec)
  self.a_id,self.a_origem, self.a_nivel, self.a_detalhes = self.item["values"]
  self.cursor_perm.execute("""
        INSERT INTO  perm2 ( origem, nivel, detalhes)
        VALUES (%s, %s,%s)
    """, (self.a_origem, self.a_nivel, self.a_detalhes))
  self.cursor.execute("""
        DELETE FROM adapt 
        WHERE origem = %s AND nivel = %s AND detalhes = %s
    """, (self.a_origem, self.a_nivel, self.a_detalhes))
  self.conn.commit()
  self.select()
  self.conn_perm.commit()
  self.desconect()
 def ver_itemP(self):
  self.itemselec = self.listaPerm.selection()
  self.item = self.listaPerm.item(self.itemselec)
  self.valor = self.item["values"]

  self.frameP1 = Canvas(self.root)
  self.frameP1.configure(background="#363331")
  self.frameP1.place(relx=0.4, rely=0.01, relwidth=0.95, relheight=0.75)

  self.frameP2=Label(self.frameP1,text="ORIGEM",font=("Arial",8)).place(relx=0.01, rely=0.1, relwidth=0.10, relheight=0.06)
  self.frameP2=Label(self.frameP1,text=self.valor[1]).place(relx=0.12, rely=0.1, relwidth=0.40, relheight=0.06)

  self.frameP2=Label(self.frameP1,text="Nivel").place(relx=0.01, rely=0.20, relwidth=0.10, relheight=0.06)
  self.frameP2=Label(self.frameP1,text= self.valor[2]).place(relx=0.12, rely=0.20, relwidth=0.10, relheight=0.06)

  self.frameP2=Label(self.frameP1,text="Detalhes:").place(relx=0.20, rely=0.30, relwidth=0.20, relheight=0.08)
  self.frameP3=Text(self.frameP1,font=("Arial", 10))
  self.frameP3.place(relx=0.07, rely=0.40, relwidth=0.5, relheight=0.5)
  self.frameP3.insert(1.0,self.valor[3])
  self.frameP3.config(state="disabled")
  self.frameP1.create_text(150, 20,text="Teste", font=("Sigilos Regular",20),fill="red")
 
  self.b_voltarP=Button(self.frameP1,text="Voltar",command=self.frameP1.destroy)
  self.b_voltarP.place(relx=0.0, rely=0.94, relwidth=0.3, relheight=0.06)
  self.b_voltarP.configure(background="#5e9943")

  self.b_voltar2P=Button(self.frameP1,text="Despromover",command=self.add_adap2)
  self.b_voltar2P.place(relx=0.35, rely=0.94, relwidth=0.3, relheight=0.06)
  self.b_voltar2P.configure(background="#2430b5")
 def deletar_itemP(self):
  self.itemselec=self.listaPerm.selection()
  self.item=self.listaPerm.item(self.itemselec)
  self.a_id,self.a_origem,self.a_nivel,self.a_detalhes = self.item["values"]
  self.conect2()
  self.cursor_perm.execute("DELETE FROM perm2 WHERE id=%s AND origem = %s AND nivel = %s AND detalhes = %s", (  self.a_id,self.a_origem,self.a_nivel,self.a_detalhes))
  self.conn_perm.commit()
  self.desconect()
  self.listaPerm.delete(self.itemselec)
 def editar_itemP(self):
  self.itemselec=self.listaPerm.selection()
  self.item=self.listaPerm.item(self.itemselec)
  self.valor=self.item["values"]
  Back.positivo=1
  Back.negativo=1
  self.j_criar()
 def salvar_itemP(self):
  self.conect2()
  self.nivel()
  Back.positivo=None  
  self.a_origem = self.o_origem.get()
  self.a_nivel = self.o_final
  self.a_detalhes = self.detalhes.get("1.0", END).strip()
  self.a_id = self.valor[0]

  self.cursor_perm.execute("""
            UPDATE perm2
            SET origem = %s, nivel = %s, detalhes = %s WHERE id=%s
        """, (self.a_origem,self.a_nivel,self.a_detalhes,self.a_id))

  Back.top_inst = None 
  self.conn_perm.commit() 
  self.desconect()
  self.select2()
  self.top.destroy()
 def conect2(self): 
  self.conn_perm = mysql.connector.connect(
   host="192.168.56.1",
    user="ADM",
    password="gugudada123",
    database="perm",
    port= 3306
     )
  
  self.cursor_perm = self.conn_perm.cursor()
    
 
 def select2(self):
    self.listaPerm.delete(*self.listaPerm.get_children())
    self.conect2()
    self.cursor_perm.execute("SELECT id, origem, nivel, detalhes FROM perm2")
    lista = self.cursor_perm.fetchall()  # Retorna todos os resultados da consulta
    for item in lista:
      self.item_id= item
      self.listaPerm.insert("",END, values=item);self.iid=self.item_id
    self.conn_perm.close()

 def listaP(self):
  self.listaPerm = ttk.Treeview(self.inicial, column=("col1","col2","col3","col4"))
  self.listaPerm.heading("#0")
  self.listaPerm.heading("#1")
  self.listaPerm.heading("#2", text="Origem")
  self.listaPerm.heading("#3", text="Nivel")
  self.listaPerm.heading("#4", text="Detalhes")
  self.listaPerm.column("#0", width=0)
  self.listaPerm.column("#1", width=0)
  self.listaPerm.column("#2", width=100)
  self.listaPerm.column("#3", width=50)
  self.listaPerm.column("#4", width=150)
  self.listaPerm.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.9)
  self.listaPerm.bind("<Button-3>",self.minimenu2)
  
class application(Back):
 
 def __init__(self):
  self.root=root
  self.janela()
  self.perm_menu()
  self.frame_j()
  self.bt_create()
  self.select()
  root.mainloop()

 def janela(self):
    # self.root.iconbitmap("J:\Enfraquecer-membrana.ico")
  self.root.geometry("450x600")
  self.root.title("ADAPTS")
  self.root.resizable(False,True)
  self.root.maxsize(width=500, height=710)
  
 def frame_j(self):
  self.inicial=Frame(self.root)
  self.inicial.configure(background="#6b4278")
  self.inicial.place(relx=0.0 ,rely=0.0, relheight=1, relwidth=1)
  self.listaAtuais = ttk.Treeview(self.inicial, column=("col1", "col2","col3", "col4" ))
  self.listaAtuais.heading("#0")
  self.listaAtuais.heading("#1")
  self.listaAtuais.heading("#2", text="Origem")
  self.listaAtuais.heading("#3", text="Nivel")
  self.listaAtuais.heading("#4", text="Detalhes")
  self.listaAtuais.column("#0", width=0)
  self.listaAtuais.column("#1", width=0)
  self.listaAtuais.column("#2", width=100)
  self.listaAtuais.column("#3", width=50)
  self.listaAtuais.column("#4", width=150)
  self.listaAtuais.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.9)

  self.listaAtuais.bind("<Button-3>",self.minimenu)

  self.scrool= Scrollbar(self.inicial, orient="vertical")
  self.listaAtuais.configure(yscroll=self.scrool.set)
  self.scrool.place(relx=0.95 ,rely=0.01, relheight=0.90, relwidth=0.03)
 def bt_create(self):
    
     self.bt_criar= Button(self.inicial,text="CRIAR",command=self.j_criar)
     self.bt_criar.place(relx=0.00, rely=0.93, relwidth=0.25, relheight=0.08)
     self.bt_criar.configure(background="#7d7777")
    
 
 


application()

#CRIAR UM BOTÃO DE ADICIONAR ADAPTAÇÃO X
#SISTEMA QUE PEGA AS ULTIMAS ADAPTAÇÕES X
#BOTÃO PARA VER MAIS DETALHES DA ADAPTAÇÃO X
#BOTÃO DE EXCLUIR ADATAÇÕES X
#BOTÃO DE EDITAR ADAPTAÇÕES X
#FAZER A AREA DE ADAPTAÇÕES PERMANENTES X
