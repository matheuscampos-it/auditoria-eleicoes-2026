"""
Integração e Armazenamento Analítico com DuckDB
Permite que os dados consolidados dos dois pilares sejam consultados via SQL nativo
com alta performance.
"""

import os
import duckdb
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "database.duckdb")

def init_duckdb():
    """Carrega os datasets CSV no DuckDB e cria tabelas e views analíticas."""
    conn = duckdb.connect(DB_PATH)
    
    macro_csv = os.path.join(DATA_DIR, "macro_series_historica.csv")
    media_csv = os.path.join(DATA_DIR, "media_audit_dataset.csv")
    
    if os.path.exists(macro_csv):
        conn.execute(f"""
            CREATE OR REPLACE TABLE macro_series AS 
            SELECT * FROM read_csv_auto('{macro_csv.replace(os.sep, "/")}');
        """)
        
    if os.path.exists(media_csv):
        conn.execute(f"""
            CREATE OR REPLACE TABLE media_audit AS 
            SELECT * FROM read_csv_auto('{media_csv.replace(os.sep, "/")}');
        """)
        
    # View analítica: Comparativo de médias macro por bloco de governo
    conn.execute("""
        CREATE OR REPLACE VIEW view_medias_por_bloco AS
        SELECT 
            bloco_politico,
            ROUND(AVG(desemprego_pct), 2) AS desemprego_medio_pct,
            ROUND(AVG(inflacao_ipca_pct), 2) AS inflacao_media_pct,
            ROUND(AVG(salario_minimo_real_indice), 2) AS indice_salario_real_medio,
            ROUND(MAX(reservas_usd_bi), 2) AS pico_reservas_usd_bi
        FROM macro_series
        GROUP BY bloco_politico
        ORDER BY indice_salario_real_medio DESC;
    """)
    
    # View analítica: Resumo de gravidade de escândalos por categoria
    conn.execute("""
        CREATE OR REPLACE VIEW view_resumo_risco_media AS
        SELECT 
            categoria,
            COUNT(*) AS total_noticias,
            ROUND(AVG(gravidade_score), 2) AS gravidade_media
        FROM media_audit
        GROUP BY categoria
        ORDER BY total_noticias DESC;
    """)
    
    conn.close()
    print(f"Banco DuckDB inicializado com sucesso em: {DB_PATH}")

def query_duckdb(sql_query: str) -> pd.DataFrame:
    """Executa uma query SQL arbitrária no DuckDB e retorna DataFrame."""
    conn = duckdb.connect(DB_PATH, read_only=True)
    df = conn.execute(sql_query).fetchdf()
    conn.close()
    return df

if __name__ == "__main__":
    init_duckdb()
