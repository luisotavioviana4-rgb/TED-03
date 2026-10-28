# TED-03

`TED 03` - Gerenciador de Persistência de Dados em Arquivos Estruturados (CSV e JSON)

Trabalho prático da disciplina sobre conversão e persistência de dados em arquivos CSV e JSON.

Alunos:

* Divino Rafael Abade Oliveira (RA:26.1.14744)
* Luis Otávio Viana dos Santos (RA:26.1.18406)

O que o projeto faz:

* Converte arquivos *CSV para JSON* e *JSON para CSV*.
* Cria *backup automático* dos arquivos antes de alterar qualquer dado.
* Usa gerenciador de contexto (`with open`) com codificação `utf-8`.
* Trata erros comuns de leitura e escrita de arquivos.

Arquivos do Projeto:

* `programa.py`: Script principal em Python.
* `dados.cs`: Arquivo CSV de teste.
* `dados.json`: Arquivo JSON gerado.
* `backup.csv`: Cópia de segurança criada automaticamente.
* `backup.json`: Cópia de segurança criada automaticamente.
* `README.md`: Documentação simples do projeto.

Como Executar:

No terminal, dentro da pasta do projeto, rode:
```bash
python3 programa.py
