"""
Publicador e Atualizador do Dossiê Completo no Telegraph (telegra.ph)
Gera uma página abrangente, altamente documentada e com dezenas de links diretos
e auditáveis para todas as 24 ocorrências factuais, séries do BACEN/IBGE e inquéritos.
"""

import os
import json
import requests

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

TELEGRAPH_TOKEN = "3ae649f00561247f6f0383afbefe76880a6ffb47275f1d5273be27061721"
PAGE_PATH = "Auditoria-2026-Fontes-e-Documentos-Oficiais-10-09"
PAGE_TITLE = "Auditoria 2026: Dossiê Completo de Fontes, Documentos e Código Aberto"
AUTHOR_NAME = "Matheus Campos (@matheuscampos-it)"
AUTHOR_URL = "https://github.com/matheuscampos-it/auditoria-eleicoes-2026"

def build_telegraph_nodes():
    nodes = [
        {
            "tag": "p",
            "children": [
                "Este dossiê reúne a totalidade dos links oficiais, decisões judiciais, inquéritos da Polícia Federal, certidões do TSE/STF, séries temporais do Banco Central e reportagens investigativas consolidadas (sem intermediários de busca) que embasam a auditoria factual independente do 2º turno das Eleições Presidenciais 2026. Todos os dados são públicos, verificáveis e 100% auditáveis."
            ]
        },
        {"tag": "hr"},
        {
            "tag": "h3",
            "children": ["🚀 HUBS CENTRAIS & AUDITORIA AO VIVO"]
        },
        {
            "tag": "p",
            "children": [
                "Você pode auditar todos os dados, códigos e gráficos interativos nos canais oficiais do projeto:",
                {"tag": "br"},
                {"tag": "b", "children": ["• Painel Analítico Interativo (Web Live): "]},
                {
                    "tag": "a",
                    "attrs": {"href": "https://matheuscampos-it.github.io/auditoria-eleicoes-2026/dashboard.html", "target": "_blank"},
                    "children": ["https://matheuscampos-it.github.io/auditoria-eleicoes-2026/dashboard.html"]
                },
                {"tag": "br"},
                {"tag": "b", "children": ["• Agregador Linktree Central (GitHub Pages): "]},
                {
                    "tag": "a",
                    "attrs": {"href": "https://matheuscampos-it.github.io/auditoria-eleicoes-2026/", "target": "_blank"},
                    "children": ["https://matheuscampos-it.github.io/auditoria-eleicoes-2026/"]
                },
                {"tag": "br"},
                {"tag": "b", "children": ["• Código Aberto & Banco DuckDB no GitHub: "]},
                {
                    "tag": "a",
                    "attrs": {"href": "https://github.com/matheuscampos-it/auditoria-eleicoes-2026", "target": "_blank"},
                    "children": ["https://github.com/matheuscampos-it/auditoria-eleicoes-2026"]
                }
            ]
        },
        {"tag": "hr"},

        # SEÇÃO 1
        {
            "tag": "h3",
            "children": ["1. VOTAÇÕES PARLAMENTARES & O IMPACTO NO SEU BOLSO"]
        },
        {
            "tag": "p",
            "children": [
                "O histórico real de votações nominais de Flávio Bolsonaro e de sua bancada no Congresso Nacional demonstra alinhamento sistemático contra o trabalhador assalariado e a favor de privilégios corporativos:"
            ]
        },
        {
            "tag": "ul",
            "children": [
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Aumento Real Permanente do Salário Mínimo (MP 1172/2023 - Lei 14.663/2023): "]},
                        "Flávio Bolsonaro e o PL votaram CONTRA a nova fórmula que garante reajuste acima da inflação pelo PIB. ",
                        {"tag": "a", "attrs": {"href": "https://www12.senado.leg.br/noticias/materias/2023/08/24/salario-minimo-de-r-1-320-e-correcao-do-ir-vao-a-sancao", "target": "_blank"}, "children": ["Agência Senado"]},
                        " | ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/congresso/relator-inclui-reajuste-do-salario-minimo-e-correcao-do-ir-na-mesma-mp/", "target": "_blank"}, "children": ["Reportagem Poder360"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Privatização da Eletrobras e Conta de Luz Mais Cara (MP 1031/2021): "]},
                        "Flávio votou SIM pela venda da estatal com emendas parlamentares ('jabutis') obrigando a contratação cara de usinas térmicas a gás. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/congresso/saiba-como-votou-cada-partido-e-senador-na-mp-da-capitalizacao-da-eletrobras/", "target": "_blank"}, "children": ["Painel de Votação Poder360"]},
                        " | ",
                        {"tag": "a", "attrs": {"href": "https://www25.senado.leg.br/web/atividade/materias/-/materia/148419", "target": "_blank"}, "children": ["Ficha Oficial MP 1031 Senado"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Relatoria da PEC das Praias (PEC 3/2022): "]},
                        "Flávio atuou como relator da proposta na CCJ do Senado que transfere terrenos de marinha do controle público para entes privados e grandes resorts. ",
                        {"tag": "a", "attrs": {"href": "https://www25.senado.leg.br/web/atividade/materias/-/materia/151923", "target": "_blank"}, "children": ["Tramitação no Senado"]},
                        " | ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/poder-congresso/ccj-do-senado-faz-audiencia-sobre-pec-que-trata-de-terrenos-de-marinha/", "target": "_blank"}, "children": ["Cobertura Poder360"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Obstrução contra Isenção do IR até R$ 5.000: "]},
                        "Bancada do PL tentou barrar e obstruir no Congresso a isenção de Imposto de Renda proposta para trabalhadores com renda mensal de até 5 salários mínimos. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/poder-congresso/493-deputados-votaram-a-urgencia-do-projeto-de-isencao-do-ir-ate-r-5-000/", "target": "_blank"}, "children": ["Votação no Poder360"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["PEC dos Precatórios (Calote Institucional): "]},
                        "Flávio e aliados articularam o adiamento do pagamento de dívidas judiciais de aposentados e professores para abrir espaço fiscal emergencial. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/congresso/senado-aprova-pec-dos-precatorios-em-2o-turno-proposta-vai-a-camara/", "target": "_blank"}, "children": ["Aprovação no Senado - Poder360"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Reforma da Previdência (PEC 6/2019): "]},
                        "Voto a favor do aumento da idade mínima e do tempo de contribuição para aposentadoria do trabalhador brasileiro. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/congresso/congresso-fiscal-saiba-como-votou-cada-senador-na-reforma-da-previdencia/", "target": "_blank"}, "children": ["Painel de Votos Poder360"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Aumento do Fundo Eleitoral Bilionário: "]},
                        "Apoio parlamentar para inflar os repasses de recursos públicos para campanhas eleitorais para quase R$ 5 bilhões. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/justica/stf-forma-maioria-para-manter-fundo-eleitoral-de-r-49-bi/", "target": "_blank"}, "children": ["Decisão STF / Poder360"]}
                    ]
                }
            ]
        },
        {"tag": "hr"},

        # SEÇÃO 2
        {
            "tag": "h3",
            "children": ["2. PATRIMÔNIO INCOMPATÍVEL, DINHEIRO VIVO & RACHADINHAS"]
        },
        {
            "tag": "p",
            "children": [
                "Investigações financeiras e perícias contábeis oficiais do Ministério Público do Estado do Rio de Janeiro (MP-RJ) e relatórios de inteligência do Coaf:"
            ]
        },
        {
            "tag": "ul",
            "children": [
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Mansão de R$ 6 Milhões no Lago Sul de Brasília: "]},
                        "Compra e financiamento atípico em banco estatal (BRB) de imóvel de alto luxo com renda parlamentar incompatível. ",
                        {"tag": "a", "attrs": {"href": "https://www.cnnbrasil.com.br/politica/flavio-bolsonaro-compra-mansao-avaliada-em-r-6-milhoes-em-brasilia/", "target": "_blank"}, "children": ["CNN Brasil"]},
                        " | ",
                        {"tag": "a", "attrs": {"href": "https://www1.folha.uol.com.br/poder/2021/03/flavio-bolsonaro-compra-mansao-de-r-6-milhoes-em-brasilia.shtml", "target": "_blank"}, "children": ["Folha de S.Paulo"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["48 Depósitos em Dinheiro Vivo na Alerj (Coaf): "]},
                        "Fracionamento sistemático de depósitos de R$ 2.000 em espécie em caixas eletrônicos para burlar alarmes antiburlas do Banco Central. ",
                        {"tag": "a", "attrs": {"href": "https://www1.folha.uol.com.br/poder/2019/01/coaf-aponta-48-depositos-suspeitos-na-conta-de-flavio-bolsonaro.shtml", "target": "_blank"}, "children": ["Folha de S.Paulo / Coaf"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Movimentação Atípica de R$ 1,2 Milhão de Fabrício Queiroz: "]},
                        "Relatório inaugural do Coaf revelando repasses de salários de assessores para o operador de Flávio. ",
                        {"tag": "a", "attrs": {"href": "https://www1.folha.uol.com.br/poder/2018/12/coaf-aponta-movimentacao-atipica-de-ex-assessor-de-flavio-bolsonaro.shtml", "target": "_blank"}, "children": ["Folha de S.Paulo"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Lavagem de R$ 1,6 Milhão na Loja de Chocolates: "]},
                        "Perícia criminal do MP-RJ demonstrando total descompasso entre a venda física de doces e os depósitos massivos de notas de dinheiro vivo. ",
                        {"tag": "a", "attrs": {"href": "https://www.estadao.com.br/politica/investigacao-apura-se-loja-de-flavio-bolsonaro-lavou-r-2-1-milhoes/", "target": "_blank"}, "children": ["Estadão / MP-RJ"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Prisão de Queiroz no Sítio do Advogado da Família: "]},
                        "Fabrício Queiroz foi localizado e preso pela polícia em Atibaia (SP) escondido no imóvel de Frederick Wassef. ",
                        {"tag": "a", "attrs": {"href": "https://www.estadao.com.br/politica/ex-assessor-de-flavio-bolsonaro-queiroz-e-preso-no-interior-de-sp-diz-tv/", "target": "_blank"}, "children": ["Estadão"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Denúncia Criminal por Organização Criminosa e Peculato: "]},
                        "Denúncia formalizada pela Procuradoria-Geral de Justiça do Rio de Janeiro apontando estrutura permanente de desvio de dinheiro público. ",
                        {"tag": "a", "attrs": {"href": "https://www.cnnbrasil.com.br/politica/mp-denuncia-flavio-bolsonaro-e-fabricio-queiroz/", "target": "_blank"}, "children": ["CNN Brasil"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Manobras para Anulação de Provas no Judiciário: "]},
                        "Série de recursos para anular provas técnicas do Coaf e paralisar investigações contra si próprio. ",
                        {"tag": "a", "attrs": {"href": "https://www.estadao.com.br/politica/supremo-manda-suspender-investigacao-de-queiroz-e-outros-servidores-diz-mp/", "target": "_blank"}, "children": ["Estadão"]},
                        " | ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/justica/stj-atende-flavio-bolsonaro-e-anula-todas-as-decisoes-do-caso-das-rachadinhas/", "target": "_blank"}, "children": ["Poder360"]}
                    ]
                }
            ]
        },
        {"tag": "hr"},

        # SEÇÃO 3
        {
            "tag": "h3",
            "children": ["3. APARELHAMENTO DO ESTADO & ESCÂNDALO DA ABIN PARALELA"]
        },
        {
            "tag": "p",
            "children": [
                "Investigações da Polícia Federal autorizadas pelo Supremo Tribunal Federal (Inquérito 4.954/DF - Operação Vigilância Aproximada):"
            ]
        },
        {
            "tag": "ul",
            "children": [
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Espionagem Clandestina de Mais de 30 Mil Celulares: "]},
                        "Uso do software invasivo FirstMile para monitorar geolocalização e rotinas de adversários políticos, juízes e jornalistas sem autorização judicial. ",
                        {"tag": "a", "attrs": {"href": "https://agenciabrasil.ebc.com.br/geral/noticia/2024-01/pf-cumpre-mandados-em-operacao-que-investiga-abin-paralela", "target": "_blank"}, "children": ["Agência Brasil / PF"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Abin Usada para Produzir Relatórios Secretos para Flávio: "]},
                        "PF comprovou que agentes clandestinos da Abin foram acionados para criar relatórios para anular a apuração de desvios na Alerj. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/poder-justica/abin-atuou-ilegalmente-em-favor-de-renan-e-flavio-bolsonaro-diz-pf/", "target": "_blank"}, "children": ["Poder360 / PF"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Gravação de Reunião no Palácio do Planalto: "]},
                        "Áudio de 1h apreendido pela PF com o diretor da Abin (Alexandre Ramagem), o presidente e advogadas de Flávio traçando planos de ação contra auditores fiscais. ",
                        {"tag": "a", "attrs": {"href": "https://www.cnnbrasil.com.br/politica/integra-gravacao-bolsonaro-ramagem/", "target": "_blank"}, "children": ["Íntegra do Áudio na CNN Brasil"]}
                    ]
                }
            ]
        },
        {"tag": "hr"},

        # SEÇÃO 4
        {
            "tag": "h3",
            "children": ["4. AMEAÇAS À DEMOCRACIA, SOBERANIA & DIREITOS DO CIDADÃO"]
        },
        {
            "tag": "p",
            "children": [
                "Documentação formal de atentados à soberania nacional, aos direitos do consumidor e às regras do Estado Democrático de Direito:"
            ]
        },
        {
            "tag": "ul",
            "children": [
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Ação para Anular 60% das Urnas Eletrônicas e Multa de R$ 22,9 Milhões (TSE): "]},
                        "O PL de Flávio tentou anular mais de 67 milhões de votos após a derrota no 2º turno sem apresentar provas. Condenação por litigância de má-fé confirmada pelo TSE. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/justica/tse-mantem-multa-de-r-229-milhoes-ao-pl/", "target": "_blank"}, "children": ["Poder360 / TSE"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Comitiva nos EUA Articulando Sanções e Tarifas contra o Brasil: "]},
                        "Deputados do PL viajaram a Washington para pedir a parlamentares trumpistas sanções e tarifas punitivas contra produtos e empresas brasileiras. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/congresso/nos-eua-deputados-do-pl-entregam-carta-sobre-censura-no-brasil/", "target": "_blank"}, "children": ["Poder360"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Ameaças ao Pix e Pressão por Tarifação Bancária: "]},
                        "Pressões de setores aliados e desinformação para tentar taxar as operações do Pix, garantido como infraestrutura 100% pública e gratuita pelo Banco Central. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/economia/nao-vamos-taxar-o-pix-diz-campos-neto/", "target": "_blank"}, "children": ["Banco Central / Poder360"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Desfile Inédito de Blindados na Esplanada durante Votação: "]},
                        "Passagem de blindados e veículos militares emitindo fumaça em frente ao Congresso Nacional em dia de votação da PEC do Voto Impresso em 2021. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/governo/veja-fotos-e-videos-do-desfile-militar-da-marinha-na-praca-dos-tres-poderes/", "target": "_blank"}, "children": ["Poder360 / Imagens"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Articulação no Congresso por Anistia aos Invasores de 8 de Janeiro: "]},
                        "Flávio Bolsonaro e cúpula do PL liderando o projeto de lei para perdoar crimes de invasão e depredação das sedes dos Três Poderes. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/poder-congresso/lider-do-pl-restringira-projeto-da-anistia-a-depredacao-no-8-de-janeiro/", "target": "_blank"}, "children": ["Poder360 / Senado"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Discursos Explícitos de Novo AI-5 e Fechamento do STF: "]},
                        "Declarações de integrantes do núcleo bolsonarista defendendo o fechamento do STF com 'um cabo e um soldado' e a reedição do AI-5 contra oposicionistas. ",
                        {"tag": "a", "attrs": {"href": "https://www.poder360.com.br/eleicoes/filho-de-bolsonaro-diz-que-basta-1-soldado-e-1-cabo-para-fechar-o-stf-assista/", "target": "_blank"}, "children": ["Poder360 / Vídeo"]}
                    ]
                }
            ]
        },
        {"tag": "hr"},

        # SEÇÃO 5
        {
            "tag": "h3",
            "children": ["5. DADOS MACROECONÔMICOS OFICIAIS (GOVERNO LULA: 2002 A 2026)"]
        },
        {
            "tag": "p",
            "children": [
                "Bases de dados oficiais e séries históricas continuadas do Estado brasileiro, disponíveis publicamente para conferência matemática:"
            ]
        },
        {
            "tag": "ul",
            "children": [
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Banco Central do Brasil - Salário Mínimo Real (Série SGS 1619): "]},
                        "Comprova o ganho real de poder de compra acumulado de +84% nos governos Lula, frente à estagnação salarial de gestões anteriores. ",
                        {"tag": "a", "attrs": {"href": "https://www.bcb.gov.br/", "target": "_blank"}, "children": ["Portal Oficial BACEN"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Banco Central do Brasil - Reservas Internacionais (Série SGS 3546): "]},
                        "Acúmulo de mais de US$ 365 bilhões em reservas soberanas que impedem calotes e crises cambiais no país. ",
                        {"tag": "a", "attrs": {"href": "https://www.bcb.gov.br/estabilidadefinanceira/reservasinternacionais", "target": "_blank"}, "children": ["Relatório de Reservas BACEN"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["IBGE - Taxa de Desocupação (PNAD Contínua): "]},
                        "Redução sistemática do desemprego para 6,2%, um dos menores patamares da série histórica nacional. ",
                        {"tag": "a", "attrs": {"href": "https://www.ibge.gov.br/", "target": "_blank"}, "children": ["IBGE PNAD Contínua"]}
                    ]
                },
                {
                    "tag": "li",
                    "children": [
                        {"tag": "b", "children": ["Dieese - Nota Técnica sobre Valorização Salarial: "]},
                        "Estudo técnico comprovando o impacto direto do aumento real do piso sobre o comércio e a massa salarial das famílias. ",
                        {"tag": "a", "attrs": {"href": "https://www.dieese.org.br/notatecnica/2023/notaTec273SalarioMinimo.html", "target": "_blank"}, "children": ["Nota Técnica Dieese 273"]}
                    ]
                }
            ]
        },
        {"tag": "hr"},

        # SEÇÃO 6
        {
            "tag": "h3",
            "children": ["6. REPRODUTIBILIDADE & CÓDIGO ABERTO NO GITHUB"]
        },
        {
            "tag": "p",
            "children": [
                "Para que qualquer cidadão, pesquisador ou estudante possa auditar estas análises de forma totalmente independente:",
                {"tag": "br"},
                {"tag": "b", "children": ["1. "]}, "Clone o repositório no seu computador: ",
                {"tag": "code", "children": ["git clone https://github.com/matheuscampos-it/auditoria-eleicoes-2026.git"]},
                {"tag": "br"},
                {"tag": "b", "children": ["2. "]}, "Instale os pacotes: ",
                {"tag": "code", "children": ["pip install -r requirements.txt"]},
                {"tag": "br"},
                {"tag": "b", "children": ["3. "]}, "Execute o dashboard local: ",
                {"tag": "code", "children": ["streamlit run app/main.py"]}
            ]
        },
        {"tag": "hr"},
        {
            "tag": "p",
            "children": [
                {"tag": "i", "children": ["Projeto de interesse público, baseado exclusivamente em fontes primárias do Estado e investigações jornalísticas comprovadas. Desenvolvido por Matheus Campos."]}
            ]
        }
    ]
    return nodes

def publish():
    content_nodes = build_telegraph_nodes()
    
    url = "https://api.telegra.ph/editPage"
    payload = {
        "access_token": TELEGRAPH_TOKEN,
        "path": PAGE_PATH,
        "title": PAGE_TITLE,
        "author_name": AUTHOR_NAME,
        "author_url": AUTHOR_URL,
        "content": content_nodes,
        "return_content": True
    }
    
    response = requests.post(url, json=payload, timeout=15)
    data = response.json()
    
    if not data.get("ok"):
        print("Erro ao atualizar Telegraph:", data)
        return False
        
    result = data.get("result", {})
    page_url = result.get("url")
    print(f"[OK] Dossie Telegraph atualizado com sucesso!")
    print(f"[URL] {page_url}")
    print(f"[NOS] Total de nos no documento: {len(result.get('content', []))}")
    
    # Salvar cópia local do resultado
    save_path = os.path.join(DATA_DIR, "telegraph_content.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[ARQUIVO] Copia salva em {save_path}")
    return True

if __name__ == "__main__":
    publish()
