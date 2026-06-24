import sqlite3

class Roupa:
    def __init__(self, id, nome, categoria, tamanho, preco, imagem):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.tamanho = tamanho
        self.preco = float(preco)
        self.imagem = imagem

class RoupaModel:
    @staticmethod
    def conectar():
        conn = sqlite3.connect('banco_loja.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS roupas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                tamanho TEXT NOT NULL,
                preco REAL NOT NULL,
                imagem TEXT NOT NULL
            )
        ''')
        
        cursor.execute('SELECT COUNT(*) FROM roupas')
        if cursor.fetchone()[0] == 0:
            pecas_iniciais = [
                ("Camiseta Algodão Premium", "Camisetas", "M", 89.90, "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500"),
                ("Calça Jeans Streetwear", "Calças", "42", 189.00, "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500"),
                ("Moletom Canguru Preto", "Casacos", "G", 239.50, "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?w=500")
            ]
            cursor.executemany('INSERT INTO roupas (nome, categoria, tamanho, preco, imagem) VALUES (?, ?, ?, ?, ?)', pecas_iniciais)
            conn.commit()
        return conn

    @classmethod
    def listar_todas(cls):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM roupas ORDER BY id DESC')
        linhas = cursor.fetchall()
        conn.close()
        return [Roupa(*linha) for linha in linhas]

    @classmethod
    def buscar_por_id(cls, id_roupa):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM roupas WHERE id = ?', (int(id_roupa),))
        linha = cursor.fetchone()
        conn.close()
        return Roupa(*linha) if linha else None

    @classmethod
    def cadastrar(cls, nome, categoria, tamanho, preco, imagem):
        if not imagem or not imagem.startswith("http"):
            imagem = "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500"
        conn = cls.conectar()
        conn.execute('INSERT INTO roupas (nome, categoria, tamanho, preco, imagem) VALUES (?, ?, ?, ?, ?)', 
                    (nome, categoria, tamanho, float(preco), imagem))
        conn.commit()
        conn.close()

    @classmethod
    def atualizar(cls, id_roupa, nome, categoria, tamanho, preco, imagem):
        conn = cls.conectar()
        conn.execute('UPDATE roupas SET nome=?, categoria=?, tamanho=?, preco=?, imagem=? WHERE id=?', 
                    (nome, categoria, tamanho, float(preco), imagem, int(id_roupa)))
        conn.commit()
        conn.close()

    @classmethod
    def deletar(cls, id_roupa):
        conn = cls.conectar()
        conn.execute('DELETE FROM roupas WHERE id = ?', (int(id_roupa),))
        conn.commit()
        conn.close()