<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <title>Editar Peça - Metaboom</title>
    <link href="/static/styles.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body class="bg-light p-5">
    <div class="container" style="max-width: 550px;">
        <div class="card shadow border-0">
            <div class="card-header bg-dark text-white fw-bold">✏️ Editando Peça #{{ID}}</div>
            <div class="card-body p-4">
                <form action="/salvar_edicao" method="POST" class="row g-3">
                    <input type="hidden" name="id" value="{{ID}}">
                    <div class="col-12"><label class="small fw-bold">Nome</label><input type="text" name="nome" class="form-control" value="{{NOME}}" required></div>
                    <div class="col-6"><label class="small fw-bold">Categoria</label><input type="text" name="categoria" class="form-control" value="{{CATEGORIA}}" required></div>
                    <div class="col-3"><label class="small fw-bold">Tamanho</label><input type="text" name="tamanho" class="form-control" value="{{TAMANHO}}" required></div>
                    <div class="col-3"><label class="small fw-bold">Preço</label><input type="number" step="0.01" name="preco" class="form-control" value="{{PRECO}}" required></div>
                    <div class="col-12"><label class="small fw-bold">URL da Imagem</label><input type="url" name="imagem" class="form-control" value="{{IMAGEM}}" required></div>
                    <div class="col-12 d-flex justify-content-between mt-4">
                        <a href="/" class="btn btn-outline-secondary">Voltar</a>
                        <button type="submit" class="btn btn-primary fw-bold">Salvar Alterações</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>
</html>