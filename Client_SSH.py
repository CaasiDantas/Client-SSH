import paramiko

host = input("Digite o host: ")

user = input("Digite o usuário: ")

senha = input("Digite a senha: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=senha)

while True:

    print()

    comando = input("Digite o comando que deseja realizar: ")

    print()

    stdin, stdout, stderr = client.exec_command(comando)

    for line in stdout.readlines():
        print(line.strip())

    erro = stderr.readlines()

    if erro:
        print(f"Comando não existente {erro}")
