# Gerenciador de Etiquetas

Este projeto é uma aplicação desenvolvida em Python com a biblioteca Tkinter, projetada para gerenciar registros de etiquetas de forma simples e eficiente. O sistema inclui funcionalidades para validação de documentos (CNPJ/CPF), registro de etiquetas, atalhos de teclado, e armazenamento persistente das informações.

## Funcionalidades

### 1. Validação de Documentos

- **Validação de CNPJ e CPF**: Implementa algoritmos para verificar os dígitos verificadores e garantir consistência.
- **Notificações ao usuário**: Sinaliza inconsistências e oferece opções para corrigir ou prosseguir com o registro.

### 2. Gestão de Etiquetas

- **Registro de etiquetas**: Suporte a etiquetas com números de 9 dígitos.
- **Armazenamento persistente**: Dados organizados em arquivos de texto para consultas futuras.
- **Reinício e edição**: Facilidade para reiniciar registros ou editar informações existentes.

### 3. Interface Gráfica Amigável

- **Design intuitivo**: Campos de entrada, botões e lista de registros salvos.
- **Feedback claro**: Mensagens temporárias e caixas de diálogo para orientação ao usuário.

### 4. Atalhos de Teclado

- **F1**: Seleciona o tipo de documento como CNPJ.
- **F2**: Seleciona o tipo de documento como CPF.
- **F3**: Reinicia o registro da etiqueta.
- **F11**: Ativa ou desativa o modo de tela cheia.

### 5. Automatização e Usabilidade

- **Navegação fluida**: Foco automático entre os campos de entrada.
- **Validação em tempo real**: Garante entradas válidas.
- **Controle de caracteres**: Impede entradas acima do limite permitido.

### 6. Persistência de Dados

- **Formato de armazenamento**: Salva registros no formato:


- **Integração facilitada**: Arquivos prontos para manipulação futura ou integração com outros sistemas.

## Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: Para a interface gráfica.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório:

 ```bash
 git clone <URL-do-repositório>
cd <nome-do-diretorio>
python <nome-do-script>.py
