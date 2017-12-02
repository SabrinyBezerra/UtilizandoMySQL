import mysql.connector
import usuario

try:
def main():
    conn = mysql.connector.connect(user='root',

                                password='ifpbinfo',

                                host='192.168.0.104',

                                database='Rede_Social')

cursor = conn.cursor()

db = ("SELECT nome, email, senha, profissao, sexo, data_nasc FROM TB_Usuario")

cursor.execute(db)

linhas = cursor.fetchall()

for ( nome, email, senha, profissao, sexo, data_nasc) in linhas:
    print( nome, email, senha, profissao, sexo, data_nasc)
    print("Nome:",nome[0])
        print("Login:", email[1])
        print("Senha:", senha[2])
        print("Profissão:", profissao[3])
        print("Gênero:", sexo[4])
        print("Data Nascimento:", data_nasc[5])

cursor.close()

except mysql.connector.Error as err:

print("Problema no banco de dados!")

else:
conn.close()

if __name__ == '__main__':
    main()
