"""
Gerador de Imagens Profissional para Carrossel do Instagram (1080 x 1350 px)
Versão 6.0:
- Atualizado com o novo módulo de Ameaças à Democracia & Soberania (Urnas R$ 23M, Trump/Sanções, Pix, Blindados)
- Fontes jornalísticas diretas consolidadas (Poder360, Folha, Estadão, CNN Brasil - sem G1)
- Perguntas reflexivas e instigantes de alto impacto fora de cards (Slides 3, 4, 5, 6, 7 e 8)
- Hub oficial de dados ao vivo: matheuscampos-it.github.io/auditoria-eleicoes-2026
- Desenho vetorial nativo (sem caracteres ausentes) e alinhamento milimétrico
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

LINKTREE_URL = "matheuscampos-it.github.io/auditoria-eleicoes-2026"

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
    draw.text((70, HEIGHT - 84), "Fontes: BACEN, IBGE, Senado, TSE, STF, PF, Poder360, Folha, Estadão, CNN", fill="#718096", font=font_foot)
    
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
    font_hl = get_font(48, bold=True)
    font_sub = get_font(25, bold=False)
    
    y = 145
    lines_hl = wrap_text(headline, font_hl, WIDTH - 140, draw)
    for line in lines_hl:
        draw.text((70, y), line, fill="#FFFFFF", font=font_hl)
        y += 62
        
    y += 8
    lines_sub = wrap_text(subhead, font_sub, WIDTH - 140, draw)
    for line in lines_sub:
        draw.text((70, y), line, fill=highlight_color, font=font_sub)
        y += 35
        
    return y + 22

def draw_unboxed_reflection(
    draw: ImageDraw.ImageDraw,
    y: int,
    eyebrow: str,
    segments: list,
    eyebrow_color: str = "#FF8C42",
    font_size: int = 31,
    line_spacing: int = 44,
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
    cur_y = y + 36
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
    draw.rounded_rectangle((70, 155, 70 + tag_w, 203), radius=10, fill="#2D1215", outline="#E53E3E", width=2)
    draw.text((90, 167), tag_str, fill="#FC8181", font=font_tag)
    
    font_main = get_font(56, bold=True)
    h_lines = [
        "AUDITEI FLÁVIO",
        "BOLSONARO NO CÓDIGO.",
        "OS DADOS ASSUSTAM."
    ]
    y = 235
    for hl in h_lines:
        color = "#FF4D4D" if "DADOS ASSUSTAM" in hl else "#FFFFFF"
        draw.text((70, y), hl, fill=color, font=font_main)
        y += 72
        
    card_y = y + 35
    card_w = WIDTH - 140
    
    font_intro = get_font(27, bold=True)
    intro_lines = wrap_text("O que encontramos nos dados oficiais que afeta diretamente a sua vida:", font_intro, card_w - 70, draw)
    
    bullets = [
        ("cross", "Voto nominal contra o Salário Mínimo e ameaças ao Pix"),
        ("cross", "Mansão de R$ 6 milhões e 48 depósitos em dinheiro vivo"),
        ("cross", "Abin paralela e ataque às urnas com multa de R$ 23 milhões"),
        ("check", "O contraste oficial com emprego (6,2%) e ganho real de Lula")
    ]
    
    font_bullet = get_font(23, bold=False)
    total_bullet_h = 0
    wrapped_bullets = []
    for icon_type, b_text in bullets:
        b_lines = wrap_text(b_text, font_bullet, card_w - 110, draw)
        wrapped_bullets.append((icon_type, b_lines))
        total_bullet_h += (len(b_lines) * 33) + 20
        
    card_h = 32 + (len(intro_lines) * 36) + 18 + total_bullet_h + 75
    draw.rounded_rectangle((70, card_y, 70 + card_w, card_y + card_h), radius=22, fill="#141824", outline="#2D3748", width=2)
    
    cur_y = card_y + 32
    for il in intro_lines:
        draw.text((105, cur_y), il, fill="#63B3ED", font=font_intro)
        cur_y += 36
    cur_y += 12
    
    for icon_type, b_lines in wrapped_bullets:
        if icon_type == "cross":
            draw_vector_cross(draw, 105, cur_y + 5, size=18, color="#FF334B")
        else:
            draw_vector_check(draw, 105, cur_y + 4, size=20, color="#00E676")
            
        for bl in b_lines:
            draw.text((145, cur_y), bl, fill="#E2E8F0", font=font_bullet)
            cur_y += 33
        cur_y += 16
        
    seal_y = card_y + card_h - 58
    draw.rounded_rectangle((105, seal_y, 105 + 440, seal_y + 40), radius=10, fill="#1B4332", outline="#2D6A4F", width=2)
    draw_vector_check(draw, 120, seal_y + 10, size=18, color="#74C69D")
    draw.text((150, seal_y + 9), "100% BASEADO EM DOCUMENTOS & APIS", fill="#74C69D", font=get_font(18, bold=True))
    
    # Box de Chamada / Swipe no rodapé
    callout_y = card_y + card_h + 25
    callout_h = 130
    draw.rounded_rectangle((70, callout_y, 70 + card_w, callout_y + callout_h), radius=18, fill="#131926", outline="#3182CE", width=2)
    draw.text((105, callout_y + 24), "ARRASTE PARA AUDITAR OS FATOS:", fill="#63B3ED", font=get_font(24, bold=True))
    draw.text((105, callout_y + 64), "Veja os documentos que não aparecem na propaganda eleitoral.", fill="#E2E8F0", font=get_font(21, bold=False))
    draw_vector_arrow(draw, 70 + card_w - 55, callout_y + 68, size=20, color="#63B3ED")
    
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
        subhead="Nenhum número aqui é opinião ou boato. Veja as fontes oficiais e diretas:",
        highlight_color="#63B3ED"
    )
    
    sources = [
        ("1. APIS DO BANCO CENTRAL E IBGE",
         "Séries temporais oficiais do Sistema SGS do BACEN (Reservas, Salário Real e Inflação) e bases SIDRA/PNAD Contínua do IBGE (Desemprego em 6,2%).",
         "#38A169"),
        ("2. REGISTROS NOMINAIS DO CONGRESSO & TSE",
         "Votações nominais no Senado, atas do Diário Oficial, acórdãos de multas do TSE e certidões judiciais do STF.",
         "#3182CE"),
        ("3. JORNALISMO PROFISSIONAL DIRETO",
         "Documentos e investigações apuradas por Poder360, Folha de S.Paulo, Estadão e CNN Brasil — com links diretos verificados no nosso hub.",
         "#DD6B20")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in sources:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 60 + (len(lines) * 32) + 16
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw.text((105, cy + 20), title, fill=border_col, font=get_font(25, bold=True))
        
        ly = cy + 64
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 32
        cy += card_h + 16
        
    code_h = 165
    draw.rounded_rectangle((70, cy, 70 + card_w, cy + code_h), radius=18, fill="#101D2C", outline="#3182CE", width=2)
    draw_vector_check(draw, 105, cy + 28, size=24, color="#63B3ED")
    draw.text((140, cy + 24), "CÓDIGO ABERTO & DASHBOARD LIVE", fill="#63B3ED", font=get_font(25, bold=True))
    
    code_desc = "O script em Python que cruza esses dados e o Dashboard interativo estão disponíveis publicamente no GitHub e GitHub Pages para você auditar em tempo real."
    code_lines = wrap_text(code_desc, get_font(22), card_w - 70, draw)
    cly = cy + 68
    for cl in code_lines:
        draw.text((105, cly), cl, fill="#CBD5E0", font=get_font(22))
        cly += 31
        
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
        subhead="O histórico real de Flávio Bolsonaro e seu grupo contra o trabalhador:",
        highlight_color="#FC8181"
    )
    
    cards = [
        ("VOTO CONTRA O SALÁRIO MÍNIMO", 
         "No Senado, votou CONTRA a política permanente de aumento real do piso salarial acima da inflação pelo PIB. Seu grupo agora defende desvincular benefícios do salário mínimo.",
         "#E53E3E"),
        ("AMEAÇA AO PIX E TARIFAS BANCÁRIAS", 
         "Pressão de setores aliados para impor tarifas sobre transações instantâneas e fake news contra a gratuidade do Pix garantida pelo Banco Central.",
         "#DD6B20"),
        ("CONTA DE LUZ MAIS CARA", 
         "Votou 'SIM' pela privatização da Eletrobras (MP 1031) com 'jabutis' que encareceram a conta de luz das famílias para bancar usinas térmicas caras.",
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in cards:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 56 + (len(lines) * 31) + 14
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw_vector_cross(draw, 105, cy + 22, size=18, color=border_col)
        draw.text((135, cy + 18), title, fill=border_col, font=get_font(24, bold=True))
        
        ly = cy + 58
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 31
        cy += card_h + 14
        
    # Pergunta Instigante ao final
    draw_unboxed_reflection(
        draw,
        y=cy + 20,
        eyebrow="PERGUNTA DIRETA PRO SEU BOLSO:",
        segments=[
            ("Quer ", "#FFFFFF"),
            ("MENOS AUMENTO NO SALÁRIO,", "#FF334B"),
            (" a volta de ", "#FFFFFF"),
            ("TAXAS NO PIX", "#FF8C42"),
            (" e a sua ", "#FFFFFF"),
            ("CONTA DE LUZ MAIS CARA?", "#ECC94B"),
            (" É justo trabalhar dobrado para bancar ", "#FFFFFF"),
            ("PRIVILÉGIO DE POLÍTICO?", "#FF334B")
        ],
        eyebrow_color="#FF8C42",
        font_size=31,
        line_spacing=44
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
         "Perícia técnica do MP-RJ comprovou descompasso milionário entre as vendas reais de doces e grandes volumes de dinheiro vivo depositados no comércio.",
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in cards:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 56 + (len(lines) * 31) + 14
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw_vector_cross(draw, 105, cy + 22, size=18, color=border_col)
        draw.text((135, cy + 18), title, fill=border_col, font=get_font(24, bold=True))
        
        ly = cy + 58
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 31
        cy += card_h + 14
        
    # Pergunta Instigante ao final
    draw_unboxed_reflection(
        draw,
        y=cy + 20,
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
        font_size=31,
        line_spacing=44
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
    card_h = 425
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + card_h), radius=22, fill="#1C141E", outline="#E53E3E", width=3)
    
    draw.text((105, start_y + 32), "O RELATÓRIO OFICIAL DA POLÍCIA FEDERAL:", fill="#FC8181", font=get_font(27, bold=True))
    
    points = [
        "A Agência Brasileira de Inteligência (Abin) monitorou ilegalmente mais de 30 mil celulares via FirstMile sem autorização judicial.",
        "Foram produzidos relatórios secretos pagos com dinheiro público para espionar auditores da Receita e BLINDAR Flávio Bolsonaro no caso Queiroz.",
        "Áudio gravado apreendido pela PF registrou reunião no Palácio do Planalto entre Bolsonaro, Ramagem e advogadas para montar a defesa privada de Flávio."
    ]
    
    py = start_y + 82
    for pt in points:
        draw_vector_dot(draw, 115, py + 12, radius=5, color="#FC8181")
        lines = wrap_text(pt, get_font(22), card_w - 90, draw)
        for l in lines:
            draw.text((135, py), l, fill="#FFFFFF", font=get_font(22))
            py += 32
        py += 12
        
    # Pergunta Instigante ao final
    draw_unboxed_reflection(
        draw,
        y=start_y + card_h + 30,
        eyebrow="RESPONDA COM SINCERIDADE:",
        segments=[
            ("Você acha certo o ", "#FFFFFF"),
            ("DINHEIRO DOS SEUS IMPOSTOS", "#ECC94B"),
            (" sustentar uma ", "#FFFFFF"),
            ("POLÍCIA SECRETA ILEGAL", "#FF334B"),
            (" para ", "#FFFFFF"),
            ("BLINDAR FAMÍLIA DE POLÍTICO", "#FC8181"),
            (" contra a Justiça?", "#FFFFFF")
        ],
        eyebrow_color="#FF4D4D",
        font_size=31,
        line_spacing=44
    )
    
    return img

# ==============================================================================
# SLIDE 6: AMEAÇAS À DEMOCRACIA, ELEIÇÕES & SOBERANIA + PERGUNTA INSTIGANTE
# ==============================================================================
def create_slide_6():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 6)
    
    start_y = draw_headline_block(
        draw,
        headline="AMEAÇAS À DEMOCRACIA E SOBERANIA.",
        subhead="Ações comprovadas de Flávio Bolsonaro, cúpula do PL e aliados diretos:",
        highlight_color="#FC8181"
    )
    
    cards = [
        ("MULTA DE R$ 22,9 MI POR ATACAR URNAS",
         "O PL de Flávio tentou anular votos de quase 60% das urnas eletrônicas após a derrota. O TSE multou o partido por litigância de má-fé pela tentativa de anular 67 milhões de votos.",
         "#E53E3E"),
        ("COMITIVA NOS EUA PEDINDO SANÇÕES",
         "Parlamentares do PL viajaram a Washington para se reunir com trumpistas e pedir sanções econômicas e tarifas contra produtos brasileiros, prejudicando empresas e empregos no país.",
         "#DD6B20"),
        ("BLINDADOS, 8 DE JANEIRO E PEC DAS PRAIAS",
         "Desfile de tanques na Esplanada em votação, defesa de anistia aos invasores do 8/1 e relatoria da PEC das Praias para cercar terrenos do litoral da União.",
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, border_col in cards:
        lines = wrap_text(desc, get_font(22), card_w - 70, draw)
        card_h = 56 + (len(lines) * 31) + 14
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=border_col, width=2)
        draw_vector_cross(draw, 105, cy + 22, size=18, color=border_col)
        draw.text((135, cy + 18), title, fill=border_col, font=get_font(24, bold=True))
        
        ly = cy + 58
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(22))
            ly += 31
        cy += card_h + 14
        
    # Pergunta Instigante ao final
    draw_unboxed_reflection(
        draw,
        y=cy + 20,
        eyebrow="O BRASIL PRECISA DE MAIS CRISE?",
        segments=[
            ("O país precisa de ", "#FFFFFF"),
            ("PAZ E EMPREGOS", "#00E676"),
            (" ou de ", "#FFFFFF"),
            ("MULTAS DE R$ 23 MILHÕES,", "#FF334B"),
            (" ameaça às urnas, ", "#FFFFFF"),
            ("TAXAS CONTRA O BRASIL", "#FF8C42"),
            (" e briga política todo dia?", "#FFFFFF")
        ],
        eyebrow_color="#FF8C42",
        font_size=31,
        line_spacing=44
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
         "Poder de compra do salário mínimo crescendo todo ano acima da inflação pela fórmula permanente vinculada ao PIB.", 
         "#38A169"),
        ("DESEMPREGO EM 6,2% (RECORDE)", 
         "Menor taxa de desocupação da série pelo IBGE (PNAD Contínua), gerando recorde de trabalhadores com carteira assinada.", 
         "#38A169"),
        ("US$ 365 BILHÕES EM RESERVAS", 
         "Muralha cambial construída no Banco Central que protege a moeda contra crises internacionais e garantiu autonomia ao país.", 
         "#3182CE"),
        ("ISENÇÃO DO IR ATÉ R$ 5.000", 
         "Alívio fiscal direto no bolso do trabalhador assalariado e da classe média, aprovado para proteger o poder de compra.", 
         "#3182CE")
    ]
    
    cy = start_y
    card_w = WIDTH - 140
    for title, desc, col in metrics:
        lines = wrap_text(desc, get_font(21), card_w - 70, draw)
        card_h = 54 + (len(lines) * 29) + 12
        
        draw.rounded_rectangle((70, cy, 70 + card_w, cy + card_h), radius=18, fill="#141824", outline=col, width=2)
        draw_vector_check(draw, 105, cy + 20, size=20, color=col)
        draw.text((135, cy + 17), title, fill=col, font=get_font(24, bold=True))
        
        ly = cy + 54
        for l in lines:
            draw.text((105, ly), l, fill="#E2E8F0", font=get_font(21))
            ly += 29
        cy += card_h + 12
        
    # Pergunta Reflexiva ao final
    draw_unboxed_reflection(
        draw,
        y=cy + 18,
        eyebrow="A ESCOLHA RACIONAL:",
        segments=[
            ("Com o ", "#FFFFFF"),
            ("SALÁRIO SUBINDO DE VERDADE,", "#00E676"),
            (" desemprego em 6,2% e ", "#FFFFFF"),
            ("ISENÇÃO DO IMPOSTO DE RENDA,", "#63B3ED"),
            (" vale a pena trocar a sua segurança por ", "#FFFFFF"),
            ("ESCÂNDALOS E AVENTURA?", "#FF334B")
        ],
        eyebrow_color="#00E676",
        font_size=31,
        line_spacing=44
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
    box_lula_h = 275
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + box_lula_h), radius=22, fill="#0F2417", outline="#2F855A", width=2)
    draw.text((105, start_y + 20), "O PROJETO LULA (PREVISIBILIDADE):", fill="#68D391", font=get_font(24, bold=True))
    lula_pts = [
        "Salário mínimo subindo todo ano com fórmula real (PIB + IPCA).",
        "Menor desemprego em anos (6,2%) e IR isento até R$ 5.000.",
        "Pix 100% público, gratuito e protegido sem tarifas bancárias.",
        "Segurança jurídica, estabilidade institucional e respeito às urnas."
    ]
    ly = start_y + 60
    for pt in lula_pts:
        draw_vector_check(draw, 105, ly + 3, size=16, color="#00E676")
        lines = wrap_text(pt, get_font(21), card_w - 70, draw)
        for l in lines:
            draw.text((135, ly), l, fill="#FFFFFF", font=get_font(21))
            ly += 29
        ly += 7
        
    box_flavio_y = start_y + box_lula_h + 16
    box_flavio_h = 275
    draw.rounded_rectangle((70, box_flavio_y, 70 + card_w, box_flavio_y + box_flavio_h), radius=22, fill="#2A1215", outline="#C53030", width=2)
    draw.text((105, box_flavio_y + 20), "O PROJETO FLÁVIO / PL (RISCO CRÔNICO):", fill="#FC8181", font=get_font(24, bold=True))
    flavio_pts = [
        "Voto formal contra a política permanente de valorização do salário.",
        "48 depósitos em dinheiro vivo rastreados pelo Coaf e mansão de R$ 6M.",
        "Abin paralela aparelhada para espionar auditores fiscais e desafetos.",
        "Multa de R$ 22,9M por atacar urnas e comitiva pedindo tarifas nos EUA."
    ]
    fy = box_flavio_y + 60
    for pt in flavio_pts:
        draw_vector_cross(draw, 105, fy + 3, size=16, color="#FF334B")
        lines = wrap_text(pt, get_font(21), card_w - 70, draw)
        for l in lines:
            draw.text((135, fy), l, fill="#FFFFFF", font=get_font(21))
            fy += 29
        fy += 7
        
    # Pergunta Instigante ao final
    draw_unboxed_reflection(
        draw,
        y=box_flavio_y + box_flavio_h + 22,
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
        line_spacing=43
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
        subhead="Nosso projeto é 100% aberto, transparente e auditável por você:",
        highlight_color="#63B3ED"
    )
    
    card_w = WIDTH - 140
    card_h = 420
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + card_h), radius=22, fill="#141824", outline="#2D3748", width=2)
    
    draw.text((105, start_y + 32), "TRANSPARÊNCIA TOTAL NO GITHUB & PAGES", fill="#63B3ED", font=get_font(27, bold=True))
    
    txts = [
        ("Desenvolvemos um Dashboard Analítico interativo publicado ao vivo com gráficos temporais, matriz de risco e terminal SQL DuckDB.", False),
        ("Você não precisa confiar na opinião de ninguém: confira os números do Banco Central, IBGE, atas do Senado e relatórios do TSE.", False),
        ("Todas as 24 ocorrências contam com links diretos para veículos confiáveis (Poder360, Folha, Estadão, CNN) sem pesquisas vagas.", False),
        ("CÓDIGO FONTE, SCRIPTS EM PYTHON E BANCO DUCKDB ABERTOS NO GITHUB.", True)
    ]
    
    ty = start_y + 80
    for t, is_highlight in txts:
        color = "#68D391" if is_highlight else "#CBD5E0"
        font_c = get_font(21, bold=is_highlight)
        lines = wrap_text(t, font_c, card_w - 70, draw)
        for l in lines:
            draw.text((105, ty), l, fill=color, font=font_c)
            ty += 31
        ty += 12
        
    act_y = start_y + card_h + 24
    act_h = 230
    draw.rounded_rectangle((70, act_y, 70 + card_w, act_y + act_h), radius=20, fill="#1A202C", outline="#4A5568", width=2)
    draw.text((105, act_y + 24), "AJUDE A FURAR A BOLHA:", fill="#ECC94B", font=get_font(25, bold=True))
    
    actions = [
        "1. Deixe sua opinião sincera nos comentários",
        "2. Salve este carrossel para consultar no dia da votação",
        "3. Compartilhe com quem ainda está em dúvida no 2º turno!"
    ]
    ay = act_y + 72
    for idx, a in enumerate(actions):
        color = "#38A169" if idx == 2 else "#FFFFFF"
        bold = (idx == 2)
        draw.text((105, ay), a, fill=color, font=get_font(22, bold=bold))
        ay += 38
        
    return img

# ==============================================================================
# SLIDE 10: VOTE 13 + AGREGADOR DE LINKS
# ==============================================================================
def create_slide_10():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B0E14")
    draw = ImageDraw.ImageDraw(img)
    draw_header_and_footer(draw, 10)
    
    # Headline Principal com destaque explícito "NO SEGUNDO TURNO, VOTE 13."
    font_main = get_font(56, bold=True)
    draw.text((70, 140), "NO SEGUNDO TURNO,", fill="#FFFFFF", font=font_main)
    draw.text((70, 208), "VOTE 13.", fill="#FF334B", font=font_main)
    
    font_sub = get_font(24, bold=False)
    sub_lines = wrap_text("Pela valorização do seu salário, Pix gratuito, democracia e contra o desvio de dinheiro público.", font_sub, WIDTH - 140, draw)
    sy = 282
    for sl in sub_lines:
        draw.text((70, sy), sl, fill="#63B3ED", font=font_sub)
        sy += 32
        
    start_y = sy + 20
    card_w = WIDTH - 140
    
    # 1. Card Central da Decisão (Selo de Voto e Racionalidade)
    box_vote_h = 275
    draw.rounded_rectangle((70, start_y, 70 + card_w, start_y + box_vote_h), radius=22, fill="#1D1217", outline="#FF334B", width=3)
    
    # Badge interno VOTE 13
    draw.rounded_rectangle((105, start_y + 20, 105 + 230, start_y + 64), radius=12, fill="#E53E3E")
    draw.text((120, start_y + 28), "LULA • VOTE 13", fill="#FFFFFF", font=get_font(22, bold=True))
    
    vote_bullets = [
        "Salário mínimo com fórmula de aumento real permanente (PIB + IPCA)",
        "Pix 100% público, gratuito e protegido sem tarifas bancárias",
        "Menor desemprego em anos (6,2%), estabilidade e respeito à democracia",
        "Sem dinheiro vivo, sem Abin paralela e sem tarifas contra o Brasil"
    ]
    by = start_y + 82
    for vb in vote_bullets:
        draw_vector_check(draw, 105, by + 4, size=18, color="#00E676")
        lines = wrap_text(vb, get_font(21), card_w - 75, draw)
        for l in lines:
            draw.text((135, by), l, fill="#E2E8F0", font=get_font(21))
            by += 30
        by += 6
        
    # 2. Card do Agregador de Links (Hub de Provas)
    hub_y = start_y + box_vote_h + 16
    hub_h = 255
    draw.rounded_rectangle((70, hub_y, 70 + card_w, hub_y + hub_h), radius=22, fill="#101D2C", outline="#3182CE", width=2)
    draw.text((105, hub_y + 20), "ACESSE O HUB COMPLETO NO LINK DA BIO:", fill="#63B3ED", font=get_font(22, bold=True))
    
    # Caixa Destacada com a URL
    url_box_y = hub_y + 56
    url_box_h = 60
    draw.rounded_rectangle((105, url_box_y, 70 + card_w - 35, url_box_y + url_box_h), radius=12, fill="#162A40", outline="#63B3ED", width=2)
    draw.text((120, url_box_y + 16), LINKTREE_URL, fill="#00E676", font=get_font(20, bold=True))
    
    hub_bullets = [
        "Dashboard analítico ao vivo, banco DuckDB e código no GitHub",
        "Links diretos para inquéritos da PF, decisões do TSE e Coaf",
        "Acesso gratuito, aberto a todos e sem necessidade de cadastro"
    ]
    hy = url_box_y + url_box_h + 16
    for hb in hub_bullets:
        draw_vector_dot(draw, 115, hy + 9, radius=5, color="#63B3ED")
        draw.text((135, hy), hb, fill="#CBD5E0", font=get_font(21))
        hy += 30
        
    # 3. Card de Engajamento e Ação Final
    act_y = hub_y + hub_h + 16
    act_h = 160
    draw.rounded_rectangle((70, act_y, 70 + card_w, act_y + act_h), radius=18, fill="#1A202C", outline="#4A5568", width=2)
    draw.text((105, act_y + 16), "O QUE VOCÊ PODE FAZER AGORA:", fill="#ECC94B", font=get_font(23, bold=True))
    
    actions = [
        "1. Salve este carrossel para consultar no dia da votação",
        "2. Compartilhe com quem ainda está indeciso no 2º turno!"
    ]
    ay = act_y + 54
    for idx, a in enumerate(actions):
        color = "#00E676" if idx == 1 else "#FFFFFF"
        bold = (idx == 1)
        draw.text((105, ay), a, fill=color, font=get_font(21, bold=bold))
        ay += 34
        
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
        
    print(f"\nTodos os {TOTAL_SLIDES} slides versão 6.0 foram gerados com sucesso com as novas formatações e dados!")

if __name__ == "__main__":
    render_all_carousel_images()
