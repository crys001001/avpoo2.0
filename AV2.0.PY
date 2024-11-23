# import mysql.connector
# from mysql.connector import Error

# # Função para conectar ao banco de dados
# def conectar_banco():
#     try:
#         conn = mysql.connector.connect(
#             host='127.0.0.1',  # Pode ser 'localhost' ou o IP do seu servidor MySQL
#             database='clinicapopular',  # Nome do seu banco de dados
#             user='root',  # Seu nome de usuário do MySQL
#             password='1234'  # A senha do seu usuário
#         )
#         if conn.is_connected():
#             print("Conexão com o banco de dados bem-sucedida!")
#         return conn
#     except Error as e:
#         print("Erro ao conectar ao banco de dados:", e)
#         return None

# # Função para inserir um paciente no banco de dados
# def inserir_paciente(conn, paciente):
#     cursor = conn.cursor()
#     query = """INSERT INTO paciente (nome, idade, cpf, endereco, historico) 
#                VALUES (%s, %s, %s, %s, %s)"""
#     values = (paciente.nome, paciente.idade, paciente.cpf, paciente.endereco, paciente.historico)
#     cursor.execute(query, values)
#     conn.commit()  # Confirma a inserção
#     print("Paciente inserido com sucesso!")



# class Pessoa:
#     def __init__(self, nome, idade, cpf, endereco="Endereço não informado"):
#         self.nome = nome
#         self.idade = idade
#         self._cpf = cpf  # Encapsulando o CPF
#         self.endereco = endereco

#     @property
#     def cpf(self):
#         return self._cpf

#     @cpf.setter
#     def cpf(self, novo_cpf):
#         self._cpf = novo_cpf  # Setter para o CPF

#     def __str__(self):
#         return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Endereço: {self.endereco}"

# # Classe Paciente
# class Paciente(Pessoa):
#     def __init__(self, nome, idade, cpf, endereco, historico):
#         super().__init__(nome, idade, cpf, endereco)
#         self._historico = historico  # Encapsulando o histórico

#     @property
#     def historico(self):
#         return self._historico

#     @historico.setter
#     def historico(self, novo_historico):
#         self._historico = novo_historico  # Setter para o histórico

#     def __str__(self):
#         return super().__str__() + f", Histórico: {self.historico}"

# # Classe Medico
# class Medico(Pessoa):
#     def __init__(self, nome, idade, cpf, endereco, especialidade):
#         super().__init__(nome, idade, cpf, endereco)
#         self.especialidade = especialidade

#     def __str__(self):
#         return super().__str__() + f", Especialidade: {self.especialidade}"

# # Classe Prontuario
# class Prontuario:
#     def __init__(self, paciente, diagnostico, observacao):
#         self.paciente = paciente
#         self._diagnostico = diagnostico  # Encapsulando o diagnóstico
#         self.observacao = observacao

#     @property
#     def diagnostico(self):
#         return self._diagnostico

#     @diagnostico.setter
#     def diagnostico(self, novo_diagnostico):
#         self._diagnostico = novo_diagnostico  # Setter para o diagnóstico

#     def __str__(self):
#         return f"Paciente: {self.paciente.nome}, Diagnóstico: {self.diagnostico}, Observação: {self.observacao}"

# # Classe Consulta
# class Consulta:
#     def __init__(self, paciente, medico, data, hora, motivo):
#         self.paciente = paciente
#         self.medico = medico
#         self.data = data
#         self.hora = hora
#         self.motivo = motivo

#     def __str__(self):
#         return f"Consulta: {self.motivo}, Data: {self.data}, Hora: {self.hora}, Paciente: {self.paciente.nome}, Médico: {self.medico.nome}"

# # Função para obter dados de entrada
# def input_paciente():
#     nome = input("Nome do paciente: ")
#     idade = int(input("Idade do paciente: "))
#     cpf = input("CPF do paciente: ")
#     endereco = input("Endereço do paciente: ")
#     historico = input("Histórico do paciente: ")
#     return Paciente(nome, idade, cpf, endereco, historico)

# def input_medico():
#     nome = input("Nome do médico: ")
#     idade = int(input("Idade do médico: "))
#     cpf = input("CPF do médico: ")
#     endereco = input("Endereço do médico: ")
#     especialidade = input("Especialidade do médico: ")
#     return Medico(nome, idade, cpf, endereco, especialidade)

# def input_prontuario(paciente):
#     diagnostico = input("Diagnóstico do paciente: ")
#     observacao = input("Observação do paciente: ")
#     return Prontuario(paciente, diagnostico, observacao)

# def input_consulta(paciente, medico):
#     data = input("Data da consulta (formato: DD/MM/AAAA): ")
#     hora = input("Hora da consulta (formato: HH:MM): ")
#     motivo = input("Motivo da consulta: ")
#     return Consulta(paciente, medico, data, hora, motivo)

# # Entrada de dados
# paciente1 = input_paciente()
# medico1 = input_medico()
# prontuario1 = input_prontuario(paciente1)
# consulta1 = input_consulta(paciente1, medico1)

# # Exibindo as informações
# print("\n--- Informações do Paciente ---")
# print(paciente1)

# print("\n--- Informações do Médico ---")
# print(medico1)

# print("\n--- Informações do Prontuário ---")
# print(prontuario1)

# print("\n--- Informações da Consulta ---")
# print(consulta1)
import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados
def conectar_banco():
    try:
        conn = mysql.connector.connect(
            host='localhost',  # Pode ser 'localhost' ou o IP do seu servidor MySQL
            database='ClinicaPopular',  # Nome do seu banco de dados
            user='root',  # Seu nome de usuário do MySQL
            password='1234'  # A senha do seu usuário
        )
        if conn.is_connected():
            print("Conexão com o banco de dados bem-sucedida!")
        return conn
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

# Função para inserir uma pessoa no banco de dados
def inserir_pessoa(conn, pessoa):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Pessoa (nome, idade, _cpf, endereco) 
                   VALUES (%s, %s, %s, %s)"""
        values = (pessoa.nome, pessoa.idade, pessoa.cpf, pessoa.endereco)
        cursor.execute(query, values)
        conn.commit()  # Confirma a inserção
        print("Pessoa inserida com sucesso!")
    except Error as e:
        print("Erro ao inserir pessoa:", e)

# Função para inserir um paciente no banco de dados
def inserir_paciente(conn, paciente):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Paciente (id_pessoa) 
                   VALUES ((SELECT id_pessoa FROM Pessoa WHERE _cpf = %s))"""
        values = (paciente.cpf,)
        cursor.execute(query, values)
        conn.commit()  # Confirma a inserção
        print("Paciente inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir paciente:", e)

# Função para inserir um médico no banco de dados
def inserir_medico(conn, medico):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Medico (id_pessoa, especialidade) 
                   VALUES ((SELECT id_pessoa FROM Pessoa WHERE _cpf = %s), %s)"""
        values = (medico.cpf, medico.especialidade)
        cursor.execute(query, values)
        conn.commit()  # Confirma a inserção
        print("Médico inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir médico:", e)

# Função para inserir um prontuário no banco de dados
def inserir_prontuario(conn, prontuario):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Prontuario (id_paciente, _diagnostico, observacoes) 
                   VALUES ((SELECT id_paciente FROM Paciente WHERE id_pessoa = (SELECT id_pessoa FROM Pessoa WHERE _cpf = %s)), %s, %s)"""
        values = (prontuario.paciente.cpf, prontuario.diagnostico, prontuario.observacao)
        cursor.execute(query, values)
        conn.commit()  # Confirma a inserção
        print("Prontuário inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir prontuário:", e)

# Função para inserir uma consulta no banco de dados
def inserir_consulta(conn, consulta):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Consulta (id_paciente, id_medico, data, horario) 
                   VALUES ((SELECT id_paciente FROM Paciente WHERE id_pessoa = (SELECT id_pessoa FROM Pessoa WHERE _cpf = %s)), 
                           (SELECT id_medico FROM Medico WHERE id_pessoa = (SELECT id_pessoa FROM Pessoa WHERE _cpf = %s)), 
                           CURDATE(), CURTIME())"""
        values = (consulta.paciente.cpf, consulta.medico.cpf)
        cursor.execute(query, values)
        conn.commit()  # Confirma a inserção
        print("Consulta inserida com sucesso!")
    except Error as e:
        print("Erro ao inserir consulta:", e)

# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, cpf, endereco="Endereço não informado"):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # Encapsulando o CPF
        self.endereco = endereco

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf  # Setter para o CPF

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Endereço: {self.endereco}"

# Classe Paciente
class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf, endereco):
        super().__init__(nome, idade, cpf, endereco)

    def __str__(self):
        return super().__str__()

# Classe Medico
class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, especialidade):
        super().__init__(nome, idade, cpf, endereco)
        self.especialidade = especialidade

    def __str__(self):
        return super().__str__() + f", Especialidade: {self.especialidade}"

# Classe Prontuario
class Prontuario:
    def __init__(self, paciente, diagnostico, observacao):
        self.paciente = paciente
        self._diagnostico = diagnostico  # Encapsulando o diagnóstico
        self.observacao = observacao

    @property
    def diagnostico(self):
        return self._diagnostico

    @diagnostico.setter
    def diagnostico(self, novo_diagnostico):
        self._diagnostico = novo_diagnostico  # Setter para o diagnóstico

    def __str__(self):
        return f"Paciente: {self.paciente.nome}, Diagnóstico: {self.diagnostico}, Observação: {self.observacao}"

# Classe Consulta
class Consulta:
    def __init__(self, paciente, medico):
        self.paciente = paciente
        self.medico = medico

    def __str__(self):
        return f"Consulta: Paciente: {self.paciente.nome}, Médico: {self.medico.nome}"

# Função para obter dados de entrada
def input_paciente():
    nome = input("Nome do paciente: ")
    idade = int(input("Idade do paciente: "))
    cpf = input("CPF do paciente: ")
    endereco = input("Endereço do paciente: ")
    return Paciente(nome, idade, cpf, endereco)

def input_medico():
    nome = input("Nome do médico: ")
    idade = int(input("Idade do médico: "))
    cpf = input("CPF do médico: ")
    endereco = input("Endereço do médico: ")
    especialidade = input("Especialidade do médico: ")
    return Medico(nome, idade, cpf, endereco, especialidade)

def input_prontuario(paciente):
    diagnostico = input("Diagnóstico do paciente: ")
    observacao = input("Observação do paciente: ")
    return Prontuario(paciente, diagnostico, observacao)

def input_consulta(paciente, medico):
    return Consulta(paciente, medico)

# Entrada de dados
paciente1 = input_paciente()
medico1 = input_medico()
prontuario1 = input_prontuario(paciente1)
consulta1 = input_consulta(paciente1, medico1)

# Conectar ao banco
conn = conectar_banco()

# Inserir dados no banco
if conn:
    inserir_pessoa(conn, paciente1)
    inserir_paciente(conn, paciente1)
    inserir_medico(conn, medico1)
    inserir_prontuario(conn, prontuario1)
    inserir_consulta(conn, consulta1)

    # Fechar a conexão
    conn.close()

# Exibindo as informações
print("\n--- Informações do Paciente ---")
print(paciente1)

print("\n--- Informações do Médico ---")
print(medico1)

print("\n--- Informações do Prontuário ---")
print(prontuario1)

print("\n--- Informações da Consulta ---")
print(consulta1)
