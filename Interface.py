class LoginWindow(QtWidgets.QWidget):
   def __init__(self):
       super().__init__()
       self.setWindowTitle('Login Window')
       self.resize(400, 200)
       self.init_ui()

   def init_ui(self):
  
       self.setWindowTitle('Login')
       self.setFixedSize(500, 400)
       self.setGeometry(700, 300, 10, 10)
       self.setStyleSheet("QMainWindow {background: SlateBlue;}")

      
       layout = QtWidgets.QVBoxLayout()
       layout.addWidget(self.username_label)
       layout.addWidget(self.username_input)
       layout.addWidget(self.password_label)
       layout.addWidget(self.password_input)
       layout.addWidget(self.login_button)
       self.setLayout(layout)

      
       self.login_button.clicked.connect(self.validate_login)

   def validate_login(self):
       username = self.username_input.text()
       password = self.password_input.text()

       if not username or not password:
           QtWidgets.QMessageBox.warning(self, 'Erro', 'Por favor, verifique os dados!')
           return

       with open('user_data.txt') as arquivo:
           dados = arquivo.readlines()
          
       validando_login = False
       for line in dados:
           linha_dados = line.split(':')
           if linha_dados[0] == username and linha_dados[1] == password:
               validando_login = True
               break

       if validando_login:
           QtWidgets.QMessageBox.information(self, 'Legal', 'Usuário cadastrado')
       else:
           QtWidgets.QMessageBox.warning(self, 'Erro', 'Usuário ou senha inválido')


class CadastroWindow(QtWidgets.QWidget):
   def __init__(self):
       super().__init__()
       self.setWindowTitle('Cadastro Window')
       self.resize(400, 200)
       self.init_ui()

   def entrada(self):
      
       self.username_label = QtWidgets.QLabel('Nome do Usuário:')
       self.username_input = QtWidgets.QLineEdit()
       self.password_label = QtWidgets.QLabel('Senha:')
       self.password_input = QtWidgets.QLineEdit()
       self.cadastro_button = QtWidgets.QPushButton('Cadastrar')

      
       layout = QtWidgets.QVBoxLayout()
       layout.addWidget(self.username_label)
       layout.addWidget(self.username_input)
       layout.addWidget(self.password_label)
       layout.addWidget(self.password_input)
       layout.addWidget(self.cadastro_button)
       self.setLayout(layout)

      
       self.cadastro_button.clicked.connect(self.cadastrar)

   def cadastrar(self):
       usuario = self.username_input.text()
       senha = self.password_input.text()

       if not usuario or not senha:
           QtWidgets.QMessageBox.warning(self, 'Erro', 'Por favor verifique seu usuário!')
           return

       # open file and append username/password
       with open('user_data.txt', 'a') as f:
           f.write(f'{usuario}:{senha}\n')

       QtWidgets.QMessageBox.information(self, 'Ótimo', 'Você foi cadastrado com sucesso!')


class BuscaWindow(QtWidgets.QWidget):
   def __init__(self):
       super().__init__()
       self.setWindowTitle('Busca Window')
       self.resize(400, 200)
       self.init_ui()

   def init_ui(self):
       # Widgets
       self.username_label = QtWidgets.QLabel('Usuário:')
       self.username_input = QtWidgets.QLineEdit()
       self.buscar_button = QtWidgets.QPushButton('Buscar')

       # Layout
       layout = QtWidgets.QVBoxLayout()
       layout.addWidget(self.username_label)
       layout.addWidget(self.username_input)
       layout.addWidget(self.buscar_button)
       self.setLayout(layout)

       self.buscar_button.clicked.connect(self.buscar)

   def buscar(self):
       username = self.username_input.text()

       if not username:
           QtWidgets.QMessageBox.warning(self, 'Erro', 'Por favor verifique o usuário')
           return

       with open('user_data.txt') as f:
           data = f.readlines()

       user_found = False
       for line in data:
           line_data = line.split(':')
           if line_data[0] == username:
               user_found = True
               password = line_data[1]
               break

       if user_found:
           QtWidgets.QMessageBox.information(self, 'Legal', f'Usuário: {username}\nPassword: {password}')
       else:
           QtWidgets.QMessageBox.warning(self, 'Erro', 'Usuário inválido')


def cancelar_login(self):
   self.close()


if __name__ == '__main__':
   app = QtWidgets.QApplication()
   window = LoginWindow()
   window.show()
   app.exec_()
