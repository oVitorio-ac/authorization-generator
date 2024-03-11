from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import utils
from datetime import datetime
from io import BytesIO

def criar_autorizacao_desbravadores(nome_responsavel, rg_responsavel, cpf_responsavel, endereco_responsavel, telefone_responsavel, nome_menor, rg_menor, cpf_menor):
    # Configurações de margem e tamanho da página
    PAGE_WIDTH, PAGE_HEIGHT = letter
    LEFT_MARGIN = 72  # 1 inch = 72 pontos
    RIGHT_MARGIN = 72
    TOP_MARGIN = 72
    BOTTOM_MARGIN = 72

    # Criar um buffer para armazenar o PDF
    buffer = BytesIO()

    # Criar um documento PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            leftMargin=LEFT_MARGIN,
                            rightMargin=RIGHT_MARGIN,
                            topMargin=TOP_MARGIN,
                            bottomMargin=BOTTOM_MARGIN)

    # Estilos de parágrafo
    styles = getSampleStyleSheet()
    body_style = styles["BodyText"]
    body_style.spaceAfter = 12  # Espaçamento após cada parágrafo
    body_style.fontName = "Helvetica"  # Alterar a fonte para remover o negrito
    center_style = ParagraphStyle(name='Center', alignment=1)
    right_style = ParagraphStyle(name='Right', alignment=2)

    # Função para adicionar imagem como marca d'água
    def add_watermark(canvas, doc):
        img_path = "static/ALPHA.png"
        img = utils.ImageReader(img_path)
        img_width = 500
        img_height = 700
        canvas.saveState()
        canvas.drawImage(img_path, (PAGE_WIDTH - img_width) / 2, (PAGE_HEIGHT - img_height) / 2, img_width, img_height, mask='auto')
        canvas.restoreState()

    # Conteúdo do documento
    content = []

    # Adicionar título
    title = "Autorização de Saída para Clube de Desbravadores"
    content.append(Paragraph(title, styles['Title']))

    # Adicionar parágrafos
    text_clube_responsavel = f"CLUBE DE DESBRAVADORES: Alpha Centauro - APAC/UCB \nRESPONSÁVEL PELO CLUBE: Evelyn Caroline Fontenele de Paula \nCPF: 44088265882"
    content.append(Paragraph(text_clube_responsavel, body_style))

    text_responsavel = f"Eu, {nome_responsavel}, Brasileiro (a), Portador do RG Nº {rg_responsavel}, CPF {cpf_responsavel}, residente na rua {endereco_responsavel}, telefone para contato com DDD {telefone_responsavel}, neste ato autorizo meu filho (a) ou dependente legal, {nome_menor}, Portador do RG Nº {rg_menor}, CPF {cpf_menor}, a participar da Caminhada, que realizar-se-á no Domingo , 24/03/2024 na Cidade de Ameircana. Nomeio neste período como responsável pelo meu dependente acima descrito, o responsável pelo Clube de Desbravadores conforme identificado acima."
    content.append(Paragraph(text_responsavel, body_style))

    content.append(Paragraph("Consciente dos grandes benefícios recebidos através do Clube de Desbravadores acima descrito, abdico de responsabilizar, em qualquer instância judicial, o (os) responsável (eis) do referido Clube em todos os níveis, bem como a Igreja Adventista do Sétimo Dia, por qualquer dano causado ou sofrido por meu dependente, devido a sua própria atuação, no percurso de ida e volta bem como no decurso do referido evento.", body_style))
    
    content.append(Paragraph("Em caso de acidente, ou doença, autorizo o responsável acima identificado a tomar toda e qualquer decisão necessária para o restabelecimento da saúde do meu dependente, junto a todo e qualquer órgão que se fizer necessário, inclusive se houver necessidade de intervenção clinica ou cirúrgica. Declaro ainda que nada omiti na declaração de saúde, sendo de minha responsabilidade qualquer complicação clínica devido ao preenchimento equivocado ou omissão.", body_style))
    
    content.append(Spacer(1, 12))

    # Adicionar a data atual alinhada à esquerda
    current_date = datetime.now().strftime("%d/%m/%Y")
    content.append(Paragraph(f"Data: {current_date}", body_style))

    # Adicionar linha acima da assinatura do responsável
    content.append(Paragraph("______________________________________________", center_style))  # Linha
    content.append(Spacer(1, 6))
    content.append(Paragraph("Assinatura do Responsável Legal:", center_style))
    content.append(Spacer(1, 6))
    content.append(Paragraph("CPF do Responsável:", center_style))
    content.append(Paragraph(f"{cpf_responsavel}", center_style))

    # Adicionar o conteúdo ao documento
    doc.build(content, onFirstPage=add_watermark)

    # Retornar o buffer
    buffer.seek(0)
    return buffer
