// 1. GATILHO DE VALIDAÇÃO DO FORMULÁRIO
function validarCadastro() {
    const precoInput = document.querySelector('input[name="preco"]');
    const preco = parseFloat(precoInput.value);

    if (preco <= 0) {
        alert("❌ Bloqueio do JavaScript:\nO preço da peça de roupa não pode ser R$ 0,00 ou negativo!");
        precoInput.focus();
        return false; // Trava o envio pro Python
    }
    return true; // Libera o envio
}

// 2. GATILHO DE DELEÇÃO VIA FETCH API
function deletarRoupa(id) {
    if (confirm(`Tem certeza que deseja remover a peça #${id} do estoque?`)) {
        fetch(`/api/deletar?id=${id}`)
            .then(response => response.json())
            .then(data => {
                if (data.status === "ok") {
                    document.body.style.opacity = '0.4'; // Efeito visual de saída
                    setTimeout(() => {
                        window.location.reload(); // Atualiza a tela
                    }, 150);
                }
            })
            .catch(error => alert("Falha de conexão com o Controller Python."));
    }
}