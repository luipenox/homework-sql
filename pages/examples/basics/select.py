from functions import load_tasks

examples = {
    '01. Všechny produkty': {
        'level': 'Začátečník',
        'title': '01. Všechny produkty',
        'instructions': 'Vypište všechny záznamy z tabulky `products`.',
        'hint':
            """
            Pro výpis celé tabulky využijeme jednoduše konstrukci `SELECT * FROM tabulka`.
            Symbol `*` znamená výběr všech sloupců.
            """,
        'sql': '''
               SELECT *
               FROM products;
               '''
    },
    '02. Seznam produktových řad': {
        'level': 'Začátečník',
        'title': '02. Seznam produktových řad',
        'instructions': 'Vypište všechny záznamy z tabulky `productlines`.',
        'hint':
            """
            Opět využijeme základní konstrukci `SELECT * FROM tabulka`.
            Tabulka `productlines` obsahuje informace o produktových řadách.
            """,
        'sql': '''
               SELECT *
               FROM productlines;
               '''
    },
    '03. Základní informace o produktech': {
        'level': 'Začátečník',
        'title': '03. Základní informace o produktech',
        'instructions': 'Vypište pouze název, měřítko a cenu produktů z tabulky `products`.',
        'hint':
            """
            Pro výběr konkrétních sloupců je uvedeme za SELECT oddělené čárkami.
            Tedy využijeme konstrukci `SELECT sloupec1, sloupec2, sloupec3 FROM tabulka`.
            """,
        'sql': '''
               SELECT productName, productScale, buyPrice
               FROM products;
               '''
    },
    '04. Kontaktní údaje zaměstnanců': {
        'level': 'Začátečník',
        'title': '04. Kontaktní údaje zaměstnanců',
            'instructions': 'Vypište jméno, příjmení a email všech zaměstnanců z tabulky `employees`.',
        'hint':
            """
            Vybereme pouze požadované sloupce z tabulky.
            Sloupce oddělujeme čárkami.
            """,
        'sql': '''
               SELECT firstName, lastName, email
               FROM employees;
               '''
    },
    '05. Informace o kancelářích': {
        'level': 'Začátečník',
        'title': '05. Informace o kancelářích',
        'instructions': 'Vypište všechny záznamy z tabulky `offices`.',
        'hint':
            """
            Pro výpis všech informací o kancelářích použijeme základní konstrukci s hvězdičkou.
            """,
        'sql': '''
               SELECT *
               FROM offices;
               '''
    },
    '06. Detaily objednávek': {
        'level': 'Začátečník',
        'title': '06. Detaily objednávek',
        'instructions': 'Vypište číslo produktu, množství a cenu za kus z tabulky `orderdetails`.',
        'hint':
            """
            Vybereme pouze potřebné sloupce z tabulky s detaily objednávek.
            """,
        'sql': '''
               SELECT productCode, quantityOrdered, priceEach
               FROM orderdetails;
               '''
    }
}

load_tasks('Příkaz SELECT', examples)
