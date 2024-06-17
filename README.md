1. Título do Projeto
Projeto: Agenda de Contatos
2. Introdução
Este projeto tem como objetivo desenvolver um sistema para gerenciar os dados de pessoas, incluindo cadastro, atualização e consulta de informações.
3. Escopo
Inclui:
•	Cadastro de novos contatos.
•	Atualização de dados de contatos já existentes.
•	Consulta de informações de contatos.
Exclui:
•	Integração com sistemas de terceiros.
4. Requisitos Funcionais
•	Cadastro de Contatos: Permitir a entrada de informações como E-mail, Nome, etc.
•	Atualização de Contato: Permitir a modificação dos dados cadastrais.
•	Consulta de Contatos: Permitir a busca de clientes pelo E-mail, Nome.
5. Requisitos Não Funcionais
•	O sistema deve suportar até 300 usuários simultâneos.
•	Tempo de resposta para consultas deve ser inferior a 2 segundos.
6. Arquitetura do Sistema
•	Front-End: HTML, CSS, JavaScript.
•	Back-End: Django.
•	Banco de Dados: SQLite.
7. Requisitos de Integração
•	Sem Integração.
8. Modelagem de Dados
•	contact/models.py
9. Design das Views e Templates
•	Página de Cadastro de Usuário: contact/templates/contact/pages/register.html.
•	Página de Login: contact/templates/contact/pages/login.html.
•	Página de Consulta: contact/templates/contact/pages/contact.html.
•	Página Index: contact/templates/contact/pages/index.html.
•	Página de Criação de Contato: contact/templates/contact/pages/create.html.
10. URLs e Rotas
•	contact/views.py
•	contact/urls.py
11. Procedimentos de Teste
•	Caso de Teste 1: Cadastro de um novo contato com todos os campos válidos.
•	Caso de Teste 2: Consulta de contato pelo E-mail e Nome.
•	Caso de Teste 3: Atualização dos dados de um contato existente.
•	Caso de Teste 4: A visualização dos contatos está disponível apenas para usuários autenticados.
12. Cronograma
•	Início do Projeto: 14/06/2024
•	Conclusão do Projeto: 17/06/2024
13. Recursos Necessários
•	Pessoal: 1 desenvolvedor Django.
•	Software: Django, SQLite, ambiente de desenvolvimento local.
14. Apêndices
•	Glossário: Django - Framework de desenvolvimento web em Python.
15. Créditos
Este projeto foi desenvolvido por [Igor Fernando Loiola].
-----------------------------------------------------------------------------
