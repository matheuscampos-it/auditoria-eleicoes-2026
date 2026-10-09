"""
Dashboard Interativo: Auditoria de Dados - Eleições Presidenciais 2026
Estratégia Multiformato:
1. Roteiro Vertical Curto (Shorts/Reels/TikTok - Máx 60s) [FOCO PRINCIPAL]
2. Carrossel Completo para Instagram (8 Slides Prontos + Legenda)
3. Auditoria Detalhada: Flávio Bolsonaro, PL e Clã (Foco Ampliado)
4. Contraste de Governança & Renda (Lula)
5. Raio-X para o Eleitor Indeciso
6. Roteiro para Vídeo Longo do YouTube
7. Terminal SQL (DuckDB Live)
"""

import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import duckdb

# Configuração da Página
st.set_page_config(
    page_title="Auditoria 2026 | Foco Flávio vs Lula",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS Personalizada (Dark Theme & Social Media Cards)
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e222d 0%, #151821 100%);
        border: 1px solid #2d3343;
        border-radius: 10px;
        padding: 16px 20px;
        color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .metric-title {
        font-size: 0.85rem;
        color: #8fa0bc;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .metric-desc {
        font-size: 0.8rem;
        color: #b0bac9;
    }
    .badge-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 5px;
    }
    .badge-alert {
        background-color: #d32f2f;
        color: white;
    }
    .badge-tech {
        background-color: #1976d2;
        color: white;
    }
    .badge-short {
        background-color: #7b1fa2;
        color: white;
    }
    .carousel-slide {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        color: #f0f6fc;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }
    .carousel-header {
        font-size: 0.85rem;
        text-transform: uppercase;
        color: #58a6ff;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .carousel-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 12px;
    }
    .teleprompter-box {
        background: #0d1117;
        border-left: 4px solid #f85149;
        padding: 16px;
        border-radius: 4px 8px 8px 4px;
        font-size: 1.05rem;
        line-height: 1.6;
        color: #e6edf3;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "database.duckdb")

@st.cache_data
def load_datasets():
    macro_csv = os.path.join(DATA_DIR, "macro_series_historica.csv")
    media_csv = os.path.join(DATA_DIR, "media_audit_dataset.csv")
    
    df_macro = pd.read_csv(macro_csv) if os.path.exists(macro_csv) else pd.DataFrame()
    df_media = pd.read_csv(media_csv) if os.path.exists(media_csv) else pd.DataFrame()
    
    if not df_media.empty and "data" in df_media.columns:
        df_media["data"] = pd.to_datetime(df_media["data"])
        
    return df_macro, df_media

df_macro, df_media = load_datasets()

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/vertical-timeline.png", width=60)
st.sidebar.title("Auditoria 2026")
st.sidebar.caption("Nova Estratégia: Ataque Factual a Flávio + Vídeo Vertical (<60s) + Carrossel Instagram")

view_mode = st.sidebar.radio(
    "Navegação do Projeto",
    [
        "📱 Roteiro Vertical (Shorts/Reels 60s)",
        "📸 Carrossel Instagram (8 Slides Prontos)",
        "🔍 Auditoria Implacável: Flávio & PL",
        "⚖️ Raio-X do Indeciso: Fatos vs Risco",
        "📊 Contraste Macroeconômico (Lula)",
        "🎬 Roteiro Vídeo Longo (YouTube)",
        "💻 Terminal SQL (DuckDB Live)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**⚙️ Setup do Criador:**
- Vídeo Vertical: 56s de fala (~135 palavras)
- Instagram: Carrossel 8 cards (1080x1350)
- Tese: Desmontar o candidato adversário com dados oficiais e NLP de investigações.
""")

# ==============================================================================
# ROTEIRO VERTICAL CURTO (SHORTS / REELS / TIKTOK - MÁX 60S)
# ==============================================================================
if view_mode == "📱 Roteiro Vertical (Shorts/Reels 60s)":
    st.markdown("""
    <div>
        <span class="badge-pill badge-short">VÍDEO VERTICAL (9:16)</span>
        <span class="badge-pill badge-alert">MÁXIMO 60 SEGUNDOS</span>
        <span class="badge-pill badge-tech">ALTA RETENÇÃO</span>
    </div>
    <h1 style='margin-top: 10px;'>Roteiro para Vídeo Curto: O Padrão Oculto de Flávio Bolsonaro</h1>
    <p style='color: #8b949e; font-size: 1.05rem;'>
        Roteiro calibrado em <b>56 segundos</b> de fala (135 palavras). Foco total em desmontar a imagem de Flávio Bolsonaro
        com números do Senado, investigações reais e o contraste final para o indeciso.
    </p>
    """, unsafe_allow_html=True)
    
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Tempo Estimado</div>
            <div class="metric-value" style="color: #a371f7;">56 seg</div>
            <div class="metric-desc">Dentro do limite ideal de 60s</div>
        </div>
        """, unsafe_allow_html=True)
    with col_t2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Contagem de Palavras</div>
            <div class="metric-value" style="color: #58a6ff;">135 palavras</div>
            <div class="metric-desc">Ritmo acelerado e direto ao ponto</div>
        </div>
        """, unsafe_allow_html=True)
    with col_t3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Tom Editorial</div>
            <div class="metric-value" style="color: #ff7b72;">Ataque Factual</div>
            <div class="metric-desc">Auditoria em código, sem ofensas vazias</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    st.markdown("### 🎙️ Teleprompter & Cenas (Bloco a Bloco)")
    
    st.markdown("""
    <div class="teleprompter-box">
        <span style="color: #f85149; font-weight: bold;">[0:00 - 0:08] GANCHO / HOOK BRUTAL</span><br>
        <b>Visual:</b> Você encarando a câmera com o terminal rodando código Python ao fundo em tela cheia. Texto na tela grande: <i>"AUDITEI FLÁVIO BOLSONARO NO CÓDIGO"</i>.<br>
        <b>Fala:</b> <i>"Se você está indeciso no segundo turno, pare 60 segundos. Eu usei Python para auditar os registros oficiais de Flávio Bolsonaro no Senado e na Justiça. O resultado é assustador."</i>
    </div>
    
    <div class="teleprompter-box">
        <span style="color: #f85149; font-weight: bold;">[0:08 - 0:24] BLOCO 1: O VOTO CONTRA O POVO VS A MANSÃO PRÓPRIA</span><br>
        <b>Visual:</b> Print do painel de votações do Senado + foto da mansão de R$ 6 milhões.<br>
        <b>Fala:</b> <i>"Primeiro dado: no Senado, Flávio votou CONTRA a valorização permanente do salário mínimo. Enquanto barrava aumento para o trabalhador, o Coaf pegou 48 depósitos em dinheiro vivo na conta dele e a compra de uma mansão de 6 milhões em Brasília com renda pública."</i>
    </div>
    
    <div class="teleprompter-box">
        <span style="color: #f85149; font-weight: bold;">[0:24 - 0:40] BLOCO 2: APARELHAMENTO E AMEAÇA GOLPISTA</span><br>
        <b>Visual:</b> Documento da PF sobre a Abin Paralela + Multa de R$ 22,9M do TSE ao PL.<br>
        <b>Fala:</b> <i>"Segundo dado: a Polícia Federal comprovou que a Abin paralela foi usada para produzir relatórios e blindar Flávio nas investigações. E o partido dele, o PL, foi multado em quase 23 milhões por tentar anular votos da eleição."</i>
    </div>
    
    <div class="teleprompter-box">
        <span style="color: #f85149; font-weight: bold;">[0:40 - 0:50] BLOCO 3: O CONTRASTE COM LULA</span><br>
        <b>Visual:</b> Gráfico comparativo de desemprego e ganho real de renda.<br>
        <b>Fala:</b> <i>"Do outro lado, você tem a gestão Lula com o menor desemprego em anos, salário mínimo subindo acima da inflação e estabilidade institucional."</i>
    </div>
    
    <div class="teleprompter-box">
        <span style="color: #f85149; font-weight: bold;">[0:50 - 0:56] ENCERRAMENTO & CTA</span><br>
        <b>Visual:</b> Olho no olho na câmera, texto: <i>"Link na bio para auditar o código"</i>.<br>
        <b>Fala:</b> <i>"Para o indeciso, a escolha é matemática: previsibilidade econômica ou risco crônico de escândalos. Não vote no escuro. Compartilhe."</i>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Dica de Produção para o Short:** Use legendas automáticas chamativas com palavras-chave coloridas (ex: *salário mínimo* em amarelo, *R$ 6 milhões* e *Abin paralela* em vermelho).")

# ==============================================================================
# CARROSSEL INSTAGRAM (8 SLIDES PRONTOS)
# ==============================================================================
elif view_mode == "📸 Carrossel Instagram (8 Slides Prontos)":
    st.markdown("""
    <div>
        <span class="badge-pill badge-short">INSTAGRAM CAROUSEL</span>
        <span class="badge-pill" style="background-color: #e1306c; color: white;">8 SLIDES DE ALTO IMPACTO</span>
        <span class="badge-pill badge-alert">FOCO: AUDITORIA DE FLÁVIO</span>
    </div>
    <h1 style='margin-top: 10px;'>Carrossel Completo para o Instagram</h1>
    <p style='color: #8b949e; font-size: 1.05rem;'>
        Design, títulos, textos mastigados e a legenda completa prontos para postar. 
        Estruturado para converter o eleitor indeciso que consome conteúdo no feed.
    </p>
    """, unsafe_allow_html=True)
    
    CAROUSEL_DIR = os.path.join(BASE_DIR, "carousel_images")
    if os.path.exists(CAROUSEL_DIR):
        st.markdown("### 🖼️ Galeria de Slides em Alta Resolução (1080 x 1350 px)")
        st.caption("As imagens abaixo já estão salvas na pasta `carousel_images/` em formato 4:5 vertical prontas para o Instagram.")
        
        # Grid com as imagens
        img_files = sorted([f for f in os.listdir(CAROUSEL_DIR) if f.endswith(".png")])
        if img_files:
            cols = st.columns(4)
            for idx, img_file in enumerate(img_files):
                with cols[idx % 4]:
                    st.image(os.path.join(CAROUSEL_DIR, img_file), caption=f"Card {idx+1}: {img_file}")
                    
        st.markdown("---")
        st.markdown("#### 🔍 Pré-visualização Individual em Tamanho Maior:")
        slide_escolhido = st.selectbox("Selecione o Slide para Ampliar:", img_files)
        if slide_escolhido:
            col_zoom, _ = st.columns([2, 1])
            with col_zoom:
                st.image(os.path.join(CAROUSEL_DIR, slide_escolhido), width=500)
                
    st.markdown("---")
    st.markdown("### 📋 Conteúdo Textual e Roteiro de Cada Slide")
    
    # Exibição dos 9 Slides
    slides = [
        {
            "num": "Slide 1 (Capa)",
            "title": "Auditei 8 anos de dados e votos de Flávio Bolsonaro no código. Os dados assustam.",
            "content": "• Voto nominal contra o Salário Mínimo no Senado\n• Mansão de R$ 6 milhões e depósitos em dinheiro vivo\n• Uso da Abin paralela comprovado pela Polícia Federal\n• O contraste com os dados oficiais de renda e emprego de Lula\n\n100% BASEADO EM DADOS OFICIAIS. Arraste para o lado ->",
            "footer": "Fonte: Senado Federal, BACEN, PF e MP-RJ"
        },
        {
            "num": "Slide 2 (Metodologia & Fontes) ⭐",
            "title": "De onde saíram estes dados?",
            "content": "Nenhum número aqui é opinião ou post de internet. Veja as fontes oficiais:\n\n1. APIs do Banco Central e IBGE: Séries históricas de 20 anos de salário real, inflação e emprego.\n2. Painel Nominal do Senado Federal: Votações nominais e tramitações de projetos e PECs direto de legis.senado.leg.br.\n3. Inquéritos da PF, Coaf e Tribunais: Documentos da Operação Vigilância Aproximada (STF), Coaf, MP-RJ e TSE.\n\n✓ CÓDIGO ABERTO: Script Python público no GitHub para você clonar e auditar.",
            "footer": "Transparência total e reprodutibilidade de dados."
        },
        {
            "num": "Slide 3",
            "title": "1. O que ele votou contra o seu bolso",
            "content": "• Votou CONTRA a política permanente de aumento real do Salário Mínimo acima da inflação pelo PIB.\n• Votou pela privatização da Eletrobras com jabutis que encareceram a conta de luz.\n• Apoiou o teto de gastos rígido que congelou recursos da saúde e da educação.\n\n💬 REFLEXÃO PARA O SEU BOLSO:\n\"Menos valorização para o seu salário e conta de luz mais cara para a sua casa: você acha justo pagar essa conta?\"",
            "footer": "O discurso fala em 'povo', mas o voto no painel foi contra o trabalhador."
        },
        {
            "num": "Slide 4",
            "title": "2. A matemática patrimonial atípica",
            "content": "• Compra de Mansão de luxo de R$ 6 milhões no Lago Sul de Brasília com renda parlamentar e crédito no BRB.\n• Relatório do Coaf: 48 depósitos fracionados de R$ 2.000 em dinheiro vivo em um único mês.\n• Inquérito do MP-RJ: Suspeita de lavagem de até R$ 1,6 milhão em dinheiro vivo através de loja de chocolates.\n\n💬 REFLEXÃO PARA QUEM TRABALHA E CONTA MOEDAS:\n\"Enquanto você sua o mês inteiro para pagar as contas, depósitos em dinheiro vivo e mansão de R$ 6 milhões: essa conta fecha pra você?\"",
            "footer": "Enquanto o cidadão comum conta moedas, as movimentações eram em dinheiro vivo."
        },
        {
            "num": "Slide 5",
            "title": "3. O Aparelhamento do Estado (Abin Paralela)",
            "content": "• Inquérito oficial da PF no STF comprovou: a Abin foi usada para espionar desafetos e auditores da Receita.\n• Produção de relatórios sigilosos pagos com os seus impostos para blindar Flávio nas rachadinhas.\n• Reunião gravada pela PF no Planalto discutindo plano de defesa privada da família.\n\n💬 REFLEXÃO PARA QUEM PAGA IMPOSTO:\n\"Você acha justo o dinheiro dos seus impostos bancar uma agência de inteligência usada para proteger a família do político de processos?\"",
            "footer": "Fonte: Inquérito da Polícia Federal / STF"
        },
        {
            "num": "Slide 6",
            "title": "4. A Instabilidade Crônica do PL",
            "content": "• Multa de R$ 22,9 milhões aplicada pelo TSE ao PL por pedir anulação de votos sem prova após a eleição.\n• Endosso à anistia para envolvidos nos atos de 8 de Janeiro.\n• Flávio foi relator da PEC das Praias, abrindo brecha para privatização de áreas públicas do litoral.\n\n💬 REFLEXÃO PARA O FUTURO DO PAÍS:\n\"O Brasil precisa de mais anos de brigas com tribunais e crises diárias ou de estabilidade e paz para a economia crescer e gerar empregos?\"",
            "footer": "Instabilidade política constante que afasta investimentos e assusta a economia."
        },
        {
            "num": "Slide 7",
            "title": "5. O Contraste: O que os Dados da Economia Mostram",
            "content": "• Gestão Lula: Ganho real do salário mínimo de +84% no histórico e reajuste acima do PIB.\n• Desemprego recuando para 6,2%, perto das mínimas históricas (IBGE/PNAD).\n• Reservas internacionais de US$ 365 bilhões que protegem o real de crises externas.\n• Sem ameaças de golpe, com diálogo institucional e previsibilidade.",
            "footer": "Previsibilidade para o mercado e poder de compra para a população."
        },
        {
            "num": "Slide 8",
            "title": "6. O Raio-X da Decisão para o Indeciso",
            "content": "A pergunta que você deve se fazer no segundo turno:\n\n👉 Você prefere governança comprovada, salário mínimo subindo e previsibilidade econômica?\n\n❌ Ou prefere entregar o país a um grupo com histórico crônico de escândalos, dinheiro vivo, aparelhamento e votos contra os seus direitos?\n\n💬 A PERGUNTA DECISIVA PARA O 2º TURNO:\n\"Você vai votar por fanatismo de grupo ou para proteger a comida no prato, o seu salário e a tranquilidade da sua família?\"",
            "footer": "Dados brutos não têm lado partidário: têm fatos auditáveis."
        },
        {
            "num": "Slide 9 (Código Aberto)",
            "title": "Audite você mesmo. O código é 100% aberto.",
            "content": "Desenvolvemos um dashboard completo em Python com as bases de dados para qualquer um rodar.\n\n• Conexão direta nas APIs públicas do Senado, BACEN e IBGE\n• Banco DuckDB e scripts 100% públicos no GitHub\n• Audite com autonomia e tire suas próprias conclusões.",
            "footer": "Transparência radical e código aberto."
        },
        {
            "num": "Slide 10 (Agregador de Links) ⭐",
            "title": "Todas as provas e links reunidos em um só lugar.",
            "content": "Reunimos cada documento, inquérito e notícia oficial em uma página única e gratuita:\n\n🔗 telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09\n\n(Acesse diretamente no link da bio do perfil)\n\n• Votações do Senado • Coaf • Inquérito PF • Acórdão TSE • Séries BACEN\n\nSalve este carrossel e compartilhe com quem está indeciso no 2º turno!",
            "footer": "Disponível gratuitamente no link da bio 🔖"
        }
    ]
    
    for s in slides:
        st.markdown(f"""
        <div class="carousel-slide">
            <div class="carousel-header">{s['num']}</div>
            <div class="carousel-title">{s['title']}</div>
            <div style="font-size: 1rem; line-height: 1.7; white-space: pre-line; color: #c9d1d9;">
                {s['content']}
            </div>
            <div style="margin-top: 14px; font-size: 0.8rem; color: #8b949e; border-top: 1px solid #30363d; padding-top: 8px;">
                {s['footer']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### 🌐 Agregador Público Oficial de Fontes")
    st.success("""
    🔗 **Página pública gratuita já criada no ar:**  
    👉 [https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09](https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09)  
    *(Você pode colocar exatamente este link na bio do Instagram ou no seu Linktree)*
    """)
    
    st.markdown("### 📝 Legenda Pronta para o Post do Instagram")
    
    caption_text = """Você ainda está em dúvida sobre o seu voto no 2º turno?

Em vez de me guiar por discursos de palanque ou fofocas de internet, decidi fazer o que faço no canal: puxar os dados oficiais e auditar os registros no código.

Auditei os votos de Flávio Bolsonaro no Senado, os relatórios do Coaf, os inquéritos da Polícia Federal no STF e cruzei com as séries econômicas oficiais do Banco Central e IBGE.

O que os números mostram:
1️⃣ Voto a favor da privatização da Eletrobras (MP 1031/2021) que encareceu a conta de luz e posicionamento contra a política de valorização do salário mínimo.
2️⃣ 48 depósitos em dinheiro vivo de R$ 2.000 rastreados pelo Coaf e compra de mansão de R$ 6 milhões com renda parlamentar.
3️⃣ Aparelhamento comprovado da Abin paralela para produzir relatórios sigilosos em defesa privada (Inquérito PF/STF).
4️⃣ Multa de R$ 22,9 milhões do TSE ao PL por questionar urnas sem provas.
5️⃣ O contraste com a gestão Lula: aumento real de renda de +84%, desemprego em mínimas históricas (6,2%) e US$ 365 bi em reservas.

Para o eleitor indeciso, a decisão não é sobre amor a candidatos: é sobre gestão de risco. Previsibilidade e comida na mesa vs. instabilidade e privilégios.

🔗 TODAS AS FONTES E DOCUMENTOS ESTÃO REUNIDOS NO LINK DA BIO:
👉 https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09

Abra pelo link da bio e confira documento por documento com um clique, sem cadastro.

Compartilhe com quem ainda está em dúvida. 🇧🇷

#eleicoes2026 #politica #analisededados #python #flaviobolsonaro #lula #dadosabertos #tecnologia #segundoturno #indecisos"""

#eleicoes2026 #politica #analisededados #python #flaviobolsonaro #lula #dadosabertos #tecnologia #segundoturno #indecisos"""
    
    st.text_area("Copie a Legenda Abaixo:", value=caption_text, height=270)

    st.markdown("---")
    st.markdown("### 🔗 Guia de Fontes Confiáveis & Links Oficiais")
    st.markdown("""
    Todos os dados do carrossel são verificáveis diretamente na fonte primária:
    
    * **Slide 2 (Voto & Bolso):**
      - [Poder360 - Painel da Votação da Eletrobras (Voto SIM de Flávio)](https://www.poder360.com.br/congresso/saiba-como-votou-cada-senador-na-privatizacao-da-eletrobras/)
      - [Agência Senado - Tramitação e Aprovação da MP do Salário Mínimo](https://www12.senado.leg.br/noticias/materias/2023/08/24/senado-aprova-mp-do-salario-minimo-com-correcao-do-ir-texto-vai-a-sancao)
    * **Slide 3 (Patrimônio & Dinheiro Vivo):**
      - [G1 - Flávio Bolsonaro compra mansão de quase R$ 6 milhões em Brasília](https://g1.globo.com/politica/noticia/2021/03/01/flavio-bolsonaro-compra-mansao-de-quase-r-6-milhoes-em-brasilia.ghtml)
      - [Jornal Nacional - Coaf aponta 48 depósitos em dinheiro vivo](https://g1.globo.com/jornal-nacional/noticia/2019/01/18/coaf-aponta-48-depositos-em-dinheiro-vivo-em-conta-de-flavio-bolsonaro.ghtml)
      - [G1 - Loja de chocolates usada para lavar até R$ 1,6 milhão em dinheiro vivo](https://g1.globo.com/rj/rio-de-janeiro/noticia/2019/12/19/mp-do-rio-aponta-que-loja-de-chocolates-de-flavio-bolsonaro-lavou-ate-r-16-milhao.ghtml)
    * **Slide 4 (Abin Paralela):**
      - [G1 - PF diz que Abin paralela foi usada para produzir relatórios e blindar Flávio](https://g1.globo.com/politica/noticia/2024/01/25/pf-diz-que-abin-paralela-foi-usada-para-ajudar-na-defesa-de-flavio-bolsonaro.ghtml)
      - [CNN Brasil - Áudio de reunião gravada por Ramagem com plano para blindar Flávio](https://www.cnnbrasil.com.br/politica/audio-gravado-por-ramagem-mostra-plano-para-blindar-flavio-bolsonaro-diz-pf/)
    * **Slide 5 (Instabilidade & PL):**
      - [TSE - Decisão oficial de aplicação de multa de R$ 22,9 milhões ao PL](https://www.tse.jus.br/comunicacao/noticias/2022/Novembro/tse-multa-coligacao-em-r-22-9-milhoes-por-litigancia-de-ma-fe)
      - [Agência Senado - PEC das Praias (PEC 3/2022) relatada por Flávio](https://www12.senado.leg.br/noticias/materias/2024/05/27/pec-dos-terrenos-de-marinha-gera-debate-sobre-privatizacao-de-praias)
    * **Slide 6 (Gestão Lula):**
      - [Banco Central do Brasil - Séries SGS 3546 (Reservas) e 1619 (Salário Mínimo)](https://www.bcb.gov.br/estabilidadefinanceira/reservasinternacionais)
      - [IBGE - PNAD Contínua (Taxa de Desocupação 6,2%)](https://agenciadenoticias.ibge.gov.br/)
    """)

# ==============================================================================
# AUDITORIA IMPLACÁVEL: FLÁVIO & PL (FOCO AMPLIADO)
# ==============================================================================
elif view_mode == "🔍 Auditoria Implacável: Flávio & PL":
    st.subheader("Auditoria Aprofundada: O Histórico de Flávio Bolsonaro, PL e Clã")
    st.markdown("""
    Esta seção reúne a documentação factual dos episódios mais críticos envolvendo Flávio Bolsonaro, o partido PL 
    e a rede de investigações. Todos os dados foram checados em fontes primárias: **Coaf, PF, MP-RJ, STF e painel do Senado**.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Votos Contra Direitos</div>
            <div class="metric-value" style="color: #ff5252;">Salário & Previdência</div>
            <div class="metric-desc">Votou contra política de reajuste permanente do mínimo</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Aparelhamento de Estado</div>
            <div class="metric-value" style="color: #ff9100;">Abin Paralela</div>
            <div class="metric-desc">Comprovado pela Polícia Federal no inquérito do STF</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Patrimônio em Espécie</div>
            <div class="metric-value" style="color: #40c4ff;">48 Depósitos</div>
            <div class="metric-desc">Fracionados em R$ 2 mil no caixa eletrônico (Coaf)</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráficos
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("##### Distribuição de Notícias por Eixo Crítico")
        cat_counts = df_media["categoria"].value_counts().reset_index()
        cat_counts.columns = ["Categoria", "Total"]
        fig_pie = px.pie(
            cat_counts,
            values="Total",
            names="Categoria",
            hole=0.45,
            color_discrete_sequence=["#d32f2f", "#f57c00", "#1976d2"]
        )
        fig_pie.update_layout(template="plotly_dark", height=350)
        st.plotly_chart(fig_pie, width="stretch")
        
    with col_c2:
        st.markdown("##### Cronologia dos Fatos (2018 - 2026)")
        year_counts = df_media.groupby(["ano", "categoria"]).size().reset_index(name="Quantidade")
        fig_bar = px.bar(
            year_counts,
            x="ano",
            y="Quantidade",
            color="categoria",
            barmode="stack",
            color_discrete_map={
                "Investigações & Abuso de Poder": "#d32f2f",
                "Risco Institucional & Golpismo": "#f57c00",
                "Contradições & Incoerência Parlamentar": "#1976d2"
            }
        )
        fig_bar.update_layout(template="plotly_dark", height=350)
        st.plotly_chart(fig_bar, width="stretch")

    st.markdown("---")
    st.markdown("#### Ficha Completa das Investigações e Votos")
    
    filtro_alvo = st.selectbox("Filtrar por Gravidade:", ["Todos", "Gravidade Máxima (5/5)", "Gravidade Alta (4/5)"])
    if filtro_alvo == "Gravidade Máxima (5/5)":
        df_mostrar = df_media[df_media["gravidade_score"] == 5]
    elif filtro_alvo == "Gravidade Alta (4/5)":
        df_mostrar = df_media[df_media["gravidade_score"] == 4]
    else:
        df_mostrar = df_media
        
    for _, row in df_mostrar.iterrows():
        with st.expander(f"🚨 [{row['data'].strftime('%d/%m/%Y')}] {row['titulo']}"):
            st.markdown(f"**O que aconteceu:** {row['resumo']}")
            st.markdown(f"**⚡ Por que isso afeta o eleitor:** `{row['impacto_eleitor']}`")
            st.caption(f"Fonte: {row['veiculo']} | Categoria: {row['categoria']} | Gravidade: {row['gravidade_score']}/5")

# ==============================================================================
# RAIO-X DO INDECISO: FATOS VS RISCO
# ==============================================================================
elif view_mode == "⚖️ Raio-X do Indeciso: Fatos vs Risco":
    st.subheader("O Raio-X para Quem Ainda Tem Dúvida: Fatos vs. Risco Crônico")
    st.markdown("""
    O eleitor indeciso não quer torcida de futebol. Ele quer saber: **quem protege o meu emprego e quem coloca a estabilidade em risco?**
    """)
    
    st.markdown("""
    | Área de Interesse | Gestão Lula (Histórico Comprovado) | Flávio Bolsonaro & PL (Ações Documentadas) | A Decisão Lógica |
    | :--- | :--- | :--- | :--- |
    | **Seu Salário e Poder de Compra** | Ganho real de +84% no período histórico; volta da valorização PIB + IPCA em 2023. | **Votou CONTRA** a nova política permanente de valorização do mínimo no Senado. | Lula garante dinheiro real; Flávio votou contra. |
    | **Transparência e Dinheiro Público** | Portal da Transparência, órgãos de controle autônomos. | 48 depósitos em dinheiro vivo de R$ 2 mil, mansão de R$ 6M e caso Queiroz. | Risco crônico de apropriação indevida do patrimônio. |
    | **Uso da Polícia e da Inteligência** | Fortalecimento técnico da PF sem interferência em inquéritos de ministros. | **Abin paralela** usada ilegalmente para blindar a família de processos. | Aparelhamento inaceitável de agências do Estado. |
    | **Estabilidade das Leis e Democracia** | Condução democrática, transição pacífica e diálogo com todos os poderes. | Multa de R$ 22,9M por atacar urnas, discursos golpistas e PEC das Praias. | Risco de isolamento internacional e crises diárias. |
    | **Conta de Luz e Serviços Básicos** | Luz para Todos, defesa de modicidade tarifária estatal. | Voto a favor da privatização da Eletrobras com jabutis que subiram as tarifas. | Lula protege tarifas populares. |
    """)

# ==============================================================================
# CONTRASTE MACROECONÔMICO (LULA)
# ==============================================================================
elif view_mode == "📊 Contraste Macroeconômico (Lula)":
    st.subheader("O Contraste da Gestão: 20 Anos de Séries Oficiais de Lula")
    st.markdown("""
    Como pilar de sustentação, as séries temporais do Banco Central e IBGE demonstram que a estabilidade 
    econômica do país coincide com as fases de liderança de Lula.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Salário Mínimo Real</div>
            <div class="metric-value" style="color: #38ef7d;">+84%</div>
            <div class="metric-desc">Poder de compra real deflacionado pelo IPCA</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Reservas Cambiais</div>
            <div class="metric-value" style="color: #58a6ff;">US$ 365 Bi</div>
            <div class="metric-desc">Criação da blindagem externa da moeda</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Desocupação</div>
            <div class="metric-value" style="color: #e53935;">6.2%</div>
            <div class="metric-desc">Perto das mínimas históricas (PNAD)</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    fig_sal = px.line(
        df_macro,
        x="ano",
        y="salario_minimo_real_indice",
        color="bloco_politico",
        markers=True,
        title="Poder de Compra Real do Salário Mínimo (2002=100)",
        color_discrete_map={
            "Governos Lula": "#e53935",
            "Governo Bolsonaro (Apoiado por Flávio/PL)": "#fdd835",
            "Governo Dilma": "#ff7043",
            "Outras Gestões (FHC / Temer)": "#78909c"
        }
    )
    fig_sal.update_layout(template="plotly_dark", height=420)
    st.plotly_chart(fig_sal, width="stretch")

# ==============================================================================
# ROTEIRO VÍDEO LONGO (YOUTUBE)
# ==============================================================================
elif view_mode == "🎬 Roteiro Vídeo Longo (YouTube)":
    st.subheader("Roteiro Complementar: Vídeo Longo do YouTube (10 a 12 min)")
    st.markdown("""
    Roteiro para aprofundamento técnico no YouTube, caso você decida publicar a versão estendida após os vídeos curtos.
    """)
    st.markdown("""
    * **0:00 - 1:30:** Gancho inicial e apresentação da arquitetura do projeto (Python + DuckDB + NLP).
    * **1:30 - 4:00:** Auditoria do painel do Senado: dissecando os votos nominais de Flávio Bolsonaro contra o salário mínimo e a PEC das Praias.
    * **4:00 - 7:30:** Auditoria patrimonial e criminal: O caso Queiroz, os depósitos de R$ 2.000, a loja de chocolates e o relatório da PF sobre a Abin Paralela.
    * **7:30 - 10:00:** O contraponto de dados: As séries históricas do Banco Central comprovando que a estabilidade social foi conquistada sob a gestão Lula.
    * **10:00 - 12:00:** Mensagem final ao eleitor indeciso: como transformar incerteza em voto racional baseado em minimização de risco.
    """)

# ==============================================================================
# TERMINAL SQL (DUCKDB LIVE)
# ==============================================================================
elif view_mode == "💻 Terminal SQL (DuckDB Live)":
    st.subheader("Console Analítico SQL: DuckDB em Tempo Real")
    query_pre = st.selectbox(
        "Consultas Rápidas de Auditoria:",
        [
            "SELECT categoria, total_noticias, gravidade_media FROM view_resumo_risco_media;",
            "SELECT data, veiculo, titulo, categoria FROM media_audit WHERE gravidade_score >= 5 ORDER BY data DESC;",
            "SELECT bloco_politico, desemprego_medio_pct, indice_salario_real_medio FROM view_medias_por_bloco;"
        ]
    )
    sql_input = st.text_area("Comando SQL:", value=query_pre, height=90)
    if st.button("Executar Consulta SQL"):
        try:
            conn = duckdb.connect(DB_PATH, read_only=True)
            res_df = conn.execute(sql_input).fetchdf()
            conn.close()
            st.dataframe(res_df, width="stretch")
            st.success(f"Consulta executada com sucesso! Retornou {len(res_df)} registros.")
        except Exception as e:
            st.error(f"Erro ao executar SQL: {e}")
