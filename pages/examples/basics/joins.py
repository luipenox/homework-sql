from functions import load_tasks

examples = {
    '01. Základní INNER JOIN': {
        'level': 'Začátečník',
        'title': '01. Základní INNER JOIN',
        'instructions': '''Vypište názvy produktů a jejich produktové řady. 
        Spojte tabulky `products` a `productlines`.''',
        'hint': '''
        - INNER JOIN spojuje řádky, kde se hodnoty v obou tabulkách shodují.
        - Spojení se definuje pomocí klíčového slova ON.
        - Použijte INNER JOIN nebo jen JOIN (jsou totožné).
        ''',
        'sql': '''
               SELECT
                   p.productName AS nazev_produktu,
                   pl.productLine AS produktova_rada
               FROM products AS p
                        INNER JOIN productlines AS pl
                                   ON p.productLine = pl.productLine;
               '''
    },
    '02. LEFT JOIN': {
        'level': 'Začátečník',
        'title': '02. LEFT JOIN',
        'instructions': '''Vypište všechny zákazníky a jejich objednávky (pokud nějaké mají).
        Použijte tabulky `customers` a `orders`.''',
        'hint': '''
        - LEFT JOIN zachová všechny řádky z levé (první) tabulky.
        - Pokud v pravé tabulce není odpovídající záznam, použijí se NULL hodnoty.
        ''',
        'sql': '''
               SELECT
                   c.customerName AS zakaznik,
                   o.orderNumber AS cislo_objednavky
               FROM customers AS c
                        LEFT JOIN orders AS o
                                  ON c.customerNumber = o.customerNumber;
               '''
    },
    '03. RIGHT JOIN': {
        'level': 'Začátečník',
        'title': '03. RIGHT JOIN',
        'instructions': '''Vypište všechny kanceláře a zaměstnance, kteří v nich pracují (pokud nějací jsou).
        Použijte tabulky `employees` a `offices`.''',
        'hint': '''
        - RIGHT JOIN zachová všechny řádky z pravé (druhé) tabulky.
        - Funguje podobně jako LEFT JOIN, ale z opačné strany.
        ''',
        'sql': '''
               SELECT
                   o.city AS mesto,
                   e.firstName AS jmeno,
                   e.lastName AS prijmeni
               FROM employees AS e
                        RIGHT JOIN offices AS o
                                   ON e.officeCode = o.officeCode;
               '''
    },
    '04. JOIN se WHERE': {
        'level': 'Začátečník',
        'title': '04. JOIN se WHERE',
        'instructions': '''Vypište všechny produkty z kategorie "Classic Cars" včetně jejich popisu.
        Použijte tabulky `products` a `productlines`.''',
        'hint': '''
        - Můžete kombinovat JOIN s podmínkou WHERE.
        - WHERE se aplikuje na výsledek spojení.
        ''',
        'sql': '''
               SELECT
                   p.productName AS nazev,
                   pl.textDescription AS popis
               FROM products AS p
                        JOIN productlines AS pl
                             ON p.productLine = pl.productLine
               WHERE p.productLine = 'Classic Cars';
               '''
    },
    '05. JOIN s aliasy': {
        'level': 'Začátečník',
        'title': '05. JOIN s aliasy',
        'instructions': '''Vypište jména zaměstnanců a města jejich kanceláří.
        Použijte tabulky `employees` a `offices` s aliasy.''',
        'hint': '''
        - Aliasy tabulek zjednodušují zápis.
        - Aliasy definujeme za názvem tabulky.
        ''',
        'sql': '''
               SELECT
                   e.firstName AS jmeno,
                   e.lastName AS prijmeni,
                   o.city AS mesto
               FROM employees AS e
                        JOIN offices AS o
                             ON e.officeCode = o.officeCode;
               '''
    },
    '06. LEFT JOIN s formátováním': {
        'level': 'Začátečník',
        'title': '06. LEFT JOIN s formátováním',
        'instructions': '''Vypište zákazníky a data jejich objednávek v českém formátu.
        Použijte tabulky `customers` a `orders`.''',
        'hint': '''
        - Můžete kombinovat JOIN s formátováním dat.
        - Použijte DATE_FORMAT pro úpravu formátu data.
        ''',
        'sql': '''
               SELECT
                   c.customerName AS zakaznik,
                   DATE_FORMAT(o.orderDate, '%d.%m.%Y') AS datum_objednavky
               FROM customers AS c
                        LEFT JOIN orders AS o
                                  ON c.customerNumber = o.customerNumber;
               '''
    },
    '07. JOIN s NULL hodnotami': {
        'level': 'Začátečník',
        'title': '07. JOIN s NULL hodnotami',
        'instructions': '''Vypište všechny produktové řady a počet produktů (stačí hvězdička).
        Použijte tabulky `productlines` a `products`.''',
        'hint': '''
        - LEFT JOIN zobrazí i řady bez produktů.
        - Pro řady bez produktů bude hodnota NULL.
        ''',
        'sql': '''
               SELECT
                   pl.productLine AS rada,
                   p.productName AS nazev_produktu
               FROM productlines AS pl
                        LEFT JOIN products AS p
                                  ON pl.productLine = p.productLine;
               '''
    },
    '08. Více podmínek v JOIN': {
        'level': 'Začátečník',
        'title': '08. Více podmínek v JOIN',
        'instructions': '''Vypište zaměstnance a jejich kanceláře v USA.
        Použijte tabulky `employees` a `offices`.''',
        'hint': '''
        - Můžete kombinovat JOIN podmínku s WHERE.
        - WHERE filtruje výsledky po spojení.
        ''',
        'sql': '''
               SELECT
                   e.firstName AS jmeno,
                   e.lastName AS prijmeni,
                   o.city AS mesto
               FROM employees AS e
                        JOIN offices AS o
                             ON e.officeCode = o.officeCode
               WHERE o.country = 'USA';
               '''
    },
    '09. JOIN s výběrem sloupců': {
        'level': 'Začátečník',
        'title': '09. JOIN s výběrem sloupců',
        'instructions': '''Vypište názvy produktů a jejich kategorie, seřazené podle názvu.
        Použijte tabulky `products` a `productlines`.''',
        'hint': '''
        - Můžete vybrat jen potřebné sloupce.
        - Použijte ORDER BY pro seřazení.
        ''',
        'sql': '''
               SELECT
                   p.productName AS nazev,
                   pl.productLine AS kategorie
               FROM products AS p
                        JOIN productlines AS pl
                             ON p.productLine = pl.productLine
               ORDER BY nazev;
               '''
    },
    '10. JOIN s formátovaným výstupem': {
        'level': 'Začátečník',
        'title': '10. JOIN s formátovaným výstupem',
        'instructions': '''Vypište zaměstnance a jejich kanceláře ve formátu "Jméno Příjmení (Město)".
        Použijte tabulky `employees` a `offices`.''',
        'hint': '''
        - Použijte CONCAT pro spojení textových hodnot.
        - Závorky a mezery přidejte jako součást řetězce.
        ''',
        'sql': '''
               SELECT
                   CONCAT(e.firstName, ' ', e.lastName, ' (', o.city, ')') AS zamestnanec
               FROM employees AS e
                        JOIN offices AS o
                             ON e.officeCode = o.officeCode;
               '''
    }
}

load_tasks('JOIN základy', examples)