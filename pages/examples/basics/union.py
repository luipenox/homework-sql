from functions import load_tasks

examples = {
    '01. Základní UNION': {
        'level': 'Začátečník',
        'title': '01. Základní UNION',
        'instructions': '''Vypište seznam všech měst, kde má firma buď zákazníky nebo kanceláře.
        Použijte tabulky `customers` a `offices`.''',
        'hint': '''
        - UNION spojuje výsledky dvou nebo více SELECT příkazů.
        - Počet a datové typy sloupců musí být stejné.
        - UNION automaticky odstraňuje duplicity.
        ''',
        'sql': '''
               SELECT city AS mesto
               FROM customers
               UNION
               SELECT city
               FROM offices
               ORDER BY mesto;
               '''
    },
    '02. UNION ALL se zachováním duplicit': {
        'level': 'Začátečník',
        'title': '02. UNION ALL se zachováním duplicit',
        'instructions': '''Vypište seznam všech zemí, kde má firma zákazníky nebo kanceláře, včetně duplicit.
        Použijte tabulky `customers` a `offices`.''',
        'hint': '''
        - UNION ALL zachová všechny řádky včetně duplicit.
        - Je rychlejší než UNION, protože nemusí odstraňovat duplicity.
        - Vhodné, když víme, že duplicity nevadí nebo je chceme zachovat.
        ''',
        'sql': '''
               SELECT country AS zeme
               FROM customers
               UNION ALL
               SELECT country
               FROM offices
               ORDER BY zeme;
               '''
    },
    '03. UNION s více sloupci': {
        'level': 'Mírně pokročilý',
        'title': '03. UNION s více sloupci',
        'instructions': '''Vytvořte seznam kontaktů obsahující jména a kontakt jak zákazníků, tak zaměstnanců.
        U zákazníků zobrazte telefonní číslo, u zaměstnanců email.
        Přidejte sloupec označující, zda jde o zákazníka nebo zaměstnance.''',
        'hint': '''
        - Můžete použít více sloupců, ale musí odpovídat v obou dotazech.
        - Pomocí literálu vytvoříte sloupec s pevnou hodnotou.
        - Názvy sloupců se berou z prvního SELECT.
        ''',
        'sql': '''
               SELECT
                    customerName AS jmeno,
                    phone AS kontakt,
                    'Zákazník' AS typ
                FROM customers
                UNION
                SELECT
                    CONCAT(firstName, ' ', lastName),
                    email,
                    'Zaměstnanec'
                FROM employees
                ORDER BY jmeno;
               '''
    }
}

load_tasks('Příkaz UNION', examples)