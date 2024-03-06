document.addEventListener('DOMContentLoaded', function () {
    var etapaAtual = 1;
    var etapa1 = document.getElementById('etapa1');
    var etapa2 = document.getElementById('etapa2');
    var etapa3 = document.getElementById('etapa3');
    var etapaAtualSpan = document.getElementById('etapa_atual');
    var proximoEtapaButton = document.getElementById('proximo_etapa');
    var enviarFormularioButton = document.getElementById('enviar_formulario');

    function mascaraCpf(input) {
        let value = input.value;
        value = value.replace(/\D/g, '');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        input.value = value;
    }

    function mascaraRg(input) {
        let value = input.value;
        value = value.replace(/\D/g, '');
        value = value.replace(/(\d{2})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        input.value = value;
    }
    

    document.getElementById('cpf_responsavel').addEventListener('input', function () {
        mascaraCpf(this);
    });

    document.getElementById('rg_responsavel').addEventListener('input', function () {
        mascaraRg(this);
    });

    document.getElementById('cpf_menor').addEventListener('input', function () {
        mascaraCpf(this);
    });

    document.getElementById('rg_menor').addEventListener('input', function () {
        mascaraRg(this);
    });

        function mascaraTelefone(input) {
            let value = input.value;
            value = value.replace(/\D/g, ''); // Remove todos os caracteres que não são dígitos
            value = value.replace(/(\d{2})(\d)/, '($1) $2'); // Formata como (XX)
            value = value.replace(/(\d{4})(\d)/, '$1-$2'); // Formata como (XX) XXXX-X
            input.value = value;
        }
    
        document.getElementById('telefone_responsavel').addEventListener('input', function () {
            mascaraTelefone(this);
        });

    function mostrarEtapa(etapa) {
        etapa1.style.display = 'none';
        etapa2.style.display = 'none';
        etapa3.style.display = 'none';

        if (etapa === 1) {
            etapa1.style.display = 'block';
        } else if (etapa === 2) {
            etapa2.style.display = 'block';
        } else if (etapa === 3) {
            etapa3.style.display = 'block';
            proximoEtapaButton.style.display = 'none';
            enviarFormularioButton.style.display = 'block';
        }
        etapaAtual = etapa;
        etapaAtualSpan.textContent = etapa;
    }

    proximoEtapaButton.addEventListener('click', function () {
        if (etapaAtual === 1) {
            // Validar dados da etapa 1
            if (validarEtapa1()) {
                // Avançar para a próxima etapa
                etapaAtual++;
                mostrarEtapa(etapaAtual);
            } else {
                alert("Por favor, preencha todos os campos da Etapa 1.");
            }
        } else if (etapaAtual === 2) {
            // Validar dados da etapa 2

            // Avançar para a próxima etapa
            etapaAtual++;
            mostrarEtapa(etapaAtual);
        }
    });

    function validarEtapa1() {
        var nome = document.getElementById('nome_responsavel').value;
        var cpf = document.getElementById('cpf_responsavel').value;
        var rg = document.getElementById('rg_responsavel').value;
        var email = document.getElementById('email_responsavel').value;

        if (nome.trim() === '' || cpf.trim() === '' || rg.trim() === '' || email.trim() === '') {
            return false;
        }
        return true;
    }

    mostrarEtapa(etapaAtual);

    document.getElementById('formulario_autorizacao').addEventListener('submit', function (event) {
        event.preventDefault(); // Impede o envio padrão do formulário
    
        var dadosFormulario = {
            nome_responsavel: document.getElementById('nome_responsavel').value,
            cpf_responsavel: document.getElementById('cpf_responsavel').value,
            rg_responsavel: document.getElementById('rg_responsavel').value,
            email_responsavel: document.getElementById('email_responsavel').value,
            rua_responsavel: document.getElementById('rua_responsavel').value,
            numero_responsavel: document.getElementById('numero_responsavel').value,
            complemento_responsavel: document.getElementById('complemento_responsavel').value,
            bairro_responsavel: document.getElementById('bairro_responsavel').value,
            cidade_responsavel: document.getElementById('cidade_responsavel').value,
            estado_responsavel: document.getElementById('estado_responsavel').value,
            telefone_responsavel: document.getElementById('telefone_responsavel').value,
            nome_menor: document.getElementById('nome_menor').value,
            rg_menor: document.getElementById('rg_menor').value,
            cpf_menor: document.getElementById('cpf_menor').value
        };
    
        fetch('/processar_formulario_saida', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dadosFormulario)
        })
            .then(response => response.json())
            .then(data => {
                // Exibir modal de sucesso
                $('#successModal').modal('show');

                // Redirecionar para a página inicial após o usuário clicar no botão "OK" do modal
                $('#successModal').on('hidden.bs.modal', function (e) {
                    window.location.href = '/';
                });
            })
            .catch(error => {
                // Exibir modal de erro
                $('#errorModal').modal('show');
                console.error('Erro ao enviar formulário:', error);
            });
    });
});
