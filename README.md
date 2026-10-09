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
├── index.html                    # Agregador Linktree oficial (GitHub Pages)
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

## 🛡️ Fontes Primárias e Documentos Oficiais (100% Auditáveis)

- **Linktree Oficial (Hub Unificado de Links):** [https://matheuscampos-it.github.io/auditoria-eleicoes-2026/](https://matheuscampos-it.github.io/auditoria-eleicoes-2026/)
- **Dossiê no Telegraph (Certidões e Inquéritos):** [https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09](https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09)
- **Banco Central do Brasil (BACEN):** [SGS Séries 3546 e 1619](https://www.bcb.gov.br/) (Reservas Internacionais e Salário Real).
- **IBGE:** [PNAD Contínua](https://www.ibge.gov.br/) (Taxa histórica de desocupação a 6,2%).
- **Senado Federal (Salário Mínimo):** [Agência Senado - Política de Valorização Permanente (MP 1172/2023)](https://www12.senado.leg.br/noticias/materias/2023/08/24/salario-minimo-de-r-1-320-e-correcao-do-ir-vao-a-sancao).
- **Privatização da Eletrobras (MP 1031/2021):** [Poder360 - Painel Nominal de Votação](https://www.poder360.com.br/congresso/saiba-como-votou-cada-partido-e-senador-na-mp-da-capitalizacao-da-eletrobras/) e [Senado Federal - Ficha da MP](https://www25.senado.leg.br/web/atividade/materias/-/materia/148419).
- **PEC das Praias (PEC 3/2022):** [Senado Federal - Tramitação](https://www25.senado.leg.br/web/atividade/materias/-/materia/151923).
- **Teto de Gastos (EC 95/2016):** [Câmara dos Deputados](https://www.camara.leg.br/propostas-legislativas/2088351).
- **Inquérito da Abin Paralela:** [G1 / PF - Espionagem de Auditores da Receita Federal](https://g1.globo.com/politica/noticia/2024/07/11/abin-espionou-auditores-da-receita-federal-que-apuravam-possivel-rachadinha-de-flavio-bolsonaro-diz-pf.ghtml).
- **Gravação no Palácio do Planalto:** [CNN Brasil - Áudio de Reunião com Ramagem e Bolsonaro](https://www.cnnbrasil.com.br/politica/integra-gravacao-bolsonaro-ramagem/).
- **Mansão no Lago Sul de R$ 6 Milhões:** [Jornal Nacional - Compra e Financiamento no BRB](https://g1.globo.com/jornal-nacional/noticia/2021/03/02/flavio-bolsonaro-compra-casa-de-quase-r-6-milhoes-em-area-nobre-de-brasilia.ghtml).
- **48 Depósitos Fracionados:** [Jornal Nacional - Relatório do Coaf na Alerj](https://g1.globo.com/jornal-nacional/noticia/2019/01/18/jn-tem-acesso-a-relatorio-do-coaf-sobre-movimentacoes-de-flavio-bolsonaro.ghtml).
- **Loja de Chocolates & MP-RJ:** [Jornal Nacional - Perícia de Lavagem de Capitais](https://g1.globo.com/jornal-nacional/noticia/2019/12/19/investigacao-que-envolve-flavio-bolsonaro-aponta-indicios-de-lavagem-de-dinheiro.ghtml).
- **Multa por Litigância de Má-Fé contra Urnas:** [G1 / TSE - Decisão de Multa de R$ 22,9M ao PL](https://g1.globo.com/politica/noticia/2022/11/23/moraes-decisao-pl-relatorio-urnas.ghtml).
