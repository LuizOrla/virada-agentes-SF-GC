
import PureCloudPlatformClientV2
import time
import json
from PureCloudPlatformClientV2.api_client import ApiException
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QCheckBox, QComboBox, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTextEdit, QWidget
from PyQt6.QtCore import Qt, QTimer

# ======================================== Funções ========================================
def imprime(janela, texto):
    janela.append(texto)
    QApplication.processEvents()
    time.sleep(0.5)

def regiao_gc():
    region = PureCloudPlatformClientV2.PureCloudRegionHosts.sa_east_1
    PureCloudPlatformClientV2.configuration.host = region.get_api_host()
def auth_client_gc(client_id, client_secret):
    regiao_gc()
    try:
        api_client = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(client_id, client_secret)
        return api_client
    except ApiException as e:
        erro_dict = {
            "status": e.status,
            "reason": e.reason,
            "body": e.body,
            "headers": dict(e.headers) if e.headers else None
        }
        error = json.dumps(erro_dict, indent=4, ensure_ascii=False, default=str)
        return error

def Groups_Api(api_client):
    try:
        api_instance = PureCloudPlatformClientV2.GroupsApi(api_client)
        return api_instance
    except ApiException as e:
        erro_dict = {
            "status": e.status,
            "reason": e.reason,
            "body": e.body,
            "headers": dict(e.headers) if e.headers else None
        }
        error = json.dumps(erro_dict, indent=4, ensure_ascii=False, default=str)
        return error
def Routing_Api(api_client):
    try:
        api_instance = PureCloudPlatformClientV2.RoutingApi(api_client)
        return api_instance
    except ApiException as e:
        erro_dict = {
            "status": e.status,
            "reason": e.reason,
            "body": e.body,
            "headers": dict(e.headers) if e.headers else None
        }
        error = json.dumps(erro_dict, indent=4, ensure_ascii=False, default=str)
        return error
def Users_Api(api_client):
    try:
        api_instance = PureCloudPlatformClientV2.UsersApi(api_client)
        return api_instance
    except ApiException as e:
        erro_dict = {
            "status": e.status,
            "reason": e.reason,
            "body": e.body,
            "headers": dict(e.headers) if e.headers else None
        }
        error = json.dumps(erro_dict, indent=4, ensure_ascii=False, default=str)
        return error
def Telephony_Api(api_client):
    try:
        api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi(api_client)
        return api_instance
    except ApiException as e:
        erro_dict = {
            "status": e.status,
            "reason": e.reason,
            "body": e.body,
            "headers": dict(e.headers) if e.headers else None
        }
        error = json.dumps(erro_dict, indent=4, ensure_ascii=False, default=str)
        return error


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ajuste de Usuários Salesforce")
        self.setMinimumSize(1400, 800)
        self.janela = QWidget()
        self.setCentralWidget(self.janela)

        cor = self.janela.palette()
        cor.setColor(QPalette.ColorRole.Window, QColor("#bababa"))
        self.janela.setPalette(cor)
        self.janela.setAutoFillBackground(True)
        self.layout_janela = QGridLayout()

        etiqueta_infos = self.etiqueta("Usuários, Filas e Grupos devem ser adicionados, separados por vírgula.")
        etiqueta_infos.setStyleSheet("""
            QLabel {
                font-weight: bold;
            }
        """)
        etiqueta_infos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_infos.setMaximumHeight(30)
        
        etiqueta_oauth = self.etiqueta("Informações OAuth.")
        entrada_client_id = self.entrada("Client ID", "password")
        entrada_client_secret = self.entrada("Client Secret", "password")

        etiqueta_usuarios = self.etiqueta("Nome dos usuários, separados por vírgula")
        entrada_usuarios = self.entrada_grande("USUARIO 1, USUARIO 2, ...")

        checkbox_filas = self.checkbox("Alterar Filas")
        entrada_filas_adicionar = self.entrada("Filas a Adicionar (FILA 1, FILA 2, ...)")
        entrada_filas_remover = self.entrada("Filas a Remover (FILA 1, FILA 2, ...)")

        checkbox_grupos = self.checkbox("Alterar Grupos")
        entrada_grupos_adicionar = self.entrada("Grupos a Adicionar (GRUPO 1, GRUPO 2, ...)")
        entrada_grupos_remover = self.entrada("Grupos a Remover (GRUPO 1, GRUPO 2, ...)")

        checkbox_webrtc = self.checkbox("Alterar estação WebRTC (Site)")
        entrada_site_estacao = self.entrada("Novo Site de telefone WebRTC")

        checkbox_autoanswer = self.checkbox("Alterar Resposta Automática (Auto Answer)")
        menu_suspenso_autoanswer = self.menu_suspenso(["Habilitado", "Desabilitado"])
        saida = self.janela_saida()

        botao_executar = self.botoes("Executar", lambda:self.coletar_dados(entrada_client_id, entrada_client_secret, entrada_usuarios, checkbox_filas,
                                                               entrada_filas_adicionar, entrada_filas_remover, checkbox_grupos, entrada_grupos_adicionar,
                                                               entrada_grupos_remover, checkbox_webrtc, entrada_site_estacao, checkbox_autoanswer,
                                                               menu_suspenso_autoanswer, saida))
        botao_sair = self.botoes("Sair", lambda: self.fechar(saida))

        self.layout_janela.addWidget(etiqueta_infos,             0, 0, 1, 3)
        self.layout_janela.addWidget(etiqueta_oauth,             1, 0)
        self.layout_janela.addWidget(entrada_client_id,          2, 0)
        self.layout_janela.addWidget(entrada_client_secret,      3, 0)
        self.layout_janela.addWidget(etiqueta_usuarios,          4, 0)
        self.layout_janela.addWidget(entrada_usuarios,           5, 0, 2, 1)
        self.layout_janela.addWidget(checkbox_filas,             1, 1)
        self.layout_janela.addWidget(entrada_filas_adicionar,    2, 1)
        self.layout_janela.addWidget(entrada_filas_remover,      3, 1)
        self.layout_janela.addWidget(checkbox_grupos,            4, 1)
        self.layout_janela.addWidget(entrada_grupos_adicionar,   5, 1)
        self.layout_janela.addWidget(entrada_grupos_remover,     6, 1)
        self.layout_janela.addWidget(checkbox_webrtc,            1, 2)
        self.layout_janela.addWidget(entrada_site_estacao,       2, 2)
        self.layout_janela.addWidget(checkbox_autoanswer,        3, 2)
        self.layout_janela.addWidget(menu_suspenso_autoanswer,   4, 2)
        self.layout_janela.addWidget(saida,                      7, 0, 3, 3)
        self.layout_janela.addWidget(botao_executar,             10, 0, 1, 3)
        self.layout_janela.addWidget(botao_sair,                 11, 0, 1, 3)

        self.janela.setLayout(self.layout_janela)
        
    def texto_janela(self, text):
        texto = QLabel(text)
        return texto
    def etiqueta(self, text):
        texto = QLabel(text)
        return texto
    def botoes(self, titulo, funcao):
        botao = QPushButton(titulo)
        botao.clicked.connect(funcao)
        return botao
    def entrada(self, placeholder, mostrar="normal"):
        entrada_texto = QLineEdit()
        entrada_texto.setPlaceholderText(placeholder)
        if mostrar == "password":
            entrada_texto.setEchoMode(QLineEdit.EchoMode.Password)
        return entrada_texto
    def entrada_grande(self, placeholder):
        entrada_grande = QTextEdit()
        entrada_grande.setPlaceholderText(placeholder)
        return entrada_grande
    def janela_entrada(self, placeholder):
        texto_entrada = QTextEdit()
        texto_entrada.setPlaceholderText(placeholder)
        return texto_entrada
    def janela_saida(self):
        texto_saida = QTextEdit()
        texto_saida.setReadOnly(True)
        return texto_saida
    def checkbox(self, titulo):
        caixa_de_selecao = QCheckBox(titulo)
        caixa_de_selecao.setChecked(False)
        return caixa_de_selecao
    def menu_suspenso(self, lista_opcoes):
        menu_suspenso = QComboBox()
        menu_suspenso.addItems(lista_opcoes)
        return menu_suspenso
        
    def fechar(self, saida):
        saida.clear()
        imprime(saida, "Saindo...")
        self.close() # Fecha janela
        QApplication.quit() # Encerra o loop da aplicação principal

    def coletar_dados(self, clientId, clientSecret, users, checkboxFilas, filasAdicionar, filasRemover, 
                 checkboxGrupos, gruposAdicionar, gruposRemover, checkboxWebrtc, siteWebrtc, 
                 ckeckboxAutoanswer, statusAutoanswer, saida):
        client_id = str(clientId.text())
        client_secret = str(clientSecret.text())

        usuarios = users.toPlainText()
        lista_usuarios = [item.strip() for item in usuarios.split(",") if item.strip()]

        marcacao_filas = checkboxFilas.isChecked()
        filas_adicionar = filasAdicionar.text()
        lista_filas_adicionar = [item.strip() for item in filas_adicionar.split(",") if item.strip()]
        filas_remover = filasRemover.text()
        lista_filas_remover = [item.strip() for item in filas_remover.split(",") if item.strip()]

        marcacao_grupos = checkboxGrupos.isChecked()
        grupos_adicionar = gruposAdicionar.text()
        lista_grupos_adicionar = [item.strip() for item in grupos_adicionar.split(",") if item.strip()]
        grupos_remover = gruposRemover.text()
        lista_grupos_remover = [item.strip() for item in grupos_remover.split(",") if item.strip()]

        marcacao_webrtc = checkboxWebrtc.isChecked()
        site_webrtc = siteWebrtc.text()

        marcacao_autoanswer = ckeckboxAutoanswer.isChecked()
        autoanswer = statusAutoanswer.currentText()

        self.executar(client_id, client_secret, lista_usuarios, marcacao_filas, lista_filas_adicionar, lista_filas_remover,
                        marcacao_grupos, lista_grupos_adicionar, lista_grupos_remover, marcacao_webrtc, site_webrtc, 
                        marcacao_autoanswer, autoanswer, saida)

    def executar(self, clientId, clientSecret, users, ckeckboxFilas, filasAdicionar, filasRemover,
                    ckeckboxGrupos, gruposAdicionar, gruposRemover, checkboxWebrtc, siteWebrtc, 
                    checkboxAutoanswer, autoAnswer, saida):
        lista_ids_agentes = []
        usuarios_filas_adicionar = [] 

        infos_agentes = {} 
        info_filas_adicionar = {}
        info_filas_remover = {}
        info_grupos_adicionar = {}
        info_grupos_remover = {}

        saida.clear()
        imprime(saida, "Autenticando")

        client = self.checa_auth(clientId, clientSecret, saida)
        if not isinstance(client, str):
            usersApi, groupsApi, routingApi, telephonyApi = self.instancia_Apis(client, saida)
            for usuario in users: # Buscar IDs de Agentes
                search_body = PureCloudPlatformClientV2.UserSearchRequest()
                search_body.query = [
                    {
                        "fields": ["name"],
                        "value": usuario,
                        "type": "CONTAINS"
                    }
                ]
                try:
                    api_response = usersApi.post_users_search(search_body).to_dict()
                except ApiException as e:
                    imprime(saida, "Erro.")
                    imprime(saida, e)

                if api_response["total"] == 0:
                    imprime(saida, f"Usuário {usuario} não encontrado. Verifique nome de usuário.")
                    continue
                else:
                    for result in api_response["results"]: # Retorna ID de Usuário
                        id_usuario = result["id"]
                        lista_ids_agentes.append(id_usuario)
                    
                    try:
                        api_response = telephonyApi.get_telephony_providers_edges_phones(web_rtc_user_id=id_usuario).to_dict()
                        if api_response["total"] == 0:
                            imprime(saida, f"Usuário {usuario} sem estação WebRTC.")
                    except ApiException as e:
                        imprime(saida, "Erro.")
                        imprime(saida, e)

                    if api_response["total"] == 0:
                            webrtc = ""
                            id_webrtc = ""
                    else: 
                        for entitie in api_response["entities"]: # Retorna estação WebRTC de usuário
                            webrtc = entitie["name"]
                            id_webrtc = entitie["id"]
                        
                    infos_agentes[usuario] = {
                        "id": id_usuario,
                        "WebRTC": webrtc,
                        "id_webrtc": id_webrtc
                    }
                    imprime(saida, f"Nome: {usuario} | ID: {id_usuario} | WebRTC: {webrtc} | ID WebRTC: {id_webrtc}")
            if ckeckboxFilas:
                if not filasAdicionar:
                    imprime(saida, "Nenhuma Fila a adicionar.")
                else:
                    for fila in filasAdicionar: # Buscar IDs de Filas
                        response = routingApi.get_routing_queues(name=fila).to_dict()
                        imprime(saida, "Filas a adicionar:")
                        for entitie in response["entities"]:
                            id_fila = entitie["id"]
                            info_filas_adicionar[fila] = {
                                "id": id_fila
                            }
                            imprime(saida, f"Fila: {fila} | ID: {id_fila}")

                if not filasRemover:
                    imprime(saida, "Nenhuma Fila a remover.")
                else:
                    imprime(saida, "Filas a remover")
                    for fila in filasRemover: # Buscar IDs de Filas
                        response = routingApi.get_routing_queues(name=fila).to_dict()
                        for entitie in response["entities"]:
                            id_fila = entitie["id"]
                            info_filas_remover[fila] = {
                                "id": id_fila
                            }
                            imprime(saida, f"Fila: {fila} | ID: {id_fila}")
                for agente in lista_ids_agentes: # Adiciona entidades de agente para adição às filas
                    usuario = PureCloudPlatformClientV2.WritableEntity()
                    usuario.id = agente
                    usuarios_filas_adicionar.append(usuario)

                for nome_fila, fila in info_filas_adicionar.items(): # Adicionar a Filas
                    imprime(saida, f"Adicionando usuários à fila {nome_fila}")
                    response = routingApi.post_routing_queue_users(fila["id"], usuarios_filas_adicionar)

                for nome_fila, fila in info_filas_remover.items(): # Remover de Filas
                    imprime(saida, f"Removendo usuários da fila {nome_fila}")
                    for nome_usuario, usuario in infos_agentes.items():
                        routingApi.delete_routing_queue_member(fila["id"], usuario["id"])

            if ckeckboxGrupos:
                if not gruposAdicionar:
                    imprime(saida, "Nenhum grupo a adicionar.")
                else:
                    imprime(saida, "Grupos a adicionar:")
                    for grupo in gruposAdicionar: # Buscar IDs de Grupos
                        search_body = {
                            "query": [
                                {
                                    "fields": ["name"],
                                    "value": grupo,
                                    "type": "EXACT"  # Use "EXACT" para nome igual ou "CONTAINS" para busca parcial
                                }
                            ]
                        }
                        response = groupsApi.post_groups_search(body=search_body).to_dict()
                        for result in response["results"]:
                            id_grupo = result["id"]
                            info_grupos_adicionar[grupo] = {
                                "id": id_grupo
                            }
                        imprime(saida, f"Grupo: {grupo} | ID: {id_grupo}")
                    for nome, grupo in info_grupos_adicionar.items(): # Adicionar a Grupos
                        imprime(saida, f"Adicionando usuários ao grupo {nome}")
                        body = PureCloudPlatformClientV2.GroupMembersUpdate()
                        body.member_ids = lista_ids_agentes
                        response = groupsApi.post_group_members(grupo["id"], body)

                if not gruposRemover:
                    imprime(saida, "Nenhum grupo a remover.")
                else:
                    imprime(saida, "Grupos a Remover:")
                    for grupo in gruposRemover: # Buscar IDs de Grupos
                        search_body = {
                            "query": [
                                {
                                    "fields": ["name"],
                                    "value": grupo,
                                    "type": "EXACT"  # Use "EXACT" para nome igual ou "CONTAINS" para busca parcial
                                }
                            ]
                        }
                        response = groupsApi.post_groups_search(body=search_body).to_dict()
                        for result in response["results"]:
                            id_grupo = result["id"]
                            info_grupos_remover[grupo] = {
                                "id": id_grupo
                            }
                        imprime(saida, f"Grupo: {grupo} | ID: {id_grupo}")
                    for nome, grupo in info_grupos_remover.items(): # Remover de Grupos
                        imprime(saida, f"Removendo usuários do grupo {nome}")
                        lista_ids = ",".join(lista_ids_agentes)
                        groupsApi.delete_group_members(group_id=grupo["id"], ids=lista_ids)

            if checkboxWebrtc:
                body = PureCloudPlatformClientV2.SiteSearchCriteria()
                body.page_size = 25
                body.page_number = 1

                try:
                    imprime(saida, "Buscando Site:")
                    api_response = telephonyApi.post_telephony_providers_edges_sites_search(body)
                    for site in api_response.results:
                        if site.name == siteWebrtc:
                            imprime(saida, f"ID: {site.id} | Nome: {site.name}")
                            site_id = site.id
                except ApiException as e:
                    imprime(saida, f"Erro ao buscar sites: {e}")

                for user_name, user in infos_agentes.items():
                    if user["WebRTC"] != "":
                        imprime(saida, f"Alterando {user["WebRTC"]} para o site Callback.")
                        telefone_atual = telephonyApi.get_telephony_providers_edges_phone(user["id_webrtc"])
                        update = PureCloudPlatformClientV2.Phone()

                        update.name = telefone_atual.name
                        update.version = telefone_atual.version
                        update.lines = telefone_atual.lines
                        update.phone_base_settings = telefone_atual.phone_base_settings
                        update.web_rtc_user = telefone_atual.web_rtc_user

                        site_novo = PureCloudPlatformClientV2.Site()
                        site_novo.id = site_id
                        update.site = site_novo
                        response = telephonyApi.put_telephony_providers_edges_phone(user["id_webrtc"], update)
                    else:
                        imprime(saida, f"Usuário {user_name} sem estação WebRTC.")

            if checkboxAutoanswer:
                user_update = PureCloudPlatformClientV2.UpdateUser()
                if autoAnswer == "Habilitado":
                    user_update.acd_auto_answer = True
                else:
                    user_update.ace_auto_answer = False

                if autoAnswer:
                    imprime(saida, "Habilitando AutoAnswer.")
                else:
                    imprime(saida, "Desabilitando Autoanswer.")
                for user_name, user in infos_agentes.items(): # Desabilitar Resposta Automática
                    usersApi.patch_user(user["id"], user_update)
        else:
            imprime(saida, client)

    def instancia_Apis(self, api_client, saida):
        usersApi = Users_Api(api_client) # Users API
        imprime(saida, "API de Usuário: OK.")
        groupsApi = Groups_Api(api_client) # Groups API
        imprime(saida, "API de Grupos: OK.")
        routingApi = Routing_Api(api_client) # Routing API
        imprime(saida, "API de Roteamento: OK.")
        telephonyApi = Telephony_Api(api_client) #Telephony Providers Edge API
        imprime(saida, "API de Telefonia: OK.")
        return usersApi, groupsApi, routingApi, telephonyApi

    def checa_auth(self, clientId, clientSecret, saida):
        auth = auth_client_gc(clientId, clientSecret)
        if isinstance(auth, str):
            imprime(saida, "Erro ao Autenticar.")
            return auth
        else:
            imprime(saida, "Autenticação OK")
            return auth


def main():
    app = QApplication([])
    janela = JanelaPrincipal()
    janela.show()
    app.exec()

main()