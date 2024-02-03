from guizero import App, Box, Text, TextBox, PushButton, Picture
import mysql.connector

def conectar():
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='aula_conexao_bd'
        )
        return con
    except mysql.connector.Error as erro:
        print(f'Erro ao conectar com o banco: {erro}')

'''Abaixo está as operações feitas no sgbd'''
def show_main_screen():
    pass

def confirm_insert(nome, email, sexo, telefone):
    nome = nome.value
    email = email.value
    sexo = sexo.value
    telefone = telefone.value
    
    conexao = conectar()
    cursor = conexao.cursor()

    inserir_cliente_query = (
        "INSERT INTO cliente (nome, email, sexo, telefone) "
        "VALUES (%s, %s, %s, %s)"
    )
    dados_cliente = (nome, email, sexo, telefone)
    cursor.execute(inserir_cliente_query, dados_cliente)
    conexao.commit()

    cursor.close()
    conexao.close()



def confirm_atualization(id_cliente, nome, email, sexo, telefone):
    id_cliente = id_cliente.value
    nome = nome.value
    email = email.value
    sexo = sexo.value
    telefone = telefone.value

    conexao = conectar()
    cursor = conexao.cursor()

    atualizar_cliente_query = (
        "UPDATE cliente "
        "SET nome=%s, email=%s, sexo=%s, telefone=%s "
        "WHERE id_cliente=%s"
    )

    dados_cliente = (nome, email, sexo, telefone, id_cliente)
    cursor.execute(atualizar_cliente_query, dados_cliente)
    conexao.commit()

    cursor.close()
    conexao.close()
    

def confirm_search(id_cliente_text):
    id_cliente = id_cliente_text.value

    conexao = conectar()
    cursor = conexao.cursor()

    buscar_cliente_query = "SELECT * FROM cliente WHERE id_cliente = %s"
    cursor.execute(buscar_cliente_query, (id_cliente,))

    usuario_buscado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if usuario_buscado:
        app.hide()

        search_result_screen = App("Resultado da Busca", width=350, height=700)
        search_result_screen.bg = "#FFFFFF"

        result_box = Box(search_result_screen, layout="grid")
        result_box.bg = "#FFFFFF"


        row = 0
        labels = ["ID do Cliente", "Nome", "Email", "Sexo", "Telefone"]
        for label, value in zip(labels, usuario_buscado):
            Text(result_box, label + ":", grid=[0, row], align="left", color="black")
            Text(result_box, str(value), grid=[1, row])
            row += 1

        

        search_result_screen.display()
    else:
        app.error("Erro na Busca", f"Não foi encontrado um cliente com o ID {id_cliente}")



def confirm_delete(id_cliente):
    id_cliente.value
    conexao = conectar()
    cursor = conexao.cursor()

    excluir_cliente_query = "DELETE FROM cliente WHERE id_cliente=%s"
    cursor.execute(excluir_cliente_query, (id_cliente.value,))  # Use id_cliente.value directly
    conexao.commit()

    cursor.close()
    conexao.close()



def insert():
        app.hide()

        insert_screen = App("Inserir Cliente", width=400, height=700)
        insert_screen.bg = "#FFFFFF"

        picture = Picture(insert_screen, image="imagens/linhas-de-calendario.png", width=350, height=350)

        insert_box = Box(insert_screen, layout="grid")
        insert_box.bg = "#FFFFFF"

        Text(insert_box, "Nome do usuário:", grid=[0, 0], align="left", color="black")
        nome = TextBox(insert_box, grid=[1, 0], width=20)

        Text(insert_box, "Email:", grid=[0, 1], align="left", color="black")
        email = TextBox(insert_box, grid=[1, 1], width=20)

        Text(insert_box, "Sexo:", grid=[0, 2], align="left", color="black")
        sexo = TextBox(insert_box, grid=[1, 2], width=20)

        Text(insert_box, "Telefone:", grid=[0, 3], align="left", color="black")
        telefone = TextBox(insert_box, grid=[1, 3], width=20)

        confirm_button = PushButton(insert_box, confirm_insert, args=[nome, email, sexo, telefone], text="Confirmar", grid=[3, 5])

       

        insert_screen.display()


def search():
    app.hide()


    insert_screen = App("Buscar Cliente", width=400, height=700)
    insert_screen.bg = "#FFFFFF"

    picture = Picture(insert_screen, image="imagens/linhas-de-calendario.png", width=350, height=350)

    
    insert_box = Box(insert_screen, layout="grid")
    insert_box.bg = "#FFFFFF"

    Text(insert_box, "Id do cliente que deseja buscar:", grid=[0, 0], align="left", color="black")
    id_cliente = TextBox(insert_box, grid=[1, 0], width=20)


    confirm_button = PushButton(insert_box, confirm_search, args=[id_cliente], text="Confirmar", grid=[1, 3])


    

 
    insert_screen.display()

def atualizar():
    app.hide()

 
    atualization_screen = App("Atualizar cliente", width=400, height=700)
    atualization_screen.bg = "#FFFFFF"

    
    picture = Picture(atualization_screen, image="imagens/linhas-de-calendario.png", width=350, height=350)

    atualization_box = Box(atualization_screen, layout="grid")
    atualization_box.bg = "#FFFFFF"

    Text(atualization_box, "ID do Cliente que deseja atualizar:", grid=[0, 0], align="left", color="black")
    id_cliente = TextBox(atualization_box, grid=[1, 0], width=20)


    Text(atualization_box, "Nome:", grid=[0, 2], align="left", color="black")
    nome = TextBox(atualization_box, grid=[1, 2], width=20)

    Text(atualization_box, "Email:", grid=[0, 3], align="left", color="black")
    email = TextBox(atualization_box, grid=[1, 3], width=20)

    Text(atualization_box, "Sexo:", grid=[0, 4], align="left", color="black")
    sexo = TextBox(atualization_box, grid=[1, 4], width=20)

    Text(atualization_box, "Telefone:", grid=[0, 5], align="left", color="black")
    telefone = TextBox(atualization_box, grid=[1, 5], width=20)

    confirm_button = PushButton(atualization_box, confirm_atualization, args=[id_cliente, nome, email, sexo, telefone], text="Confirmar", grid=[1, 6])



    atualization_screen.display()

def delete():
    app.hide()

    delete_screen = App("Deletar Cliente", width=500, height=700)
    delete_screen.bg = "#FFFFFF"

    picture = Picture(delete_screen, image="imagens/linhas-de-calendario.png", width=350, height=350)
    delete_box = Box(delete_screen, layout="grid")
    delete_box.bg = "#FFFFFF"

    Text(delete_box, "ID do Cliente que deseja Deletar:", grid=[0, 0], align="left", color="black")
    id_cliente = TextBox(delete_box, grid=[1, 0], width=20)


    confirm_button = PushButton(delete_box, confirm_delete, args=[id_cliente], text="Confirmar", grid=[3, 5])

    
    delete_screen.display()
def checarClient(username, password):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        
        check_login_query = "SELECT * FROM usuario WHERE usuario = %s AND senha = %s"
        cursor.execute(check_login_query, (username, password))

        result = cursor.fetchone()

        cursor.close()
        conexao.close()

        if result:
            print('Usuário pode acessar')
            return True
        else:
            print('Usuário não encontrado ou senha incorreta')
            return False

    except Exception as e:
        print(f"Erro de login: {e}")
        return False


def checandoLogin():
    username = username_entry.value
    password = password_entry.value

    if checarClient(username, password):
        app.info("Login bem-sucedido", "Bem-vindo, " + username)
        show_next_screen()
    else:
        app.error("Login falhou", "Usuário ou senha incorretos")

def show_next_screen():

    app.hide()

    
    next_screen = App("Menu Principal", width=400, height=700)
    next_screen.bg = "#181F29"

    button_box = Box(next_screen, layout="grid")
    button_box.bg = "#ffffff"

    
    ButaoInsert = PushButton(button_box, text="Inserir Usuário", command=insert, grid=[0, 0], padx=10, pady=10)
    BotaoUpdate = PushButton(button_box, text="Atualizar Cliente", command=atualizar, grid=[1, 0], padx=10, pady=10)
    BotaoSearch = PushButton(button_box, text="Buscar Cliente",command=search,  grid=[0, 1], padx=10, pady=10)
    BotaoDel = PushButton(button_box, text="Deletar", command=delete, grid=[1, 1], padx=10, pady=10)

   

app = App(width=400, height=700)
app.bg = "#181F29"

title = Text(app, "", size=20, color="white")
title.font = "Arial"
background_text = Text(app, "TechFlow", size=20, color="white", grid=[1,0])
background_text.font = "Arial"
background_text.bg = "#F03737"

title = Text(app, "Gerencie o banco de dados", size=20, color="white")
title.font = "Arial"


picture = Picture(app, image="imagens/logo(1).png", width=350, height=350)
title = Text(app, "Comece com seus dados", size=15, color="white")
title.font = "Verdana"
center_box = Box(app, layout="grid")
center_box.bg = "#FFFFFF"


empty_space_top = Text(center_box, "", grid=[1, 0])


Text(center_box, "Usuário:", grid=[0, 1], align="left", color="black")
username_entry = TextBox(center_box, grid=[1, 1], width=35, height=45)

Text(center_box, "Senha:", grid=[0, 2], align="left", color="black")
password_entry = TextBox(center_box, grid=[1, 2], width=35, height=20, hide_text=True)

empty_space_bottom = Text(center_box, "", grid=[1, 3])

login_button = PushButton(center_box, checandoLogin, text="Login", grid=[1, 4], align="center")
login_button.text_color = "white"
login_button.bg = "#F03737"
login_button.font = "Arial"

login_button.when_mouse_over = "black"
login_button.when_mouse_out = "#000000"


app.display()