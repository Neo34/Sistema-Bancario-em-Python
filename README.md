# 💰 Sistema Bancário Simples em Python

Este é um projeto de **sistema bancário básico** desenvolvido em Python, criado como exercício de prática de programação.  
O sistema permite que o usuário faça depósitos, saques, consulte o extrato e encerre o programa.  

---

## 📌 Funcionalidades
- [x] **Depósito**: permite adicionar valores positivos à conta.  
- [x] **Saque**: possui regras de limite:
  - Saque máximo de R$ 500,00 por operação  
  - Limite de 3 saques por sessão  
  - Não permite sacar valores maiores que o saldo disponível  
- [x] **Extrato**: mostra todas as movimentações realizadas (depósitos e saques) e o saldo final.  
- [x] **Sair**: finaliza a execução do programa.  

---

## 🛠️ Tecnologias Utilizadas
- Python 3.x

---

## 📂 Estrutura do Projeto
.
├── banco.py # Código principal do sistema bancário
└── README.md # Documentação do projeto


---

## ▶️ Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git

   cd sistema-bancario
   python banco.py
📜 Licença

Este projeto foi desenvolvido para fins de estudo.
Sinta-se à vontade para usar e modificar!
