# Dicionário que mapeia números de portas aos serviços correspondentes
port_services = {
    21: "FTP",      # Serviço de transferência de arquivos
    22: "SSH",      # Secure Shell (acesso remoto seguro)
    23: "Telnet",   # Protocolo de acesso remoto inseguro
    25: "SMTP",     # Serviço de envio de emails
    53: "DNS",      # Serviço de tradução de nomes de domínio
    80: "HTTP",     # Protocolo de transferência de hipertexto (web)
    110: "POP3",    # Serviço de recebimento de emails
    143: "IMAP",    # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",   # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",    # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL", # Banco de dados PostgreSQL
    6379: "Redis"   # Banco de dados Redis
}

# Função que realiza a enumeração de serviços
def enumerate_services(ports):
    # Inicializamos uma lista para armazenar os serviços correspondentes
    services = []
    
    # Iteramos sobre cada porta fornecida na lista de portas
    for port in ports:
        # Verificamos se a porta existe no dicionário de serviços
        if port in port_services:
            # Se existir, adicionamos o serviço correspondente à lista de serviços
            services.append(port_services[port])
        else:
            # Se a porta não estiver mapeada, adicionamos "Desconhecido"
            services.append("Desconhecido")
    
    return services

# Função principal que lida com a entrada do usuário e exibe o resultado:
def main():
    ports_input = input("Digite os números das portas, separados por vírgula: ")
    
    # Convertemos a string de entrada para uma lista de inteiros (números de portas)
    # strip() remove espaços em branco e split(",") separa por vírgula
    ports = [int(port.strip()) for port in ports_input.split(",")]

    # Chamamos a função de enumeração para obter a lista de serviços correspondentes
    services = enumerate_services(ports)
    
    print(services)

# Ponto de entrada do script
if __name__ == "__main__":
    main()
