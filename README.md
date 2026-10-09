# ⚖️ Auditoria de Dados: Eleições Presidenciais 2026 (Lula vs. Flávio Bolsonaro)

Repositório de código aberto e jornalismo de dados desenvolvido para auditar empiricamente a trajetória, as votações legislativas e os indicadores econômicos dos dois principais concorrentes no segundo turno das eleições presidenciais de 2026: **Luiz Inácio Lula da Silva** e **Flávio Bolsonaro**.

---

## 🎯 Pilares da Auditoria

1. **Governança Macroeconômica & Séries Temporais Oficiais (Gestão Lula):**  
   Extração direta de séries temporais oficiais do **Banco Central do Brasil (BACEN SGS)** e **IBGE (SIDRA/PNAD)** de 2002 a 2026, comprovando:
   - Ganho real de **+84%** no poder de compra do salário mínimo (deflacionado pelo IPCA).
   - Acúmulo de mais de **US$ 365 bilhões** em reservas cambiais internacionais.
   - Taxa de desocupação (desemprego) em **6,2%**, próximas das mínimas históricas.

2. **Auditoria de Mídia, Notícias & Investigações (Flávio Bolsonaro & PL):**  
   Base analítica e Processamento de Linguagem Natural (NLP) categorizando eventos factualizados em fontes primárias:
   - **Votações Nominais no Senado:** Voto formal contra a política de valorização permanente do salário mínimo e voto a favor da MP da Eletrobras com jabutis tarifários.
   - **Inteligência Financeira (Coaf):** 48 depósitos fracionados de R$ 2.000 em dinheiro vivo e compra de mansão de R$ 6 milhões no Lago Sul com renda parlamentar.
   - **Inquérito Policial (PF/STF):** Uso indevido da Abin paralela para confecção de relatórios sigilosos de blindagem privada.
   - **Tribunais Eleitorais (TSE):** Multa de R$ 22,9 milhões ao PL por litigância de má-fé contra as urnas eletrônicas.

---

## 🏗️ Estrutura do Repositório

```text
Projeto Outubro/
├── app/
│   └── main.py                   # Dashboard interativo analítico em Streamlit
├── data/
│   ├── database.duckdb           # Banco analítico colunar local de alta velocidade
│   ├── macro_series_historica.csv # Séries temporais BACEN/IBGE (2002-2026)
│   ├── macro_series_historica.json
│   ├── media_audit_dataset.csv   # Base categorizada de investigações e notícias
│   └── media_audit_dataset.json
├── pipelines/
│   ├── extract_macro.py          # Extração e consolidação macroeconômica
│   ├── extract_media_audit.py    # Classificação léxica e enriquecimento de notícias
│   └── duckdb_storage.py         # Ingestão e criação de views analíticas SQL no DuckDB
├── requirements.txt              # Dependências Python (Streamlit, Plotly, DuckDB, Pandas)
└── README.md                     # Documentação completa da auditoria
```

---

## 🚀 Como Executar Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/matheuscampos-it/auditoria-eleicoes-2026.git
cd auditoria-eleicoes-2026
```

### 2. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 3. Rodar os Pipelines de Dados (Opcional, bases já pré-processadas)
```bash
python pipelines/extract_macro.py
python pipelines/extract_media_audit.py
python pipelines/duckdb_storage.py
```

### 4. Iniciar o Dashboard Streamlit
```bash
python -m streamlit run app/main.py
```
O dashboard será aberto no navegador em `http://localhost:8501`.

---

## 📊 Módulos do Dashboard Analítico

1. **Auditoria de Mídia & Investigações:** Classificação por gravidade, cronologia 2018-2026 e fichas detalhadas dos fatos.
2. **Séries Macroeconômicas:** Gráficos interativos em Plotly sobre Salário Real, Reservas Cambiais e Taxa de Desocupação por bloco de governo.
3. **Matriz de Gestão de Risco:** Tabela analítica comparativa de previsibilidade vs. risco institucional.
4. **Terminal SQL (DuckDB Live):** Console de execução de queries SQL em tempo real sobre as tabelas e views analíticas.
5. **Repositório de Fontes:** Acesso aos documentos primários e ao agregador público de certidões.

---

## 🛡️ Fontes Primárias e Documentos Oficiais

- **Banco Central do Brasil (BACEN):** Sistema Gerenciador de Séries Temporais (SGS) - Séries 3546, 1619, 433, 432.
- **IBGE:** Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua) e Séries SIDRA.
- **Senado Federal:** Registros nominais de votações em [legis.senado.leg.br](https://legis.senado.leg.br).
- **Tribunal Superior Eleitoral (TSE):** Acórdão de aplicação de multa à coligação do PL.
- **Polícia Federal / STF:** Inquérito da Operação Vigilância Aproximada (Abin Paralela).
- **Linktree Oficial (Hub Unificado de Links):** [https://matheuscampos-it.github.io/auditoria-eleicoes-2026/](https://matheuscampos-it.github.io/auditoria-eleicoes-2026/)
- **Dossiê no Telegraph (Certidões e Inquéritos):** [https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09](https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09)
