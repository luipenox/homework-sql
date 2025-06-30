from functions import load_tasks

examples = {
    '01. Základní výběr podle data': {
        'level': 'Začátečník',
        'title': '01. Základní výběr podle data',
        'instructions': 'Vypište všechny objednávky z tabulky `orders` z konkrétního data (1. ledna 2004).',
        'hint': '''
        - Data se v SQL zapisují ve formátu 'YYYY-MM-DD'.
        - Pro porovnání data použijte operátor =.
        ''',
        'sql': '''
               SELECT *
               FROM orders
               WHERE orderDate = '2004-01-01';
               '''
    },
    '02. Získání roku z data': {
        'level': 'Začátečník',
        'title': '02. Získání roku z data',
        'instructions': 'Vypište všechny objednávky z roku 2004 a zobrazte pouze datum a status.',
        'hint': '''
        - Použijte funkci YEAR() pro získání roku z data.
        - Funkce YEAR() vrací číslo reprezentující rok.
        ''',
        'sql': '''
               SELECT orderDate, status
               FROM orders
               WHERE YEAR(orderDate) = 2004;
               '''
    },
    '03. Měsíc a den': {
        'level': 'Začátečník',
        'title': '03. Měsíc a den',
        'instructions': 'Vypište datum objednávky a k němu samostatně měsíc a den pro všechny objednávky.',
        'hint': '''
        - Použijte funkce MONTH() a DAY() pro extrakci částí data.
        - Každou část data můžete pojmenovat pomocí AS.
        ''',
        'sql': '''
               SELECT
                   orderDate,
                   MONTH(orderDate) AS mesic,
                   DAY(orderDate) AS den
               FROM orders;
               '''
    },
    '04. Název měsíce': {
        'level': 'Mírně pokročilý',
        'title': '04. Název měsíce',
        'instructions': 'Vypište všechny objednávky a u každé zobrazte název měsíce, ve kterém byla vytvořena.',
        'hint': '''
        - Použijte funkci MONTHNAME() pro získání názvu měsíce.
        - Alternativně lze použít DATE_FORMAT() s %M.
        ''',
        'sql': '''
               SELECT
                   orderDate,
                   MONTHNAME(orderDate) AS nazev_mesice
               FROM orders;
               '''
    },
    '05. Číslo týdne': {
        'level': 'Mírně pokročilý',
        'title': '05. Číslo týdne',
        'instructions': 'Vypište všechny objednávky z prvního týdne roku 2004.',
        'hint': '''
        - Použijte funkci WEEK() pro získání čísla týdne.
        - Kombinujte s podmínkou na rok.
        ''',
        'sql': '''
               SELECT *
               FROM orders
               WHERE WEEK(orderDate) = 1
                         AND YEAR(orderDate) = 2004;
               '''
    },
    '06. Rozdíl mezi daty': {
        'level': 'Mírně pokročilý',
        'title': '06. Rozdíl mezi daty',
        'instructions': 'Vypište všechny objednávky a spočítejte počet dní mezi datem objednávky a datem odeslání.',
        'hint': '''
        - Použijte DATEDIFF() pro výpočet rozdílu mezi daty.
        - Funkce vrací počet dní.
        ''',
        'sql': '''
               SELECT
                   orderNumber,
                   orderDate,
                   shippedDate,
                   DATEDIFF(shippedDate, orderDate) AS dny_do_odeslani
               FROM orders
               WHERE shippedDate IS NOT NULL;
               '''
    },
    '07. Formátování data': {
        'level': 'Pokročilý',
        'title': '07. Formátování data',
        'instructions': 'Vypište všechny objednávky s datem ve formátu "den.měsíc.rok" (např. 1.1.2004).',
        'hint': '''
        - Použijte DATE_FORMAT() pro vlastní formát data.
        - %d = den, %m = měsíc, %Y = rok.
        ''',
        'sql': '''
               SELECT
                   orderNumber,
                   DATE_FORMAT(orderDate, '%d.%m.%Y') AS datum_objednavky
               FROM orders;
               '''
    },
    '08. Práce s časovými obdobími': {
        'level': 'Pokročilý',
        'title': '08. Práce s časovými obdobími',
        'instructions': 'Najděte objednávky z posledního čtvrtletí roku 2004.',
        'hint': '''
        - Použijte funkci QUARTER() pro určení čtvrtletí.
        - Kombinujte s podmínkou na rok.
        ''',
        'sql': '''
               SELECT *
               FROM orders
               WHERE YEAR(orderDate) = 2004
                 AND QUARTER(orderDate) = 4;
               '''
    },
    '09. Přidávání k datu': {
        'level': 'Pokročilý',
        'title': '09. Přidávání k datu',
        'instructions': 'Vypište všechny objednávky a datum o 30 dní později jako předpokládané datum doručení.',
        'hint': '''
        - Použijte DATE_ADD() nebo + INTERVAL pro přičtení dnů k datu.
        - Výsledek můžete formátovat pomocí DATE_FORMAT().
        ''',
        'sql': '''
               SELECT
                   orderNumber,
                   orderDate,
                   DATE_ADD(orderDate, INTERVAL 30 DAY) AS predpokladane_doruceni
               FROM orders;
               '''
    },
    '10. Komplexní práce s daty': {
        'level': 'Expert',
        'title': '10. Komplexní práce s daty',
        'instructions': 'Pro každou objednávku vypište číslo objednávky, datum, den v týdnu, čtvrtletí a počet dní do konce roku.',
        'hint': '''
        - Použijte kombinaci různých datových funkcí.
        - DAYNAME() pro název dne v týdnu.
        - Použijte DATEDIFF() s MAKEDATE() pro dny do konce roku.
        ''',
        'sql': '''
               SELECT
                   orderNumber,
                   orderDate,
                   DAYNAME(orderDate) AS den_v_tydnu,
                   QUARTER(orderDate) AS ctvrtleti,
                   DATEDIFF(
                           MAKEDATE(YEAR(orderDate) + 1, 1),
                           orderDate
                   ) AS dnu_do_konce_roku
               FROM orders;
               '''
    }
}

load_tasks('Práce s datumy', examples)