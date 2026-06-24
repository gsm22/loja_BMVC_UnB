import http.server
import socketserver
import urllib.parse
import json
import webbrowser
import threading
from models.roupa import RoupaModel

PORTA = 8000

# Função para abrir o navegador automaticamente
def abrir_navegador():
    webbrowser.open(f"http://localhost:{PORTA}")

class BMVC_Controller(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 1. ROTA DA HOME
        if self.path == '/' or self.path == '/index':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            roupas = RoupaModel.listar_todas()
            cards_html = ""
            for r in roupas:
                cards_html += f"""
                <div class="col mb-5">
                    <div class="card h-100 shadow-sm border-0">
                        <div class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem">{r.tamanho}</div>
                        <img class="card-img-top" src="{r.imagem}" alt="{r.nome}" style="height: 270px; object-fit: cover;" />
                        <div class="card-body p-4">
                            <div class="text-center">
                                <span class="text-muted small d-block mb-1">{r.categoria}</span>
                                <h5 class="fw-bolder mb-2">{r.nome}</h5>
                                <span class="fs-5 fw-bold text-success">R$ {r.preco:.2f}</span>
                            </div>
                        </div>
                        <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                            <div class="d-flex justify-content-center gap-2">
                                <a class="btn btn-outline-dark btn-sm w-50" href="/editar?id={r.id}">Editar</a>
                                <a class="btn btn-outline-danger btn-sm w-50" href="/deletar?id={r.id}">Excluir</a>
                            </div>
                        </div>
                    </div>
                </div>
                """
            with open("views/index.tpl", "r", encoding="utf-8") as f:
                template = f.read()
            html_final = template.replace("{{VITRINE_DINAMICA}}", cards_html)
            self.wfile.write(html_final.encode("utf-8"))
            return

        # 2. ROTA DE EDIÇÃO
        elif self.path.startswith('/editar'):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            id_roupa = query.get('id', [None])[0]
            peca = RoupaModel.buscar_por_id(id_roupa)
            if peca:
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                with open("views/editar.tpl", "r", encoding="utf-8") as f:
                    tpl = f.read()
                html = tpl.replace("{{ID}}", str(peca.id)).replace("{{NOME}}", peca.nome)\
                          .replace("{{CATEGORIA}}", peca.categoria).replace("{{TAMANHO}}", peca.tamanho)\
                          .replace("{{PRECO}}", f"{peca.preco:.2f}").replace("{{IMAGEM}}", peca.imagem)
                self.wfile.write(html.encode("utf-8"))
            return

        # 3. ROTA DE DELEÇÃO
        elif self.path.startswith('/deletar'):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            id_roupa = query.get('id', [None])[0]
            if id_roupa:
                RoupaModel.deletar(id_roupa)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return

        # 4. ROTA DE ARQUIVOS ESTÁTICOS (CSS E JS)
        elif self.path.startswith('/static/'):
            return super().do_GET()

    def do_POST(self):
        tamanho = int(self.headers['Content-Length'])
        corpo = self.rfile.read(tamanho).decode('utf-8')
        form = urllib.parse.parse_qs(corpo)

        if self.path == '/cadastrar':
            nome = form.get('nome', [''])[0].strip()
            cat = form.get('categoria', [''])[0].strip()
            tam = form.get('tamanho', ['M'])[0].strip()
            preco = form.get('preco', ['0'])[0].strip()
            img = form.get('imagem', [''])[0].strip()
            if nome and preco:
                RoupaModel.cadastrar(nome, cat, tam, preco, img)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return

        elif self.path == '/salvar_edicao':
            id_r = form.get('id', [None])[0]
            nome = form.get('nome', [''])[0].strip()
            cat = form.get('categoria', [''])[0].strip()
            tam = form.get('tamanho', ['M'])[0].strip()
            preco = form.get('preco', ['0'])[0].strip()
            img = form.get('imagem', [''])[0].strip()
            if id_r and nome:
                RoupaModel.atualizar(id_r, nome, cat, tam, preco, img)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return

# BLOCO DE INICIALIZAÇÃO
if __name__ == "__main__":
    # Abre o navegador automaticamente
    threading.Timer(1, abrir_navegador).start()
    with socketserver.TCPServer(("", PORTA), BMVC_Controller) as httpd:
        print(f"Servidor BMVC Nível 2 rodando em: http://localhost:{PORTA}")
        httpd.serve_forever()