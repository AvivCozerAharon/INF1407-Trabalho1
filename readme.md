# Projeto Django - Blog de Notícias


## Integrantes
 - Aviv Cozer Aharon - 2211745
 - Gabriel Pereira da Silva Araujo - 2211136 

##  Resumo do Projeto  
Este projeto consiste em um **blog de notícias desenvolvido em Django**, que permite a interação de usuários com o sistema por meio de autenticação e gerenciamento de conteúdo.  

As principais funcionalidades são:  
- Cadastro de novos usuários.  
- Login e logout de usuários cadastrados.  
- Alteração de senha.  
- Criação, visualização, edição e exclusão de notícias.  

---

## Escopo do Site  
O sistema foi desenvolvido com foco em simplicidade e organização. Ele é dividido em duas principais áreas:  

1. **Área de autenticação**  
   - Criar conta (cadastro).  
   - Login/logout.  
   - Troca de senha.  
   - Vizualização de Perfil

2. **Área de gerenciamento de notícias**  
   - Criar notícia.  
   - Visualizar todas as notícias cadastradas.  
   - Editar notícia criada pelo próprio usuário.  
   - Excluir notícia criada pelo próprio usuário.  

---

## Manual de uso do Usuário  

### 1. Acesso inicial  
- Ao entrar no site, o usuário verá a página inicial com as notícias publicadas.  
- No canto superior direito, haverá opções de **Login**.  

### 2. Criar conta  
- Na tela de login click em  **Ainda não tem conta criada? Clique aqui!**.  
- Preencha os campos de nome de usuário, e-mail, nome, ultimo nome e senha.  
- Após o cadastro, o usuário pode realizar login normalmente.  

### 3. Login  
- Informe nome de usuário e senha cadastrados.  
- Após o login, o usuário poderá criar e gerenciar notícias.  

### 4. Criar notícia  
- Clique em **Adicionar Notícias** no menu principal.  
- Preencha os campos de título , conteúdo e uma foto de capa.  
- Clique em **Publicar** para publicar a notícia.  

### 5. Visualizar notícias  
- Todas as notícias cadastradas ficam listadas na página inicial.  
- É possível clicar em uma notícia para visualizar seu conteúdo completo.  

### 6. Editar notícia  
- O dono da notícia possui duas formas de acessar a edição:  
  1. Pela **tela inicial**, onde suas notícias aparecem listadas com o botão **Editar**.  
  2. Pela **tela de perfil**, que mostra apenas as notícias criadas pelo usuário.  
- Após editar os campos desejados, clique em **Salvar alterações** para confirmar a atualização.  

### 7. Excluir notícia  
- Assim como na edição, o usuário pode excluir suas próprias notícias de duas formas:  
  1. Pela **tela inicial (home)**, clicando em **Excluir** na notícia correspondente.  
  2. Pela **tela de perfil**, onde também aparece a opção **Excluir**.  
- Após clicar, confirme a exclusão para remover a notícia permanentemente.  

### 8. Alterar senha  
O usuário tem duas formas de alterar a senha:  

1. **Pelo menu de perfil (logado):**  
   - Clique em **Alterar minha senha**.  
   - Informe a senha atual e a nova senha.  
   - Após confirmar, o login será atualizado com a nova senha.  

2. **Pela tela de login (quando esqueceu a senha):**  
   - Clique em **Esqueceu a senha? Clique aqui!**  
   - Preencha o campo com seu e-mail.  
   - Você receberá um link de redefinição de senha por e-mail.  
   - Acesse o link, escolha a nova senha e confirme.  

### 9. Logout  
- Clique em **Logout** para encerrar a sessão.  

---

##  O que funcionou no projeto
- Cadastro de usuários.  
- Login e logout.  
- Alteração de senha.  
- Criação, listagem, visualização, edição e exclusão de notícias.  

---

## Passos para rodar o projeto localmente

1. **Clonar o repositório**

```bash
git clone https://github.com/AvivCozerAharon/INF1407-Trabalho1.git
cd INF1407-Trabalho1
```
## Criar e ativar ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

## Instalar dependencias
pip install -r requirements.txt

## Criar as tabelas do banco de dados
python manage.py makemigrations
python manage.py migrate

## Rodar o servidor
python manage.py runserver
