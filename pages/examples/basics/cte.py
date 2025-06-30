from functions import load_tasks

examples = {
    '01. Jednoduchý CTE': {
        'level': 'Začátečník',
        'title': '01. Jednoduchý CTE',
        'instructions': '''Vytvořte CTE s názvem `francouzsti_zakaznici`, který bude obsahovat všechny zákazníky z Francie,
        a poté z něj vypište všechny záznamy.''',
        'hint': '''
        - CTE začíná klíčovým slovem WITH následovaným názvem.
        - Po AS následuje poddotaz v závorkách.
        - CTE můžete použít jako běžnou tabulku.
        ''',
        'sql': '''
               WITH francouzsti_zakaznici AS (
                   SELECT *
                   FROM customers
                   WHERE country = 'France'
               )
               SELECT *
               FROM francouzsti_zakaznici;
               '''
    },
    '02. CTE s přejmenovanými sloupci': {
        'level': 'Začátečník',
        'title': '02. CTE s přejmenovanými sloupci',
        'instructions': '''Vytvořte CTE, který bude obsahovat jména a emaily zaměstnanců s českými názvy sloupců,
        a poté vypište všechny záznamy.''',
        'hint': '''
        - V CTE můžete používat aliasy sloupců.
        - Tyto aliasy jsou pak dostupné v hlavním dotazu.
        ''',
        'sql': '''
               WITH zamestnanci_kontakty AS (
                   SELECT
                       firstName AS jmeno,
                       lastName AS prijmeni,
                       email AS emailova_adresa
                   FROM employees
               )
               SELECT *
               FROM zamestnanci_kontakty;
               '''
    },
    '03. CTE s formátováním data': {
        'level': 'Začátečník',
        'title': '03. CTE s formátováním data',
        'instructions': '''Vytvořte CTE obsahující objednávky s přeformátovaným datem do českého formátu,
        a poté vypište objednávky z roku 2004.''',
        'hint': '''
        - Použijte DATE_FORMAT pro úpravu formátu data.
        - V hlavním dotazu můžete filtrovat podle původního data.
        ''',
        'sql': '''
               WITH formatovane_objednavky AS (
                   SELECT
                       orderNumber AS cislo_objednavky,
                       orderDate AS datum_objednavky,
                       DATE_FORMAT(orderDate, '%d.%m.%Y') AS ceske_datum
                   FROM orders
               )
               SELECT *
               FROM formatovane_objednavky
               WHERE YEAR(datum_objednavky) = 2004;
               '''
    },
    '04. CTE s podmínkou WHERE': {
        'level': 'Začátečník',
        'title': '04. CTE s podmínkou WHERE',
        'instructions': '''Vytvořte CTE obsahující drahé produkty (nad 100 dolarů), 
        a poté vypište pouze ty z kategorie "Classic Cars".''',
        'hint': '''
        - Můžete použít WHERE jak v CTE, tak v hlavním dotazu.
        - Podmínky se aplikují postupně.
        ''',
        'sql': '''
               WITH drahe_produkty AS (
                   SELECT
                       productName AS nazev,
                       productLine AS kategorie,
                       buyPrice AS cena
                   FROM products
                   WHERE buyPrice > 100
               )
               SELECT *
               FROM drahe_produkty
               WHERE kategorie = 'Classic Cars';
               '''
    },
    '05. CTE s více sloupci': {
        'level': 'Začátečník',
        'title': '05. CTE s více sloupci',
        'instructions': '''Vytvořte CTE obsahující základní informace o zákaznících včetně formátované adresy,
        a poté vypište zákazníky z USA.''',
        'hint': '''
        - V CTE můžete kombinovat více sloupců.
        - Použijte CONCAT pro spojení textových hodnot.
        ''',
        'sql': '''
               WITH zakaznici_info AS (
                   SELECT
                       customerNumber AS cislo,
                       customerName AS nazev,
                       CONCAT(addressLine1, ', ', city, ', ', country) AS adresa,
                       country AS zeme
                   FROM customers
               )
               SELECT
                   cislo,
                   nazev,
                   adresa
               FROM zakaznici_info
               WHERE zeme = 'USA';
               '''
    }
}

load_tasks('Příkaz WITH', examples)