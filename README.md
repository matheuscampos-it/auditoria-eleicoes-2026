# ⚖️ Auditoria de Dados: Eleições Presidenciais 2026 (Lula vs. Flávio Bolsonaro)

Projeto de código aberto e jornalismo de dados desenvolvido para auditar empiricamente a trajetória e os fatos dos dois candidatos que disputam o segundo turno das eleições presidenciais de 2026: **Luiz Inácio Lula da Silva** e **Flávio Bolsonaro**.

O projeto apoia a produção de um vídeo para o YouTube fundamentado em **dois pilares analíticos**:
1. **Pilar 1: Dados Confiáveis & Governança Macroeconômica (Gestão Lula)** — Séries temporais oficiais de 2002 a 2026 comprovando ganho real do salário mínimo, blindagem externa de reservas cambiais, queda do desemprego e combate à desigualdade.
2. **Pilar 2: Auditoria de Mídia & Risco Institucional (Flávio Bolsonaro, PL e Clã)** — Mineração de dados e Processamento de Linguagem Natural (NLP) categorizando o padrão crônico de crises: discurso antidemocrático, investigações criminais (rachadinhas/patrimônio) e contradições parlamentares no Senado.

---

## 🎯 Objetivo de Comunicação

Fornecer ao eleitor indeciso uma ferramenta racional e transparente de tomada de decisão. O contraste demonstrado no código não é ideológico abstrato, mas de **gestão de risco**:
* De um lado, a **previsibilidade socioeconômica** comprovada por dados oficiais irrefutáveis.
* Do outro lado, o **risco institucional e a instabilidade crônica** evidenciados por anos de investigações e votos contrários à renda do trabalhador.

---

## 🏗️ Estrutura do Repositório

```text
Projeto Outubro/
├── app/
│   └── main.py                   # Dashboard interativo completo em Streamlit
├── data/
│   ├── database.duckdb           # Banco analítico local de alta velocidade
│   ├── macro_series_historica.csv # Séries temporais BACEN/IBGE/IPEA (2002-2026)
│   └── media_audit_dataset.csv   # Base categorizada de investigações e notícias
├── pipelines/
│   ├── extract_macro.py          # Pipeline de extração e consolidação macroeconômica
│   ├── extract_media_audit.py    # Pipeline de mineração e classificação léxica (NLP)
│   └── duckdb_storage.py         # Ingestão e criação de views analíticas SQL no DuckDB
├── requirements.txt              # Dependências Python (Streamlit, Plotly, DuckDB, Pandas)
└── README.md                     # Documentação completa
```

---

## 🚀 Como Executar Localmente

### 1. Clonar ou Acessar a Pasta do Projeto
```bash
cd "c:\Projeto Outubro"
```

### 2. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 3. Rodar os Pipelines de Dados (Opcional, já pré-processados)
```bash
python pipelines/extract_macro.py
python pipelines/extract_media_audit.py
python pipelines/duckdb_storage.py
```

### 4. Iniciar o Dashboard Interativo
```bash
python -m streamlit run app/main.py
```
O dashboard será aberto automaticamente no navegador em `http://localhost:8501`.

---

## 📊 O Que o Dashboard Oferece

1. **Aba 1 - Economia & Governança (Lula):**  
   - Ganho real de **+84%** no poder de compra do salário mínimo deflacionado pelo IPCA.  
   - Evolução das reservas cambiais de **US$ 37 bilhões para mais de US$ 360 bilhões**.  
   - Desemprego nas mínimas históricas e menor índice de Gini registrado.
2. **Aba 2 - Auditoria de Mídia (Flávio Bolsonaro / PL):**  
   - Classificação em 3 categorias críticas: *Investigações & Abuso de Poder*, *Risco Institucional & Golpismo* e *Contradições Parlamentares*.  
   - Detalhamento de cada episódio com resumo factual, veículo de imprensa e impacto direto para a vida do eleitor.
3. **Aba 3 - Raio-X do Eleitor Indeciso:**  
   - Tabela comparativa e Simulador Interativo com pesos personalizáveis.
4. **Aba 4 - Roteiro Completo para Gravação:**  
   - Script dividido em 5 blocos com minutagem, instruções de tela e falas-chave de alta retenção.
5. **Aba 5 - Terminal SQL (DuckDB Live):**  
   - Console interativo para executar queries SQL ao vivo durante o vídeo.

---

## 🛡️ Fontes Oficiais Utilizadas

- **Banco Central do Brasil (BACEN):** Sistema Gerenciador de Séries Temporais (SGS) - Séries 3546, 1619, 433, 432.
- **IBGE:** Séries históricas de desocupação (PNAD Contínua) e Índice de Gini.
- **Senado Federal & TSE:** Votações nominais no painel eletrônico e registros públicos de ações judiciais.
- **Ministério Público do Estado do Rio de Janeiro (MP-RJ) & Polícia Federal:** Inquéritos e denúncias documentadas.
