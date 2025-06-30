from functions import load_tasks

examples = {
    '01. Základní alias sloupce': {
        'level': 'Začátečník',
        'title': '01. Základní alias sloupce',
        'instructions': 'Vypište jméno produktu (productName) z tabulky `products` a přejmenujte sloupec na "Název produktu".',
        'hint': '''
        - Pro vytvoření aliasu použijte klíčové slovo AS.
        - Alias obsahující mezeru musí být v uvozovkách.
        - Syntax: SELECT sloupec AS "nový název"
        ''',
        'sql': '''
               SELECT productName AS "Název produktu"
               FROM products;
               '''
    },
    '02. Více aliasů': {
        'level': 'Začátečník',
        'title': '02. Více aliasů',
        'instructions': 'Vypište z tabulky `employees` jméno (firstName) a příjmení (lastName) zaměstnance s českými názvy sloupců.',
        'hint': '''
        - Můžete použít více aliasů v jednom dotazu.
        - Každý sloupec může mít vlastní alias.
        - Aliasy bez mezer není nutné dávat do uvozovek.
        ''',
        'sql': '''
               SELECT
                   firstName AS Jméno,
                   lastName AS Příjmení
               FROM employees;
               '''
    },
    '03. Alias tabulky': {
        'level': 'Mírně pokročilý',
        'title': '03. Alias tabulky',
        'instructions': 'Vypište všechny produkty z tabulky `products` a použijte alias "p" pro tabulku.',
        'hint': '''
        - Alias tabulky se definuje přímo za jejím názvem.
        - Pak můžete používat tento alias místo celého názvu tabulky.
        - Užitečné zejména u složitějších dotazů s více tabulkami.
        ''',
        'sql': '''
               SELECT p.*
               FROM products AS p
               WHERE p.buyPrice > 100;
               '''
    },
    '04. Alias s výpočtem': {
        'level': 'Mírně pokročilý',
        'title': '04. Alias s výpočtem',
        'instructions': 'Vypište z tabulky `orderdetails` číslo produktu, množství, cenu a celkovou cenu (množství * cena) s vhodnými českými názvy.',
        'hint': '''
        - Můžete vytvořit alias pro vypočítaný sloupec.
        - Výpočet může obsahovat matematické operace.
        - Vhodné pojmenování usnadňuje čtení výsledků.
        ''',
        'sql': '''
               SELECT
                   productCode AS "Kód produktu",
                   quantityOrdered AS "Množství",
                   priceEach AS "Cena za kus",
                   quantityOrdered * priceEach AS "Celková cena"
               FROM orderdetails;
               '''
    }
}

load_tasks('Příkaz AS', examples)