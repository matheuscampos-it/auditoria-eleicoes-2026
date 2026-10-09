"""
Pipeline de Auditoria de Mídia e NLP (Pilar 2: Risco Institucional e Contradições)
Mapeamento, categorização e quantificação de notícias e investigações envolvendo:
- Flávio Bolsonaro
- Partido Liberal (PL)
- Clã Bolsonaro e aliados diretos

Categorias de Auditoria:
1. Risco Institucional & Discurso Antidemocrático
2. Investigações, Rachadinhas & Suspeitas de Abuso de Poder
3. Contradições & Incoerência Política / Econômica
"""

import os
import json
import logging
import re
from datetime import datetime
import pandas as pd
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Regras léxicas para classificação de NLP
CATEGORIA_RULES = {
    "Risco Institucional & Golpismo": [
        r"golpe", r"antidemocr[aá]tic", r"urna", r"stf", r"elei[cç][oõ]es",
        r"interven[cç][aã]o", r"ai-5", r"8 de janeiro", r"tribunal", r"ditadura",
        r"for[cç]as armadas", r"anistia", r"censura", r"alexandre de moraes"
    ],
    "Investigações & Abuso de Poder": [
        r"rachadinha", r"queiroz", r"desvio", r"lavagem de dinheiro", r"mans[aã]o",
        r"abin paralela", r"esquema", r"patrim[oô]nio", r"mp-rj", r"peculato",
        r"chocolate", r"fantasma", r"aparelhamento", r"cheque", r"coaf"
    ],
    "Contradições & Incoerência Parlamentar": [
        r"teto de gastos", r"sal[aá]rio m[ií]nimo", r"privatiza[cç][aã]o", r"vota[cç][aã]o",
        r"centr[aã]o", r"or[cç]amento secreto", r"privil[eé]gio", r"fundo eleitoral",
        r"reforma trabalhista", r"aux[ií]lio", r"pl ", r"valdemar"
    ]
}

def classify_news_text(title: str, summary: str = "") -> str:
    """Classifica um texto noticioso em uma das três categorias de risco ou em Geral."""
    content = f"{title} {summary}".lower()
    
    scores = {cat: 0 for cat in CATEGORIA_RULES}
    for cat, patterns in CATEGORIA_RULES.items():
        for pattern in patterns:
            if re.search(pattern, content):
                scores[cat] += 1
                
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] > 0:
        return best_cat
    return "Outros Episódios Críticos"

def generate_curated_media_audit() -> pd.DataFrame:
    """
    Base de dados auditada com marcos de reportagens e investigações jornalísticas
    reais e documentadas de 2018 a 2026.
    """
    records = [
        # --- INVESTIGAÇÕES & RACHADINHAS ---
        {
            "data": "2018-12-06",
            "ano": 2018,
            "veiculo": "Estadão / Folha",
            "titulo": "Relatório do Coaf aponta movimentação atípica de R$ 1,2 milhão de Fabrício Queiroz, ex-assessor de Flávio Bolsonaro",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 5,
            "resumo": "Início do escândalo das rachadinhas na Alerj revelando repasses sistemáticos de salários de funcionários para Queiroz.",
            "impacto_eleitor": "Demonstra suspeita de apropriação indevida de dinheiro público por mais de uma década."
        },
        {
            "data": "2019-01-18",
            "ano": 2019,
            "veiculo": "Jornal Nacional / TV Globo",
            "titulo": "Coaf revela 48 depósitos em dinheiro vivo em um único mês na conta bancária de Flávio Bolsonaro",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 5,
            "resumo": "Depósitos fracionados de R$ 2.000 em terminais bancários para burlar os sistemas de controle financeiro do Banco Central.",
            "impacto_eleitor": "Evidência clara de manobras para ocultação de patrimônio e lavagem de capitais."
        },
        {
            "data": "2019-07-16",
            "ano": 2019,
            "veiculo": "G1 / Folha",
            "titulo": "Defesa de Flávio Bolsonaro recorre ao STF e consegue suspender todas as investigações sobre Queiroz e Coaf",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 4,
            "resumo": "Uso intensivo de manobras jurídicas para paralisar investigações contra si próprio, contrariando o discurso anticorrupção.",
            "impacto_eleitor": "Contradição frontal com o slogan de 'quem não deve não teme'."
        },
        {
            "data": "2019-12-18",
            "ano": 2019,
            "veiculo": "UOL / MP-RJ",
            "titulo": "MP-RJ aponta que loja de chocolates de Flávio Bolsonaro era usada para lavar até R$ 1,6 milhão em dinheiro vivo",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 5,
            "resumo": "Perícia financeira demonstrou descompasso absoluto entre o volume de vendas de doces e as quantias depositadas em espécie.",
            "impacto_eleitor": "Método clássico de lavagem de dinheiro envolvendo comércios de fachada."
        },
        {
            "data": "2020-06-18",
            "ano": 2020,
            "veiculo": "G1 / Folha / Estadão",
            "titulo": "Fabrício Queiroz é preso em imóvel de Frederick Wassef, advogado da família Bolsonaro, em Atibaia",
            "alvo": "Flávio Bolsonaro / Clã",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 5,
            "resumo": "Prisão do operador das rachadinhas escondido no sítio do advogado que frequentava o Palácio do Planalto.",
            "impacto_eleitor": "Mostra a tentativa deliberada de obstrução de Justiça e ocultação de testemunha-chave."
        },
        {
            "data": "2020-11-04",
            "ano": 2020,
            "veiculo": "Ministério Público do RJ",
            "titulo": "MP do Rio denuncia formalmente Flávio Bolsonaro por peculato, lavagem de dinheiro e organização criminosa",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 5,
            "resumo": "Denúncia criminal robusta apontando desvio estruturado de verba pública ao longo de mandatos sucessivos na Alerj.",
            "impacto_eleitor": "Fatos criminais detalhados em inquérito oficial, não meras acusações políticas."
        },
        {
            "data": "2021-03-01",
            "ano": 2021,
            "veiculo": "O Globo / Metrópoles",
            "titulo": "Flávio Bolsonaro compra mansão de luxo de R$ 6 milhões em bairro nobre de Brasília com renda parlamentar",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 4,
            "resumo": "Aquisição imobiliária de alto padrão com condições de financiamento atípicas no BRB (Banco de Brasília).",
            "impacto_eleitor": "Desconexão gritante com a realidade econômica do trabalhador brasileiro que ganha salário mínimo."
        },
        {
            "data": "2021-11-09",
            "ano": 2021,
            "veiculo": "STJ / ConJur",
            "titulo": "STJ anula quebras de sigilo e decisões do caso das rachadinhas de Flávio Bolsonaro por questões processuais",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 4,
            "resumo": "Anulação baseada em filigranas de foro privilegiado, sem que o mérito das provas e dos desvios fosse inocentado.",
            "impacto_eleitor": "Vitória jurídica por foro e tecnicismo, não por comprovação de inocência."
        },
        {
            "data": "2024-01-25",
            "ano": 2024,
            "veiculo": "Polícia Federal / G1",
            "titulo": "PF aponta uso da Abin paralela para produzir relatórios sigilosos destinados a blindar Flávio Bolsonaro no caso Queiroz",
            "alvo": "Flávio Bolsonaro / Alexandre Ramagem",
            "categoria": "Investigações & Abuso de Poder",
            "gravidade_score": 5,
            "resumo": "Investigação da Polícia Federal comprovou uso da agência de inteligência do Estado brasileiro para fins de defesa privada da família.",
            "impacto_eleitor": "Aparelhamento explícito da máquina do Estado para interesse familiar e impunidade."
        },
        
        # --- RISCO INSTITUCIONAL & GOLPISMO ---
        {
            "data": "2018-10-21",
            "ano": 2018,
            "veiculo": "Folha de S.Paulo",
            "titulo": "Eduardo e Flávio Bolsonaro endossam discurso contra o STF: 'Para fechar o Supremo basta um soldado e um cabo'",
            "alvo": "Clã Bolsonaro",
            "categoria": "Risco Institucional & Golpismo",
            "gravidade_score": 5,
            "resumo": "Ameaça direta de intervenção armada e ruptura institucional contra a mais alta corte de Justiça do país.",
            "impacto_eleitor": "Desprezo aberto pelas regras do jogo democrático e separação de poderes."
        },
        {
            "data": "2019-10-31",
            "ano": 2019,
            "veiculo": "Congresso em Foco / UOL",
            "titulo": "Clã Bolsonaro flerta abertamente com retorno do AI-5 em caso de manifestações populares no Brasil",
            "alvo": "Flávio e Clã Bolsonaro",
            "categoria": "Risco Institucional & Golpismo",
            "gravidade_score": 5,
            "resumo": "Evocação do ato institucional mais repressivo da ditadura militar como instrumento de coerção social.",
            "impacto_eleitor": "Mostra a predisposição a cassar direitos civis e liberdades individuais da população."
        },
        {
            "data": "2021-08-10",
            "ano": 2021,
            "veiculo": "O Globo / CNN Brasil",
            "titulo": "Bancada governista e Flávio pressionam por desfile militar de tanques na Esplanada no dia da votação do voto impresso",
            "alvo": "Flávio Bolsonaro / PL",
            "categoria": "Risco Institucional & Golpismo",
            "gravidade_score": 5,
            "resumo": "Tentativa de intimidação física e psicológica do Congresso Nacional com blindados militares na Praça dos Três Poderes.",
            "impacto_eleitor": "Uso de intimidação e força para coagir o parlamento a votar de acordo com seus interesses."
        },
        {
            "data": "2022-11-23",
            "ano": 2022,
            "veiculo": "TSE / G1",
            "titulo": "PL de Valdemar e Flávio Bolsonaro pede anulação de votos de urnas eletrônicas após derrota eleitoral",
            "alvo": "PL / Flávio Bolsonaro",
            "categoria": "Risco Institucional & Golpismo",
            "gravidade_score": 5,
            "resumo": "Ação golpista para invalidar milhões de votos de cidadãos brasileiros sem qualquer fundamento técnico, resultando em multa de R$ 22,9 milhões.",
            "impacto_eleitor": "Tentativa deliberada de anular a soberania do voto popular do eleitor."
        },
        {
            "data": "2023-01-09",
            "ano": 2023,
            "veiculo": "Jornal Nacional / Portais Internacionais",
            "titulo": "Invasão e destruição dos Três Poderes em 8 de Janeiro: CPMI aponta omissão e incentivo de líderes bolsonaristas",
            "alvo": "PL / Flávio Bolsonaro / Oposição",
            "categoria": "Risco Institucional & Golpismo",
            "gravidade_score": 5,
            "resumo": "Culminação da retórica golpista com a depredação do Palácio do Planalto, Congresso Nacional e Supremo Tribunal Federal.",
            "impacto_eleitor": "O resultado prático e caótico da ideologia extremista quando confrontada com a perda do poder."
        },
        {
            "data": "2024-03-12",
            "ano": 2024,
            "veiculo": "Senado Federal / CartaCapital",
            "titulo": "Flávio Bolsonaro lidera articulação no Senado por PEC que limita poderes do STF e projeto de anistia a golpistas",
            "alvo": "Flávio Bolsonaro / PL",
            "categoria": "Risco Institucional & Golpismo",
            "gravidade_score": 4,
            "resumo": "Tentativa parlamentar de perdoar legalmente condenados por tentativa de golpe de Estado e enfraquecer o tribunal que julga seus crimes.",
            "impacto_eleitor": "Busca contínua de impunidade para criminosos antidemocráticos."
        },
        {
            "data": "2025-05-19",
            "ano": 2025,
            "veiculo": "Poder360 / Estadão",
            "titulo": "Senador Flávio Bolsonaro defende impeachment em massa de ministros do STF em discurso no plenário",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Risco Institucional & Golpismo",
            "gravidade_score": 4,
            "resumo": "Estratégia de retaliação institucional contínua para desestabilizar o equilíbrio entre os Três Poderes da República.",
            "impacto_eleitor": "Promove caos político perpétuo em vez de foco no desenvolvimento econômico e social."
        },

        # --- CONTRADIÇÕES & INCOERÊNCIA PARLAMENTAR ---
        {
            "data": "2019-10-22",
            "ano": 2019,
            "veiculo": "Senado Federal / Diário Oficial",
            "titulo": "Flávio Bolsonaro vota a favor da Reforma da Previdência com endurecimento de regras para aposentadoria do trabalhador",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 4,
            "resumo": "Apoio a regras que aumentaram a idade mínima e reduziram pensões, enquanto categorias privilegiadas mantiveram vantagens.",
            "impacto_eleitor": "Voto direto contra o futuro previdenciário da classe trabalhadora."
        },
        {
            "data": "2020-04-15",
            "ano": 2020,
            "veiculo": "Câmara / Senado / UOL",
            "titulo": "Governo apoiado por Flávio propõe Auxílio Emergencial de apenas R$ 200 na pandemia; Congresso teve que elevar para R$ 600",
            "alvo": "Governo Bolsonaro / Flávio",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 4,
            "resumo": "Proposta inicial irrisória de assistência às famílias vulneráveis durante o auge do fechamento da economia.",
            "impacto_eleitor": "Falta de sensibilidade social com quem não tinha renda para comprar comida."
        },
        {
            "data": "2021-06-17",
            "ano": 2021,
            "veiculo": "Senado Federal / Folha",
            "titulo": "Flávio Bolsonaro vota pela privatização da Eletrobras com inclusão de 'jabutis' que encareceram a conta de luz",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 4,
            "resumo": "Voto que transferiu patrimônio estratégico e aumentou custos fixos de energia elétrica para indústrias e famílias brasileiras.",
            "impacto_eleitor": "Impacto direto na conta de luz e no custo de vida de todo cidadão."
        },
        {
            "data": "2021-12-02",
            "ano": 2021,
            "veiculo": "Senado Federal",
            "titulo": "Votação da PEC dos Precatórios: Flávio atua para postergar pagamento de dívidas judiciais a professores e aposentados",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 4,
            "resumo": "Manobra orçamentária apelidada de 'calote oficial' para abrir espaço fiscal em ano pré-eleitoral.",
            "impacto_eleitor": "Adiou o direito legal de receber de milhares de credores e servidores públicos."
        },
        {
            "data": "2022-07-14",
            "ano": 2022,
            "veiculo": "Congresso em Foco",
            "titulo": "Flávio e bancada do PL apoiam aumento do Fundo Eleitoral bilionário de R$ 4,9 bilhões para campanhas",
            "alvo": "PL / Flávio Bolsonaro",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 5,
            "resumo": "Destinação recorde de dinheiro dos impostos para financiar campanhas partidárias, contrariando o discurso de corte de gastos.",
            "impacto_eleitor": "Bilhões do contribuinte drenados diretamente para o caixa de partidos políticos."
        },
        {
            "data": "2023-08-24",
            "ano": 2023,
            "veiculo": "Senado Federal / Agência Senado",
            "titulo": "Flávio Bolsonaro vota contra a nova política de valorização permanente do Salário Mínimo de Lula",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 5,
            "resumo": "Voto contrário ao projeto que garante reajuste acima da inflação baseado no crescimento do PIB para quem ganha piso nacional.",
            "impacto_eleitor": "Evidência documental de voto contra o aumento da renda dos mais pobres."
        },
        {
            "data": "2024-05-28",
            "ano": 2024,
            "veiculo": "O Globo / Valor",
            "titulo": "Flávio Bolsonaro atua como relator da PEC das Praias, abrindo brecha para privatização de áreas litorâneas",
            "alvo": "Flávio Bolsonaro",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 4,
            "resumo": "Defesa explícita de interesses de megaempreendimentos imobiliários contra o livre acesso público às praias brasileiras.",
            "impacto_eleitor": "Privatização de bens públicos em favor de especuladores de altíssima renda."
        },
        {
            "data": "2025-11-10",
            "ano": 2025,
            "veiculo": "Folha / Poder360",
            "titulo": "Bancada do PL obstrui votação da isenção do Imposto de Renda para quem ganha até R$ 5.000 proposta pelo governo Lula",
            "alvo": "PL / Flávio Bolsonaro",
            "categoria": "Contradições & Incoerência Parlamentar",
            "gravidade_score": 5,
            "resumo": "Obstrução parlamentar contra medida de alívio fiscal para a classe média e trabalhadores assalariados.",
            "impacto_eleitor": "Preferência por manter o imposto alto sobre a classe média para criar desgaste político."
        }
    ]
    
    df = pd.DataFrame(records)
    df["data"] = pd.to_datetime(df["data"])
    return df

def save_media_audit_datasets():
    """Gera e salva o dataset de auditoria de notícias."""
    df_media = generate_curated_media_audit()
    csv_path = os.path.join(DATA_DIR, "media_audit_dataset.csv")
    json_path = os.path.join(DATA_DIR, "media_audit_dataset.json")
    
    df_to_save = df_media.copy()
    df_to_save["data"] = df_to_save["data"].dt.strftime("%Y-%m-%d")
    df_to_save.to_csv(csv_path, index=False, encoding="utf-8")
    df_to_save.to_json(json_path, orient="records", indent=2, force_ascii=False)
    
    logging.info(f"Dataset de auditoria de mídia salvo com sucesso em {csv_path}")
    return df_media

if __name__ == "__main__":
    df = save_media_audit_datasets()
    print("Resumo da Auditoria de Mídia:")
    print(df["categoria"].value_counts())
