# 🎮 Jogo da Forca (Hangman em Python)

Um clássico dos tempos antigos rodando em Python puro no terminal. Sem dependência externa, só lógica e diversão.

---

## 📌 Sobre o projeto

Este é um jogo da forca desenvolvido em Python onde o jogador tenta adivinhar uma palavra aleatória antes de completar o boneco da forca.

As palavras são carregadas de um arquivo `.txt` e o jogo roda diretamente no terminal.

---

## ⚙️ Funcionalidades

- Sorteio aleatório de palavras
- Controle de letras corretas e erradas
- Interface ASCII da forca no terminal
- Limpeza de tela automática
- Sistema de vitória e derrota
- Validação de tentativas repetidas

---

## 🧠 Como funciona

- O jogo escolhe uma palavra aleatória
- O jogador tenta adivinhar letra por letra
- Letras corretas são reveladas
- Letras erradas constroem o boneco da forca
- 6 erros = derrota
- Palavra completa = vitória

---

## 📁 Estrutura do projeto

```bash
Game_Forca/
│
├── main.py
├── palavras/
│   └── palavras_200.txt
└── README.md
```
---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd Game_Forca
```

### 2. Execute o jogo

    
    python main.py

---

## 📌 Conclusão

Este projeto foi desenvolvido com o objetivo de praticar lógica de programação e conceitos fundamentais de Python.

Apesar de simples, ele reforça habilidades importantes como controle de fluxo, manipulação de dados e organização de código.