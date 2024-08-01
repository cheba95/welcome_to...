# сделать нулевого бота
# добавить планы застройки и автоматизировать их применение к ботам
# отбор планов можно сделать через метод random.sample
# добавить основной режим

from random import shuffle
print("Это программа для игры в 'Бумажные кварталы' в одиночном режиме. Подготовьте планшет игрока")

park = "сквер"
workers = "рабочие"
pool = "бассеин"
realtor = "риэлтор"
fence = "забор"
app = "строение"

cards_base = [(5, park), (4, workers), (9, park), (3, pool), (7, realtor), (12, park), (8, workers), (5, realtor),
              (8, app), (6, pool), (3, workers), (5, realtor), (7, pool), (4, park), (11, fence), (10, realtor),
              (9, pool), (7, park), (9, realtor), (13, workers), (8, park), (6, fence), (5, fence), (8, fence),
              (10, fence), (7, park), (3, app), (10, workers), (11, fence), (15, fence), (9, park), (11, realtor),
              (11, park), (6, app), (4, app), (10, park), (12, realtor), (6, park), (10, pool), (9, fence),
              (12, workers), (13, app), (13, pool), (12, app), (5, fence), (2, fence), (11, realtor), (15, realtor),
              (14, park), (4, realtor), (10, app), (8, fence), (7, fence), (8, park), (6, workers), (2, park),
              (1, realtor), (6, realtor), (7, realtor), (14, fence), (9, realtor), (8, pool), (1, fence)]

harry_potter_cards = [("9 и 3/4", realtor), ("9 и 3/4", park), ("9 и 3/4", fence)]

if input('''Для небольшого упрощения игры вы можете добавить 3 дополнительные карты "9 и 3/4" в колоду. 
Введите "да", если хотите их добавить, либо нажмите "ENTER" для продолжения без них''') == "да":
    cards_base += harry_potter_cards
    print('Вы добавили карты "9 и 3/4"')
else:
    print('Вы играете со стандартным набором карт, без карт "9 и 3/4"')

shuffle(cards_base)

# if input('''Для игры в одиночном режиме введите "да". В колоду будет замешано 3 карты бота "План выполнен"''') == "да":
    # print("Вы выбрали одиночный режим") - задел для будущего сшивания в единый проект соло и мультиплеера


from random import randint
ai_plan_A = "А"
ai_plan_B = "Б"
ai_plan_C = "В"
ai_plan_A_points = 0
ai_plan_B_points = 0
ai_plan_C_points = 0
ai_plan = {ai_plan_A: ai_plan_A_points, ai_plan_B: ai_plan_B_points, ai_plan_C: ai_plan_C_points}
ai_plan_list = list(ai_plan.keys())
current_ai_plan = [i for i in ai_plan_list]
cards = [i for i in cards_base]
cards.insert(-randint(1,20), current_ai_plan.pop(randint(0,2)))

ai_opponents = (("номер", "имя", "сложность", "сквер", "бассеин", "рабочие", "забор", "строение", "риэлтор", "планы застройки"), 
                (1, "Сергей", 1, 1, 1, 1, 2, 1, 2, ai_plan_A), (2, "Алекс", 2, 3, 1, 1, 2, 1, 2, "-"), 
                (3, "Роза", 3, 4, 0, 2, 2, 2, 1, (ai_plan_A, ai_plan_B)), (4, "Мария", 3, 0, 5, 2, 2, 3, 2, ai_plan_B), 
                (5, "Алан", 4, 3, 2, 2, 1, 2, 2, (ai_plan_A, ai_plan_B, ai_plan_C)), 
                (6, "Ирина", 4, 2, 3, 1, 3, 2, 2, (ai_plan_A, ai_plan_C)), (7, "Анн", 5, 3, 2, 1, 3, 3, 3, ai_plan_B), 
                (8, "Кармен", 5, 0, 3, 2, 3, 4, 3, (ai_plan_A, ai_plan_B)), (9, "Амаза", 6, 4, 4, 1, 3, 2, 3, (ai_plan_A, ai_plan_B)), 
                (10, "Фрэнк", 6, 4, 3, 2, 2, 1, 4, (ai_plan_B, ai_plan_C)), 
                (11, "Бен", 7, 4, 4, 2, 3, 4, 4, ((ai_plan_A, ai_plan_B, ai_plan_C)))) 
# модификаторы очков для бота в последовательности: номер(0), имя(1), уровень сложности(2), сквер(3), бассеин(4), рабочие(5), забор(6), 
# строение(7), риэлтор(8), планы застройки
print("Выберите оппонента. В таблице ниже указаны их номера, имена и модификаторы свойств карт")

for i in ai_opponents:
    for j in i:
        print(str(j).ljust(10), end="")
    print()

ai_point_tuple_num = 0
while not 1 <= ai_point_tuple_num <= 11:
    print("Введите номер оппонента, с которым хотите сыграть")
    ai_point_tuple_num_base = input()
    if ai_point_tuple_num_base.isdigit() and 1 <= int(ai_point_tuple_num_base) <= 11:
        ai_point_tuple_num = int(ai_point_tuple_num_base)
        break
    else:
        print("!!!Ошибка!!!")

ai_point_tuple = ai_opponents[ai_point_tuple_num]

print(f'Вы играете с ботом "{ai_point_tuple[1]}", уровень сложности "{ai_point_tuple[0]}"')

ai_set = []
wannaplay = True
while wannaplay:
    for i in range(3):
        if cards[i] in ai_plan_list:
            print(f'Вышел план застройки "{cards[i]}"')
            if cards[i] in ai_point_tuple[9]:
                plan_points = int(input(f'''Бот "{ai_point_tuple[1]}" может выполнить этот план застройки. Если вы не успели выполнить 
                  этот план раньше бота, введите большее число очков, причитающееся за выполнение плана - их получит бот. 
                  Вы в дальнейшем за выполнение плана сможете получить лишь меньшее количество очков. 
                  Если же вы успели выполнить план раньше бота - введите меньшее число очков, причитающееся за выполнение плана - 
                  их получит бот''')) 
                ai_plan[cards[i]] = plan_points
                # здесь пока вручную вводить очки с планов застройки, 
            # впоследствии их нужно автоматизировать.
                print(f'Бот получил {plan_points} очков за план застройки "{cards[i]}"')
            else:
                print("Данный план не может быть выполнен ботом. Негативных последствий нет - вы всё ещё можете выполнить этот план. Бот не получает очков")
            del cards[i]
    ai_card = 0
    while not 1 <= ai_card <= 3:
        print(f'''Выберите цифру из одной пары и эффект из другой пары. Введи номер оставшейся пары - её вы отдаете боту:
        1) {cards[0][0]} и {cards[0][1]}
        2) {cards[1][0]} и {cards[1][1]}
        3) {cards[2][0]} и {cards[2][1]}''')
        ai_card_base = input()
        if ai_card_base.isdigit() and 1 <= int(ai_card_base) <= 3:    
            ai_card = int(ai_card_base)
            ai_set.append(cards[ai_card - 1][1])
            break
        else:
            print("!!!Ошибка!!!")
    print(f" Застройка бота: {ai_set}")
    for i in range(3):
        del cards[0]
    wannaplay = False
    if len(cards) == 3:
        print("ВНИМАНИЕ! Колода закончилась и затасована заново")
        cards = [i for i in cards_base]
        cards.extend(current_ai_plan) # одиночный режим
        print("В колоду замешаны 2 оставшихся плана застройки бота. Поторопитесь выполнить планы застройки, чтобы успеть раньше него!")
        shuffle(cards)
    if input("Нажми 'ENTER' для продолжения игры или введите любой символ для завершения и подсчета очков") == "":
        wannaplay = True

# считаем очки бота за выполнение планов застройки

ai_plan_points = ai_plan_A_points + ai_plan_B_points + ai_plan_C_points

# считаем очки бота за рабочих, бассейны, заборы и парки
ai_workers = ai_set.count(workers)
ai_points_workers = ai_workers * ai_point_tuple[5]
if ai_workers == 0:
    ai_workers_place_points = 0
    print("У бота нет карточек с рабочими, поэтому за рабочих он получает 0 очков")
else:
    if input(f'''Количество карточек рабочих у бота - {ai_workers}. 
Если у вас меньше карточек с рабочими, чем у бота, введите 'да' - мы добавим боту 7 очков за первое место по рабочим.
Если у вас таких карточек больше - нажмите 'ENTER' - и добавьте 7 очков себе. Мы добавим боту 4 очка''') == "да":
        ai_workers_place_points = 7
        print("Мы добавили боту 7 очков")
    else:
        ai_workers_place_points = 4
        print("Мы добавили боту 4 очка")

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

# считаем очки за кварталы

ai_quarter_points_list = []

#здесь будет разница в количестве очков за элементы квартала в зависимости от уровня сложности. Пока ставлю по уровню сложности 1
app_bonus = ai_point_tuple[7]
realtor_mult = ai_point_tuple[8]

for quarter in ai_quarter_set_good:
    houses_in_quarter = 0
    points_per_quarter = 0
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

ai_quarter_points = sum(sorted(ai_quarter_points_list, reverse=True)[:5])

ai_vic_points = ai_plan_points + ai_points_workers +  ai_workers_place_points + ai_pools_points + ai_fences_points + ai_parks_points + ai_quarter_points
print(f'''Итоговая застройка бота: {ai_set}. 
{ai_point_tuple[1]} получает {ai_vic_points} очков, а именно:
{ai_plan_points} - количество очков за выолнение планов застройки, 
в том числе {ai_plan_A_points} за план "А", {ai_plan_B_points} за план "Б", {ai_plan_C_points} за план "В";
{ai_points_workers} - очки за рабочих;
{ai_workers_place_points} - очки за место по количеству рабочих;
{ai_pools_points} - очки за бассейны;
{ai_fences_points} - очки за заборы;
{ai_parks_points} - очки за скверы;
{ai_quarter_points} - очки за кварталы между заборами бота''')

print("Спасибо за игру")
