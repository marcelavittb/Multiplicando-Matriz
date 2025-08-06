# 🔢 Multiplicação de Matrizes NxN em Python

Este projeto realiza a leitura de **duas matrizes NxN** a partir de arquivos Excel, verifica se elas são quadradas, e realiza a **multiplicação passo a passo** utilizando funções personalizadas de **soma** e **multiplicação**.

---

## 📂 Estrutura do Projeto

```
MultiplicacaoMatrizes/
│
├── matriz1.xlsx     # Matriz de entrada 1 (exemplo 3x3)
├── matriz2.xlsx     # Matriz de entrada 2 (exemplo 3x3)
├── matriz.py        # Código Python principal
└── README.md        # Documentação do projeto
```

---

## ⚙️ Pré-requisitos

* **Python 3** instalado
* Bibliotecas necessárias:

  * pandas
  * openpyxl

Instale as dependências com:

```bash
pip install pandas openpyxl
```

---

## ▶️ Como Executar

1. Coloque os arquivos `matriz1.xlsx` e `matriz2.xlsx` na mesma pasta do `matriz.py`.
2. Execute o programa no terminal ou VS Code:

```bash
python matriz.py
```

---

## 📊 O que o programa faz

* Lê as matrizes dos arquivos Excel.
* Verifica se ambas são **quadradas (NxN)**.
* Cria funções de **soma** e **multiplicação** de dois números.
* Realiza a multiplicação de matrizes usando essas funções.
* Exibe:

  * Matrizes de entrada
  * Passo a passo de cada multiplicação parcial
  * Matriz resultado final

---

## 📝 Exemplo de Saída

```
Matriz 1:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Matriz 2:
[[9 8 7]
 [6 5 4]
 [3 2 1]]

Passo a passo da multiplicação:

resultado[0][0] += 1 * 9  => 9
resultado[0][0] += 2 * 6  => 21
resultado[0][0] += 3 * 3  => 30
...

Resultado da multiplicação de matrizes:
[30, 24, 18]
[84, 69, 54]
[138, 114, 90]
```

---

## 📌 Observações

* O programa lê apenas **matrizes quadradas**.
* Caso queira usar arquivos TXT, adapte `read_excel` para `read_csv` no código.
* O projeto é simples e ideal para fins didáticos de **Programação e Álgebra Linear**.

---

### 👤 Autor

Projeto criado para fins acadêmicos.
Sinta-se livre para usar e melhorar!


