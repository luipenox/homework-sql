import streamlit as st
import pandas as pd

from utils.connection import get_connection

examples = [
    {
        'level': 'Začátečník',
        'title': '01. Všechny záznamy zákazníků bez omezení',
        'description': 'Vypište všechny záznamy z tabulky `customers`.',
        'tips':
            """
            Pro výpis celé tabulky, u kterého neomezujeme ani sloupce, ani řádky, využijeme jednoduše konstrukci `SELECT * FROM tabulka`.            
            """,
        'sql': '''
               SELECT *
               FROM customers;
               '''
    },
    {
        'level': 'Začátečník',
        'title': '02. Vybrané sloupce všech zákazníků',
        'description': 'Vypište pouze sloupec se jménem a telefonním číslem zákazníka z tabulky `customers`.',
        'tips':
            """
            Pro výpis jednoho, nebo více sloupců, stačí tyto sloupce výjmenovat. Tedy využijeme konstrukci `SELECT sloupec_1, sloupec_2 FROM tabulka`.            
            """,
        'sql': '''
               SELECT customerName, phone
               FROM customers;
               '''
    },
    {
        'level': 'Začátečník',
        'title': '03. Jednoduchá podmínka',
        'description': 'Vypište všechny zákazníky z tabulky `customers`, kteří jsou z Francie.',
        'tips':
            """
- Pro omezení výpisu dat použijeme klíčové slovo WHERE, za které uvedene požadovanou podmínku. 
- Tedy využijeme konstrukci `SELECT * FROM tabulka WHERE sloupec = 'hodnota'`.
- Pro uvození textu musíme využít jednodchou úvozovku (`'`). 
- Je také nutné zjistit název sloupce a hodnotu, které chceme v podmínce použít (záznamy jsou zjevně anglicky).           
            """,
        'sql': '''
               SELECT *
               FROM customers
               WHERE country = 'France';
               '''
    },
    {
        'level': 'Začátečník',
        'title': '04. Jednoduchá podmínka',
        'description': 'Vypište všechny zákazníky z tabulky `customers`, kteří jsou z Francie.',
        'tips':
            """
- Pro omezení výpisu dat použijeme klíčové slovo WHERE, za které uvedene požadovanou podmínku. 
- Tedy využijeme konstrukci `SELECT * FROM tabulka WHERE sloupec = 'hodnota'`.
- Pro uvození textu musíme využít jednodchou úvozovku (`'`). 
- Je také nutné zjistit název sloupce a hodnotu, které chceme v podmínce použít (záznamy jsou zjevně anglicky).           
            """,
        'sql': '''
               SELECT *
               FROM customers
               WHERE country = 'France';
               '''
    },
{
        'level': 'Začátečník',
        'title': '05. Řazení výsledků',
        'description': 'Vypište všechny zákazníky z tabulky `customers` seřazené podle jména.',
        'tips':
            """
- Pro seřazení výsledků použijeme klíčové slovo ORDER BY následované názvem sloupce.
- Výchozí řazení je vzestupné (ASC), pro sestupné řazení použijeme DESC.
- Tedy využijeme konstrukci `SELECT * FROM tabulka ORDER BY sloupec`.
            """,
        'sql': '''
               SELECT *
               FROM customers
               ORDER BY customerName;
               '''
    },
    {
        'level': 'Začátečník',
        'title': '06. Omezení počtu záznamů',
        'description': 'Vypište prvních 5 zákazníků z tabulky `customers`.',
        'tips':
            """
- Pro omezení počtu vrácených záznamů použijeme klíčové slovo LIMIT.
- Tedy využijeme konstrukci `SELECT * FROM tabulka LIMIT počet`.
- LIMIT se typicky používá v kombinaci s ORDER BY pro získání např. Top N záznamů.
            """,
        'sql': '''
               SELECT *
               FROM customers
               LIMIT 5;
               '''
    },
    {
        'level': 'Začátečník',
        'title': '07. Podmínka s operátorem LIKE',
        'description': 'Vypište všechny zákazníky z tabulky `customers`, jejichž název začíná na písmeno "A".',
        'tips':
            """
- Pro vyhledávání podle vzoru použijeme operátor LIKE.
- Symbol % zastupuje libovolný počet znaků.
- Symbol _ zastupuje právě jeden znak.
- Tedy využijeme konstrukci `SELECT * FROM tabulka WHERE sloupec LIKE 'vzor'`.
            """,
        'sql': '''
               SELECT *
               FROM customers
               WHERE customerName LIKE 'A%';
               '''
    },
    {
        'level': 'Začátečník',
        'title': '08. Složená podmínka s AND',
        'description': 'Vypište všechny zákazníky z tabulky `customers`, kteří jsou z USA a jejich město je New York.',
        'tips':
            """
- Pro kombinaci více podmínek použijeme logické operátory AND nebo OR.
- Podmínky spojené operátorem AND musí být splněny všechny najednou.
- Tedy využijeme konstrukci `SELECT * FROM tabulka WHERE podmínka1 AND podmínka2`.
            """,
        'sql': '''
               SELECT *
               FROM customers
               WHERE country = 'USA' AND city = 'New York';
               '''
    },
{
        'level': 'Začátečník',
        'title': '09. Složená podmínka s OR',
        'description': 'Vypište všechny zákazníky z tabulky `customers`, kteří jsou buď z Francie nebo z Německa.',
        'tips':
            """
- Pro alternativní podmínky použijeme operátor OR.
- Stačí, když je splněna alespoň jedna z podmínek.
- Tedy využijeme konstrukci `SELECT * FROM tabulka WHERE podmínka1 OR podmínka2`.
- Pozor na správné použití závorek při kombinaci AND a OR.
            """,
        'sql': '''
               SELECT *
               FROM customers
               WHERE country = 'France' OR country = 'Germany';
               '''
    },
    {
        'level': 'Začátečník',
        'title': '10. Operátor IN',
        'description': 'Vypište všechny zákazníky z tabulky `customers`, kteří jsou z některé ze zemí: Francie, Německo nebo Španělsko.',
        'tips':
            """
- Pro testování, zda hodnota patří do množiny hodnot, použijeme operátor IN.
- Je to kratší zápis než několik podmínek spojených pomocí OR.
- Tedy využijeme konstrukci `SELECT * FROM tabulka WHERE sloupec IN (hodnota1, hodnota2, ...)`.
            """,
        'sql': '''
               SELECT *
               FROM customers
               WHERE country IN ('France', 'Germany', 'Spain');
               '''
    },
    {
        'level': 'Začátečník',
        'title': '11. Seřazení podle více sloupců',
        'description': 'Vypište všechny zákazníky z tabulky `customers` seřazené nejprve podle země a v rámci země podle jména.',
        'tips':
            """
- Pro řazení podle více sloupců je uvedeme za ORDER BY oddělené čárkami.
- Pořadí sloupců určuje prioritu řazení.
- U každého sloupce můžeme určit směr řazení (ASC nebo DESC).
- Tedy využijeme konstrukci `SELECT * FROM tabulka ORDER BY sloupec1, sloupec2`.
            """,
        'sql': '''
               SELECT *
               FROM customers
               ORDER BY country, customerName;
               '''
    },
    {
        'level': 'Začátečník',
        'title': '12. Vyloučení duplicit',
        'description': 'Vypište seznam všech zemí z tabulky `customers` bez opakování.',
        'tips':
            """
- Pro odstranění duplicitních záznamů použijeme klíčové slovo DISTINCT.
- DISTINCT se uvádí hned za SELECT.
- Tedy využijeme konstrukci `SELECT DISTINCT sloupec FROM tabulka`.
- Můžeme použít i více sloupců pro unique kombinace hodnot.
            """,
        'sql': '''
               SELECT DISTINCT country
               FROM customers
               ORDER BY country;
               '''
    },
    {
        'level': 'Začátečník',
        'title': '13. Operátor BETWEEN',
        'description': 'Vypište všechny objednávky z tabulky `orders`, které byly vytvořeny v roce 2003.',
        'tips':
            """
- Pro testování rozsahu hodnot použijeme operátor BETWEEN.
- BETWEEN je včetně hraničních hodnot.
- Lze použít pro čísla, data i text.
- Tedy využijeme konstrukci `SELECT * FROM tabulka WHERE sloupec BETWEEN hodnota1 AND hodnota2`.
            """,
        'sql': '''
               SELECT *
               FROM orders
               WHERE orderDate BETWEEN '2003-01-01' AND '2003-12-31';
               '''
    },
]


st.title('Jednoduché příklady')

example_titles = [example['title'] for example in examples]
selected_title = st.selectbox("Vyberte příklad:", options=example_titles)

st.markdown('## Zadání')
st.write(f"**{examples[example_titles.index(selected_title)]['description']}**")

sql_code = examples[example_titles.index(selected_title)]['sql']

st.markdown('### Přepínače')
col1, col2, col3 = st.columns(3)
with col1:
    show_tips = st.toggle("Zobrazit nápovědu")

with col2:
    show_code = st.toggle("Zobrazit řešení")

with col3:
    show_data = st.toggle("Zobrazit data")

st.markdown('## Nápověda')
if show_tips:
    st.markdown(examples[example_titles.index(selected_title)]['tips'])
else:
    st.markdown("**... skryto ...**")

st.markdown('## Řešení')
if show_code:
    st.code(sql_code, language="sql")
else:
    st.markdown("**... skryto ...**")

st.markdown('## Výsledná data')
if show_data:
    df = pd.read_sql(sql_code, get_connection())
    selected_code = st.dataframe(df)
    st.write(f"Celkový počet záznamů: `{df.shape[0]}`")
else:
    st.markdown("**... skryto ...**")
