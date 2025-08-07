# 📖 Projeto de Estudo: Comunicação via Sockets em Python

Projeto desenvolvido com o objetivo de compreender na prática a comunicação entre cliente e servidor utilizando **Sockets em Python**, abordando os protocolos **TCP (confiável)** e **UDP (não confiável)**.

## 📌 Objetivo

Demonstrar o uso básico de sockets para:
* Criar um servidor Web simples usando TCP.
* Implementar um cliente "ping" e um servidor "pong" usando UDP.
* Medir a latência de uma conexão (RTT - Round Trip Time).
* Simular perda de pacotes em redes não confiáveis.

## 🧩 Funcionalidades

### 🔹 Servidor TCP (`servidor_web_tcp.py`)
* Servidor HTTP que responde a requisições de navegadores.
* Serve páginas e arquivos estáticos (HTML, CSS, imagens).
* Retorna um erro `404 Not Found` caso o arquivo solicitado não seja encontrado.

### 🔹 Cliente UDP (`cliente_ping.py`)
* Envia 10 mensagens "Ping" ao servidor UDP.
* Mede o tempo de resposta (RTT) para cada pacote recebido.
* Possui um timeout de 1 segundo e exibe uma mensagem de "Tempo limite excedido" caso não haja resposta.

### 🔹 Servidor UDP (`servidor_udp.py`)
* Recebe pacotes do cliente e os retorna com a mensagem em letras maiúsculas.
* Simula a perda de pacotes de forma aleatória (aproximadamente 40% de chance de perda).

## 🗂️ Estrutura do Projeto

projeto-sockets/

├── servidor_web_tcp.py         # Servidor Web com socket TCP

├── servidor_udp.py             # Servidor de "pong" com socket UDP

├── cliente_ping.py             # Cliente de "ping" com medição de RTT

├── index.html                  # Página web principal do servidor TCP

├── style.css                   # Arquivo de estilos para a página HTML

├── qrcode_perguntas.png        # Imagem usada no servidor TCP

└── README.md                   # Este arquivo


## ▶️ Como Executar

### 1. Requisitos
* Python 3.x instalado.
* Navegador web (Chrome, Firefox, etc.).
* Os scripts utilizam bibliotecas padrão do Python (socket, time, random, os, sys).

### 2. Passo a passo

#### 🔸 Servidor Web (TCP)
1.  Abra um terminal e execute o servidor na porta `8080`:
    ```bash
    python servidor_web_tcp.py
    ```
2.  Acesse a página no seu navegador:
    ```
    http://localhost:8080
    ```
    _Se a porta 8080 estiver em uso, o script irá falhar. Você pode alterar a porta no arquivo `servidor_web_tcp.py`._

#### 🔸 Servidor Ping (UDP)
1.  Abra **outro** terminal e execute o servidor UDP na porta `1200`:
    ```bash
    python servidor_udp.py
    ```
    _O servidor irá aguardar pacotes de ping e responder a alguns deles, simulando perdas._

#### 🔸 Cliente Ping (UDP)
1.  Abra um **terceiro** terminal e execute o cliente UDP:
    ```bash
    python cliente_ping.py
    ```
2.  A saída esperada mostrará uma mistura de RTT (tempo de resposta) e timeouts:
    ```
    Resposta de 127.0.0.1:1200, RTT: 20.83 ms
    Tempo limite excedido para Ping 2
    Resposta de 127.0.0.1:1200, RTT: 4.22 ms
    ...
    ```

## 📚 Aprendizados

Este projeto visa demonstrar conceitos importantes de redes e programação com sockets, incluindo:

| Conceito | Aplicação |
| :--- | :--- |
| **TCP** | Comunicação confiável, orientada a conexão, usada no servidor web. |
| **UDP** | Comunicação rápida, sem garantias de entrega, usada no sistema ping. |
| **Socket** | Interface de programação para comunicação de rede em Python. |
| **RTT (Round Trip Time)** | Medição do tempo de ida e volta de uma mensagem pelo cliente. |
| **Timeout** | Tratamento de falhas em redes não confiáveis, como a espera por uma resposta do servidor. |
| **Perda de Pacotes** | Simulação de falhas de rede no servidor UDP para demonstrar o comportamento não confiável do protocolo. |

## 💡 Ideias para Melhorias Futuras
* **Servidor Web**: Mudar o tema da página HTML para algo mais pessoal, como um portfólio simples, e praticar o desenvolvimento web.
* **Servidor TCP**: Adicionar a capacidade de servir outros tipos de arquivos ou rotas mais complexas.
* **Sistema Ping UDP**: Calcular estatísticas de perda de pacotes e RTT médio no cliente.

## 🎓 Autora
Amanda Machado

## 📬 Contato

**LinkedIn:**
www.linkedin.com/in/amanda-machado-a78b43215
