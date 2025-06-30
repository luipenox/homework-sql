from functions import load_tasks

examples = {
    '01. Základní podmínka s rovností': {
        'level': 'Začátečník',
        'title': '01. Základní podmínka s rovností',
        'instructions': 'Vypište všechny produkty z tabulky `products`, které patří do produktové řady "Classic Cars".',
        'hint': 'Použijte jednoduchou podmínku s operátorem = pro porovnání hodnoty ve sloupci `productLine`.',
        'sql': '''
               SELECT *
               FROM products
               WHERE productLine = 'Classic Cars';
               '''
    },
    '02. Podmínka větší než': {
        'level': 'Začátečník',
        'title': '02. Podmínka větší než',
        'instructions': 'Vypište všechny produkty z tabulky `products`, které stojí více než 100 dolarů.',
        'hint': 'Použijte operátor > pro porovnání hodnoty ve sloupci `buyPrice`.',
        'sql': '''
               SELECT *
               FROM products
               WHERE buyPrice > 100;
               '''
    },
    '03. Podmínka menší nebo rovno': {
        'level': 'Začátečník',
        'title': '03. Podmínka menší nebo rovno',
        'instructions': 'Najděte všechny objednávky z tabulky `orders`, které mají status "Shipped" a byly vytvořeny před rokem 2004.',
        'hint': 'Použijte operátor <= pro porovnání data a = pro porovnání stavu.',
        'sql': '''
               SELECT *
               FROM orders
               WHERE status = 'Shipped' AND orderDate <= '2003-12-31';
               '''
    },
    '04. Jednoduchá podmínka LIKE': {
        'level': 'Začátečník',
        'title': '04. Jednoduchá podmínka LIKE',
        'instructions': 'Vypište všechny produkty, jejichž název obsahuje slovo "Ford".',
        'hint': 'Použijte operátor LIKE s % před a za hledaným textem.',
        'sql': '''
               SELECT *
               FROM products
               WHERE productName LIKE '%Ford%';
               '''
    },
    '05. Podmínka IN': {
        'level': 'Začátečník',
        'title': '05. Podmínka IN',
        'instructions': 'Najděte všechny zaměstnance z tabulky `employees`, kteří mají pozici "Sales Rep" nebo "VP Sales".',
        'hint': 'Použijte operátor IN pro testování více možných hodnot.',
        'sql': '''
               SELECT *
               FROM employees
               WHERE jobTitle IN ('Sales Rep', 'VP Sales');
               '''
    },
    '06. Podmínka BETWEEN': {
        'level': 'Mírně pokročilý',
        'title': '06. Podmínka BETWEEN',
        'instructions': 'Vypište všechny produkty s cenou mezi 50 a 100 dolary (včetně).',
        'hint': 'Použijte operátor BETWEEN, který je včetně hraničních hodnot.',
        'sql': '''
               SELECT *
               FROM products
               WHERE buyPrice BETWEEN 50 AND 100;
               '''
    },
    '07. Složená podmínka s AND': {
        'level': 'Mírně pokročilý',
        'title': '07. Složená podmínka s AND',
        'instructions': 'Najděte všechny produkty, které jsou automobily (Classic Cars nebo Vintage Cars) a stojí více než 150 dolarů.',
        'hint': 'Použijte závorky pro správné seskupení podmínek s OR a kombinaci s AND.',
        'sql': '''
               SELECT *
               FROM products
               WHERE (productLine = 'Classic Cars' OR productLine = 'Vintage Cars')
                 AND buyPrice > 150;
               '''
    },
    '08. NOT IN': {
        'level': 'Mírně pokročilý',
        'title': '08. NOT IN',
        'instructions': 'Vypište všechny produkty, které nepatří do kategorií "Motorcycles", "Planes" a "Ships".',
        'hint': 'Použijte operátor NOT IN pro vyloučení množiny hodnot.',
        'sql': '''
               SELECT *
               FROM products
               WHERE productLine NOT IN ('Motorcycles', 'Planes', 'Ships');
               '''
    },
    '09. NOT LIKE': {
        'level': 'Mírně pokročilý',
        'title': '09. NOT LIKE',
        'instructions': 'Najděte všechny produkty, jejichž název nezačíná na písmeno "F".',
        'hint': 'Použijte NOT LIKE s vzorem začínajícím na "F".',
        'sql': '''
               SELECT *
               FROM products
               WHERE productName NOT LIKE 'F%';
               '''
    },
    '10. Komplexní LIKE': {
        'level': 'Mírně pokročilý',
        'title': '10. Komplexní LIKE',
        'instructions': 'Vypište všechny produkty, které mají v názvu přesně 5 znaků před slovem "Car".',
        'hint': 'Použijte podtržítko (_) pro reprezentaci přesného počtu znaků.',
        'sql': '''
               SELECT *
               FROM products
               WHERE productName LIKE '_____Car%';
               '''
    },
    '11. Více podmínek s OR': {
        'level': 'Pokročilý',
        'title': '11. Více podmínek s OR',
        'instructions': 'Najděte všechny objednávky, které jsou buď zrušené (status "Cancelled"), nebo mají komentář obsahující slovo "delay".',
        'hint': 'Kombinujte podmínku na přesnou shodu a LIKE s OR.',
        'sql': '''
               SELECT *
               FROM orders
               WHERE status = 'Cancelled'
                  OR comments LIKE '%delay%';
               '''
    },
    '12. NULL hodnoty': {
        'level': 'Pokročilý',
        'title': '12. NULL hodnoty',
        'instructions': 'Vypište všechny objednávky, které nemají vyplněný komentář.',
        'hint': 'Pro testování NULL hodnot použijte IS NULL.',
        'sql': '''
               SELECT *
               FROM orders
               WHERE comments IS NULL;
               '''
    },
    '13. NOT NULL hodnoty': {
        'level': 'Pokročilý',
        'title': '13. NOT NULL hodnoty',
        'instructions': 'Najděte všechny objednávky s vyplněným komentářem, které byly vytvořeny v roce 2004.',
        'hint': 'Kombinujte IS NOT NULL s podmínkou na datum.',
        'sql': '''
               SELECT *
               FROM orders
               WHERE comments IS NOT NULL
                         AND YEAR(orderDate) = 2004;
               '''
    },
    '14. Složitá podmínka s závorkami': {
        'level': 'Pokročilý',
        'title': '14. Složitá podmínka s závorkami',
        'instructions': 'Vypište všechny produkty, které jsou buď dražší než 150 dolarů a jsou auta, nebo levnější než 50 dolarů a jsou motorky.',
        'hint': 'Použijte závorky pro správné seskupení podmínek.',
        'sql': '''
               SELECT *
               FROM products
               WHERE (buyPrice > 150 AND productLine IN ('Classic Cars', 'Vintage Cars'))
                  OR (buyPrice < 50 AND productLine = 'Motorcycles');
               '''
    },
    '15. Komplexní datové podmínky': {
        'level': 'Pokročilý',
        'title': '15. Komplexní datové podmínky',
        'instructions': 'Najděte všechny objednávky z druhého čtvrtletí roku 2004, které byly odeslány (shipped) nebo zrušeny (cancelled).',
        'hint': 'Použijte funkce pro práci s daty a komplexní podmínky.',
        'sql': '''
               SELECT *
               FROM orders
               WHERE YEAR(orderDate) = 2004
                 AND QUARTER(orderDate) = 2
                 AND status IN ('Shipped', 'Cancelled');
               '''
    }
}

load_tasks('Příkaz WHERE', examples)