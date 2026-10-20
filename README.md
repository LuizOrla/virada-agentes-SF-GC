
# Ajuste de Usuários Salesforce (Genesys Cloud Automation)

Aplicação desktop desenvolvida em **Python** utilizando **PyQt6** e o **PureCloud Platform Client V2** (`PureCloudPlatformClientV2`). O objetivo principal é automatizar operações em lote no Genesys Cloud para operadores/agentes (vínculo ou remoção de filas e grupos, alteração de site/estação WebRTC e configuração de resposta automática - _Auto Answer_).

## Tecnologias e Dependências

O projeto foi construído utilizando as seguintes bibliotecas e ferramentas:

- **Python** (versão 3.8 ou superior recomendada)
- **PyQt6** (para a interface gráfica de usuário)
- **PureCloudPlatformClientV2** (SDK oficial do Genesys Cloud para Python)

## Pré-requisitos de Instalação

### 1. Instalação do Python

Antes de executar a aplicação, certifique-se de que o Python está instalado em sua máquina:

1. Acesse o [site oficial do Python](https://www.python.org/downloads/ "null").
2. Baixe e execute o instalador mais recente para o seu sistema operacional (compatível com Windows, macOS ou Linux).
3. **Importante:** Durante a instalação, certifique-se de marcar a opção **"Add Python to PATH"** (Adicionar o Python ao PATH) para garantir que os comandos funcionem corretamente no terminal.
4. Para confirmar a instalação, abra o terminal (Prompt de Comando ou PowerShell) e digite:
 
```
python --version
```
    

### 2. Instalação das Bibliotecas

Com o Python instalado, abra o terminal e execute o seguinte comando para instalar as dependências necessárias do projeto:
```
pip install PyQt6 purecloud-platform-client-v2
```

## Configuração da Credencial (OAuth Client)

Para que a aplicação consiga se comunicar com a API do Genesys Cloud, é necessário criar uma credencial do tipo **Client Credentials** na sua organização Genesys Cloud:

1. Acesse o **Admin** do Genesys Cloud.
2. Navegue até **Integrations** > **OAuth**.
3. Clique em **Add Client**.
4. Defina um nome para a integração e selecione a opção **Client Credentials**.
5. Na aba **Roles**, atribua as permissões necessárias para gerenciar usuários, filas, grupos e estações de telefonia (ex: `directory:user:any`, `routing:queue:any`, `group:any`, `telephony:phones:any`, etc.).
6. Copie o **Client ID** e o **Client Secret** gerados para utilizá-los na interface da aplicação.

## Como Executar a Aplicação

1. Baixe ou clone o repositório contendo o código-fonte.
2. Abra o terminal na pasta onde o arquivo **`virada_SF_Qt.py`** está localizado.
3. Execute o comando:
```
python virada_SF_Qt.py
```

## Guia de Uso da Interface

1. **Credenciais OAuth:** Preencha os campos de **Client ID** e **Client Secret** com as chaves geradas no Genesys Cloud.
2. **Usuários:** Insira os nomes dos agentes na caixa de texto maior, separados por vírgula (ex: `JOAO SILVA, MARIA SOUZA`).
3. **Filas (Opcional):** Marque a caixa **"Alterar Filas"** e informe os nomes exatos das filas nos campos correspondentes para adicionar ou remover os usuários em lote.
4. **Grupos (Opcional):** Marque a caixa **"Alterar Grupos"** e informe os nomes dos grupos para adicionar ou remover os operadores.
5. **Estação WebRTC / Site (Opcional):** Marque a caixa correspondente para atualizar a estação/site de telefonia associada aos usuários.
6. **Auto Answer (Opcional):** Marque para habilitar ou desabilitar o atendimento automático de chamadas ACD nos perfis dos usuários selecionados.
7. **Execução:** Clique no botão **Executar** para iniciar o processamento. O painel inferior exibirá em tempo real o progresso e eventuais retornos/erros da API.
8. **Sair:** Clique em **Sair** para encerrar a aplicação com segurança.

## Estrutura do Código

- **Funções de Apoio:** Gerenciamento de tratamento de exceções da API (`ApiException`) com conversão para JSON estruturado e atraso controlado (`imprime`) para atualização fluida da interface via `QApplication.processEvents()`.
- **Inicialização de APIs:** Conexão direcionada para a região padrão configurada (`sa_east_1`) e instanciação modular das APIs (`UsersApi`, `GroupsApi`, `RoutingApi`, `TelephonyProvidersEdgeApi`).
- **Classe `JanelaPrincipal`:** Constrói a interface em grade (`QGridLayout`) utilizando componentes do PyQt6 e gerencia de forma assíncrona/sequencial as chamadas de automação em lote.
