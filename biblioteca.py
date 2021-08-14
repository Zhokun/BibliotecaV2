from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Treeview

import psycopg2
from PIL import Image, ImageTk


class Biblioteca(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.conn = psycopg2.connect(host="localhost", database="biblioteca", user="postgres", password="postgres")
        x = 900
        y = 840
        self.geometry(f"{x}x{y}+"
                      f"{int(self.winfo_screenwidth() / 2 - x / 2)}+{int(self.winfo_screenheight() / 2 - y / 2)}")
        self.title('Biblioteca')
        self.iconphoto(True, ImageTk.PhotoImage(Image.open("Da.png")))
        # ===========================================================================================================
        # Frame para o logo
        self.f_logo = Frame(self)
        self.f_logo.pack()
        self.img = ImageTk.PhotoImage(Image.open("Logo.png"))
        self.img_log = Label(self.f_logo, image=self.img)
        self.img_log.pack()
        # ===========================================================================================================
        # Frame para suportar os dois campos do aluno
        self.f_aluno_info = Frame(self)
        self.f_aluno_info.pack()
        # Frame para o campo do aluno a esquerda, suportando ID, nome, e outras informações
        self.f_aluno_esquerda = LabelFrame(self.f_aluno_info)
        self.f_aluno_esquerda.pack(side=LEFT)
        # Campos de texto e entrada de dados
        self.txt_id_aluno = Label(self.f_aluno_esquerda, text="ID: ", )  # Texto ID aluno
        self.txt_id_aluno.grid(row=0, column=0)
        self.e_aluno_id = Entry(self.f_aluno_esquerda, )  # Entrada do ID aluno
        self.e_aluno_id.grid(row=0, column=1, sticky='w', padx=5, pady=5)
        self.e_aluno_id.focus_set()
        self.e_aluno_id.bind('<KeyRelease>', self.enter)

        self.txt_nome_aluno = Label(self.f_aluno_esquerda, text='Nome: ', )  # Texto Nome
        self.txt_nome_aluno.grid(row=1, column=0)
        # Carrega o nome do aluno se existir na base
        self.load_nome_aluno = Label(self.f_aluno_esquerda, font=("Verdana", 10), fg='green', width=20, anchor='w', )
        self.load_nome_aluno.grid(row=1, column=1, padx=5)
        # Botão para carregar o aluno caso ele exista e também o título dos livros alugados caso tenha algum
        self.b_load = Button(self.f_aluno_esquerda, text='Buscar', command=self.buscar_aluno, )
        self.b_load.grid(row=2, column=0, columnspan=2, pady=5)

        # ===========================================================================================================
        # Frame para os dados informando se o o aluno já tem algum livro alugado
        self.f_aluno_direita = Frame(self.f_aluno_info)
        self.f_aluno_direita.pack(side=RIGHT)

        # Campos relacionados ao cliente, mostrando se ele já tem livro alugado e qual o livro
        self.titulo_info_livro = Frame(self.f_aluno_direita)  # Frame para uma mensagem acima dos livros alugados
        self.titulo_info_livro.pack()
        self.info_livros_alugados = Label(self.titulo_info_livro, text='Livros alugados pelo aluno',
                                          borderwidth=1, relief='solid', width=80)  # Mensagem acima dos livros
        self.info_livros_alugados.grid(row=0, column=1, columnspan=2)
        # Frame para carregar os livros alugados
        self.info_livros = Frame(self.f_aluno_direita)
        self.info_livros.pack()
        # Campos com texto, o livro alugado caso exista e check box para devolução caso solicitado
        self.info_livro1 = Label(self.info_livros, text="Livro 1: ")
        self.info_livro1.grid(row=1, column=0)
        self.load_livro1 = Label(self.info_livros, width=70)  # Carrega o livro 1
        self.load_livro1.grid(row=1, column=1)
        # Checkbox livro 1
        self.livro1 = IntVar()
        self.check_livro1 = Checkbutton(self.info_livros, variable=self.livro1, state=DISABLED, )
        self.check_livro1.grid(row=1, column=2)

        self.info_livro2 = Label(self.info_livros, text="Livro 2: ")
        self.info_livro2.grid(row=2, column=0)
        self.load_livro2 = Label(self.info_livros, )  # Carrega o livro 2
        self.load_livro2.grid(row=2, column=1)
        # Checkbox livro 2
        self.livro2 = IntVar()
        self.check_livro2 = Checkbutton(self.info_livros, variable=self.livro2, state=DISABLED)
        self.check_livro2.grid(row=2, column=2)

        self.info_livro3 = Label(self.info_livros, text="Livro 3: ")
        self.info_livro3.grid(row=3, column=0)
        self.load_livro3 = Label(self.info_livros, )  # Carrega o livro 3
        self.load_livro3.grid(row=3, column=1)
        # Checkbox livro 2
        self.livro3 = IntVar()
        self.check_livro3 = Checkbutton(self.info_livros, variable=self.livro3, state=DISABLED)
        self.check_livro3.grid(row=3, column=2)
        # ===========================================================================================================

        # ===========================================================================================================
        # Carrega os livros
        # Frame para os livros
        self.f_tipo_busca = Frame(self, )
        self.f_tipo_busca.pack(pady=5, padx=5)

        self.l_texto_buscar = Label(self.f_tipo_busca, text='Buscar por: ')
        self.l_texto_buscar.grid(row=1, column=0)
        # Pesquisar por Titulo
        self.l_titulo = Label(self.f_tipo_busca, text='Título')
        self.l_titulo.grid(row=0, column=1, pady=(10, 3))
        self.e_titulo = Entry(self.f_tipo_busca, )
        self.e_titulo.grid(row=1, column=1, padx=(0, 5))

        # Pesquisar por autor
        self.l_autor = Label(self.f_tipo_busca, text='Autor')
        self.l_autor.grid(row=0, column=2, )
        self.e_autor = Entry(self.f_tipo_busca, )
        self.e_autor.grid(row=1, column=2, padx=(0, 5))

        # Pesquisar por autor
        self.l_editora = Label(self.f_tipo_busca, text='Editora')
        self.l_editora.grid(row=0, column=3, )
        self.e_editora = Entry(self.f_tipo_busca, )
        self.e_editora.grid(row=1, column=3, )
        self.e_titulo.bind("<KeyRelease>", self.load_lista) \
        and self.e_autor.bind("<KeyRelease>", self.load_lista) \
        and self.e_editora.bind("<KeyRelease>", self.load_lista)

        for i in (self.e_titulo, self.e_autor, self.e_editora):
            i["state"] = DISABLED
        # ===========================================================================================================
        # Scrollbar para o treeview
        self.f_livros = Frame(self, )
        self.f_livros.pack(pady=10, fill=X, padx=5)
        self.scrollbar = Scrollbar(self.f_livros)
        self.scrollbar.pack(side=LEFT, fill=Y)

        self.original_msg = "Digite o nome do livro, autor ou editora para encontrar o que procura."
        # Treeview para carregar os livros
        self.tree = Treeview(self.f_livros, columns=('c1', 'c2', 'c3'), show='headings', )
        self.tree.column("#1", anchor=CENTER)
        self.tree.heading("#1", text="Título")

        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="Autor")

        self.tree.column("#3", anchor=CENTER)
        self.tree.heading("#3", text="Editora")

        self.tree.pack(side=RIGHT, fill=X, expand=True)

        self.scrollbar.config(command=self.tree.yview)
        self.estilo_tree = ttk.Style()
        self.tree.bind("<ButtonRelease-1>", self.loadbookinfo)
        self.estilo_tree.configure('Treeview', )
        self.estilo_tree.map('Treeview', background=[('selected', 'gray')])
        self.lst_com_livros = []
        # ===========================================================================================================
        # Frame para carregar os botões Carregar informção do livro, devolver livro e alugar
        self.f_buttons = Frame(self)
        self.f_buttons.pack()

        self.b_carregar = Button(self.f_buttons, text='Limpar tela', width=14, command=self.clear_all)
        self.b_carregar.pack(side=LEFT, padx=(0, 10), pady=(5, 10))

        self.b_alugar = Button(self.f_buttons, text='Alugar', width=14, state=DISABLED, command=self.alugar)
        self.b_alugar.pack(side=LEFT)

        self.b_devolver = Button(self.f_buttons, text='Devolver', width=14, state=DISABLED, command=self.devolver)
        self.b_devolver.pack(side=LEFT, padx=(10, 0))
        # ===========================================================================================================
        # Frame book info
        self.f_book_info = Frame(self)
        self.f_book_info.pack()

        self.t_titulo = Label(self.f_book_info, text='Título: ', borderwidth=1, relief='solid')
        self.t_titulo.grid(row=0, column=0, sticky='we', )
        self.load_titulo = Label(self.f_book_info, width=105, anchor=W, borderwidth=1, relief='sunken')
        self.load_titulo.grid(row=0, column=1, columnspan=4, sticky=W, padx=5, pady=5)

        self.t_ean = Label(self.f_book_info, text='EAN: ', borderwidth=1, relief='solid', )
        self.t_ean.grid(row=1, column=0, sticky='we', )
        self.load_ean = Label(self.f_book_info, width=13, borderwidth=1, relief='sunken')
        self.load_ean.grid(row=1, column=1, padx=5, )

        self.t_editora = Label(self.f_book_info, text='Editora: ', borderwidth=1, relief='solid', )
        self.t_editora.grid(row=2, column=0, sticky='we', )
        self.load_editora = Label(self.f_book_info, width=13, borderwidth=1, relief='sunken')
        self.load_editora.grid(row=2, column=1, padx=5, )

        self.t_npaginas = Label(self.f_book_info, text='N. Páginas: ', borderwidth=1, relief='solid', )
        self.t_npaginas.grid(row=3, column=0, sticky='we', )
        self.load_npaginas = Label(self.f_book_info, width=13, borderwidth=1, relief='sunken')
        self.load_npaginas.grid(row=3, column=1, )

        self.t_ano = Label(self.f_book_info, text="Lançado: ", borderwidth=1, relief='solid', )
        self.t_ano.grid(row=4, column=0, sticky='we', )
        self.load_ano = Label(self.f_book_info, width=13, borderwidth=1, relief='sunken')
        self.load_ano.grid(row=4, column=1, )

        self.t_idioma = Label(self.f_book_info, text="Idioma: ", borderwidth=1, relief='solid', )
        self.t_idioma.grid(row=5, column=0, sticky='we', )
        self.load_idioma = Label(self.f_book_info, width=13, borderwidth=1, relief='sunken')
        self.load_idioma.grid(row=5, column=1, )

        self.t_genero = Label(self.f_book_info, text="Gênero: ", borderwidth=1, relief='solid', )
        self.t_genero.grid(row=6, column=0, sticky='we', )
        self.load_genero = Label(self.f_book_info, width=13, borderwidth=1, relief='sunken')
        self.load_genero.grid(row=6, column=1, )

        self.t_autor = Label(self.f_book_info, text="Autor: ", borderwidth=1, relief='solid', )
        self.t_autor.grid(row=8, column=2, sticky='we', pady=(10, 0))
        self.load_autor = Label(self.f_book_info, width=70, borderwidth=1, relief='sunken')
        self.load_autor.grid(row=8, column=3, columnspan=3, padx=5, pady=(10, 0))

        self.t_avaliacao = Label(self.f_book_info, text='Avaliação: ', borderwidth=1, relief='solid', )
        self.t_avaliacao.grid(row=1, column=2, sticky='we', )
        self.load_avaliacao = Label(self.f_book_info, anchor=W, width=3, borderwidth=1, relief='sunken')
        self.load_avaliacao.grid(row=1, column=3, sticky='w', padx=5, pady=5)

        self.t_descricao = Label(self.f_book_info, text='Descrição: ', borderwidth=1, relief='solid', )
        self.t_descricao.grid(row=2, column=2, sticky='we', )
        self.load_descricao = Text(self.f_book_info, width=70, height=10, border=1, background='#F0F0F0', wrap=WORD,
                                   relief='sunken')
        self.load_descricao.grid(row=2, column=3, rowspan=6, padx=5)
        self.load_descricao["state"] = DISABLED

    def enter(self, e):
        if self.e_aluno_id.get():
            if e.keysym == 'Return':
                self.buscar_aluno()
        else:
            self.load_nome_aluno['text'] = ''
            self.clear_all()
            for i in (self.e_titulo, self.e_autor, self.e_editora, ):
                i["state"] = DISABLED

    def devolver(self):
        for i in (self.e_titulo, self.e_autor, self.e_editora):
            i['state'] = NORMAL
        idaluno = self.e_aluno_id.get()
        cur = self.conn.cursor()
        if self.livro1.get() and self.livro2.get() and self.livro3.get():
            cur.execute(f"SELECT livrolocado FROM alugar WHERE id_aluno = {idaluno}")
            ean = cur.fetchall()
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[0][0]}")
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[1][0]}")
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[2][0]}")
        elif self.livro1.get() and self.livro2.get():
            cur.execute(f"SELECT livrolocado FROM alugar WHERE id_aluno = {idaluno}")
            ean = cur.fetchall()
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[0][0]}")
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[1][0]}")
        elif self.livro1.get() and self.livro3.get():
            cur.execute(f"SELECT livrolocado FROM alugar WHERE id_aluno = {idaluno}")
            ean = cur.fetchall()
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[0][0]}")
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[2][0]}")
        elif self.livro2.get() and self.livro3.get():
            cur.execute(f"SELECT livrolocado FROM alugar WHERE id_aluno = {idaluno}")
            ean = cur.fetchall()
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[1][0]}")
            cur.execute(f"DELETE FROM alugar WHERE id_aluno = {idaluno} AND livrolocado = {ean[2][0]}")
        elif self.livro1.get():
            cur.execute(f"SELECT ean FROM livros WHERE titulo = '{self.load_livro1['text']}'")
            ean = cur.fetchone()
            cur.execute(f"DELETE FROM alugar WHERE livrolocado = {ean[0]} AND id_aluno = {idaluno}")
        elif self.livro2.get():
            cur.execute(f"SELECT ean FROM livros WHERE titulo = '{self.load_livro2['text']}'")
            ean = cur.fetchone()
            cur.execute(f"DELETE FROM alugar WHERE livrolocado = {ean[0]} AND id_aluno = {idaluno}")
        elif self.livro3.get():
            cur.execute(f"SELECT ean FROM livros WHERE titulo = '{self.load_livro3['text']}'")
            ean = cur.fetchone()
            cur.execute(f"DELETE FROM alugar WHERE livrolocado = {ean[0]} AND id_aluno = {idaluno}")

        self.livro1.set(0)
        self.livro2.set(0)
        self.livro3.set(0)
        self.clear()
        self.load_qnt()
        self.conn.commit()

    def alugar(self):
        selecionado = self.tree.focus()

        cur = self.conn.cursor()
        cur.execute(f"SELECT ean FROM livros WHERE titulo = '{self.tree.item(selecionado).get('values')[0]}'")
        ean = cur.fetchone()

        cur.execute(
            f"SELECT livrolocado FROM alugar WHERE id_aluno = {self.e_aluno_id.get()} AND livrolocado = {ean[0]}")
        alugado = cur.fetchone()
        if alugado:
            messagebox.showinfo('Informação', 'Aluno já está em posse deste livro.')
        else:
            cur.execute(f"INSERT INTO alugar VALUES (NOW(), {ean[0]}, {self.e_aluno_id.get()})")
        self.load_qnt()
        self.conn.commit()

    # Carrega a quantidade de livros o aluno possui atualmente com ele
    def load_qnt(self):
        cur = self.conn.cursor()
        aluno = self.e_aluno_id.get()
        cur.execute(f"SELECT count(id_aluno) FROM alugar WHERE id_aluno = {aluno}")
        qnt = cur.fetchone()
        cur.execute(f"SELECT livros.titulo FROM livros INNER JOIN alugar ON alugar.livrolocado = livros.ean "
                    f"WHERE id_aluno = {aluno}")
        livros = cur.fetchall()
        # Caso possua três livros, não permite alugar outro, precisa devolver algum.
        if qnt[0] == 3:
            for i in (self.e_titulo, self.e_autor, self.e_editora, self.b_alugar):
                i["state"] = DISABLED

            for i in (self.check_livro1, self.check_livro2, self.check_livro3, self.b_devolver):
                i["state"] = NORMAL

            self.load_livro1["text"] = livros[0][0]
            self.load_livro2["text"] = livros[1][0]
            self.load_livro3["text"] = livros[2][0]

            self.clear_book_info()

            messagebox.showinfo("Informação", "O aluno possui 3 livros alugados. "
                                              "\nPara alugar outro livro, precisa devolver algum que já possui.")
            # return 0
        else:
            if qnt[0] == 0:
                self.b_alugar["state"] = NORMAL
                for i in (self.check_livro1, self.check_livro2, self.check_livro3, self.b_devolver):
                    i["state"] = DISABLED
            else:
                self.b_alugar["state"] = NORMAL
                self.b_devolver["state"] = NORMAL
                if qnt[0] == 1:
                    # Informa qual o livro alugado
                    self.load_livro1["text"] = livros[0][0]
                    self.check_livro1["state"] = NORMAL
                    self.check_livro2["state"] = DISABLED
                    self.check_livro3["state"] = DISABLED
                elif qnt[0] == 2:
                    # Informa qual o livro alugado
                    self.load_livro1["text"] = livros[0][0]
                    self.load_livro2["text"] = livros[1][0]
                    self.check_livro1["state"] = NORMAL
                    self.check_livro2["state"] = NORMAL
                    self.check_livro3["state"] = DISABLED

    # Carrega os livros na lista
    def loadbooks(self, data):
        self.tree.delete(*self.tree.get_children())
        if self.e_titulo.get() == '' and self.e_autor.get() == '' and self.e_editora.get() == '':
            self.tree.insert('', END, values=('', '', ''))
        else:
            for i in data:
                self.tree.insert('', END, values=(i[0], i[1], i[2]))

    # Carrega os livros em uma lista e também mostra na caixa de exibição para seleção
    def load_lista(self, e):
        cur = self.conn.cursor()
        if self.e_titulo.get():
            if self.e_autor.get():
                if self.e_editora.get():  # Todos os campos digitados
                    cur.execute(f"SELECT livros.titulo, autor.nome, editora.nome FROM livros "
                                f"INNER JOIN autor ON autor.id = livros.idautor "
                                f"INNER JOIN editora ON editora.id = livros.ideditora "
                                f"WHERE livros.titulo ILIKE '%{self.e_titulo.get()}%' "
                                f"AND autor.nome ILIKE '%{self.e_autor.get()}%'"
                                f"AND editora.nome ILIKE '%{self.e_editora.get()}%'")
                else:  # Titulo e autor
                    cur.execute(f"SELECT livros.titulo, autor.nome, editora.nome FROM livros "
                                f"INNER JOIN autor ON autor.id = livros.idautor "
                                f"INNER JOIN editora ON editora.id = livros.ideditora "
                                f"WHERE livros.titulo ILIKE '%{self.e_titulo.get()}%' "
                                f"AND autor.nome ILIKE '%{self.e_autor.get()}%'")
            else:
                if self.e_editora.get():
                    cur.execute(f"SELECT livros.titulo, autor.nome, editora.nome FROM livros "
                                f"INNER JOIN autor ON autor.id = livros.idautor "
                                f"INNER JOIN editora ON editora.id = livros.ideditora "
                                f"WHERE livros.titulo ILIKE '%{self.e_titulo.get()}%' "
                                f"AND editora.nome ILIKE '%{self.e_editora.get()}%'")
                else:
                    cur.execute(f"SELECT livros.titulo, autor.nome, editora.nome FROM livros "
                                f"INNER JOIN autor ON autor.id = livros.idautor "
                                f"INNER JOIN editora ON editora.id = livros.ideditora "
                                f"WHERE livros.titulo ILIKE '%{self.e_titulo.get()}%' ")
        else:
            if self.e_autor.get():
                if self.e_editora.get():
                    cur.execute(f"SELECT livros.titulo, autor.nome, editora.nome FROM livros "
                                f"INNER JOIN autor ON autor.id = livros.idautor "
                                f"INNER JOIN editora ON editora.id = livros.ideditora "
                                f"WHERE autor.nome ILIKE '%{self.e_autor.get()}%'"
                                f"AND editora.nome ILIKE '%{self.e_editora.get()}%'")
                else:
                    cur.execute(f"SELECT livros.titulo, autor.nome, editora.nome FROM livros "
                                f"INNER JOIN autor ON autor.id = livros.idautor "
                                f"INNER JOIN editora ON editora.id = livros.ideditora "
                                f"WHERE autor.nome ILIKE '%{self.e_autor.get()}%'")
            else:
                cur.execute(f"SELECT livros.titulo, autor.nome, editora.nome FROM livros "
                            f"INNER JOIN autor ON autor.id = livros.idautor "
                            f"INNER JOIN editora ON editora.id = livros.ideditora "
                            f"WHERE editora.nome ILIKE '%{self.e_editora.get()}%'")

        data = cur.fetchall()

        self.loadbooks(data)

    # Limpa os livros alugados
    def clear(self):
        self.load_livro1["text"] = ""
        self.load_livro2["text"] = ""
        self.load_livro3["text"] = ""

    def clear_book_info(self):
        self.load_titulo["text"] = ''
        self.load_ean["text"] = ''
        self.load_npaginas["text"] = ''
        self.load_ano["text"] = ''
        self.load_idioma["text"] = ''
        self.load_genero["text"] = ''
        self.load_avaliacao["text"] = ''

        self.load_autor["text"] = ''
        self.load_editora["text"] = ''

        self.load_descricao["state"] = NORMAL
        self.load_descricao.delete('1.0', END)
        self.load_descricao["state"] = DISABLED

        # Limpa as entradas
        for i in (self.e_autor, self.e_titulo, self.e_editora):
            i['state'] = NORMAL
        self.e_autor.delete(0, END)
        self.e_titulo.delete(0, END)
        self.e_editora.delete(0, END)
        for i in (self.e_autor, self.e_titulo, self.e_editora):
            i['state'] = DISABLED
        self.tree.delete(*self.tree.get_children())

    def clear_all(self):
        self.clear()
        self.clear_book_info()
        self.e_aluno_id.delete(0, END)
        self.load_nome_aluno['text'] = ''
        self.check_livro1['state'] = DISABLED
        self.check_livro2['state'] = DISABLED
        self.check_livro3['state'] = DISABLED
        self.e_autor.delete(0, END)
        self.e_titulo.delete(0, END)
        self.e_editora.delete(0, END)
        self.b_devolver["state"] = DISABLED
        self.b_alugar["state"] = DISABLED
        self.e_aluno_id.focus_set()

    # Efetua busca do aluno caso exista, carrega os livros caso alugado, etc.
    def buscar_aluno(self):
        # Limpa todos os dados do livro
        self.clear_book_info()
        cur = self.conn.cursor()
        self.tree.delete(*self.tree.get_children())
        if self.e_aluno_id.get():
            # Caso seja digitado algo diferente de número no campo ID, uma mensagem de erro aparece
            if self.e_aluno_id.get().isnumeric():
                self.clear()  # Limpa a tela caso tenha algo
                cur.execute(f"SELECT nome FROM aluno WHERE id = {self.e_aluno_id.get()}")
                nome = cur.fetchone()

                if nome:
                    self.load_nome_aluno['text'] = nome[0]  # Carrega o nome do aluno

                    for i in (self.e_titulo, self.e_autor, self.e_editora,):
                        i["state"] = NORMAL

                    self.load_qnt()
                else:
                    self.load_nome_aluno["text"] = ""
                    for i in (self.e_titulo, self.e_autor, self.e_editora,
                              self.check_livro1, self.check_livro2, self.check_livro3,):
                        i["state"] = DISABLED

                    messagebox.showwarning('Erro', 'O ID informado não existe')
            else:
                messagebox.showwarning('Erro', 'Permitido apenas números no campo ID')
        else:
            messagebox.showwarning('Em branco', 'Digite o ID a ser pesquisado')

    def loadbookinfo(self, e):
        treevalues = self.tree.focus()
        cur = self.conn.cursor()
        try:
            cur.execute(f"SELECT titulo, ean, npaginas, ano, descricao, idioma, genero, avaliacao FROM livros "
                        f"WHERE titulo = '{self.tree.item(treevalues).get('values')[0]}'")
            teste = cur.fetchone()

            self.load_titulo["text"] = teste[0]
            self.load_ean["text"] = teste[1]
            self.load_npaginas["text"] = teste[2]
            self.load_ano["text"] = teste[3]
            self.load_idioma["text"] = teste[5]
            self.load_genero["text"] = teste[6]
            self.load_avaliacao["text"] = teste[7]

            self.load_autor["text"] = self.tree.item(treevalues).get('values')[1]
            self.load_editora["text"] = self.tree.item(treevalues).get('values')[2]

            self.load_descricao["state"] = NORMAL
            self.load_descricao.delete('1.0', END)
            self.load_descricao.insert('1.0', teste[4])
            self.load_descricao["state"] = DISABLED
        except IndexError:
            print('Não existe nada na tela ou nada foi selecionado')


if __name__ == '__main__':
    app = Biblioteca()
    app.mainloop()
