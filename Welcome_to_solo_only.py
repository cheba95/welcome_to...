# сделать нулевого бота - ?
# добавить экспертные планы застройки и возможность выбора планов: либо только стандартные, либо расширенные, либо и то и то, в различных вариациях
# т.е. допустим планы А расширенные, планы Б стандартные, планы С - смесь расширенных и стандартных
# по необходимости автоматизировать применение планов застройки к боту

print("Это программа для игры в 'Бумажные кварталы' в одиночном режиме. Подготовьте планшет игрока", '\n')

#создаем основную базу карт для игры.

park = "сквер"
workers = "рабочие"
pool = "бассеин"
realtor = "риэлтор"
fence = "забор"
app = "строение"

cards_base = ((5, park), (4, workers), (9, park), (3, pool), (7, realtor), (12, park), (8, workers), (5, realtor),
              (8, app), (6, pool), (3, workers), (5, realtor), (7, pool), (4, park), (11, fence), (10, realtor),
              (9, pool), (7, park), (9, realtor), (13, workers), (8, park), (6, fence), (5, fence), (8, fence),
              (10, fence), (7, park), (3, app), (10, workers), (11, fence), (15, fence), (9, park), (11, realtor),
              (11, park), (6, app), (4, app), (10, park), (12, realtor), (6, park), (10, pool), (9, fence),
              (12, workers), (13, app), (13, pool), (12, app), (5, fence), (2, fence), (11, realtor), (15, realtor),
              (14, park), (4, realtor), (10, app), (8, fence), (7, fence), (8, park), (6, workers), (2, park),
              (1, realtor), (6, realtor), (7, realtor), (14, fence), (9, realtor), (8, pool), (1, fence))

# добавляем базу дополнительных карт 9 и 3/4, предусматриваем возможность их добавления в колоду
harry_potter_cards = (("9 и 3/4", realtor), ("9 и 3/4", park), ("9 и 3/4", fence))

# if input('''Для игры в одиночном режиме введите "да". В колоду будет замешано 3 карты бота "План выполнен"''') == "да":
# print("Вы выбрали одиночный режим") - задел для возможного сшивания в единый проект соло и мультиплеера

# создаем базу планов застройки - их выполнение является одной из целей игры
basic_city_plan_cards_A = (("два квартала по 5 домов в каждом", 8, 4), ("6 кварталов по 1 дому в каждом", 8, 4), 
                         ("3 квартала по 4 дома в каждом", 11, 6), ("2 квартала по 4 дома в каждом", 6, 3), 
                         ("3 квартала по 3 дома в каждом", 8, 4), ("4 квартала по 2 дома в каждом", 8, 4),
                         ("2 квартала по 6 домов в каждом", 10, 6))

basic_city_plan_cards_B = (("1 квартал из 2 домов + 1 квартал из 5 домов", 7, 3), ("1 квартал из 4 домов + 1 квартал из 5 домов", 9, 5),
                           ("1 квартал из 3 домов + 1 квартал из 6 домов", 8, 4), ("2 квартала из 2 домов + 1 квартал из 5 домов", 10, 6),
                           ("3 квартала из 1 дома + 1 квартал из 4 домов", 9, 5), ("2 квартала из 3 домов + 1 квартал из 4 домов", 12, 7),
                           ("3 квартала из 1 дома + 1 квартал из 6 домов", 11, 6))

basic_city_plan_cards_С = (("1 квартал из 2 домов + 1 квартал из 3 домов + 1 квартал из 5 домов", 13, 7),
                           ("1 квартал из 1 дома + 1 квартал из 4 домов + 1 квартал из 5 домов", 13, 7),
                           ("2 квартала из 1 дома + 1 квартал из 2 домов + 1 квартал из 5 домов", 12, 6),
                           ("1 квартал из 2 домов + 1 квартал из 3 домов + 1 квартал из 4 домов", 11, 6),
                           ("1 квартал из 1 дома + 1 квартал из 2 домов + 1 квартал из 6 домов", 11, 6),
                           ("1 квартал из 1 дома + 1 квартал из 3 домов + 1 квартал из 6 домов", 12, 7),
                           ("1 квартал из 1 дома + 2 квартала из 2 домов + 1 квартал из 3 домов", 11, 6))

from random import choice, shuffle, randint

# выбираем случайные планы застройки на игру
current_plan_A, current_plan_B, current_plan_C = choice(basic_city_plan_cards_A), choice(basic_city_plan_cards_B), choice(basic_city_plan_cards_С)

# выводим игру планы застройки на текущую игру
print(f'''Ваши планы застройки на игру:
План А: {current_plan_A[0]}, {current_plan_A[1]} очков, если успеете выполнить план раньше бота, иначе {current_plan_A[2]}
План Б: {current_plan_B[0]}, {current_plan_B[1]} очков, если успеете выполнить план раньше бота, иначе {current_plan_B[2]}
План В: {current_plan_C[0]}, {current_plan_C[1]} очков, если успеете выполнить план раньше бота, иначе {current_plan_C[2]}''', '\n')

# создаем планы застройки бота на игру
ai_plan_A = "А"
ai_plan_B = "Б"
ai_plan_C = "В"
ai_plan_A_points = 0
ai_plan_B_points = 0
ai_plan_C_points = 0
ai_plan = {ai_plan_A: ai_plan_A_points, ai_plan_B: ai_plan_B_points, ai_plan_C: ai_plan_C_points}
ai_plan_list = list(ai_plan.keys())
current_ai_plan = [i for i in ai_plan_list]

#создаем список карт для игры. Посколько он будет изменяться, нельзя просто использовать базу в виде кортежа.
cards = [i for i in cards_base]

# предусматриваем возможность добавить карты 9 и 3/4 в колоду
if input('''Для небольшого упрощения игры вы можете добавить 3 дополнительные карты "9 и 3/4" в колоду. 
Введите "да", если хотите их добавить, либо нажмите "ENTER" для продолжения без них''') == "да":
    cards += harry_potter_cards
    print('\n', 'Вы добавили карты "9 и 3/4"', '\n')
else:
    print('\n', 'Вы играете со стандартным набором карт, без карт "9 и 3/4"', '\n')

# тасуем колоду для получения уникального порядка выхода карт на игру
shuffle(cards)

# добавляем один случайный план бота в последние 20 карт колоды
cards.insert(-randint(1,20), current_ai_plan.pop(randint(0,2)))

# база ботов с разными уровнями сложности у каждого
ai_opponents = (("номер", "имя", "сложность", "сквер", "бассеин", "рабочие", "забор", "строение", "риэлтор", "планы застройки"), 
                (1, "Сергей", 1, 1, 1, 1, 2, 1, 2, (ai_plan_A, )), 
                (2, "Алекс", 2, 3, 1, 1, 2, 1, 2, ("-", )), 
                (3, "Роза", 3, 4, 0, 2, 2, 2, 1, (ai_plan_A, ai_plan_B)), 
                (4, "Мария", 3, 0, 5, 2, 2, 3, 2, (ai_plan_B, )), 
                (5, "Алан", 4, 3, 2, 2, 1, 2, 2, (ai_plan_A, ai_plan_B, ai_plan_C)), 
                (6, "Ирина", 4, 2, 3, 1, 3, 2, 2, (ai_plan_A, ai_plan_C)), 
                (7, "Анн", 5, 3, 2, 1, 3, 3, 3, (ai_plan_B, )), 
                (8, "Кармен", 5, 0, 3, 2, 3, 4, 3, (ai_plan_A, ai_plan_B)), 
                (9, "Амаза", 6, 4, 4, 1, 3, 2, 3, (ai_plan_A, ai_plan_B)), 
                (10, "Фрэнк", 6, 4, 3, 2, 2, 1, 4, (ai_plan_B, ai_plan_C)), 
                (11, "Бен", 7, 4, 4, 2, 3, 4, 4, ((ai_plan_A, ai_plan_B, ai_plan_C)))) 

# предлагаем игроку выбрать оппонента
print("Выберите оппонента. В таблице ниже указаны их номера, имена и модификаторы свойств карт", '\n')

for opponent in ai_opponents:
    for i in range(9):
        print(str(opponent[i]).ljust(10), end="")
    print(str("".join(opponent[9])).ljust(10), '\n')

ai_point_tuple_num = 0
while not 1 <= ai_point_tuple_num <= 11:
    print("Введите номер оппонента, с которым хотите сыграть", '\n')
    ai_point_tuple_num_base = input()
    if ai_point_tuple_num_base.isdigit() and 1 <= int(ai_point_tuple_num_base) <= 11:
        ai_point_tuple_num = int(ai_point_tuple_num_base)
        break
    else:
        print("!!!Ошибка!!!", '\n')

# закрепляем выбранного оппонента-бота
ai_point_tuple = ai_opponents[ai_point_tuple_num]
ai_name = ai_point_tuple[1]
ai_plans = ai_point_tuple[9]

print(f'Вы играете с ботом "{ai_name}", уровень сложности "{ai_point_tuple[0]}"', '\n')

# предусматриваем список, в который будем добавлять карты, отданные игроком боту - это его застройка, 
# которая будет использоваться для подсчета очков
ai_set = []

# создаем сброс
discard = []

# создаем счетчик количества ходов
turn_counter = 0

# движок игры
wannaplay = True
# на каждом этапе выводим игроку списокк планов застройки - чтобы не забыл
while wannaplay:
    print()
    print(f'''Планы застройки:
План А: {current_plan_A[0]}, очки: {current_plan_A[1]} / {current_plan_A[2]}
План Б: {current_plan_B[0]}, очки: {current_plan_B[1]} / {current_plan_B[2]}
План В: {current_plan_C[0]}, очки: {current_plan_C[1]} / {current_plan_C[2]}''', '\n')
    # здесь тянем 3 верхние карты колоды. Если среди них есть карта плана застройки бота - он выполняет план, 
    # если может, и получает очки, после чего эта карта удаляется в сброс. Вместо неё извлекается новая карта.
    for i in range(3):
        if cards[i] in ai_plan_list:
            print(f'Вышел план застройки "{cards[i]}"', '\n')
            if cards[i] in ai_plans:
            # здесь пока вручную вводить очки с планов застройки, 
            # впоследствии попробовать автоматизировать, если в этом будет смысл.
                plan_points = int(input(f'''Бот "{ai_name}" может выполнить этот план застройки. Если вы не успели выполнить 
этот план раньше бота, введите большее число очков, причитающееся за выполнение плана - их получит бот. 
Вы в дальнейшем за выполнение плана сможете получить лишь меньшее количество очков. 
Если же вы успели выполнить план раньше бота - введите меньшее число очков, причитающееся за выполнение плана - 
их получит бот''')) 
                ai_plan[cards[i]] = plan_points
                print()
                print(f'Бот получил {plan_points} очков за план застройки "{cards[i]}"', '\n')
            else:
                print(f'Данный план не может быть выполнен ботом "{ai_name}". Негативных последствий нет - вы всё ещё можете выполнить этот план. Бот не получает очков', '\n')
            del cards[i]
    ai_card = 0
    # игроку на выбор предоставляется 3 верхних карты из колоды, на каждой из которых есть число и эффект
    while not 1 <= ai_card <= 3:
        print(f'''Выберите число из одной пары и эффект из другой пары. Введи номер оставшейся пары - её вы отдаете боту:
        1) {cards[0][0]} и {cards[0][1]}
        2) {cards[1][0]} и {cards[1][1]}
        3) {cards[2][0]} и {cards[2][1]}''')
        # игрок выбирает карту для бота, она добавляется ему в список и не попадает в сброс
        ai_card_base = input()
        if ai_card_base.isdigit() and 1 <= int(ai_card_base) <= 3:    
            ai_card = int(ai_card_base) - 1
            ai_set.append(cards.pop(ai_card)[1])
            turn_counter += 1
            break
        else:
            print("!!!Ошибка!!!", '\n')
    print(f"Застройка бота: {ai_set}", '\n')
    # 2 оставшиеся карты отправляются в сброс 
    for i in range(2):
        discard.append(cards.pop(0))
    # когда колода пуста - колода замешивается заново из сброса
    if not cards:
        print("ВНИМАНИЕ! Колода закончилась и затасована заново.", '\n')
        # превращаем сброс в новую колоду
        cards = discard[:]
        # добавляем в затасованную из сброса колоду оставшиеся 2 плана застройки
        cards.extend(current_ai_plan) # одиночный режим
        # тасуем колоду
        shuffle(cards)
        print("В колоду замешаны 2 оставшихся плана застройки бота. Поторопитесь выполнить планы застройки, чтобы успеть раньше него!", '\n')
    # максимальное количество ходов в игре - 36 (33 дома + 3 ошибки). Соответственно больше 36 ходов априори быть не может.
    if turn_counter == 36:
        wannaplay = False
        print("Вы совершили максимально возможное количество ходов. Игра завершена")
        break
    # опция для завершения игры и подсчета очков - если у игрока 3 ошибки и размещение домов невозможно
    if input("Нажми 'ENTER' для продолжения игры или введите любой символ для завершения и подсчета очков") != "":
        wannaplay = False

# считаем очки бота за выполнение планов застройки

ai_plan_points = ai_plan_A_points + ai_plan_B_points + ai_plan_C_points

# считаем очки бота за рабочих, бассейны, заборы и парки

# cчитаем число рабочих
ai_workers = ai_set.count(workers)
# очки за рабочих = число рабочих умноженный на коэффициент конкретного бота
ai_points_workers = ai_workers * ai_point_tuple[5]
# определяем очки за соревнование между игроком и ботом по числу рабочих
print()
if ai_workers == 0:
    ai_workers_place_points = 0
    print("У бота нет карточек с рабочими, поэтому за рабочих он получает 0 очков", '\n')
else:
    if input(f'''Количество карточек рабочих у бота - {ai_workers}. 
Если у вас меньше карточек с рабочими, чем у бота, введите 'да' - боту добавится 7 очков за первое место по рабочим.
Если у вас таких карточек больше - нажмите 'ENTER' - и добавьте 7 очков себе. Боту добавится 4 очка''') == "да":
        ai_workers_place_points = 7
        print('\n', "Боту добавлено 7 очков", '\n')
    else:
        ai_workers_place_points = 4
        print('\n', "Боту добавлено 4 очка", '\n')

# очки за бассейны, заборы и парки - по количеству соответствующих карточек, умноженному на коэффициент бота
ai_pools_points = ai_set.count(pool) * ai_point_tuple[4]
ai_fences_points = ai_set.count(fence) * ai_point_tuple[6]
ai_parks_points = ai_set.count(park) * ai_point_tuple[3]

# расчленяем кварталы бота по заборам

ai_quarter_set = []
ai_current_quarter = []
for i in ai_set:
    if i == fence:
        ai_quarter_set.append(ai_current_quarter)
        ai_current_quarter = []
    else:
        ai_current_quarter.append(i)
ai_quarter_set.append(ai_current_quarter)
ai_quarter_set_good = [i for i in ai_quarter_set if i != []]

# считаем очки за кварталы. Кварталом у бота считается группа карточек (домов) между заборами, 
# либо между началом или концом списка и забором.
# сквер, бассейн, рабочий и риэлтор считается за 1 дом
# карточка строения считается за 1, 2, 3 или 4 дома в зависимости от модификатора бота - app bonus
# если в квартале нет риэлтора - каждый дом приносит 1 очко
# если в квартале есть риэлтор - каждый дом приносит от 1 до 4 очков в зависимости от модификатора бота - realtor mult

ai_quarter_points_list = []

app_bonus = ai_point_tuple[7]
realtor_mult = ai_point_tuple[8]

for quarter in ai_quarter_set_good:
    houses_in_quarter = 0
    for house in quarter:
        if house == app:
            houses_in_quarter += app_bonus
        else:
            houses_in_quarter += 1
    if realtor in quarter:
        mult = realtor_mult
    else:
        mult = 1
    ai_quarter_points_list.append(houses_in_quarter * mult)

# бот получает очки за 5 самых больших кварталов
ai_quarter_points = sum(sorted(ai_quarter_points_list, reverse=True)[:5])

# итоговый подсчет

ai_vic_points = ai_plan_points + ai_points_workers +  ai_workers_place_points + ai_pools_points + ai_fences_points + ai_parks_points + ai_quarter_points
print(f'''Итоговая застройка бота: {ai_set}. 
Очки бота "{ai_name}": {ai_vic_points}, а именно:
{ai_plan_points} - очки за выполнение планов застройки, 
в том числе {ai_plan_A_points} за план "А", {ai_plan_B_points} за план "Б", {ai_plan_C_points} за план "В";
{ai_points_workers} - очки за рабочих;
{ai_workers_place_points} - очки за место по количеству рабочих;
{ai_pools_points} - очки за бассейны;
{ai_fences_points} - очки за заборы;
{ai_parks_points} - очки за скверы;
{ai_quarter_points} - очки за кварталы между заборами бота''', '\n')

print("Спасибо за игру")

end = input('Нажмите "ENTER" или введите любой символ чтобы закрыть программу')
