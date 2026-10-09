"""
Gerador de Imagens Profissional para Carrossel do Instagram (1080 x 1350 px)
Versão 5.0:
- Perguntas reflexivas e instigantes ao final de cada slide contra Flávio Bolsonaro
- Slides 3, 4, 5, 6 e 8 equipados com box de reflexão ("Você acha justo?")
- Agregador de Links Oficial ao vivo: https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09
- Desenho vetorial nativo (zero tofus) e layout auto-adaptável
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "carousel_images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH = 1080
HEIGHT = 1350
TOTAL_SLIDES = 10

FONT_BOLD_PATH = "C:/Windows/Fonts/segoeuib.ttf"
FONT_REGULAR_PATH = "C:/Windows/Fonts/segoeui.ttf"
FONT_SEMIBOLD_PATH = "C:/Windows/Fonts/seguisb.ttf"

TELEGRAPH_URL = "telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09"

def get_font(size: int, bold: bool = False):
    try:
        path = FONT_BOLD_PATH if bold else FONT_REGULAR_PATH
        if not os.path.exists(path):
            path = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    paragraphs = text.split("\n")
    lines = []
    for para in paragraphs:
        if not para.strip():
            continue
        words = para.split(" ")
        current_line = []
        for word in words:
            test_line = " ".join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if (bbox[2] - bbox[0]) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
        if current_line:
            lines.append(" ".join(current_line))
    return lines

# ==============================================================================
# DESENHO VETORIAL LIMPO
# ==============================================================================
def draw_vector_check(draw: ImageDraw.ImageDraw, x: int, y: int, size: int = 20, color: str = "#00E676"):
    draw.line([(x, y + size * 0.5), (x + size * 0.35, y + size * 0.85)], fill=color, width=3)
    draw.line([(x + size * 0.35, y + size * 0.85), (x + size, y + size * 0.15)], fill=color, width=3)

def draw_vector_cross(draw: ImageDraw.ImageDraw, x: int, y: int, size: int = 18, color: str = "#FF334B"):
    draw.line([(x, y), (x + size, y + size)], fill=color, width=3)
    draw.line([(x + size, y), (x, y + size)], fill=color, width=3)

def draw_vector_dot(draw: ImageDraw.ImageDraw, x: int, y: int, radius: int = 5, color: str = "#63B3ED"):
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)

def draw_vector_arrow(draw: ImageDraw.ImageDraw, x: int, y: int, size: int = 16, color: str = "#63B3ED"):
    draw.line([(x, y + size // 2), (x + size, y + size // 2)], fill=color, width=3)
    draw.polygon([(x + size - 5, y), (x + size + 5, y + size // 2), (x + size - 5, y + size)], fill=color)

def draw_vector_bookmark(draw: ImageDraw.ImageDraw, x: int, y: int, width: int = 14, height: int = 18, color: str = "#63B3ED"):
    draw.polygon([(x, y), (x + width, y), (x + width, y + height), (x + width // 2, y + height - 5), (x, y + height)], fill=color)

def draw_header_and_footer(draw: ImageDraw.ImageDraw, slide_num: int, total_slides: int = TOTAL_SLIDES):
    badge_text = "AUDITORIA DE DADOS • ELEIÇÕES 2026"
    font_badge = get_font(20, bold=True)
    bbox_b = draw.textbbox((0, 0), badge_text, font=font_badge)
    text_w = bbox_b[2] - bbox_b[0]
    text_h = bbox_b[3] - bbox_b[1]
    
    pill_w = text_w + 48
    pill_h = text_h + 22
    pill_x = 70
    pill_y = 50
    
    draw.rounded_rectangle((pill_x, pill_y, pill_x + pill_w, pill_y + pill_h), radius=pill_h // 2, fill="#161B26", outline="#2D3748", width=2)
    draw.text((pill_x + 24, pill_y + (pill_h - text_h) // 2 - 2), badge_text, fill="#63B3ED", font=font_badge)
    
    font_slide = get_font(21, bold=True)
    slide_str = f"SLIDE {slide_num}/{total_slides}"
    bbox_s = draw.textbbox((0, 0), slide_str, font=font_slide)
    w_s = bbox_s[2] - bbox_s[0]
    draw.text((WIDTH - 70 - w_s, 60), slide_str, fill="#A0AEC0", font=font_slide)
    
    draw.line([(70, HEIGHT - 110), (WIDTH - 70, HEIGHT - 110)], fill="#202736", width=2)
    
    font_foot = get_font(20, bold=False)
    draw.text((70, HEIGHT - 84), "Fontes: Senado, BACEN, IBGE, TSE, PF e Coaf", fill="#718096", font=font_foot)
    
    font_cta = get_font(21, bold=True)
    cta_str = "ARRASTE PRO LADO" if slide_num < total_slides else "SALVE & COMPARTILHE"
    bbox_cta = draw.textbbox((0, 0), cta_str, font=font_cta)
    w_cta = bbox_cta[2] - bbox_cta[0]
    
    icon_w = 20
    total_w = w_cta + 12 + icon_w
    cta_x = WIDTH - 70 - total_w
    cta_y = HEIGHT - 84
    
    draw.text((cta_x, cta_y), cta_str, fill="#63B3ED", font=font_cta)
    if slide_num < total_slides:
        draw_vector_arrow(draw, cta_x + w_cta + 8, cta_y + 3, size=16, color="#63B3ED")
    else:
        draw_vector_bookmark(draw, cta_x + w_cta + 8, cta_y + 2, width=14, height=18, color="#63B3ED")

def draw_headline_block(draw: ImageDraw.ImageDraw, headline: str, subhead: str, highlight_color="#FF4D4D") -> int:
    font_hl = get_font(50, bold=True)
    font_sub = get_font(26, bold=False)
    
    y = 150
    lines_hl = wrap_text(headline, font_hl, WIDTH - 140, draw)
    for line in lines_hl:
        draw.text((70, y), line, fill="#FFFFFF", font=font_hl)
        y += 64
        
    y += 10
    lines_sub = wrap_text(subhead, font_sub, WIDTH - 140, draw)
    for line in lines_sub:
        draw.text((70, y), line, fill=highlight_color, font=font_sub)
        y += 36
        
    return y + 25

def draw_unboxed_reflection(
    draw: ImageDraw.ImageDraw,
    y: int,
    eyebrow: str,
    segments: list,
    eyebrow_color: str = "#FF8C42",
    font_size: int = 32,
    line_spacing: int = 46,
    start_x: int = 70,
    max_width: int = WIDTH - 140
) -> int:
    """
    Desenha uma pergunta reflexiva / provocativa de grande impacto FORA de cards,
    com visual editorial direto, quebra de linha inteligente e palavras-chave coloridas.
    """
    font = get_font(font_size, bold=True)
    space_w = draw.textlength(" ", font=font)
    
    # 1. Eyebrow com indicador vertical arredondado
    font_eye = get_font(22, bold=True)
    draw.rounded_rectangle((start_x, y + 2, start_x + 6, y + 24), radius=3, fill=eyebrow_color)
    draw.text((start_x + 18, y), eyebrow, fill=eyebrow_color, font=font_eye)
    
    # 2. Tokenizar palavras preservando cores e evitando espaços indesejados
    tokens = []
    for chunk_text, color in segments:
        words = chunk_text.split(" ")
        for w in words:
            if not w:
                continue
            tokens.append((w, color))
            
    # 3. Quebra de linha inteligente
    lines = []
    current_line = []
    current_line_w = 0
    
    for word, color in tokens:
        w_len = draw.textlength(word, font=font)
        is_punct = word in [":", "?", "!", ",", ".", ";"]
        needs_space = (current_line_w > 0) and not is_punct
        needed_w = (space_w if needs_space else 0) + w_len
        
        if current_line_w + needed_w <= max_width:
            current_line.append((word, color, needs_space, w_len))
            current_line_w += needed_w
        else:
            if current_line:
                lines.append(current_line)
            current_line = [(word, color, False, w_len)]
            current_line_w = w_len
            
    if current_line:
        lines.append(current_line)
        
    # 4. Renderizar texto
    cur_y = y + 40
    for line in lines:
        cur_x = start_x
        for word, color, has_space, w_len in line:
            if has_space:
                cur_x += space_w
            draw.text((cur_x, cur_y), word, fill=color, font=font)
            cur_x += w_len
        cur_y += line_spacing
        
    return cur_y

# ==============================================================================
# SLIDE 1: CAPA
# ==============================================================================
def create_slide_1():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 1)
    
    tag_str = "RELATÓRIO INDEPENDENTE • DADOS ABERTOS"
    font_tag = get_font(20, bold=True)
    bbox_t = draw.textbbox((0, 0), tag_str, font=font_tag)
    tag_w = (bbox_t[2] - bbox_t[0]) + 40
    draw.rounded_rectangle((70, 160, 70 + tag_w, 208), radius=10, fill="#2D1215", outline="#E53E3E", width=2)
    draw.text((90, 172), tag_str, fill="#FC8181", font=font_tag)
    
    font_main = get_font(58, bold=True)
    h_lines = [
        "AUDITEI FLÁVIO",
        "BOLSONARO NO CÓDIGO.",
        "OS DADOS ASSUSTAM."
    ]
    y = 245
    for hl in h_lines:
        color = "#FF4D4D" if "DADOS ASSUSTAM" in hl else "#FFFFFF"
        draw.text((70, y), hl, fill=color, font=font_main)
        y += 74
        
    card_y = y + 40
    card_w = WIDTH - 140
    
    font_intro = get_font(28, bold=True)
    intro_lines = wrap_text("O que encontrei no terminal assusta quem ainda está indeciso no 2º turno:", font_intro, card_w - 70, draw)
    
    bullets = [
        ("cross", "Voto nominal contra o Salário Mínimo no Senado"),
        ("cross", "Mansão de R$ 6 milhões e depósitos em dinheiro vivo"),
        ("cross", "Uso da Abin paralela comprovado pela Polícia Federal"),
        ("check", "O contraste com os dados oficiais de renda e emprego de Lula")
    ]
    
    font_bullet = get_font(24, bold=False)
    total_bullet_h = 0
    wrapped_bullets = []
    for icon_type, b_text in bullets:
        b_lines = wrap_text(b_text, font_bullet, card_w - 110, draw)
        wrapped_bullets.append((icon_type, b_lines))
        total_bullet_h += (len(b_lines) * 34) + 24
        
    card_h = 35 + (len(intro_lines) * 38) + 20 + total_bullet_h + 80
    draw.rounded_rectangle((70, card_y, 70 + card_w, card_y + card_h), radius=22, fill="#141824", outline="#2D3748", width=2)
    
    cur_y = card_y + 35
    for il in intro_lines:
        draw.text((105, cur_y), il, fill="#63B3ED", font=font_intro)
        cur_y += 38
    cur_y += 15
    
    for icon_type, b_lines in wrapped_bullets:
        if icon_type == "cross":
            draw_vector_cross(draw, 105, cur_y + 5, size=18, color="#FF334B")
        else:
            draw_vector_check(draw, 105, cur_y + 4, size=20, color="#00E676")
            
        for bl in b_lines:
            draw.text((145, cur_y), bl, fill="#E2E8F0", font=font_bullet)
            cur_y += 34
        cur_y += 18
        
    seal_y = card_y + card_h - 60
    draw.rounded_rectangle((105, seal_y, 105 + 390, seal_y + 42), radius=10, fill="#1B4332", outline="#2D6A4F", width=2)
    draw_vector_check(draw, 120, seal_y + 11, size=18, color="#74C69D")
    draw.text((150, seal_y + 10), "100% BASEADO EM DADOS OFICIAIS", fill="#74C69D", font=get_font(19, bold=True))
    
    return img

# ==============================================================================
# SLIDE 2: METODOLOGIA E DE ONDE SAÍRAM OS DADOS
# ==============================================================================
def create_slide_2():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 2)
    
    start_y = draw_headline_block(
        draw,
        headline="DE ONDE SAÍRAM ESTES DADOS?",
        subhead="Nenhum número aqui é opinião ou post de internet. Veja as fontes oficiais:",
        highlight_color="#63B3ED"
    )
    
    sources = [
        ("1. APIS DO BANCO CENTRAL E IBGE",
         "Séries temporais oficiais do Sistema SGS do BACEN (Reservas, Salário Real e Inflação) e bases SIDRA/PNAD Contínua do IBGE (Desemprego e Renda).",
         "#38A169"),
        ("2. REGISTROS NOMINAIS DO SENADO FEDERAL",
         "Votações nominais no painel eletrônico, diários oficiais e tramitação de projetos de lei e PECs direto de legis.senado.leg.br.",
         "#3182CE"),
        ("3. INQUÉRITOS DA PF, COAF E TRIBUNAIS",
         "Documentos oficiais da Operação Vigilância Aproximada (STF), relatórios de inteligência financeira do Coaf, denúncias do MP-RJ e acórdãos do TSE.",
         "#DD6B20")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in sources:
        lines = wrap_text(desc, get_font(23), card_w - 70, draw)
        card_h = 65 + (len(lines) * 34) + 20
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw.text((105, cy + 22), title, fill=border_col, font=get_font(26, bold=True))
        
        ly = cy + 68
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(23))
            ly += 34
        cy += card_h + 18
        
    code_h = 160
    draw.rounded_rectangle((70, cy, 70 + card_w, cy + code_h), radius=18, fill="#101D2C", outline="#3182CE", width=2)
    draw_vector_check(draw, 105, cy + 30, size=24, color="#63B3ED")
    draw.text((140, cy + 26), "CÓDIGO ABERTO E REPRODUTÍVEL", fill="#63B3ED", font=get_font(26, bold=True))
    
    code_desc = "O script em Python que consulta essas APIs e cruza os dados está 100% público no GitHub para você clonar e auditar na sua própria máquina."
    code_lines = wrap_text(code_desc, get_font(22), card_w - 70, draw)
    cly = cy + 72
    for cl in code_lines:
        draw.text((105, cly), cl, fill="#CBD5E0", font=get_font(22))
        cly += 32
        
    return img

# ==============================================================================
# SLIDE 3: O BOLSO DO TRABALHADOR + PERGUNTA INSTIGANTE
# ==============================================================================
def create_slide_3():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 3)
    
    start_y = draw_headline_block(
        draw,
        headline="ELE VOTOU CONTRA O SEU BOLSO.",
        subhead="O histórico real de Flávio Bolsonaro no Senado Federal:",
        highlight_color="#FC8181"
    )
    
    cards = [
        ("VOTO CONTRA O SALÁRIO MÍNIMO", 
         "No Senado, votou CONTRA a política permanente de aumento real do piso salarial acima da inflação pelo PIB. Seu grupo agora defende desvincular benefícios do salário mínimo.",
         "#E53E3E"),
        ("CONTA DE LUZ MAIS CARA", 
         "Votou 'SIM' pela privatização da Eletrobras (MP 1031) com 'jabutis' legislativos que aumentaram as tarifas de energia para as famílias brasileiras.",
         "#DD6B20"),
        ("SAÚDE E EDUCAÇÃO CONGELADAS", 
         "Apoiou o teto de gastos rígido que cortou verbas de hospitais, Farmácia Popular e merenda escolar em todo o país.",
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in cards:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 58 + (len(lines) * 32) + 16
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw_vector_cross(draw, 105, cy + 23, size=18, color=border_col)
        draw.text((135, cy + 20), title, fill=border_col, font=get_font(25, bold=True))
        
        ly = cy + 62
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 32
        cy += card_h + 14
        
    # Pergunta Instigante ao final (FORA DE CARD + FONTE MAIOR + PALAVRAS-CHAVE DESTACADAS)
    draw_unboxed_reflection(
        draw,
        y=cy + 25,
        eyebrow="PERGUNTA DIRETA PRO SEU BOLSO:",
        segments=[
            ("Quer ", "#FFFFFF"),
            ("MENOS AUMENTO NO SALÁRIO", "#FF334B"),
            (" e a sua ", "#FFFFFF"),
            ("CONTA DE LUZ MAIS CARA?", "#FF8C42"),
            (" É justo você trabalhar dobrado para bancar ", "#FFFFFF"),
            ("PRIVILÉGIO DE POLÍTICO?", "#ECC94B")
        ],
        eyebrow_color="#FF8C42",
        font_size=32,
        line_spacing=46
    )
    
    return img

# ==============================================================================
# SLIDE 4: EVOLUÇÃO PATRIMONIAL + PERGUNTA INSTIGANTE
# ==============================================================================
def create_slide_4():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 4)
    
    start_y = draw_headline_block(
        draw,
        headline="MANSÃO DE R$ 6 MI E DINHEIRO VIVO.",
        subhead="A matemática financeira apontada por Coaf e Ministério Público:",
        highlight_color="#FC8181"
    )
    
    cards = [
        ("MANSÃO DE R$ 6 MILHÕES NO LAGO SUL",
         "Comprou imóvel de altíssimo luxo em bairro nobre de Brasília com renda parlamentar e condições de crédito atípicas no Banco de Brasília (BRB).",
         "#E53E3E"),
        ("48 DEPÓSITOS EM DINHEIRO VIVO EM 1 MÊS",
         "O Coaf identificou 48 depósitos fracionados de R$ 2.000 em espécie em caixas eletrônicos da Alerj, método clássico para burlar o Banco Central.",
         "#DD6B20"),
        ("R$ 1,6 MILHÃO NA LOJA DE CHOCOLATES",
         "Perícia técnica do MP-RJ revelou descompasso milionário entre as vendas reais de doces e grandes volumes de dinheiro vivo depositados no comércio.",
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in cards:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 58 + (len(lines) * 32) + 16
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw_vector_cross(draw, 105, cy + 23, size=18, color=border_col)
        draw.text((135, cy + 20), title, fill=border_col, font=get_font(25, bold=True))
        
        ly = cy + 62
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 32
        cy += card_h + 14
        
    # Pergunta Instigante ao final (FORA DE CARD + FONTE MAIOR + PALAVRAS-CHAVE DESTACADAS)
    draw_unboxed_reflection(
        draw,
        y=cy + 25,
        eyebrow="A CONTA FECHA PRA VOCÊ?",
        segments=[
            ("Enquanto você ", "#FFFFFF"),
            ("SUA O MÊS TODO", "#CBD5E0"),
            (" contando moedas, ele comprou ", "#FFFFFF"),
            ("MANSÃO DE R$ 6 MILHÕES", "#FF334B"),
            (" e fez ", "#FFFFFF"),
            ("48 DEPÓSITOS EM DINHEIRO VIVO.", "#ECC94B"),
            (" Você aceita sustentar essa farra?", "#FC8181")
        ],
        eyebrow_color="#ECC94B",
        font_size=32,
        line_spacing=46
    )
    
    return img

# ==============================================================================
# SLIDE 5: ABIN PARALELA + PERGUNTA INSTIGANTE
# ==============================================================================
def create_slide_5():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 5)
    
    start_y = draw_headline_block(
        draw,
        headline="ABIN PARALELA: POLÍCIA FAMILIAR.",
        subhead="Inquérito oficial da Polícia Federal no STF comprovou o esquema:",
        highlight_color="#FC8181"
    )
    
    card_w = WIDTH - 140
    card_h = 440
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + card_h), radius=22, fill="#1C141E", outline="#E53E3E", width=3)
    
    draw.text((105, start_y + 35), "O RELATÓRIO OFICIAL DA POLÍCIA FEDERAL:", fill="#FC8181", font=get_font(28, bold=True))
    
    points = [
        "A Agência Brasileira de Inteligência (Abin) foi usada ilegalmente para espionar desafetos políticos e auditores da Receita.",
        "Foram produzidos relatórios secretos pagos com os seus impostos para BLINDAR Flávio Bolsonaro no caso das rachadinhas.",
        "Áudio gravado apreendido pela PF registrou reunião no Planalto com plano direto de defesa privada de Flávio."
    ]
    
    py = start_y + 90
    for pt in points:
        draw_vector_dot(draw, 115, py + 12, radius=5, color="#FC8181")
        lines = wrap_text(pt, get_font(23), card_w - 90, draw)
        for l in lines:
            draw.text((135, py), l, fill="#FFFFFF", font=get_font(23))
            py += 34
        py += 14
        
    # Pergunta Instigante ao final (FORA DE CARD + FONTE MAIOR + PALAVRAS-CHAVE DESTACADAS)
    draw_unboxed_reflection(
        draw,
        y=start_y + card_h + 35,
        eyebrow="RESPONDA COM SINCERIDADE:",
        segments=[
            ("Você acha certo o ", "#FFFFFF"),
            ("DINHEIRO DOS SEUS IMPOSTOS", "#ECC94B"),
            (" sustentar uma ", "#FFFFFF"),
            ("POLÍCIA SECRETA ILEGAL", "#FF334B"),
            (" para ", "#FFFFFF"),
            ("BLINDAR FILHO DE POLÍTICO", "#FC8181"),
            (" contra a Justiça?", "#FFFFFF")
        ],
        eyebrow_color="#FF4D4D",
        font_size=32,
        line_spacing=46
    )
    
    return img

# ==============================================================================
# SLIDE 6: INSTABILIDADE E PL + PERGUNTA INSTIGANTE
# ==============================================================================
def create_slide_6():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 6)
    
    start_y = draw_headline_block(
        draw,
        headline="GOLPISMO E MULTA DE R$ 23 MILHÕES.",
        subhead="A instabilidade política crônica provocada pelo partido de Flávio:",
        highlight_color="#FC8181"
    )
    
    cards = [
        ("MULTA DE R$ 22,9 MI DO TSE",
         "O PL de Flávio Bolsonaro foi condenado pelo TSE por litigância de má-fé ao pedir a anulação de votos sem apresentar nenhuma prova técnica.",
         "#E53E3E"),
        ("DEFESA DE ANISTIA AO 8 DE JANEIRO",
         "Flávio lidera articulações no Senado para perdoar judicialmente os envolvidos na depredação dos Três Poderes, promovendo impunidade.",
         "#DD6B20"),
        ("RELATOR DA 'PEC DAS PRAIAS'",
         "Atuou diretamente na proposta polêmica que abre brechas para privatização de faixas de praia no litoral brasileiro.",
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in cards:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 58 + (len(lines) * 32) + 16
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw_vector_cross(draw, 105, cy + 23, size=18, color=border_col)
        draw.text((135, cy + 20), title, fill=border_col, font=get_font(25, bold=True))
        
        ly = cy + 62
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 32
        cy += card_h + 14
        
    # Pergunta Instigante ao final (FORA DE CARD + FONTE MAIOR + PALAVRAS-CHAVE DESTACADAS)
    draw_unboxed_reflection(
        draw,
        y=cy + 25,
        eyebrow="O BRASIL AGUENTA MAIS CRISE?",
        segments=[
            ("O país precisa de ", "#FFFFFF"),
            ("PAZ E ESTABILIDADE", "#00E676"),
            (" para gerar empregos ou de ", "#FFFFFF"),
            ("MULTAS DE R$ 23 MILHÕES,", "#FF334B"),
            (" ameaça de golpe e ", "#FFFFFF"),
            ("BRIGA POLÍTICA TODO DIA?", "#FF8C42")
        ],
        eyebrow_color="#FF8C42",
        font_size=32,
        line_spacing=46
    )
    
    return img

# ==============================================================================
# SLIDE 7: O CONTRASTE (LULA)
# ==============================================================================
def create_slide_7():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 7)
    
    start_y = draw_headline_block(
        draw,
        headline="O CONTRASTE: TRABALHO E RENDA.",
        subhead="O que as séries oficiais do Banco Central e IBGE comprovam sobre Lula:",
        highlight_color="#68D391"
    )
    
    metrics = [
        ("+84% GANHO REAL NO SALÁRIO", 
         "Poder de compra do salário mínimo deflacionado pelo IPCA crescendo todo ano acima da inflação.", 
         "#38A169"),
        ("US$ 365 BILHÕES EM RESERVAS", 
         "O Brasil saiu de devedor do FMI para a construção de uma muralha cambial que protege o real.", 
         "#3182CE"),
        ("DESEMPREGO EM 6,2%", 
         "Taxa de desocupação nas mínimas históricas pela PNAD Contínua do IBGE.", 
         "#38A169"),
        ("ESTABILIDADE DAS REGRAS", 
         "Diálogo com os poderes, respeito às eleições e previsibilidade para quem produz.", 
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, col in metrics:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 60 + (len(lines) * 32) + 16
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=col, width=2)
        draw_vector_check(draw, 105, cy + 22, size=20, color=col)
        draw.text((135, cy + 20), title, fill=col, font=get_font(26, bold=True))
        
        ly = cy + 62
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 32
        cy += card_h + 16
        
    # Pergunta Reflexiva ao final (FORA DE CARD + FONTE MAIOR + PALAVRAS-CHAVE DESTACADAS)
    draw_unboxed_reflection(
        draw,
        y=cy + 25,
        eyebrow="A ESCOLHA RACIONAL:",
        segments=[
            ("Com o ", "#FFFFFF"),
            ("SALÁRIO SUBINDO DE VERDADE", "#00E676"),
            (" e o ", "#FFFFFF"),
            ("DESEMPREGO EM QUEDA RECORDE,", "#63B3ED"),
            (" vale a pena trocar a sua segurança por ", "#FFFFFF"),
            ("ESCÂNDALO E AVENTURA?", "#FF334B")
        ],
        eyebrow_color="#00E676",
        font_size=32,
        line_spacing=46
    )
        
    return img

# ==============================================================================
# SLIDE 8: A ESCOLHA RACIONAL PARA O INDECISO + PERGUNTA INSTIGANTE
# ==============================================================================
def create_slide_8():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 8)
    
    start_y = draw_headline_block(
        draw,
        headline="A ESCOLHA RACIONAL PARA O INDECISO.",
        subhead="Não é sobre torcer para um time. É sobre gerenciar riscos para o seu bolso:",
        highlight_color="#63B3ED"
    )
    
    card_w = WIDTH - 140
    box_lula_h = 280
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + box_lula_h), radius=22, fill="#0F2417", outline="#2F855A", width=2)
    draw.text((105, start_y + 22), "O PROJETO LULA (PREVISIBILIDADE):", fill="#68D391", font=get_font(25, bold=True))
    lula_pts = [
        "Salário mínimo subindo todo ano com fórmula real (PIB + IPCA).",
        "Isenção do Imposto de Renda para quem ganha até R$ 5.000.",
        "Mercado de trabalho aquecido e programas sociais fortalecidos.",
        "Segurança jurídica e respeito absoluto às eleições."
    ]
    ly = start_y + 65
    for pt in lula_pts:
        draw_vector_check(draw, 105, ly + 3, size=16, color="#00E676")
        lines = wrap_text(pt, get_font(21), card_w - 70, draw)
        for l in lines:
            draw.text((135, ly), l, fill="#FFFFFF", font=get_font(21))
            ly += 29
        ly += 8
        
    box_flavio_y = start_y + box_lula_h + 18
    box_flavio_h = 280
    draw.rounded_rectangle((70, box_flavio_y, 70 + card_w, box_flavio_y + box_flavio_h), radius=22, fill="#2A1215", outline="#C53030", width=2)
    draw.text((105, box_flavio_y + 22), "O PROJETO FLÁVIO / PL (RISCO CRÔNICO):", fill="#FC8181", font=get_font(25, bold=True))
    flavio_pts = [
        "Voto formal contra a valorização permanente do salário.",
        "48 depósitos em dinheiro vivo rastreados pelo Coaf e mansão de R$ 6M.",
        "Aparelhamento comprovado da Abin paralela para proteção privada.",
        "Multas milionárias por questionar urnas e instabilidade diária."
    ]
    fy = box_flavio_y + 65
    for pt in flavio_pts:
        draw_vector_cross(draw, 105, fy + 3, size=16, color="#FF334B")
        lines = wrap_text(pt, get_font(21), card_w - 70, draw)
        for l in lines:
            draw.text((135, fy), l, fill="#FFFFFF", font=get_font(21))
            fy += 29
        fy += 8
        
    # Pergunta Instigante ao final (FORA DE CARD + FONTE MAIOR + PALAVRAS-CHAVE DESTACADAS)
    draw_unboxed_reflection(
        draw,
        y=box_flavio_y + box_flavio_h + 25,
        eyebrow="A PERGUNTA DECISIVA PARA O 2º TURNO:",
        segments=[
            ("Na urna, você vai votar por ", "#FFFFFF"),
            ("FANATISMO DE INTERNET", "#FF334B"),
            (" ou para proteger a ", "#FFFFFF"),
            ("COMIDA NO PRATO,", "#00E676"),
            (" o seu ", "#FFFFFF"),
            ("SALÁRIO", "#ECC94B"),
            (" e a tranquilidade da sua família?", "#FFFFFF")
        ],
        eyebrow_color="#63B3ED",
        font_size=30,
        line_spacing=44
    )
    
    return img

# ==============================================================================
# SLIDE 9: CÓDIGO ABERTO NO GITHUB
# ==============================================================================
def create_slide_9():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 9)
    
    start_y = draw_headline_block(
        draw,
        headline="NÃO ACREDITE EM PALAVRAS. AUDITE.",
        subhead="Nosso projeto é 100% em código aberto e auditável por qualquer pessoa:",
        highlight_color="#63B3ED"
    )
    
    card_w = WIDTH - 140
    card_h = 420
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + card_h), radius=22, fill="#141824", outline="#2D3748", width=2)
    
    draw.text((105, start_y + 35), "TRANSPARÊNCIA TOTAL NO GITHUB", fill="#63B3ED", font=get_font(28, bold=True))
    
    txts = [
        ("Criamos um dashboard interativo em Python que conecta diretamente nas APIs públicas do Senado Federal, Banco Central e IBGE.", False),
        ("Você não precisa confiar na opinião de ninguém. Baixe o código, audite as fontes e tire suas próprias conclusões com autonomia.", False),
        ("O CÓDIGO FONTE E O BANCO DUCKDB ESTÃO DISPONÍVEIS NO GITHUB.", True)
    ]
    
    ty = start_y + 90
    for t, is_highlight in txts:
        color = "#68D391" if is_highlight else "#CBD5E0"
        font_c = get_font(23, bold=is_highlight)
        lines = wrap_text(t, font_c, card_w - 70, draw)
        for l in lines:
            draw.text((105, ty), l, fill=color, font=font_c)
            ty += 34
        ty += 16
        
    act_y = start_y + card_h + 25
    act_h = 240
    draw.rounded_rectangle((70, act_y, 70 + card_w, act_y + act_h), radius=20, fill="#1A202C", outline="#4A5568", width=2)
    draw.text((105, act_y + 25), "AJUDE A FURAR A BOLHA:", fill="#ECC94B", font=get_font(26, bold=True))
    
    actions = [
        "1. Deixe sua opinião sincera nos comentários",
        "2. Salve este carrossel para consultar no dia da votação",
        "3. Compartilhe com quem ainda está em dúvida no 2º turno!"
    ]
    ay = act_y + 75
    for idx, a in enumerate(actions):
        color = "#38A169" if idx == 2 else "#FFFFFF"
        bold = (idx == 2)
        draw.text((105, ay), a, fill=color, font=get_font(22, bold=bold))
        ay += 40
        
    return img

# ==============================================================================
# SLIDE 10: VOTE 13 + AGREGADOR DE LINKS
# ==============================================================================
def create_slide_10():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 10)
    
    # Headline Principal com destaque explícito "NO SEGUNDO TURNO, VOTE 13."
    font_main = get_font(58, bold=True)
    draw.text((70, 142), "NO SEGUNDO TURNO,", fill="#FFFFFF", font=font_main)
    draw.text((70, 212), "VOTE 13.", fill="#FF334B", font=font_main)
    
    font_sub = get_font(24, bold=False)
    sub_lines = wrap_text("Pela valorização do seu salário, democracia e contra o desvio de dinheiro público.", font_sub, WIDTH - 140, draw)
    sy = 290
    for sl in sub_lines:
        draw.text((70, sy), sl, fill="#63B3ED", font=font_sub)
        sy += 33
        
    start_y = sy + 22
    card_w = WIDTH - 140
    
    # 1. Card Central da Decisão (Selo de Voto e Racionalidade)
    box_vote_h = 280
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + box_vote_h), radius=22, fill="#1D1217", outline="#FF334B", width=3)
    
    # Badge interno VOTE 13
    draw.rounded_rectangle((105, start_y + 22, 105 + 230, start_y + 68), radius=12, fill="#E53E3E")
    draw.text((120, start_y + 30), "LULA • VOTE 13", fill="#FFFFFF", font=get_font(23, bold=True))
    
    vote_bullets = [
        "Salário mínimo subindo todo ano com aumento real (PIB + IPCA)",
        "Menor desemprego em anos e estabilidade das instituições",
        "Sem dinheiro vivo, sem Abin paralela e sem risco de golpe"
    ]
    by = start_y + 88
    for vb in vote_bullets:
        draw_vector_check(draw, 105, by + 4, size=18, color="#00E676")
        lines = wrap_text(vb, get_font(22), card_w - 75, draw)
        for l in lines:
            draw.text((135, by), l, fill="#E2E8F0", font=get_font(22))
            by += 32
        by += 8
        
    # 2. Card do Agregador de Links (Hub de Provas)
    hub_y = start_y + box_vote_h + 18
    hub_h = 260
    draw.rounded_rectangle((70, hub_y, 70 + card_w, hub_y + hub_h), radius=22, fill="#101D2C", outline="#3182CE", width=2)
    draw.text((105, hub_y + 22), "CONFIRA TODAS AS PROVAS NO LINK DA BIO:", fill="#63B3ED", font=get_font(23, bold=True))
    
    # Caixa Destacada com a URL
    url_box_y = hub_y + 60
    url_box_h = 62
    draw.rounded_rectangle((105, url_box_y, 70 + card_w - 35, url_box_y + url_box_h), radius=12, fill="#162A40", outline="#63B3ED", width=2)
    draw.text((125, url_box_y + 16), TELEGRAPH_URL, fill="#00E676", font=get_font(22, bold=True))
    
    hub_bullets = [
        "Votações do Senado, relatórios do Coaf e inquérito da PF no STF",
        "Página pública gratuita, aberta e sem necessidade de cadastro"
    ]
    hy = url_box_y + url_box_h + 18
    for hb in hub_bullets:
        draw_vector_dot(draw, 115, hy + 10, radius=5, color="#63B3ED")
        draw.text((135, hy), hb, fill="#CBD5E0", font=get_font(21))
        hy += 32
        
    # 3. Card de Engajamento e Ação Final
    act_y = hub_y + hub_h + 18
    act_h = 165
    draw.rounded_rectangle((70, act_y, 70 + card_w, act_y + act_h), radius=18, fill="#1A202C", outline="#4A5568", width=2)
    draw.text((105, act_y + 18), "O QUE VOCÊ PODE FAZER AGORA:", fill="#ECC94B", font=get_font(24, bold=True))
    
    actions = [
        "1. Salve este carrossel para consultar no dia da votação",
        "2. Compartilhe com quem ainda está indeciso no 2º turno!"
    ]
    ay = act_y + 58
    for idx, a in enumerate(actions):
        color = "#00E676" if idx == 1 else "#FFFFFF"
        bold = (idx == 1)
        draw.text((105, ay), a, fill=color, font=get_font(22, bold=bold))
        ay += 36
        
    return img

def render_all_carousel_images():
    slides_map = [
        ("slide_01_capa.png", create_slide_1),
        ("slide_02_fontes_metodologia.png", create_slide_2),
        ("slide_03_bolso.png", create_slide_3),
        ("slide_04_patrimonio.png", create_slide_4),
        ("slide_05_abin.png", create_slide_5),
        ("slide_06_instabilidade.png", create_slide_6),
        ("slide_07_contraste_lula.png", create_slide_7),
        ("slide_08_raio_x_indeciso.png", create_slide_8),
        ("slide_09_codigo_aberto.png", create_slide_9),
        ("slide_10_agregador_links.png", create_slide_10),
    ]
    
    for filename, func in slides_map:
        path = os.path.join(OUTPUT_DIR, filename)
        img = func()
        img.save(path, "PNG", quality=98)
        print(f"Slide renderizado: {path}")
        
    print(f"\nTodos os {TOTAL_SLIDES} slides versão 5.0 foram gerados com sucesso com as perguntas reflexivas inclusas!")

if __name__ == "__main__":
    render_all_carousel_images()
