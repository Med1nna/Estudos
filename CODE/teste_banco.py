import pyodbc

# Formato correto para pyodbc usando o driver instalado na VM:
CONN_STR = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=sqldev.timbrotrading.com;"
    "DATABASE=dbdev_TTMANAGER;"
    "UID=dbUserAutomation;"
    "PWD=k$7pmTg@F7;"
)

try:
    with pyodbc.connect(CONN_STR, timeout=5) as conn:
        print("Conexão OK!")
except Exception as e:
    print(f"Erro ao conectar: {e}")