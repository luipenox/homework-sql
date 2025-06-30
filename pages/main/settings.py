import streamlit as st

st.title('Připojení k databázi classicmodels')

st.markdown("""
#### Údaje pro připojení k DB classicmodels na ČVUT (MariaDB)

| Parametr | Hodnota |
|----------|---------|
| Host | `relational.fel.cvut.cz` |
| Port | `3306` |
| Databáze | `classicmodels` |
| Uživatel | `guest` |
| Heslo | `ctu-relational` |

""")

st.markdown("""
### Poznámky
- Uživatel má práva pouze pro čtení dat
""")