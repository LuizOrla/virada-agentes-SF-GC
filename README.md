# Ajuste de Usuários Salesforce - Genesys Cloud (`virada_SF_Qt.py`)

Aplicação desktop desenvolvida em **Python** utilizando **PyQt6** e o SDK oficial **PureCloud Platform Client V2** (`PureCloudPlatformClientV2`). O objetivo principal é automatizar operações em lote no **Genesys Cloud** para operadores e agentes (vínculo ou remoção de filas e grupos, alteração de site/estação WebRTC e configuração de resposta automática - *Auto Answer*).

---

## 🚀 Como Usar (Sem precisar instalar o Python)

Se você deseja apenas executar a aplicação de forma rápida no Windows, pode utilizar o executável pré-compilado:

1. Acesse a aba **[Releases](../../releases)** deste repositório.
2. Baixe a versão mais recente do arquivo **`virada_SF_Qt.exe`**.
3. Dê um duplo clique para abrir e preencha as credenciais e parâmetros diretamente na interface gráfica.

---

## 🛠️ Executando o Código-Fonte (Desenvolvedores)

Caso queira executar o script diretamente ou contribuir com o projeto, siga os passos abaixo:

### Pré-requisitos
* **Python** (versão 3.8 ou superior recomendada)
* **Git** instalado na máquina

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
```
2. Instalar as Dependências
Instale o PyQt6 e o SDK do Genesys Cloud executando o comando no terminal:

Bash
python -m pip install PyQt6 purecloud-platform-client-v2
3. Executar a Aplicação
Bash
python virada_SF_Qt.py

## Configuração da Credencial (OAuth Client)
Para que a aplicação consiga se comunicar com a API do Genesys Cloud, é necessário criar uma credencial do tipo Client Credentials na sua organização:

Acesse o Admin do Genesys Cloud.

Navegue até Integrations > OAuth.

Clique em Add Client e selecione a opção Client Credentials.

Na aba Roles, atribua as permissões necessárias para gerenciar usuários, filas, grupos e estações de telefonia (ex: directory:user:any, routing:queue:any, group:any, telephony:phones:any).

Copie o Client ID e o Client Secret para utilizá-los na interface da aplicação.

## Guia de Uso da Interface
Credenciais OAuth: Preencha os campos de Client ID e Client Secret.

Usuários: Insira os nomes dos agentes na caixa de texto maior, separados por vírgula (ex: JOAO SILVA, MARIA SOUZA).

Filas (Opcional): Marque "Alterar Filas" e informe os nomes exatos para adicionar ou remover os usuários em lote.

Grupos (Opcional): Marque "Alterar Grupos" e informe os nomes dos grupos correspondentes.

Estação WebRTC / Site (Opcional): Atualize a estação ou site de telefonia associada aos operadores.

Auto Answer (Opcional): Habilite ou desabilite o atendimento automático de chamadas ACD.

Execução: Clique em Executar. O painel inferior exibirá o progresso em tempo real e eventuais retornos/erros formatados.

## Como Gerar o Executável (.exe) Localmente
Se precisar recompilar a aplicação utilizando o PyInstaller:

Instale o PyInstaller:

Bash
python -m pip install pyinstaller
Gere o executável empacotado em arquivo único sem a janela de console:

Bash
python -m pyinstaller --noconsole --onefile virada_SF_Qt.py
O executável pronto estará localizado dentro da pasta dist/virada_SF_Qt.exe.

## Tecnologias Utilizadas
Python

PyQt6 (Interface Gráfica)

PureCloudPlatformClientV2 (API SDK Oficial do Genesys Cloud)

PyInstaller (Empacotamento)


---

### Próximos passos para subir ao GitHub:
1. Crie o arquivo `.gitignore` na raiz do seu projeto com o seguinte conteúdo para ignorar pastas temporárias de compilação:
   ```text
   build/
   dist/
   *.spec
   __pycache__/
   .vscode/
   .idea/
No terminal do VS Code, envie o projeto:

Bash
git init
git add .
git commit -m "Commit inicial: Aplicação Genesys Cloud Salesforce com PyQt6 e README"
git branch -M main
git remote add origin SUA_URL_DO_GITHUB
git push -u origin main
