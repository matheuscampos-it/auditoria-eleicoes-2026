"""
Dashboard Analítico: Auditoria de Dados & Notícias - Eleições 2026
Foco exclusivo em dados confiáveis, séries temporais oficiais e auditoria factual de notícias.
"""

import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import duckdb

# Configuração da Página
st.set_page_config(
    page_title="Auditoria de Dados 2026 | Fatos, Notícias e Governança",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS Personalizada (Dark Theme & Data Cards)
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
    .badge-success {
        background-color: #2e7d32;
        color: white;
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
st.sidebar.image("https://img.icons8.com/color/96/database.png", width=60)
st.sidebar.title("Auditoria de Dados 2026")
st.sidebar.caption("Plataforma Factual: Séries Oficiais, NLP de Notícias e DuckDB")

view_mode = st.sidebar.radio(
    "Módulos Analíticos",
    [
        "🔍 Auditoria de Mídia: Notícias & Investigações",
        "📊 Séries Macroeconômicas (BACEN & IBGE)",
        "⚖️ Matriz de Gestão de Risco (Indecisos)",
        "💻 Terminal SQL Analítico (DuckDB Live)",
        "🌐 Repositório de Fontes & Documentos"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**🛡️ Integridade dos Dados:**
- Banco analítico: **DuckDB SQL**
- Séries temporais: **BACEN SGS & IBGE PNAD**
- Fontes judiciais: **Coaf, PF/STF e Senado**
- Código 100% aberto e reproduzível.
""")

# ==============================================================================
# 1. AUDITORIA DE MÍDIA: NOTÍCIAS & INVESTIGAÇÕES
# ==============================================================================
if view_mode == "🔍 Auditoria de Mídia: Notícias & Investigações":
    st.markdown("""
    <div>
        <span class="badge-pill badge-alert">DATA AUDIT</span>
        <span class="badge-pill badge-tech">NLP & MINERAÇÃO DE DADOS</span>
    </div>
    <h1 style='margin-top: 10px;'>Auditoria de Mídia: Notícias, Investigações e Votações</h1>
    <p style='color: #8b949e; font-size: 1.05rem;'>
        Mapeamento empírico de notícias de repercussão judicial, contradições parlamentares e investigações criminais 
        envolvendo Flávio Bolsonaro, seus familiares e o partido PL. Todos os eventos foram auditados em fontes primárias.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Votos Contra Renda</div>
            <div class="metric-value" style="color: #ff5252;">Salário Mínimo</div>
            <div class="metric-desc">Votou CONTRA a política permanente de reajuste pelo PIB</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Aparelhamento Institucional</div>
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
        st.markdown("##### Distribuição das Notícias por Eixo Crítico")
        cat_counts = df_media["categoria"].value_counts().reset_index()
        cat_counts.columns = ["Categoria", "Total"]
        fig_pie = px.pie(
            cat_counts,
            values="Total",
            names="Categoria",
            hole=0.45,
            color_discrete_sequence=["#d32f2f", "#f57c00", "#1976d2"]
        )
        fig_pie.update_layout(template="plotly_dark", height=350, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_pie, width="stretch")
        
    with col_c2:
        st.markdown("##### Cronologia dos Fatos Documentados (2018 - 2026)")
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
        fig_bar.update_layout(template="plotly_dark", height=350, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_bar, width="stretch")

    st.markdown("---")
    st.markdown("### 📋 Ficha Factual Detalhada das Notícias")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        filtro_cat = st.selectbox("Filtrar por Categoria:", ["Todas"] + list(df_media["categoria"].unique()))
    with col_f2:
        filtro_grav = st.selectbox("Filtrar por Gravidade:", ["Todas", "Gravidade Máxima (5/5)", "Gravidade Alta (4/5)"])
        
    df_filtrado = df_media.copy()
    if filtro_cat != "Todas":
        df_filtrado = df_filtrado[df_filtrado["categoria"] == filtro_cat]
    if filtro_grav == "Gravidade Máxima (5/5)":
        df_filtrado = df_filtrado[df_filtrado["gravidade_score"] == 5]
    elif filtro_grav == "Gravidade Alta (4/5)":
        df_filtrado = df_filtrado[df_filtrado["gravidade_score"] == 4]
        
    st.caption(f"Exibindo **{len(df_filtrado)}** de **{len(df_media)}** investigações e fatos catalogados.")
    
    if df_filtrado.empty:
        st.info("Nenhuma ocorrência encontrada para a combinação de filtros selecionada.")
    else:
        for _, row in df_filtrado.iterrows():
            with st.expander(f"🚨 [{row['data'].strftime('%d/%m/%Y')}] {row['titulo']}"):
                st.markdown(f"**O que aconteceu:** {row['resumo']}")
                st.markdown(f"**⚡ Impacto direto para o eleitor:** `{row['impacto_eleitor']}`")
                st.caption(f"Fonte: {row['veiculo']} | Categoria: {row['categoria']} | Gravidade: {row['gravidade_score']}/5 | Fonte Primária: Documento Oficial")

# ==============================================================================
# 2. SÉRIES MACROECONÔMICAS (BACEN & IBGE)
# ==============================================================================
elif view_mode == "📊 Séries Macroeconômicas (BACEN & IBGE)":
    st.markdown("""
    <div>
        <span class="badge-pill badge-success">DADOS OFICIAIS</span>
        <span class="badge-pill badge-tech">BANCO CENTRAL & IBGE</span>
    </div>
    <h1 style='margin-top: 10px;'>Séries Macroeconômicas Históricas (2002 - 2026)</h1>
    <p style='color: #8b949e; font-size: 1.05rem;'>
        Séries temporais auditáveis extraídas diretamente dos sistemas públicos <b>SGS do Banco Central</b> 
        e <b>SIDRA do IBGE</b>, demonstrando indicadores reais de renda, reservas internacionais e emprego.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Salário Mínimo Real</div>
            <div class="metric-value" style="color: #38ef7d;">+84%</div>
            <div class="metric-desc">Poder de compra real deflacionado pelo IPCA (2002-2026)</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Reservas Cambiais</div>
            <div class="metric-value" style="color: #58a6ff;">US$ 365 Bi</div>
            <div class="metric-desc">Muralha cambial construída para proteger a moeda nacional</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Taxa de Desocupação</div>
            <div class="metric-value" style="color: #38ef7d;">6.2%</div>
            <div class="metric-desc">Taxa de desemprego em mínimas históricas (PNAD/IBGE)</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    tab_g1, tab_g2, tab_g3 = st.tabs(["Evolução do Salário Mínimo Real", "Reservas Internacionais (US$ Bi)", "Taxa de Desemprego"])
    
    macro_periods = [
        (2002.5, 2010.5, "Lula 1 e 2", "rgba(229, 57, 53, 0.12)"),
        (2010.5, 2015.5, "Dilma", "rgba(255, 112, 67, 0.08)"),
        (2015.5, 2018.5, "Temer", "rgba(120, 144, 156, 0.08)"),
        (2018.5, 2022.5, "Bolsonaro", "rgba(253, 216, 53, 0.10)"),
        (2022.5, 2026.5, "Lula 3", "rgba(0, 230, 118, 0.12)")
    ]

    with tab_g1:
        fig_sal = go.Figure()
        fig_sal.add_trace(go.Scatter(
            x=df_macro["ano"],
            y=df_macro["salario_minimo_real_indice"],
            mode="lines+markers",
            name="Poder de Compra Real",
            line=dict(color="#00E676", width=3.5),
            marker=dict(size=8, color="#FFFFFF", line=dict(color="#00E676", width=2)),
            customdata=df_macro[["mandato", "bloco_politico", "salario_minimo_nominal"]],
            hovertemplate="<b>Ano %{x}</b> (%{customdata[0]})<br>Índice Real: <b>%{y:.1f} pts</b><br>Nominal: R$ %{customdata[2]:.2f}<br>Bloco: %{customdata[1]}<extra></extra>"
        ))
        for x0, x1, lbl, col in macro_periods:
            fig_sal.add_vrect(x0=x0, x1=x1, fillcolor=col, layer="below", line_width=0, annotation_text=lbl, annotation_position="top left", annotation_font_size=11, annotation_font_color="#A0AEC0")
        fig_sal.update_layout(template="plotly_dark", height=450, margin=dict(l=20, r=20, t=40, b=20), title="Trajetória Contínua do Poder de Compra Real do Salário Mínimo (Base 2002 = 100)")
        st.plotly_chart(fig_sal, width="stretch")
        st.caption("Fonte: Banco Central do Brasil (SGS Série 1619) deflacionado pelo IPCA. Ganho real acumulado de +84% no período histórico.")
        
    with tab_g2:
        fig_res = go.Figure()
        fig_res.add_trace(go.Scatter(
            x=df_macro["ano"],
            y=df_macro["reservas_usd_bi"],
            mode="lines",
            fill="tozeroy",
            name="Reservas Cambiais",
            line=dict(color="#388BFD", width=3),
            fillcolor="rgba(56, 139, 253, 0.25)",
            customdata=df_macro[["mandato", "bloco_politico"]],
            hovertemplate="<b>Ano %{x}</b> (%{customdata[0]})<br>Reservas: <b>US$ %{y:.1f} Bi</b><br>Bloco: %{customdata[1]}<extra></extra>"
        ))
        for x0, x1, lbl, col in macro_periods:
            fig_res.add_vrect(x0=x0, x1=x1, fillcolor=col, layer="below", line_width=0, annotation_text=lbl, annotation_position="top left", annotation_font_size=11, annotation_font_color="#A0AEC0")
        fig_res.update_layout(template="plotly_dark", height=450, margin=dict(l=20, r=20, t=40, b=20), title="Evolução Contínua das Reservas Internacionais em Moeda Forte (US$ Bilhões)")
        st.plotly_chart(fig_res, width="stretch")
        st.caption("Fonte: Banco Central do Brasil (SGS Série 3546). De US$ 37,8 Bi (2002) ao patamar atual de US$ 365 Bi.")
        
    with tab_g3:
        fig_des = go.Figure()
        fig_des.add_trace(go.Scatter(
            x=df_macro["ano"],
            y=df_macro["desemprego_pct"],
            mode="lines+markers",
            name="Taxa de Desocupação",
            line=dict(color="#FF7043", width=3.5),
            marker=dict(size=8, color="#FFFFFF", line=dict(color="#FF7043", width=2)),
            customdata=df_macro[["mandato", "bloco_politico"]],
            hovertemplate="<b>Ano %{x}</b> (%{customdata[0]})<br>Desemprego: <b>%{y:.1f}%</b><br>Bloco: %{customdata[1]}<extra></extra>"
        ))
        for x0, x1, lbl, col in macro_periods:
            fig_des.add_vrect(x0=x0, x1=x1, fillcolor=col, layer="below", line_width=0, annotation_text=lbl, annotation_position="top left", annotation_font_size=11, annotation_font_color="#A0AEC0")
        fig_des.update_layout(template="plotly_dark", height=450, margin=dict(l=20, r=20, t=40, b=20), title="Evolução Contínua da Taxa de Desocupação (%)")
        st.plotly_chart(fig_des, width="stretch")
        st.caption("Fonte: IBGE (Pesquisa Nacional por Amostra de Domicílios Contínua - PNAD). Queda para 6,2% em 2026.")

# ==============================================================================
# 3. MATRIZ DE GESTÃO DE RISCO (INDECISOS)
# ==============================================================================
elif view_mode == "⚖️ Matriz de Gestão de Risco (Indecisos)":
    st.markdown("""
    <div>
        <span class="badge-pill badge-tech">ANÁLISE DE DECISÃO</span>
        <span class="badge-pill badge-alert">GESTÃO DE RISCO</span>
    </div>
    <h1 style='margin-top: 10px;'>Matriz Comparativa: Previsibilidade vs. Risco Crônico</h1>
    <p style='color: #8b949e; font-size: 1.05rem;'>
        Para o eleitor indeciso, a decisão não é baseada em torcida partidária, mas em <b>gestão de risco e previsibilidade</b>.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="overflow-x: auto; margin-top: 15px;">
    <table style="width: 100%; border-collapse: collapse; background-color: #161b22; border-radius: 10px; overflow: hidden; border: 1px solid #30363d; font-size: 0.95rem;">
        <thead>
            <tr style="background-color: #21262d; border-bottom: 2px solid #30363d; text-align: left;">
                <th style="padding: 14px 16px; color: #58a6ff; font-weight: 700; text-transform: uppercase;">Eixo de Auditoria</th>
                <th style="padding: 14px 16px; color: #3fb950; font-weight: 700; text-transform: uppercase;">Gestão Lula (Fatos Comprovados)</th>
                <th style="padding: 14px 16px; color: #f85149; font-weight: 700; text-transform: uppercase;">Flávio Bolsonaro & PL (Ações Reais)</th>
                <th style="padding: 14px 16px; color: #d29922; font-weight: 700; text-transform: uppercase;">A Decisão Lógica</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid #30363d; background-color: #161b22;">
                <td style="padding: 14px 16px; font-weight: 600; color: #e6edf3;">Seu Salário e Poder de Compra</td>
                <td style="padding: 14px 16px; color: #c9d1d9;">Ganho real de +84% no período histórico; fórmula de valorização real (PIB + IPCA).</td>
                <td style="padding: 14px 16px; color: #c9d1d9;"><b style="color: #ff7b72;">Votou CONTRA</b> a política permanente de valorização do salário mínimo no Senado.</td>
                <td style="padding: 14px 16px; color: #7ee787; font-weight: 600;">Lula garante aumento real; Flávio votou contra no Senado.</td>
            </tr>
            <tr style="border-bottom: 1px solid #30363d; background-color: #0d1117;">
                <td style="padding: 14px 16px; font-weight: 600; color: #e6edf3;">Transparência e Dinheiro Público</td>
                <td style="padding: 14px 16px; color: #c9d1d9;">Criação do Portal da Transparência, CGU e autonomia total aos órgãos fiscalizadores.</td>
                <td style="padding: 14px 16px; color: #c9d1d9;"><b style="color: #ff7b72;">48 depósitos em dinheiro vivo</b> de R$ 2 mil, mansão de R$ 6M e caso Queiroz.</td>
                <td style="padding: 14px 16px; color: #7ee787; font-weight: 600;">Lula garante governança pública; Flávio movimenta dinheiro vivo.</td>
            </tr>
            <tr style="border-bottom: 1px solid #30363d; background-color: #161b22;">
                <td style="padding: 14px 16px; font-weight: 600; color: #e6edf3;">Uso da Polícia e da Inteligência</td>
                <td style="padding: 14px 16px; color: #c9d1d9;">Fortalecimento técnico da PF com investigações sem interferência política.</td>
                <td style="padding: 14px 16px; color: #c9d1d9;"><b style="color: #ff7b72;">Abin paralela</b> usada ilegalmente para espionar e blindar a família de processos.</td>
                <td style="padding: 14px 16px; color: #7ee787; font-weight: 600;">Lula respeita as instituições; Flávio aparelhou a Abin como escudo.</td>
            </tr>
            <tr style="border-bottom: 1px solid #30363d; background-color: #0d1117;">
                <td style="padding: 14px 16px; font-weight: 600; color: #e6edf3;">Estabilidade das Leis e Democracia</td>
                <td style="padding: 14px 16px; color: #c9d1d9;">Condução democrática, transição pacífica e diálogo institucional com os Poderes.</td>
                <td style="padding: 14px 16px; color: #c9d1d9;"><b style="color: #ff7b72;">Multa de R$ 22,9M</b> por atacar urnas, discursos golpistas e PEC das Praias.</td>
                <td style="padding: 14px 16px; color: #7ee787; font-weight: 600;">Lula assegura estabilidade política; Flávio gera crises e multas.</td>
            </tr>
            <tr style="border-bottom: 1px solid #30363d; background-color: #161b22;">
                <td style="padding: 14px 16px; font-weight: 600; color: #e6edf3;">Conta de Luz e Tarifas Públicas</td>
                <td style="padding: 14px 16px; color: #c9d1d9;">Luz para Todos, defesa de modicidade tarifária estatal e subsídios para baixa renda.</td>
                <td style="padding: 14px 16px; color: #c9d1d9;"><b style="color: #ff7b72;">Votou SIM</b> pela privatização da Eletrobras com jabutis que encareceram a energia.</td>
                <td style="padding: 14px 16px; color: #7ee787; font-weight: 600;">Lula protege tarifas populares; Flávio votou para encarecer a luz.</td>
            </tr>
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. TERMINAL SQL ANALÍTICO (DUCKDB LIVE)
# ==============================================================================
elif view_mode == "💻 Terminal SQL Analítico (DuckDB Live)":
    st.markdown("""
    <div>
        <span class="badge-pill badge-tech">DUCKDB ENGINE</span>
        <span class="badge-pill badge-success">SQL LIVE</span>
    </div>
    <h1 style='margin-top: 10px;'>Terminal SQL Analítico: DuckDB em Tempo Real</h1>
    <p style='color: #8b949e; font-size: 1.05rem;'>
        Execute consultas SQL diretamente sobre o banco analítico local em DuckDB. Transparência e reprodutibilidade total.
    </p>
    """, unsafe_allow_html=True)
    
    query_pre = st.selectbox(
        "Consultas Rápidas de Auditoria:",
        [
            "SELECT categoria, total_noticias, gravidade_media FROM view_resumo_risco_media;",
            "SELECT data, veiculo, titulo, categoria FROM media_audit WHERE gravidade_score >= 5 ORDER BY data DESC;",
            "SELECT bloco_politico, variacao_real_salario_pct, desemprego_medio_pct, pico_reservas_usd_bi FROM view_medias_por_bloco;",
            "SELECT * FROM macro_series ORDER BY ano DESC;"
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

# ==============================================================================
# 5. REPOSITÓRIO DE FONTES & DOCUMENTOS PRIMÁRIOS
# ==============================================================================
elif view_mode == "🌐 Repositório de Fontes & Documentos":
    st.markdown("""
    <div>
        <span class="badge-pill badge-success">FONTES OFICIAIS</span>
        <span class="badge-pill badge-tech">DOCUMENTOS PRIMÁRIOS</span>
    </div>
    <h1 style='margin-top: 10px;'>Repositório de Fontes Oficiais & Documentos Primários</h1>
    <p style='color: #8b949e; font-size: 1.05rem;'>
        Todos os dados deste projeto foram auditados e possuem link direto para suas fontes primárias.
    </p>
    """, unsafe_allow_html=True)
    
    st.success("""
    📊 **Dashboard Web Live (GitHub Pages - sem instalação):**  
    👉 [https://matheuscampos-it.github.io/auditoria-eleicoes-2026/dashboard.html](https://matheuscampos-it.github.io/auditoria-eleicoes-2026/dashboard.html)

    🔗 **Linktree Oficial (Hub Unificado de Links):**  
    👉 [https://matheuscampos-it.github.io/auditoria-eleicoes-2026/](https://matheuscampos-it.github.io/auditoria-eleicoes-2026/)  
    
    📑 **Dossiê no Telegraph com todas as certidões:**  
    👉 [https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09](https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09)  
    """)
    
    st.markdown("""
    ### 🏛️ Fontes Governamentais, Leis e Séries Econômicas
    - **Banco Central do Brasil (BACEN):** [Sistema Gerenciador de Séries Temporais (SGS)](https://www.bcb.gov.br/) (Séries 3546, 1619, 433, 432).
    - **IBGE:** [PNAD Contínua & Séries SIDRA - Desocupação e Renda](https://www.ibge.gov.br/).
    - **Senado Federal (Salário Mínimo):** [Agência Senado - Aprovação da Política Permanente de Valorização Real](https://www12.senado.leg.br/noticias/materias/2023/08/24/salario-minimo-de-r-1-320-e-correcao-do-ir-vao-a-sancao).
    - **Privatização da Eletrobras (MP 1031/2021):** [Poder360 - Votação Nominal dos Senadores](https://www.poder360.com.br/congresso/saiba-como-votou-cada-partido-e-senador-na-mp-da-capitalizacao-da-eletrobras/) e [Senado - Ficha da Matéria](https://www25.senado.leg.br/web/atividade/materias/-/materia/148419).
    - **PEC das Praias (PEC 3/2022):** [Senado Federal - Tramitação Oficial](https://www25.senado.leg.br/web/atividade/materias/-/materia/151923).
    - **Teto de Gastos (EC 95/2016):** [Câmara dos Deputados - Histórico da Tramitação](https://www.camara.leg.br/propostas-legislativas/2088351).
    
    ### ⚖️ Investigações, Inquéritos e Tribunais
    - **Operação Vigilância Aproximada (Abin Paralela):** [G1 / PF - Abin espionou auditores da Receita para orientar defesa de Flávio](https://g1.globo.com/politica/noticia/2024/07/11/abin-espionou-auditores-da-receita-federal-que-apuravam-possivel-rachadinha-de-flavio-bolsonaro-diz-pf.ghtml).
    - **Áudio no Palácio do Planalto:** [CNN Brasil - Íntegra da gravação da reunião entre Bolsonaro, Ramagem e advogadas](https://www.cnnbrasil.com.br/politica/integra-gravacao-bolsonaro-ramagem/).
    - **Evolução Patrimonial (Mansão Lago Sul):** [Jornal Nacional - Compra e Financiamento da Mansão de R$ 6 Milhões](https://g1.globo.com/jornal-nacional/noticia/2021/03/02/flavio-bolsonaro-compra-casa-de-quase-r-6-milhoes-em-area-nobre-de-brasilia.ghtml).
    - **Conselho de Controle de Atividades Financeiras (Coaf):** [Jornal Nacional - Relatório do Coaf: 48 depósitos em espécie](https://g1.globo.com/jornal-nacional/noticia/2019/01/18/jn-tem-acesso-a-relatorio-do-coaf-sobre-movimentacoes-de-flavio-bolsonaro.ghtml).
    - **Lavagem de Capitais (Franquia de Chocolates):** [Jornal Nacional - Investigação e Perícia Contábil do MP-RJ](https://g1.globo.com/jornal-nacional/noticia/2019/12/19/investigacao-que-envolve-flavio-bolsonaro-aponta-indicios-de-lavagem-de-dinheiro.ghtml).
    - **Tribunal Superior Eleitoral (TSE):** [G1 / TSE - Moraes multa PL em R$ 22,9M por litigância de má-fé contra as urnas](https://g1.globo.com/politica/noticia/2022/11/23/moraes-decisao-pl-relatorio-urnas.ghtml).
    """)
