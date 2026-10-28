import sqlite3

def login_vulneravel(username, password):
    # ATENÇÃO: Código vulnerável a SQL Injection para fins de estudo em laboratório!
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Interpolação direta de strings (Vulnerável)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[DEBUG] Executando query: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

def login_seguro(username, password):
    # Código corrigido com consulta parametrizada (Prepared Statement)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

if __name__ == "__main__":
    print("Módulo de autenticação do laboratório carregado.")
