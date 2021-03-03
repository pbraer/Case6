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
            name = text[text.find('>',part_name) + 1:text.find('</h1',part_name)]
            print(name, file = f_out, end =' '*(20 - len(name)))

            comp_name = text.find('passingCompletions" scope="col"')
            name_1 = text[text.find('>', comp_name) + 20:text.find('</th>', comp_name) - 22]
            print(name_1, file = f_out, end = ' '*(10 - len(name_1)))

            att_name = text.find('passingAttempts" scope="col"')
            name_2 = text[text.find('>', att_name) + 20:text.find('</th>', att_name) - 22]
            print(name_2, file=f_out, end = ' '*(10 - len(name_2)))

            yds_name = text.find('passingYards" scope="col"')
            name_3 = text[text.find('>', yds_name) + 20:text.find('</th>', yds_name) - 22]
            print(name_3, file=f_out, end=' ' * (10 - len(name_3)))

            td_name = text.find('passingTouchdowns" scope="col"')
            name_4 = text[text.find('>', td_name) + 20:text.find('</th>', td_name) - 22]
            print(name_4, file=f_out, end=' ' * (10 - len(name_4)))

            int_name = text.find('passingInterceptions" scope="col"')
            name_5 = text[text.find('>', int_name) + 20:text.find('</th>', int_name) - 22]
            print(name_5, file=f_out, end=' ' * (10 - len(name_5)))

            pr_name = text.find('passingPasserRating" scope="col"')
            name_6 = text[text.find('>', pr_name) + 20:text.find('</th>', pr_name) - 22]
            print(name_6,'0', sep='', file=f_out)