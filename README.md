# ⚖️ Auditoria de Dados: Eleições Presidenciais 2026 (Lula vs. Flávio Bolsonaro)

Repositório aberto e independente com dados oficiais, estatísticas do Banco Central e documentos da Justiça para comparar com rigor e clareza os dois principais candidatos no 2º turno de 2026: **Luiz Inácio Lula da Silva** e **Flávio Bolsonaro**.

> 🚀 **Acesse Online Sem Instalar Nada:**  
> - 📊 **[Painel Analítico Interativo (Web Live)](https://matheuscampos-it.github.io/auditoria-eleicoes-2026/dashboard.html)**  
> - 🔗 **[Agregador Central de Links (GitHub Pages)](https://matheuscampos-it.github.io/auditoria-eleicoes-2026/)**  
> - 📑 **[Dossiê de Fontes e Certidões Oficiais (Telegraph)](https://telegra.ph/Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09)**

---

## 🎯 Pilares da Auditoria

1. **Economia Real & Séries Oficiais (Governo Lula):**  
   Extração direta de dados públicos do **Banco Central do Brasil (BACEN SGS)** e **IBGE (PNAD Contínua)** de 2002 a 2026, comprovando:
   - Ganho real de **+84%** no poder de compra do salário mínimo (acima da inflação).
   - Acúmulo de mais de **US$ 365 bilhões** em reservas cambiais para proteger o país de crises.
   - Taxa de desemprego em **6,2%**, próxima das mínimas históricas.

2. **Fatos, Votações & Investigações Judiciais (Flávio Bolsonaro & PL):**  
   Base factual de investigações e votações no Congresso, todas com link para a notícia ou documento original:
   - **Salário Mínimo e Energia:** Votou CONTRA a valorização permanente do salário mínimo e a favor de emendas na privatização da Eletrobras que encareceram a conta de luz.
   - **Dinheiro em Espécie (Coaf):** 48 depósitos fracionados de R$ 2.000 em dinheiro vivo na conta e compra de mansão de R$ 6 milhões no Lago Sul com renda parlamentar.
   - **Abin Paralela (PF/STF):** Polícia Federal comprovou espionagem ilegal para blindar Flávio nas investigações das rachadinhas.
   - **Tribunal Superior Eleitoral (TSE):** Multa de R$ 22,9 milhões ao PL por tentar anular a eleição presidencial sem apresentar provas.

3. **Alertas Institucionais: Ameaças à Democracia, Eleições & Soberania:**  
   Módulo analítico documentando ataques sistemáticos às instituições e aos direitos da população:
   - **Voto Popular & Urnas:** Ação do PL para anular quase 60% das urnas no 2º turno e desfile intimidatório de blindados na Praça dos Três Poderes.
   - **Submissão a Trump & Sanções contra o Brasil:** Comitiva do PL em Washington articulando com deputados trumpistas pedidos de sanções e tarifas comerciais punitivas contra a economia brasileira.
   - **Ameaças aos Direitos do Cidadão & ao Pix:** Pressão por custos no Pix, anistia ampla aos invasores e golpistas do 8 de Janeiro e PEC das Praias (PEC 3/2022) relatada por Flávio para privatizar terrenos de marinha.

---

## 🏗️ Estrutura do Repositório

```text
Projeto Outubro/
├── app/
│   └── main.py                   # Dashboard analítico interativo em Streamlit (Local/Cloud)
├── dashboard.html                # Dashboard interativo Web nativo (GitHub Pages Live)
├── index.html                    # Agregador Linktree oficial (GitHub Pages)
├── legenda_instagram.txt         # Legenda pronta e otimizada (máx 1.700 caracteres)
├── carousel_images/              # 10 slides em alta resolução (1080x1350) para Instagram (v6.0)
├── data/
│   ├── database.duckdb           # Banco analítico colunar local de alta velocidade
│   ├── macro_series_historica.csv # Séries temporais BACEN/IBGE (2002-2026)
│   ├── macro_series_historica.json
│   ├── media_audit_dataset.csv   # Base categorizada de 24 investigações e notícias com links
│   └── media_audit_dataset.json
├── pipelines/
│   ├── extract_macro.py          # Extração e consolidação macroeconômica
│   ├── extract_media_audit.py    # Classificação léxica, fontes diretas e enriquecimento de notícias
│   ├── duckdb_storage.py         # Ingestão e criação de views analíticas SQL no DuckDB
│   └── generate_carousel_images.py # Renderizador visual em lote dos 10 slides do Instagram
├── requirements.txt              # Dependências Python (Streamlit, Plotly, DuckDB, Pandas, Pillow)
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

### 3. Rodar os Pipelines de Dados & Carrossel (Opcional, bases já pré-processadas)
```bash
python pipelines/extract_macro.py
python pipelines/extract_media_audit.py
python pipelines/duckdb_storage.py
python pipelines/generate_carousel_images.py
```

### 4. Iniciar o Dashboard Streamlit
```bash
python -m streamlit run app/main.py
```
O dashboard será aberto no navegador em `http://localhost:8501`.

---

## 📊 Módulos do Dashboard Analítico

1. **Auditoria de Mídia & Investigações:** Classificação de 24 ocorrências por gravidade (1 a 5), cronologia 2018-2026, fichas detalhadas e links diretos para portais confiáveis (Poder360, Folha, Estadão, CNN Brasil - sem G1).
2. **Séries Macroeconômicas (BACEN & IBGE):** Gráficos interativos sobre Salário Real (+84%), Reservas Cambiais (US$ 365 bi) e Desemprego (6,2%) por bloco de governo.
3. **Matriz de Gestão de Risco:** Tabela analítica comparativa de previsibilidade socioeconômica vs. risco crônico institucional para o eleitor indeciso.
4. **🚨 Ameaças à Democracia & Soberania (Módulo em Destaque):** Ataques às urnas eletrônicas (multa de R$ 22,9M do TSE ao PL), articulação de tarifas e sanções contra empresas do Brasil nos EUA, pressões contra o Pix gratuito e invasões do 8/1.
5. **Terminal SQL (DuckDB Live):** Console de execução de queries SQL em tempo real sobre as tabelas e views analíticas colunares.
6. **Repositório de Fontes & Documentos:** Acesso rápido aos documentos primários, inquéritos e ao agregador público de certidões.

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
- **Inquérito da Abin Paralela:** [Poder360 / PF - Abin atuou ilegalmente em favor de Flávio Bolsonaro](https://www.poder360.com.br/poder-justica/abin-atuou-ilegalmente-em-favor-de-renan-e-flavio-bolsonaro-diz-pf/).
- **Gravação no Palácio do Planalto:** [CNN Brasil - Áudio de Reunião com Ramagem e Bolsonaro](https://www.cnnbrasil.com.br/politica/integra-gravacao-bolsonaro-ramagem/).
- **Mansão no Lago Sul de R$ 6 Milhões:** [CNN Brasil - Compra e Financiamento da Mansão](https://www.cnnbrasil.com.br/politica/flavio-bolsonaro-compra-mansao-avaliada-em-r-6-milhoes-em-brasilia/).
- **48 Depósitos Fracionados:** [Folha de S.Paulo - Coaf aponta 48 depósitos suspeitos na conta de Flávio](https://www1.folha.uol.com.br/poder/2019/01/coaf-aponta-48-depositos-suspeitos-na-conta-de-flavio-bolsonaro.shtml).
- **Loja de Chocolates & MP-RJ:** [Estadão - Investigação apura se loja de chocolates lavou dinheiro](https://www.estadao.com.br/politica/investigacao-apura-se-loja-de-flavio-bolsonaro-lavou-r-2-1-milhoes/).
- **Multa por Litigância de Má-Fé contra Urnas:** [Poder360 / TSE - Decisão de Multa de R$ 22,9M ao PL](https://www.poder360.com.br/justica/tse-mantem-multa-de-r-229-milhoes-ao-pl/).
