# Introdução ao Python

Este repositório registra meu primeiro contato com a linguagem `Python`! Ele possui exercícios com algumas funções para solucionar problemas (básicos) diversos.

## Detalhes

<details>
  <summary><strong>Objetivos:</strong></summary>
  <br />
  <ul>
    <li>Utilizar o terminal interativo do `Python`.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Adaptar as boas práticas de desenvolvimento em `Python`.</li>
    <li>Escrever funções.</li>
  </ul>
</details>

<details>
  <summary><strong>Linter:</strong></summary>
  <br />
  
  Para garantir a qualidade do código, foi utilizado nesses exercícios o linter `Flake8`.
  Para garantir que os códigos estão alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção!

  Comando para rodar o `Flake8`:

  ```bash
  python3 -m flake8
  ```

</details>

<details>
  <summary><strong>Ambiente Virtual:</strong></summary>
  <br />

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas.
  > - `wheel`
  > - `black`
  > - `flake8`

  1. **criar e ativar o ambiente virtual**

  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  ```

  2. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`.
  
</details>

## Exercícios

- `src/average.py` : Calcula a média aritmética dos valores contidos em uma lista

- `src/biggest_name.py` : Cria uma função que recebe uma lista de nomes e retorna o nome com a maior quantidade de caracteres.

- `src/biggest_number.py` : Cria uma função que recebe dois números e retorna o maior deles

- `src/open_close_file.py` : Treina comandos de Leitura e escrita em arquivos

- `src/read_student_grades.py` : Lê um arquivo contendo notas de estudantes. Aplica um filtro e escreve os nomes dos que estão reprovadas (<6) em outro arquivo.

- `src/square.py` : Recebe um valor `n` qualquer, sendo `n > 1`, e imprime um quadrado `n x n` feito de asteriscos.

- `src/summation.py` : Recebe vários números e calcule a soma deles. Caso algum valor seja inválido (`string`), uma mensagem é exibida informando o erro. Ao final, a soma dos valores válidos é imprimida.

- `src/triangle_checker.py` : Recebe 3 valores e informa se é possível formar um triangulo e qual o seu tipo.