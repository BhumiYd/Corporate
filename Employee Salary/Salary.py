import sqlite3
from pathlib import Path
import pandas as pd

def query_database(db_path: Path, query: str) -> pd.DataFrame:
    """Execute SQL query and return results as DataFrame."""
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(query, conn)

# File naam ab "employee.db" (naya naam)
db = Path('C:/Users/manvi/Downloads/sqlite-tools-win-x64-3530400/employee.db')

df = query_database(db, '''
    SELECT department, ROUND(AVG(salary)) AS avg_salary
    FROM employees
    GROUP BY department
    ORDER BY department ASC
''')

print(df)