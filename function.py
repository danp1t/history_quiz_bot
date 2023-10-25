import telebot

bot = telebot.TeleBot("") #TOKEN BOT

def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать в викторину, посвященную Военно-историческому музею артиллерии, инженерных войск и войск связи! Здесь вы сможете проверить свои знания о военной истории и узнать много интересного о военных технологиях и оружии. Приготовьтесь к захватывающему путешествию в прошлое!",
                     reply_markup=create_start_markup())

def reaction_on_text(message):
    bot.send_message(message.chat.id,
                     "Привет! Я бот, созданный для проведения викторины по военной истории. К сожалению, я не могу распознавать сообщения и отвечать на них. Однако, я готов задавать вам интересные вопросы и жду ваших ответов. Давайте начнем!",
                     reply_markup=create_start_markup())

def reaction_lets_start(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Первый вопрос будет касаться военной техники.
Данное орудие предназначено для навесной стрельбы по открытым целям, поэтому на боевой позиции у этой пушки ствол поднят вверх. Как называется это орудие?

Выбери правильный ответ!""",
                    reply_markup=create_markup_start_question())

def reaction_true1(call):
    photo = open("photo/1.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Мортира — артиллерийское орудие с коротким стволом для навесной стрельбы. В Россию термин «мортира» проник при Петре I, когда артиллерийские орудия разделили на длинноствольные (пушки), средние (гаубицы) и короткоствольные (мортиры).''', reply_markup=create_markup_test2())

def reaction_no_true1(call):
    photo = open("photo/1.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Мортира — артиллерийское орудие с коротким стволом для навесной стрельбы. В Россию термин «мортира» проник при Петре I, когда артиллерийские орудия разделили на длинноствольные (пушки), средние (гаубицы) и короткоствольные (мортиры).''', reply_markup=create_markup_test2())

def create_markup_test2():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test2')
    markup.add(answer1)
    return markup

#Вопрос 2
def reaction_question2(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Второй вопрос.
    
Какой массы были ядра пушки Инрог?""",
                    reply_markup=create_markup_start_question2())

def create_markup_start_question2():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("2 кг", callback_data='no_true2')
    answer2 = telebot.types.InlineKeyboardButton("11 кг", callback_data='no_true2')
    answer3 = telebot.types.InlineKeyboardButton("27 кг", callback_data='true2')
    answer4 = telebot.types.InlineKeyboardButton("103 кг", callback_data='no_true2')
    markup.add(answer1, answer2, answer3, answer4)
    return markup

def reaction_true2(call):
    photo = open("photo/2.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Железные ядра весили примерно 27 кг.''', reply_markup=create_markup_test3())

def reaction_no_true2(call):
    photo = open("photo/2.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Железные ядра весили примерно 27 кг.''', reply_markup=create_markup_test3())

def create_markup_test3():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test3')
    markup.add(answer1)
    return markup

#Вопрос 3
def reaction_question3(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Третий вопрос.

Кто сказал следующие слова: «Пушки – ключ к городу»?""",
                     reply_markup=create_markup_start_question3())


def create_markup_start_question3():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Петр I", callback_data='no_true3')
    answer2 = telebot.types.InlineKeyboardButton("Иван Грозный", callback_data='no_true3')
    answer3 = telebot.types.InlineKeyboardButton("Карл Смелый", callback_data='true3')
    answer4 = telebot.types.InlineKeyboardButton("Филипп II", callback_data='no_true3')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true3(call):
    photo = open("photo/3.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Карл Смелый последний герцог Бургундии из династии Валуа, сын герцога Филиппа Доброго, говорил: “Пушки – ключ к городу”.''', reply_markup=create_markup_test4())


def reaction_no_true3(call):
    photo = open("photo/3.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Карл Смелый последний герцог Бургундии из династии Валуа, сын герцога Филиппа Доброго, говорил: “Пушки – ключ к городу”.''', reply_markup=create_markup_test4())


def create_markup_test4():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test4')
    markup.add(answer1)
    return markup

#Вопрос 4
def reaction_question4(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Четвертый вопрос.

Для уничтожения каких целей использовалась 280-мм береговая пушка?""",
                     reply_markup=create_markup_start_question4())


def create_markup_start_question4():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Корабли", callback_data='no_true4')
    answer2 = telebot.types.InlineKeyboardButton("Укрепления", callback_data='no_true4')
    answer3 = telebot.types.InlineKeyboardButton("Крупные скопления пехоты", callback_data='no_true4')
    answer4 = telebot.types.InlineKeyboardButton("Все варианты", callback_data='true4')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true4(call):
    photo = open("photo/4.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Орудие использовали как береговое, так и осадное. Таким образом его использовали для поражения всех вышеперечисленных целей.''', reply_markup=create_markup_test5())


def reaction_no_true4(call):
    photo = open("photo/4.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Орудие использовали как береговое, так и осадное. Таким образом его использовали для поражения всех вышеперечисленных целей.''', reply_markup=create_markup_test5())


def create_markup_test5():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test5')
    markup.add(answer1)
    return markup

#Вопрос 5
def reaction_question5(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Пятый вопрос.

Почему средневековые орудия имели такие толстые стенки ствола?""",
                     reply_markup=create_markup_start_question5())


def create_markup_start_question5():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Из-за несовершенства технологии производства", callback_data='true5')
    answer2 = telebot.types.InlineKeyboardButton("Чтобы устрашать врага", callback_data='no_true5')
    answer3 = telebot.types.InlineKeyboardButton("Для повышения поражающего действия снаряда", callback_data='no_true5')
    answer4 = telebot.types.InlineKeyboardButton("Все варианты", callback_data='no_true5')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true5(call):
    photo = open("photo/5.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: В то время технологические ограничения не позволяли мастерам идеально подгонять снаряды под диаметр ствола. Иногда из-за этого несовершенства зазор между ядром и стенками ствола доходил до нескольких миллиметров, поэтому мастера делали стенки ствола толще, чтобы повысить прочность орудия.''', reply_markup=create_markup_test6())


def reaction_no_true5(call):
    photo = open("photo/5.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: В то время технологические ограничения не позволяли мастерам идеально подгонять снаряды под диаметр ствола. Иногда из-за этого несовершенства зазор между ядром и стенками ствола доходил до нескольких миллиметров, поэтому мастера делали стенки ствола толще, чтобы повысить прочность орудия.''', reply_markup=create_markup_test6())


def create_markup_test6():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test6')
    markup.add(answer1)
    return markup

#Вопрос 6
def reaction_question6(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Шестой вопрос.

Орудия какого мастера конца XVI – начала XVII в сравнительно большом количестве представлены в музее?""",
                     reply_markup=create_markup_start_question6())


def create_markup_start_question6():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Андрей Чохов", callback_data='true6')
    answer2 = telebot.types.InlineKeyboardButton("мастер Игнатий", callback_data='no_true6')
    answer3 = telebot.types.InlineKeyboardButton("Клавдий Фреми", callback_data='no_true6')
    answer4 = telebot.types.InlineKeyboardButton("Н.В. Маиевский", callback_data='no_true6')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true6(call):
    photo = open("photo/6.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Мастер Андрей Чохов отлил пушку «Инрог», мортиру «Егун», а также под его надзором отливалась мортира «Самозванец». Все вышеперечисленные орудия представлены в музее.''', reply_markup=create_markup_test7())


def reaction_no_true6(call):
    photo = open("photo/6.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Мастер Андрей Чохов отлил пушку «Инрог», мортиру «Егун», а также под его надзором отливалась мортира «Самозванец». Все вышеперечисленные орудия представлены в музее.''', reply_markup=create_markup_test7())


def create_markup_test7():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test7')
    markup.add(answer1)
    return markup

#Вопрос 7
def reaction_question7(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Седьмой вопрос.

Про какое орудие во время его испытаний сказали: «сии инвестиции в настоящем употреблении полезны быть не могут»?""",
                     reply_markup=create_markup_start_question7())


def create_markup_start_question7():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("«Секретная» гаубица", callback_data='no_true7')
    answer2 = telebot.types.InlineKeyboardButton("105-ти ствольная скорострельная батарейка", callback_data='no_true7')
    answer3 = telebot.types.InlineKeyboardButton("«Потешная» пушка", callback_data='no_true7')
    answer4 = telebot.types.InlineKeyboardButton("25-ти ствольная мортирная батарея", callback_data='true7')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true7(call):
    photo = open("photo/7.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: В 1762 году проводились испытания 25-ти ствольной мортирной батареи, резолюция которых звучала так: "сии инвестиции в настоящем употреблении полезны быть не могут".''', reply_markup=create_markup_test8())


def reaction_no_true7(call):
    photo = open("photo/7.png", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: В 1762 году проводились испытания 25-ти ствольной мортирной батареи, резолюция которых звучала так: "сии инвестиции в настоящем употреблении полезны быть не могут".''', reply_markup=create_markup_test8())


def create_markup_test8():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test8')
    markup.add(answer1)
    return markup

#8 вопрос
def reaction_question8(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Восьмой вопрос.

В каком веке появилось первое русское артиллерийское орудие с нарезным стволом?""",
                     reply_markup=create_markup_start_question8())


def create_markup_start_question8():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("XV", callback_data='no_true8')
    answer2 = telebot.types.InlineKeyboardButton("XVII", callback_data='no_true8')
    answer3 = telebot.types.InlineKeyboardButton("XIX", callback_data='true8')
    answer4 = telebot.types.InlineKeyboardButton("XXI", callback_data='no_true8')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true8(call):
    photo = open("photo/8.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Полевая пушка образца 1867 г, сконструированная Н.В. Маиевсским, стала первым русским артиллерийским орудием с нарезным стволом.''', reply_markup=create_markup_test9())


def reaction_no_true8(call):
    photo = open("photo/8.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Полевая пушка образца 1867 г, сконструированная Н.В. Маиевсским, стала первым русским артиллерийским орудием с нарезным стволом.''', reply_markup=create_markup_test9())


def create_markup_test9():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test9')
    markup.add(answer1)
    return markup

#9 вопрос
def reaction_question9(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Девятый вопрос.

Чем хороша пуша с нарезным каналом ствола?""",
                     reply_markup=create_markup_start_question9())


def create_markup_start_question9():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Красивее выглядит", callback_data='no_true9')
    answer2 = telebot.types.InlineKeyboardButton("Стреляет дальше", callback_data='no_true9')
    answer3 = telebot.types.InlineKeyboardButton("Стреляет точнее", callback_data='true9')
    answer4 = telebot.types.InlineKeyboardButton("Имеет большее поражающее действие", callback_data='no_true9')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true9(call):
    photo = open("photo/9.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Придание вращения снаряду вокруг его продольной оси во время стрельбы для стабилизации снаряда в продольном направлении за счет сохранения момента импульса, улучшает его аэродинамическую устойчивость и точность по сравнению с гладкоствольными конструкциями''', reply_markup=create_markup_test10())


def reaction_no_true9(call):
    photo = open("photo/9.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Придание вращения снаряду вокруг его продольной оси во время стрельбы для стабилизации снаряда в продольном направлении за счет сохранения момента импульса, улучшает его аэродинамическую устойчивость и точность по сравнению с гладкоствольными конструкциями''', reply_markup=create_markup_test10())


def create_markup_test10():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test10')
    markup.add(answer1)
    return markup
#10 вопрос
def reaction_question10(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Деcятый вопрос.

Почему немецкие солдаты называли 76-мм пушку «Ратш-бум»?""",
                     reply_markup=create_markup_start_question10())


def create_markup_start_question10():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Потому что она русская", callback_data='no_true10')
    answer2 = telebot.types.InlineKeyboardButton("Скорость снаряда опережала скорость звука выстрела", callback_data='true10')
    answer3 = telebot.types.InlineKeyboardButton("Снаряд вылетал с огромной вспышкой пламени", callback_data='no_true10')
    answer4 = telebot.types.InlineKeyboardButton("Снаряд орудия взрывался в воздухе", callback_data='no_true10')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true10(call):
    photo = open("photo/10.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Немецких войсках советские дивизионки называли «ратш-бум» — звук пролетающего со сверхзвуковой скоростью снаряда был слышен чуть раньше, чем долетал звук выстрела.''', reply_markup=create_markup_test11())


def reaction_no_true10(call):
    photo = open("photo/10.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Немецких войсках советские дивизионки называли «ратш-бум» — звук пролетающего со сверхзвуковой скоростью снаряда был слышен чуть раньше, чем долетал звук выстрела.''', reply_markup=create_markup_test11())


def create_markup_test11():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Следующий вопрос", callback_data='test11')
    markup.add(answer1)
    return markup

#11 вопрос
def reaction_question11(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Одиннацатый вопрос.

Как называлась пушка, подаренная в детстве Петру I его отцом?""",
                     reply_markup=create_markup_start_question11())


def create_markup_start_question11():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Игрушечная", callback_data='no_true11')
    answer2 = telebot.types.InlineKeyboardButton("Смешная", callback_data='no_true11')
    answer3 = telebot.types.InlineKeyboardButton("Потешная", callback_data='true11')
    answer4 = telebot.types.InlineKeyboardButton("Секретная", callback_data='no_true11')
    markup.add(answer1, answer2, answer3, answer4)
    return markup


def reaction_true11(call):
    photo = open("photo/11.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили верно! 

Ответ: Алексей Михайлович подарил молодому Петру «Потешную» пушку. Будущий император активно применял её в своих играх с потешными полками.''', reply_markup=create_markup_test12())


def reaction_no_true11(call):
    photo = open("photo/11.jpg", 'rb')
    bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='''Вы ответили неверно! Но не расстраивайтесь. 

Ответ: Алексей Михайлович подарил молодому Петру «Потешную» пушку. Будущий император активно применял её в своих играх с потешными полками.''', reply_markup=create_markup_test12())


def create_markup_test12():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    answer1 = telebot.types.InlineKeyboardButton("Конец :)", callback_data='about_us')
    markup.add(answer1)
    return markup
#Остальное
def reaction_about_us(call):
    bot.send_message(chat_id=call.message.chat.id, text="""Создатели:

Главный по пушкам @tovarishpointeresam
Отец бота: @danp1t""",
                     reply_markup=create_start_markup())

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
