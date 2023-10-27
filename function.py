import telebot

bot = telebot.TeleBot("")

def welcome(message):
        photo = open("photo/main.jpeg", 'rb')
        bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Добро пожаловать в викторину, посвященную Военно-историческому музею артиллерии, инженерных войск и войск связи! Здесь вы сможете проверить свои знания о военной истории и узнать много интересного о военных технологиях и оружии. Приготовьтесь к захватывающему путешествию в прошлое!",
                     reply_markup=create_start_markup())
def reaction_on_text(message):
    bot.send_message(message.chat.id,
                     "Привет! Я бот, созданный для проведения викторины по военной истории. К сожалению, я не могу распознавать сообщения и отвечать на них. Однако, я готов задавать вам интересные вопросы и жду ваших ответов. Давайте начнем!",
                     reply_markup=create_start_markup())


def reaction_lets_start(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""Первый вопрос будет касаться военной техники.
Данное орудие предназначено для навесной стрельбы по открытым целям, поэтому на боевой позиции у этой пушки ствол поднят вверх. Как называется это орудие?

Выбери правильный ответ!""",
                    reply_markup=create_markup_start_question())

def reaction_true1(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/1.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Мортира — артиллерийское орудие с коротким стволом для навесной стрельбы. В Россию термин «мортира» проник при Петре I, когда артиллерийские орудия разделили на длинноствольные (пушки), средние (гаубицы) и короткоствольные (мортиры).</i>''', reply_markup=create_markup_test2(), parse_mode='html')

def reaction_no_true1(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/1.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Мортира — артиллерийское орудие с коротким стволом для навесной стрельбы. В Россию термин «мортира» проник при Петре I, когда артиллерийские орудия разделили на длинноствольные (пушки), средние (гаубицы) и короткоствольные (мортиры).</i>''', reply_markup=create_markup_test2(), parse_mode='html')

def create_markup_test2():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test2')
    markup.add(answer1)
    return markup

#Вопрос 2
def reaction_question2(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Второй вопрос.</b>
    
Какой массы были ядра пушки Инрог?""",
                    reply_markup=create_markup_start_question2(), parse_mode='html')

def create_markup_start_question2():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("2 кг", callback_data='no_true2')
    answer2 = telebot.types.InlineKeyboardButton("11 кг", callback_data='no_true2')
    answer3 = telebot.types.InlineKeyboardButton("27 кг", callback_data='true2')
    answer4 = telebot.types.InlineKeyboardButton("103 кг", callback_data='no_true2')
    markup.add(answer1, answer2, answer3, answer4)
    return markup

def reaction_true2(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/2.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Железные ядра весили примерно 27 кг.</i>''', reply_markup=create_markup_test3(), parse_mode='html')

def reaction_no_true2(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/2.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Железные ядра весили примерно 27 кг.</i>''', reply_markup=create_markup_test3(), parse_mode='html')

def create_markup_test3():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test3')
    markup.add(answer1)
    return markup

#Вопрос 3
def reaction_question3(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Третий вопрос</b>.

Кто сказал следующие слова: «Пушки – ключ к городу»?""",
                     reply_markup=create_markup_start_question3(), parse_mode='html')


def create_markup_start_question3():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Петр I", callback_data='no_true3')
    answer2 = telebot.types.InlineKeyboardButton("Иван Грозный", callback_data='no_true3')
    answer3 = telebot.types.InlineKeyboardButton("Карл Смелый", callback_data='true3')
    answer4 = telebot.types.InlineKeyboardButton("Филипп II", callback_data='no_true3')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true3(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/3.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Карл Смелый последний герцог Бургундии из династии Валуа, сын герцога Филиппа Доброго, говорил: “Пушки – ключ к городу”.</i>''', reply_markup=create_markup_test4(), parse_mode='html')


def reaction_no_true3(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/3.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Карл Смелый последний герцог Бургундии из династии Валуа, сын герцога Филиппа Доброго, говорил: “Пушки – ключ к городу”.</i>''', reply_markup=create_markup_test4(), parse_mode='html')


def create_markup_test4():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test4')
    markup.add(answer1)
    return markup

#Вопрос 4
def reaction_question4(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Четвертый вопрос</b>.

Для уничтожения каких целей использовалась 280-мм береговая пушка?""",
                     reply_markup=create_markup_start_question4(), parse_mode='html')


def create_markup_start_question4():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Корабли", callback_data='no_true4')
    answer2 = telebot.types.InlineKeyboardButton("Укрепления", callback_data='no_true4')
    answer3 = telebot.types.InlineKeyboardButton("Крупные скопления пехоты", callback_data='no_true4')
    answer4 = telebot.types.InlineKeyboardButton("Все варианты", callback_data='true4')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true4(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/4.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Орудие использовали как береговое, так и осадное. Таким образом его использовали для поражения всех вышеперечисленных целей.</i>''', reply_markup=create_markup_test5(), parse_mode='html')


def reaction_no_true4(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/4.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Орудие использовали как береговое, так и осадное. Таким образом его использовали для поражения всех вышеперечисленных целей.</i>''', reply_markup=create_markup_test5(), parse_mode='html')


def create_markup_test5():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test5')
    markup.add(answer1)
    return markup

#Вопрос 5
def reaction_question5(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Пятый вопрос</b>.

Почему средневековые орудия имели такие толстые стенки ствола?""",
                     reply_markup=create_markup_start_question5(), parse_mode='html')


def create_markup_start_question5():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Из-за несовершенства технологии производства", callback_data='true5')
    answer2 = telebot.types.InlineKeyboardButton("Чтобы устрашать врага", callback_data='no_true5')
    answer3 = telebot.types.InlineKeyboardButton("Для повышения поражающего действия снаряда", callback_data='no_true5')
    answer4 = telebot.types.InlineKeyboardButton("Все варианты", callback_data='no_true5')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true5(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/5.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>В то время технологические ограничения не позволяли мастерам идеально подгонять снаряды под диаметр ствола. Иногда из-за этого несовершенства зазор между ядром и стенками ствола доходил до нескольких миллиметров, поэтому мастера делали стенки ствола толще, чтобы повысить прочность орудия.</i>''', reply_markup=create_markup_test6(), parse_mode='html')


def reaction_no_true5(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/5.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>В то время технологические ограничения не позволяли мастерам идеально подгонять снаряды под диаметр ствола. Иногда из-за этого несовершенства зазор между ядром и стенками ствола доходил до нескольких миллиметров, поэтому мастера делали стенки ствола толще, чтобы повысить прочность орудия.</i>''', reply_markup=create_markup_test6(), parse_mode='html')


def create_markup_test6():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test6')
    markup.add(answer1)
    return markup

#Вопрос 6
def reaction_question6(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Шестой вопрос</b>.

Орудия какого мастера конца XVI – начала XVII в сравнительно большом количестве представлены в музее?""",
                     reply_markup=create_markup_start_question6(), parse_mode='html')


def create_markup_start_question6():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Андрей Чохов", callback_data='true6')
    answer2 = telebot.types.InlineKeyboardButton("мастер Игнатий", callback_data='no_true6')
    answer3 = telebot.types.InlineKeyboardButton("Клавдий Фреми", callback_data='no_true6')
    answer4 = telebot.types.InlineKeyboardButton("Н.В. Маиевский", callback_data='no_true6')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true6(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/6.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Мастер Андрей Чохов отлил пушку «Инрог», мортиру «Егун», а также под его надзором отливалась мортира «Самозванец». Все вышеперечисленные орудия представлены в музее.</i>''', reply_markup=create_markup_test7(), parse_mode='html')


def reaction_no_true6(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/6.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Мастер Андрей Чохов отлил пушку «Инрог», мортиру «Егун», а также под его надзором отливалась мортира «Самозванец». Все вышеперечисленные орудия представлены в музее.</i>''', reply_markup=create_markup_test7(), parse_mode='html')


def create_markup_test7():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test7')
    markup.add(answer1)
    return markup

#Вопрос 7
def reaction_question7(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Седьмой вопрос</b>.

Про какое орудие во время его испытаний сказали: «сии инвестиции в настоящем употреблении полезны быть не могут»?""",
                     reply_markup=create_markup_start_question7(), parse_mode='html')


def create_markup_start_question7():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("«Секретная» гаубица", callback_data='no_true7')
    answer2 = telebot.types.InlineKeyboardButton("105-ти ствольная скорострельная батарейка", callback_data='no_true7')
    answer3 = telebot.types.InlineKeyboardButton("«Потешная» пушка", callback_data='no_true7')
    answer4 = telebot.types.InlineKeyboardButton("25-ти ствольная мортирная батарея", callback_data='true7')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true7(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/7.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>В 1762 году проводились испытания 25-ти ствольной мортирной батареи, резолюция которых звучала так: "сии инвестиции в настоящем употреблении полезны быть не могут".</i>''', reply_markup=create_markup_test8(), parse_mode='html')


def reaction_no_true7(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/7.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>В 1762 году проводились испытания 25-ти ствольной мортирной батареи, резолюция которых звучала так: "сии инвестиции в настоящем употреблении полезны быть не могут".</i>''', reply_markup=create_markup_test8(), parse_mode='html')


def create_markup_test8():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test8')
    markup.add(answer1)
    return markup

#8 вопрос
def reaction_question8(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Восьмой вопрос</b>.

В каком веке появилось первое русское артиллерийское орудие с нарезным стволом?""",
                     reply_markup=create_markup_start_question8(), parse_mode='html')


def create_markup_start_question8():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("XV", callback_data='no_true8')
    answer2 = telebot.types.InlineKeyboardButton("XVII", callback_data='no_true8')
    answer3 = telebot.types.InlineKeyboardButton("XIX", callback_data='true8')
    answer4 = telebot.types.InlineKeyboardButton("XXI", callback_data='no_true8')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true8(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/8.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Полевая пушка образца 1867 г, сконструированная Н.В. Маиевсским, стала первым русским артиллерийским орудием с нарезным стволом.</i>''', reply_markup=create_markup_test9(), parse_mode='html')


def reaction_no_true8(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/8.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Полевая пушка образца 1867 г, сконструированная Н.В. Маиевсским, стала первым русским артиллерийским орудием с нарезным стволом.</i>''', reply_markup=create_markup_test9(), parse_mode='html')


def create_markup_test9():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test9')
    markup.add(answer1)
    return markup

#9 вопрос
def reaction_question9(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Девятый вопрос</b>.

Чем хороша пуша с нарезным каналом ствола?""",
                     reply_markup=create_markup_start_question9(), parse_mode='html')


def create_markup_start_question9():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Красивее выглядит", callback_data='no_true9')
    answer2 = telebot.types.InlineKeyboardButton("Стреляет дальше", callback_data='no_true9')
    answer3 = telebot.types.InlineKeyboardButton("Стреляет точнее", callback_data='true9')
    answer4 = telebot.types.InlineKeyboardButton("Имеет большее поражающее действие", callback_data='no_true9')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true9(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/9.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Придание вращения снаряду вокруг его продольной оси во время стрельбы для стабилизации снаряда в продольном направлении за счет сохранения момента импульса, улучшает его аэродинамическую устойчивость и точность по сравнению с гладкоствольными конструкциями</i>''', reply_markup=create_markup_test10(), parse_mode='html')


def reaction_no_true9(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/9.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Придание вращения снаряду вокруг его продольной оси во время стрельбы для стабилизации снаряда в продольном направлении за счет сохранения момента импульса, улучшает его аэродинамическую устойчивость и точность по сравнению с гладкоствольными конструкциями</i>''', reply_markup=create_markup_test10(), parse_mode='html')


def create_markup_test10():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test10')
    markup.add(answer1)
    return markup
#10 вопрос
def reaction_question10(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Деcятый вопрос</b>.

Почему немецкие солдаты называли 76-мм пушку «Ратш-бум»?""",
                     reply_markup=create_markup_start_question10(), parse_mode='html')


def create_markup_start_question10():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Потому что она русская", callback_data='no_true10')
    answer2 = telebot.types.InlineKeyboardButton("Скорость снаряда опережала скорость звука выстрела", callback_data='true10')
    answer3 = telebot.types.InlineKeyboardButton("Снаряд вылетал с огромной вспышкой пламени", callback_data='no_true10')
    answer4 = telebot.types.InlineKeyboardButton("Снаряд орудия взрывался в воздухе", callback_data='no_true10')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true10(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/10.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Немецких войсках советские дивизионки называли «ратш-бум» — звук пролетающего со сверхзвуковой скоростью снаряда был слышен чуть раньше, чем долетал звук выстрела.</i>''', reply_markup=create_markup_test11(), parse_mode='html')


def reaction_no_true10(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/10.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Немецких войсках советские дивизионки называли «ратш-бум» — звук пролетающего со сверхзвуковой скоростью снаряда был слышен чуть раньше, чем долетал звук выстрела.</i>''', reply_markup=create_markup_test11(), parse_mode='html')


def create_markup_test11():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test11')
    markup.add(answer1)
    return markup

#11 вопрос
def reaction_question11(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Одиннацатый вопрос.</b>

Как называлась пушка, подаренная в детстве Петру I его отцом?""",
                     reply_markup=create_markup_start_question11(), parse_mode='html')


def create_markup_start_question11():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Игрушечная", callback_data='no_true11')
    answer2 = telebot.types.InlineKeyboardButton("Смешная", callback_data='no_true11')
    answer3 = telebot.types.InlineKeyboardButton("Потешная", callback_data='true11')
    answer4 = telebot.types.InlineKeyboardButton("Секретная", callback_data='no_true11')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true11(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/11.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Алексей Михайлович подарил молодому Петру «Потешную» пушку. Будущий император активно применял её в своих играх с потешными полками.</i>''', reply_markup=create_markup_test12(), parse_mode='html')


def reaction_no_true11(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/11.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Алексей Михайлович подарил молодому Петру «Потешную» пушку. Будущий император активно применял её в своих играх с потешными полками.</i>''', reply_markup=create_markup_test12(), parse_mode='html')


def create_markup_test12():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test12')
    markup.add(answer1)
    return markup

#12 вопрос
def reaction_question12(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Двенацатый вопрос.</b>

Кто изобрел принцип работы радио?""",
                     reply_markup=create_markup_start_question12(), parse_mode='html')


def create_markup_start_question12():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Александр Греков", callback_data='no_true12')
    answer2 = telebot.types.InlineKeyboardButton("Гульельмо Маркони", callback_data='no_true12')
    answer3 = telebot.types.InlineKeyboardButton("Александр Попов", callback_data='true12')
    answer4 = telebot.types.InlineKeyboardButton("Лев Термен", callback_data='no_true12')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true12(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/12.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>7 мая 1895 года Александр Попов прочел в Санкт-Петербургском университете лекцию «Об отношении металлических порошков к электрическим колебаниям» и продемонстрировал тот самый революционный прибор, который мог передавать сигналы без проводов. Этот день стал днем рождения радио.</i>''', reply_markup=create_markup_test13(), parse_mode='html')


def reaction_no_true12(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/12.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>7 мая 1895 года Александр Попов прочел в Санкт-Петербургском университете лекцию «Об отношении металлических порошков к электрическим колебаниям» и продемонстрировал тот самый революционный прибор, который мог передавать сигналы без проводов. Этот день стал днем рождения радио.</i>''', reply_markup=create_markup_test13(), parse_mode='html')


def create_markup_test13():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test13')
    markup.add(answer1)
    return markup

#13 вопрос
def reaction_question13(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Тринадцатый вопрос.</b>

В каком году в России началось регулярное радиовещание?""",
                     reply_markup=create_markup_start_question13(), parse_mode='html')


def create_markup_start_question13():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("1924", callback_data='true13')
    answer2 = telebot.types.InlineKeyboardButton("1922", callback_data='no_true13')
    answer3 = telebot.types.InlineKeyboardButton("1919", callback_data='no_true13')
    answer4 = telebot.types.InlineKeyboardButton("1916", callback_data='no_true13')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true13(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/13.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Регулярное радиовещание началось 23 ноября 1924 года, когда в эфир был передан первый номер радиогазеты. В программах вещания значительное место занимали трансляции партийных съездов, конференций, передачи для детей, образовательные программы.</i>''', reply_markup=create_markup_test14(), parse_mode='html')


def reaction_no_true13(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/13.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Регулярное радиовещание началось 23 ноября 1924 года, когда в эфир был передан первый номер радиогазеты. В программах вещания значительное место занимали трансляции партийных съездов, конференций, передачи для детей, образовательные программы.</i>''', reply_markup=create_markup_test14(), parse_mode='html')


def create_markup_test14():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test14')
    markup.add(answer1)
    return markup

#14 вопрос
def reaction_question14(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Четырнадцатый вопрос.</b>

Кто был главным человеком (нарком) в войсках связи СССР во времена Великой Отечественной войны?""",
                     reply_markup=create_markup_start_question14(), parse_mode='html')


def create_markup_start_question14():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Иван Терентьевич Пересыпкин", callback_data='true14')
    answer2 = telebot.types.InlineKeyboardButton("Матвей Давыдович Берман", callback_data='no_true14')
    answer3 = telebot.types.InlineKeyboardButton("Константин Яковлевич Сергейчук", callback_data='no_true14')
    answer4 = telebot.types.InlineKeyboardButton("Иннокентий Андреевич Халепский", callback_data='no_true14')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true14(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/14.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Пересыпкин во время Великой Отечественной войны обеспечивал управление войсками связи и обеспечение связью действующей армии. Лично выезжал на фронт 24 раза (некоторые его командировки на фронт превышали 2-3 месяца)</i>''', reply_markup=create_markup_test15(), parse_mode='html')


def reaction_no_true14(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/14.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Пересыпкин во время Великой Отечественной войны обеспечивал управление войсками связи и обеспечение связью действующей армии. Лично выезжал на фронт 24 раза (некоторые его командировки на фронт превышали 2-3 месяца)</i>''', reply_markup=create_markup_test15(), parse_mode='html')


def create_markup_test15():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test15')
    markup.add(answer1)
    return markup
#15 вопрос
def reaction_question15(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Пятнадцатый вопрос.</b>

Какая была дальность связи в телеграфном режиме у корабельного радиопередатчика образца 1938 года «Шквал»""",
                     reply_markup=create_markup_start_question15(), parse_mode='html')


def create_markup_start_question15():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("500 км", callback_data='no_true15')
    answer2 = telebot.types.InlineKeyboardButton("750 км", callback_data='no_true15')
    answer3 = telebot.types.InlineKeyboardButton("1000 км", callback_data='true15')
    answer4 = telebot.types.InlineKeyboardButton("600 км", callback_data='no_true15')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true15(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/15.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>1000 км. Использовался в штабах флота, на крейсерских подводных лодках и кораблях 1-го ранга. Имел дальность до 500 км в телефонном режиме.</i>''', reply_markup=create_markup_test16(), parse_mode='html')


def reaction_no_true15(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/15.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>1000 км. Использовался в штабах флота, на крейсерских подводных лодках и кораблях 1-го ранга. Имел дальность до 500 км в телефонном режиме.</i>''', reply_markup=create_markup_test16(), parse_mode='html')


def create_markup_test16():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test16')
    markup.add(answer1)
    return markup

#16 вопрос
def reaction_question16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Шестнадцатый вопрос.</b>

Какой подвиг связистов в период блокады Ленинграда был совершен?""",
                     reply_markup=create_markup_start_question16(), parse_mode='html')


def create_markup_start_question16():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Проведение связи с Москвой", callback_data='no_true16')
    answer2 = telebot.types.InlineKeyboardButton("Обновленные версии радиостанций", callback_data='no_true16')
    answer3 = telebot.types.InlineKeyboardButton("Прокладка морского кабеля по дну Ладожского озера", callback_data='true16')
    answer4 = telebot.types.InlineKeyboardButton("Улучшенная версия шифрования связи", callback_data='no_true16')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/16.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>Прокладка морского кабеля по дну Ладожского озера. Линия связи была проложена 29 октября 1941 г., вступила в строй на следующий день и бесперебойно работала все 900 дней блокады</i>''', reply_markup=create_markup_test17(), parse_mode='html')


def reaction_no_true16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/16.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>Прокладка морского кабеля по дну Ладожского озера. Линия связи была проложена 29 октября 1941 г., вступила в строй на следующий день и бесперебойно работала все 900 дней блокады</i>''', reply_markup=create_markup_test17(), parse_mode='html')


def create_markup_test17():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test17')
    markup.add(answer1)
    return markup

#17 вопрос
def reaction_question17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Семнадцатый вопрос.</b>

Как назывался длиннодревковый боевой топор с лезвием в форме полумесяца, который стоял на вооружении русской пехоты и конных воинов в XV – XVII  веках.""",
                     reply_markup=create_markup_start_question17(), parse_mode='html')


def create_markup_start_question17():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Алебарда", callback_data='no_true17')
    answer2 = telebot.types.InlineKeyboardButton("Кистень", callback_data='no_true17')
    answer3 = telebot.types.InlineKeyboardButton("Томагавк", callback_data='no_true17')
    answer4 = telebot.types.InlineKeyboardButton("Бердыш", callback_data='true17')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/17.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>По сказаниям иностранцев, вооружённые саблями и бердышами военнослужащие русского войска, или «бердышники», считались лучшей пехотой. Практическим аналогом бердыша был западноевропейский бардуций (barducium) и алебарда.</i>''', reply_markup=create_markup_test18(), parse_mode='html')


def reaction_no_true17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/17.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>По сказаниям иностранцев, вооружённые саблями и бердышами военнослужащие русского войска, или «бердышники», считались лучшей пехотой. Практическим аналогом бердыша был западноевропейский бардуций (barducium) и алебарда.</i>''', reply_markup=create_markup_test18(), parse_mode='html')


def create_markup_test18():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test18')
    markup.add(answer1)
    return markup
#18 вопрос
def reaction_question18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Восемнадцатый вопрос</b>.

В каком веке были популярны такие виды стрелкового оружия как штуцер и мушкет?""", reply_markup=create_markup_start_question18(), parse_mode='html')


def create_markup_start_question18():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("XVI - XVII", callback_data='no_true18')
    answer2 = telebot.types.InlineKeyboardButton("XVI – XVIII", callback_data='true18')
    answer3 = telebot.types.InlineKeyboardButton("XIV", callback_data='no_true18')
    answer4 = telebot.types.InlineKeyboardButton("XIX", callback_data='no_true18')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/18.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>C удешевлением штуцера ближе к концу XVIII века стал появляться и на вооружении лёгкой пехоты (стрелков, егерей) многих европейских армий, действующей в рассыпном строю и редко вступающей в штыковой бой.</i>''', reply_markup=create_markup_test19(), parse_mode='html')


def reaction_no_true18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/18.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>C удешевлением штуцера ближе к концу XVIII века стал появляться и на вооружении лёгкой пехоты (стрелков, егерей) многих европейских армий, действующей в рассыпном строю и редко вступающей в штыковой бой.</i>''', reply_markup=create_markup_test19(), parse_mode='html')


def create_markup_test19():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test19')
    markup.add(answer1)
    return markup
#19 вопрос
def reaction_question19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Девятнадцатый вопрос.</b>

В каком городе производится автомат Калашникова?""", reply_markup=create_markup_start_question19(), parse_mode='html')


def create_markup_start_question19():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Тула", callback_data='no_true19')
    answer2 = telebot.types.InlineKeyboardButton("Ижевск", callback_data='true19')
    answer3 = telebot.types.InlineKeyboardButton("Самара", callback_data='no_true19')
    answer4 = telebot.types.InlineKeyboardButton("Саратов", callback_data='no_true19')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/20.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b>

Ответ: <i>В 1950-х годах лицензии на производство АК были переданы СССР 18 странам (главным образом, союзникам по Варшавскому договору).
Особенно активно выпускают подобия автомата Калашникова польское предприятие «Бумар» и болгарская фирма «Арсенал», которая в настоящее время открыла филиал в США и наладила там выпуск автоматов</i>''', reply_markup=create_markup_test20(), parse_mode='html')


def reaction_no_true19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/20.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>В 1950-х годах лицензии на производство АК были переданы СССР 18 странам (главным образом, союзникам по Варшавскому договору).
Особенно активно выпускают подобия автомата Калашникова польское предприятие «Бумар» и болгарская фирма «Арсенал», которая в настоящее время открыла филиал в США и наладила там выпуск автоматов</i>''', reply_markup=create_markup_test20(), parse_mode='html')


def create_markup_test20():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test20')
    markup.add(answer1)
    return markup

#20 вопрос
def reaction_question20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Двацатый вопрос.</b>

Какая из перечисленных стран производит собственные варианты на базе АК?""", reply_markup=create_markup_start_question20(), parse_mode='html')


def create_markup_start_question20():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Казахстан", callback_data='no_true20')
    answer2 = telebot.types.InlineKeyboardButton("Индия", callback_data='true20')
    answer3 = telebot.types.InlineKeyboardButton("Зимбабве", callback_data='no_true20')
    answer4 = telebot.types.InlineKeyboardButton("Америка", callback_data='no_true20')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/21.jpeg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили верно!</b> 

Ответ: <i>В Индии стартовал долгожданный проект по производству автоматов Калашникова АК-203. О начале выпуска АК-203 на заводе Korwa Ordnance Factory в Амети в штате Уттар-Прадеш 17 января сообщила пресс-служба "Рособоронэкспорта". По данным источника, в производственных планах совместного предприятия Indo-Russian Rifles Private Limited заложена 100-процентная локализация производства автоматов АК-203 в Индии.</i>''', reply_markup=create_markup_end(), parse_mode='html')


def reaction_no_true20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    photo = open("photo/21.jpeg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''<b>Вы ответили неверно!</b> Но не расстраивайтесь. 

Ответ: <i>В Индии стартовал долгожданный проект по производству автоматов Калашникова АК-203. О начале выпуска АК-203 на заводе Korwa Ordnance Factory в Амети в штате Уттар-Прадеш 17 января сообщила пресс-служба "Рособоронэкспорта". По данным источника, в производственных планах совместного предприятия Indo-Russian Rifles Private Limited заложена 100-процентная локализация производства автоматов АК-203 в Индии.</i>''', reply_markup=create_markup_end(), parse_mode='html')

#Остальное
def create_markup_end():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Конец :)", callback_data='about_us')
    markup.add(answer1)
    return markup
def reaction_about_us(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="""<b>Создатели:</b>

Главный по пушкам @tovarishpointeresam
Главный по оружию:@RiaIII
Главный по связи: @ster1ing
Главный по боту: @danp1t""",
                     reply_markup=create_start_markup(), parse_mode='html')

def create_markup_start_question():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Пищаль", callback_data='no_true1')
    answer2 = telebot.types.InlineKeyboardButton("Мортира", callback_data='true1')
    answer3 = telebot.types.InlineKeyboardButton("Бомбарда", callback_data='no_true1')
    answer4 = telebot.types.InlineKeyboardButton("Зенитное орудие", callback_data='no_true1')
    markup.add(answer1, answer2, answer3, answer4)
    return markup
def create_start_markup():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    lessons = telebot.types.InlineKeyboardButton("Начать прохождение викторины", callback_data='lets_start')
    questions = telebot.types.InlineKeyboardButton("О нас", callback_data='about_us')
    markup.add(lessons, questions)
    return markup
