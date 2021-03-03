# Case-study #4
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print('''Case-study #4 Парсинг web-страниц
Разработчики:
Браер П.С., Новоселов В.В., Кокорина Д.Е.

''')
import urllib.request

with open('input.txt','r') as f_in:
    with open('output.txt','w') as f_out:
        for line in f_in:
            url = line
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)
            part_name = text.find('nfl-c-player-header__title')
            name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
            print(name, file = f_out, end =' '*(20-len(name)))
            comp_name = text.find('passingCompletions" scope="col"')
            name_1 = text[text.find('>', comp_name) + 3:text.find('</th>', comp_name) - 22]
            print(name_1, file = f_out)