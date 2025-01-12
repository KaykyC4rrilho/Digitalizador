Gerenciador de Etiquetas

Este projeto é uma aplicação desenvolvida em Python com a biblioteca Tkinter, projetada para gerenciar registros de etiquetas de forma simples e eficiente. O sistema inclui funcionalidades para validação de documentos (CNPJ/CPF), registro de etiquetas, atalhos de teclado, e armazenamento persistente das informações.

Funcionalidades

1. Validação de Documentos

Implementa algoritmos para validação de CNPJ e CPF, verificando os dígitos verificadores.

Notifica o usuário sobre inconsistências nos documentos e permite corrigir ou continuar com o registro.

2. Gestão de Etiquetas

Permite o registro de etiquetas com números de 9 dígitos.

Armazena os dados em arquivos de texto organizados para facilitar consultas futuras.

Opções para reiniciar o registro de uma nova etiqueta e editar informações existentes.

3. Interface Gráfica Amigável

Design intuitivo com campos de entrada, botões e uma lista para exibir registros salvos.

Mensagens temporárias e caixas de diálogo para feedback claro ao usuário.

4. Atalhos de Teclado

F1: Seleciona o tipo de documento como CNPJ.

F2: Seleciona o tipo de documento como CPF.

F3: Reinicia o registro da etiqueta.

F11: Ativa ou desativa o modo de tela cheia.

5. Automatização e Usabilidade

Navegação fluida com foco automático entre os campos de entrada.

Validação em tempo real para garantir entradas válidas.

Controle de caracteres máximos e prevenção de erros.

6. Persistência de Dados

Salva os registros em arquivos de texto no formato:

<número da etiqueta>;<documento>;<nome>;<status do DV>

Facilita integração com outros sistemas e manipulação futura dos dados.

Tecnologias Utilizadas

Python 3.x

Tkinter (para a interface gráfica)

Como Executar

Certifique-se de ter o Python instalado em seu sistema.

Clone este repositório:

git clone <URL-do-repositório>

Navegue até o diretório do projeto:

cd <nome-do-diretorio>

Execute o script principal:

python <nome-do-script>.py

A aplicação será aberta em tela cheia.

Exemplos de Uso

Gerenciamento de etiquetas para organização de produtos ou documentos.

Validação e armazenamento seguro de dados como CNPJ e CPF.

Fluxo rápido com suporte a atalhos de teclado.
