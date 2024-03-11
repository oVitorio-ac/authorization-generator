import subprocess
from flask import Flask, render_template, request , jsonify
from backend.gen.criar_pdf import criar_autorizacao_desbravadores
from backend.mailer.send_email import enviar_email


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/autorizar_saida', methods=['GET', 'POST'])
def autorizar_saida():
    if request.method == 'POST':
        # Lógica para processar a autorização de saída aqui
        # Redirecionar para a página inicial após o processamento

        return render_template('forms_de_saida.html')


@app.route('/cadastrar_clube', methods=['GET', 'POST'])
def cadastrar_clube():
    if request.method == 'POST':
        # Lógica para processar o formulário de cadastro aqui
        # Redirecionar para a página inicial após o processamento do formulário

        return render_template('forms_de_cadastro.html')


@app.route('/processar_formulario_saida', methods=['POST'])
def processar_formulario_saida():
    dados = request.json
    dados_formatados = {
    'nome_responsavel': dados['nome_responsavel'],
    'cpf_responsavel': dados['cpf_responsavel'],
    'rg_responsavel': dados['rg_responsavel'],
    'telefone_responsavel': dados['telefone_responsavel'],
    'email_responsavel': dados['email_responsavel'],
    'endereco_responsavel': {
        'rua': dados['rua_responsavel'],
        'numero': dados['numero_responsavel'],
        'complemento': dados['complemento_responsavel'],
        'bairro': dados['bairro_responsavel'],
        'cidade': dados['cidade_responsavel'],
        'estado': dados['estado_responsavel']

    },
    'nome_menor': dados['nome_menor'],
    'rg_menor': dados['rg_menor'],
    'cpf_menor': dados['cpf_menor']
}
    endereco = f"{dados_formatados['endereco_responsavel']['rua']}, numero: {dados_formatados['endereco_responsavel']['numero']} {dados_formatados['endereco_responsavel']['complemento']} - {dados_formatados['endereco_responsavel']['bairro']}, {dados_formatados['endereco_responsavel']['cidade']} - {dados_formatados['endereco_responsavel']['estado']}"
    pdf_buffer = criar_autorizacao_desbravadores(dados_formatados['nome_responsavel'], dados_formatados['cpf_responsavel'], dados_formatados['rg_responsavel'],endereco, dados_formatados['telefone_responsavel'], dados_formatados['nome_menor'], dados_formatados['rg_menor'], dados_formatados['cpf_menor'])
    corpo= f"""
    Prezado(a) {dados_formatados['nome_responsavel']},

Espero que esta mensagem o encontre bem.

Gostaríamos de informá-lo(a) sobre os a altorização de saida para o(a) {dados_formatados['nome_menor']} crucial que o documento anexo seja assinado o mais rápido possível.

Para isso, oferecemos duas opções de assinatura:

Opção 1: Impressão e Escaneamento

Baixe o arquivo PDF anexado.
Imprima o documento.
Assine manualmente.
Escaneie o documento assinado.
Envie o arquivo escaneado para o endereço de e-mail: secretaria.alphacentauro@gmail.com.


Opção 2: Assinatura Digital pelo gov.br

Baixe o arquivo PDF anexado.
Utilize a assinatura digital disponível no gov.br para assinar o documento.
Envie o arquivo assinado digitalmente para o endereço de e-mail: secretaria.alphacentauro@gmail.com.
É fundamental que essas etapas sejam concluídas dentro do prazo estabelecido para evitar qualquer atraso nos processos seguintes.

Em caso de dúvidas ou dificuldades técnicas, não hesite em nos contatar.
pelo grupo dos pais do whatsapp

Agradecemos antecipadamente pela sua colaboração e compreensão.

Atenciosamente,

secrtaria do alpha centauro
"""
    enviar_email(dados_formatados['email_responsavel'], f'autorização de saida para o {dados_formatados["nome_menor"]}',corpo, pdf_buffer)
    return jsonify({"message": "authorização finalizada"})



if __name__ == '__main__':
    app.run(debug=True)
