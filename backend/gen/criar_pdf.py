from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime

def criar_autorizacao_passeio(nome_responsavel, cpf_responsavel, rg_responsavel, endereco_responsavel, telefone_responsavel, nome_menor, rg_menor, cpf_menor):
    # Configurações de margem e tamanho da página
    PAGE_WIDTH, PAGE_HEIGHT = letter
    LEFT_MARGIN = 72  # 1 inch = 72 pontos
    RIGHT_MARGIN = 72
    TOP_MARGIN = 72
    BOTTOM_MARGIN = 72

    # Espaçamento entre parágrafos
    PARAGRAPH_SPACING = 12

    # Criar um documento PDF
    doc = SimpleDocTemplate("pdf/autorizacao_passeio.pdf", pagesize=letter,
                            leftMargin=LEFT_MARGIN,
                            rightMargin=RIGHT_MARGIN,
                            topMargin=TOP_MARGIN,
                            bottomMargin=BOTTOM_MARGIN)

    # Estilos de parágrafo
    styles = getSampleStyleSheet()
    body_style = styles["BodyText"]
    body_style.spaceAfter = PARAGRAPH_SPACING  # Espaçamento após cada parágrafo
    center_style = ParagraphStyle(name='Center', alignment=1)
    right_style = ParagraphStyle(name='Right', alignment=2)

    # Conteúdo do documento
    content = []

    # Adicionar título
    title = "Autorização de Saída"
    content.append(Paragraph(title, styles['Title']))

    # Adicionar parágrafos
    text_responsavel = f"Eu, {nome_responsavel}, portador do CPF nº {cpf_responsavel}, RG nº {rg_responsavel}, residente no endereço {endereco_responsavel}, telefone de contato {telefone_responsavel}, neste ato autorizo o(a) menor {nome_menor}, portador do RG nº {rg_menor} e CPF nº {cpf_menor}, a sair para o Curso de Capiates de Conselheiros em Limeira Sp, conforme os dados do evento baixo:"
    content.append(Paragraph(text_responsavel, body_style))

    # Adicionar detalhes do passeio
    content.append(Paragraph("Detalhes do Passeio:", styles['Heading2']))
    content.append(Paragraph(f"<b>Destino:</b> Escola Municipal Maria Apª de Luca Moore", body_style))
    content.append(Paragraph(f"<b>Endereço:</b> Rua Jorge Antonio , 69 Jd Aeroporto – Limeira SP", body_style))
    content.append(Paragraph(f"<b>Horário que inicia o curso do CCC:</b> 7h00", body_style))
    content.append(Paragraph(f"<b>Horário que finaliza o curso do CCC:</b> 16h30", body_style))
    content.append(Paragraph(f"<b>Data:</b> {datetime.now().strftime('%d/%m/%Y')} ", right_style))
    content.append(Spacer(1, 50))  # Espaço adicional

    # Adicionar linha acima da assinatura do responsável
    content.append(Paragraph("______________________________________________", center_style))  # Linha
    content.append(Spacer(1, 6))
    content.append(Paragraph("Assinatura do Responsável Legal:", center_style))
    content.append(Spacer(1, 6))
    content.append(Paragraph("CPF do Responsável:", center_style))
    content.append(Paragraph(f"{cpf_responsavel}", center_style))

    # Adicionar o conteúdo ao documento
    doc.build(content)
