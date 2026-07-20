# **FORMULÁRIOS**

## **Pesquisa**

### Pesquisa

Pesquisar sobre validação no lado do cliente (Client-Side) através do JavaScript e HTML nativo e no lado do servidor (Server-Side).

### Download

E adicionar uma seção no menu principal para download dessa pesquisa.


## **Processamento de Dados**

Criar uma seção ou arquivo de destino que será responsável por receber e procesasr os dados do formulário.


## **ETAPAS**

### Etapa 1

Realizar uma pesquisa técnica e conceitual --> entregar na raiz do projeto

- **Validação Client-Side vs. Server-Side:** Explique o que é a validação no lado do cliente (HTML/JS) e no lado do servidor (Back-end). Discuta sobre essas duas vertentes.

- **Atributos de Validação Nativa:** O papel dos atributos required, pattern (Expressões Regulares) e seletores de tamanho (minlength/maxlength).

- **Estados Visuais (CSS):** Como usar as pseudo-classes CSS :valid e :invalid para colorir ou estilizar os campos de acordo com o preenchimento.



### Etapa 2

Implementar a pesquisa na prática

#### 1. Criação da Seção "Contato" e Estrurura Semântica

- **Navegação Dinâmica:** O menu do site deve ganhar um novo botão chamado "Contato". Ao ser clicado, o JavaScript interno deve carregar o formulário dentro da tag `<main>` sem dar refresh na página.

- **Agrupamento Lógico:** O formulário deve estar envolvido pela tag `<form>` configurada obrigatoriamente com o atributo method="`GET`". Os campos devem ser agrupados utilizando a tag `<fieldset>` com uma legenda visível `<legend>`.

---

#### 2. Componentes e Elementos do Formulário

Todos os campos devem possuir obrigatoriamente uma tag `<label>` associada corretamente pelo atributo for vinculado ao id do respectivo input:

- Campo de Texto para o Nome Completo --> ***Obrigatório***.

- Campo do tipo type="email" para o E-mail --> ***Obrigatório***.

- Campo do tipo type="tel" para o Telefone --> ***Obrigatório***.

- Caixa de seleção `<select>` com opções de Assunto (Ex: Dúvida, Sugestão, Crítica) --> ***Obrigatório***.

- Botões de opção type="radio" para definir o Perfil do Usuário (Ex: 
Aluno, Professor, Comunidade Externa) --> ***Obrigatório***.

- Uma área de texto `<textarea>` para a Mensagem (mínimo de 15 caracteres via `minlength`) --> ***Obrigatório***.

---

#### 3. Interceptação JavaScript, Tela de Confirmação e Processamento de Dados

- **Prevenção e Resumo Prévio:** O formulário deve disparar uma função JavaScript interna no evento de submissão (onsubmit). Caso o formulário passe nas validações básicas do HTML, a função deve interceptar o envio automático inicial para exibir na tela um Resumo de Revisão contendo os dados digitados (pode ser usando o comando confirm() do navegador).

- **Fluxo de Decisão:**
    - Se o usuário Cancelar a confirmação, o formulário impede o envio e volta para a tela de edição exatamente com os dados preenchidos para que possam ser corrigidos.
    - Se o usuário Confirmar, o formulário realiza o envio real via método `GET`.


**Processamento e Leitura de Dados (Sem Servidor):** A página/seção que receber o envio do formulário deverá utilizar o objeto nativo `URLSearchParams` do JavaScript para capturar os parâmetros que foram anexados à URL. O sistema deverá exibir na tela uma mensagem de sucesso altamente personalizada, contendo dinamicamente o Nome e o E-mail capturados da URL daquela requisição.

---

#### 4. Padronização de Entrega e Identificação (Guia de Entrega)

Se atentar as orientações de entrega, como o nome da pasta o formato (zip), etc.



## **RESUMO**

TOMAMO NO CU