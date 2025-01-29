# Explicação Detalhada da Sintaxe do Código

Este código em Python realiza a enumeração de serviços associados a números de portas fornecidos pelo usuário. Vamos explicar detalhadamente cada parte do código para um aluno iniciante entender sua estrutura e funcionamento.

---

## 🔹 1. Dicionário `port_services`
```python
port_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis"
}
```
### ✨ O que é um dicionário em Python?
- Um **dicionário** (`dict`) é uma estrutura de dados que armazena pares **chave-valor**.
- No nosso caso, as **chaves** são números de portas (ex: `21`, `22`, `80`) e os **valores** são os serviços correspondentes (ex: `"FTP"`, `"SSH"`, `"HTTP"`).
- Usamos `{}` para definir um dicionário e `:` para separar a chave do valor.

### 🔍 Exemplo de acesso a um valor no dicionário:
```python
print(port_services[80])  # Saída: HTTP
```
Isso retorna `"HTTP"`, pois `80` é a chave correspondente.

---

## 🔹 2. Função `enumerate_services(ports)`

```python
def enumerate_services(ports):
    services = []  # Criamos uma lista vazia para armazenar os serviços correspondentes
    
    for port in ports:  # Percorremos cada porta na lista de portas fornecidas
        if port in port_services:  # Se a porta estiver no dicionário
            services.append(port_services[port])  # Adicionamos o serviço correspondente
        else:
            services.append("Desconhecido")  # Caso contrário, adicionamos "Desconhecido"
    
    return services  # Retornamos a lista final de serviços
```

### ✨ O que é uma função?
- **Função** é um bloco de código reutilizável que executa uma tarefa específica.
- Definimos uma função usando `def nome_da_funcao():`.
- Ela pode receber **parâmetros** e pode **retornar** valores.

### 📌 Passo a passo do que acontece na função:
1. Criamos uma **lista vazia** chamada `services` para armazenar os serviços encontrados.
2. Usamos um **loop `for`** para percorrer cada número de porta na lista `ports`.
3. **Verificamos** se a porta está no dicionário `port_services`:
   - Se estiver, adicionamos o serviço correspondente à lista `services`.
   - Se não estiver, adicionamos `"Desconhecido"`.
4. **Retornamos** a lista de serviços ao final da função.

---

## 🔹 3. Função `main()`
```python
def main():
    ports_input = input("Digite os números das portas, separados por vírgula: ")
    
    ports = [int(port.strip()) for port in ports_input.split(",")]

    services = enumerate_services(ports)
    
    print(services)
```

### ✨ O que faz essa função?
- **Recebe a entrada do usuário**, que deve digitar os números das portas separados por vírgula.
- **Processa a entrada**:
  - `input()` recebe a string digitada.
  - `split(",")` separa os números onde houver vírgula, criando uma lista de strings.
  - `strip()` remove espaços extras.
  - `int()` converte cada número para inteiro.
  - Usamos **list comprehension** para criar a lista final de números de portas.
- **Chama a função `enumerate_services()`** para obter a lista de serviços correspondentes.
- **Imprime a lista de serviços** encontrada.

### 🔍 Explicação da List Comprehension:
```python
ports = [int(port.strip()) for port in ports_input.split(",")]
```
Isso equivale a:
```python
ports = []
for port in ports_input.split(","):
    ports.append(int(port.strip()))
```
Ou seja:
- **`split(",")`** separa os números em uma lista de strings.
- **`strip()`** remove espaços extras.
- **`int()`** converte a string para número.
- **O `for` percorre a lista e preenche a nova lista `ports`**.

---

## 🔹 4. Estrutura `if __name__ == "__main__"`
```python
if __name__ == "__main__":
    main()
```

### ✨ Para que serve essa estrutura?
- Em Python, esse bloco garante que a função `main()` só será executada **se o script for rodado diretamente**, e não se for importado como um módulo em outro código.

---

## 🔹 5. Entrada e Saída

### ✅ Entrada do usuário:
```
22, 80, 443
```
- O usuário digita os números das portas separados por vírgula.

### ✅ Processamento:
- A entrada é convertida para `[22, 80, 443]`.
- A função `enumerate_services()` busca os serviços correspondentes.

### ✅ Saída esperada:
```python
['SSH', 'HTTP', 'HTTPS']
```

---

## 🔹 6. Testando o Código com Exemplos

### 📌 Exemplo 1:
**Entrada:**  
```
21, 53, 3306
```
**Processamento:**  
- `21 → FTP`
- `53 → DNS`
- `3306 → MySQL`

**Saída:**
```python
['FTP', 'DNS', 'MySQL']
```

---

### 📌 Exemplo 2:
**Entrada:**  
```
23, 443, 8080
```
**Processamento:**  
- `23 → Telnet`
- `443 → HTTPS`
- `8080 → Não está no dicionário → "Desconhecido"`

**Saída:**
```python
['Telnet', 'HTTPS', 'Desconhecido']
```

---

## 🔹 Resumo da Sintaxe Utilizada

| Elemento | Explicação |
|----------|------------|
| `dict` | Dicionário para mapear portas e serviços. |
| `def` | Define uma função. |
| `return` | Retorna um valor de uma função. |
| `for` | Loop para percorrer listas. |
| `if ... else` | Estrutura condicional. |
| `input()` | Lê entrada do usuário. |
| `split(",")` | Divide uma string em partes. |
| `strip()` | Remove espaços extras. |
| `int()` | Converte string para número. |
| `list comprehension` | Forma compacta de criar listas. |
| `print()` | Exibe um resultado na tela. |
| `if __name__ == "__main__"` | Garante que o código só rode diretamente. |

---

## 🎯 Conclusão
Este código ensina conceitos fundamentais de Python, como:
✅ Dicionários  
✅ Funções  
✅ Estruturas de controle (`if`, `for`)  
✅ Manipulação de strings e listas  
✅ Entrada e saída de dados  

Agora, com essa explicação detalhada, um iniciante pode entender **cada parte do código** e como ele funciona! 🚀
