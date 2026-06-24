<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>Loja BMVC</title>
    <link href="/static/styles.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body class="bg-light">
    
    <nav class="navbar navbar-expand-lg navbar-light bg-white border-bottom shadow-sm">
        <div class="container px-4 px-lg-5">
            <a class="navbar-brand fw-bold" href="/">LOJA BMVC</a>
        </div>
    </nav>

    <header class="bg-dark py-4 mb-4">
        <div class="container px-4 px-lg-5 my-2 text-center text-white">
            <h1 class="display-5 fw-bolder">Loja BMVC</h1>
            <p class="lead fw-normal text-white-50 mb-0">Catálogo de Roupas & Acessórios</p>
        </div>
    </header>

    <div class="container px-4 px-lg-5 mb-5">
        <div class="card border-0 shadow-sm">
            <div class="card-header bg-dark text-white fw-bold">➕ Cadastrar Nova Peça no Estoque</div>
            <div class="card-body p-4">
                <form action="/cadastrar" method="POST" class="row g-3" onsubmit="return validarCadastro()">
                    <div class="col-md-4">
                        <label class="form-label small fw-bold">Nome da Roupa</label>
                        <input type="text" name="nome" class="form-control" placeholder="Ex: Camisa Polo" required>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label small fw-bold">Categoria</label>
                        <select name="categoria" class="form-select" required>
                            <option value="Camisetas">Camisetas</option>
                            <option value="Calças">Calças</option>
                            <option value="Casacos">Casacos</option>
                            <option value="Acessórios">Acessórios</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label small fw-bold">Tamanho/Numeração</label>
                        <input type="text" name="tamanho" class="form-control" placeholder="Ex: M ou 40" required>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label small fw-bold">Preço (R$)</label>
                        <input type="number" step="0.01" name="preco" class="form-control" placeholder="119.90" required>
                    </div>
                    <div class="col-md-10">
                        <label class="form-label small fw-bold">Link da Foto (Deixe vazio para foto padrão)</label>
                        <input type="url" name="imagem" class="form-control" placeholder="https://images.unsplash.com/...">
                    </div>
                    <div class="col-md-2 d-flex align-items-end">
                        <button type="submit" class="btn btn-success w-100 fw-bold">Cadastrar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <div class="container px-4 px-lg-5">
        <h4 class="fw-bolder mb-4">Peças Disponíveis:</h4>
        <div class="row gx-4 gx-lg-5 row-cols-1 row-cols-md-2 row-cols-xl-3 justify-content-center">
            {{VITRINE_DINAMICA}}
        </div>
    </div>

    <script src="/static/scripts.js"></script>
</body>
</html>