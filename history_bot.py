import telebot, function

bot = telebot.TeleBot("6743483800:AAEgeLSXH33LyvBNFhqsiqr64lZ6VWZfMpw")

@bot.message_handler(commands=["start"])
def welcome(message):
    function.welcome(message)

@bot.message_handler(content_types=['text'])
def reaction_on_text(message):
    function.reaction_on_text(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            #1 вопрос
            if call.data == 'lets_start':
                function.reaction_lets_start(call)
            elif call.data == 'true1':
                function.reaction_true1(call)
            elif call.data == 'no_true1':
                function.reaction_no_true1(call)
            #2 вопрос
            elif call.data == 'test2':
                function.reaction_question2(call)
            elif call.data == 'true2':
                function.reaction_true2(call)
            elif call.data == 'no_true2':
                function.reaction_no_true2(call)
            #3 вопрос
            elif call.data == 'test3':
                function.reaction_question3(call)
            elif call.data == 'true3':
                function.reaction_true3(call)
            elif call.data == 'no_true3':
                function.reaction_no_true3(call)
            #4 вопрос
            elif call.data == 'test4':
                function.reaction_question4(call)
            elif call.data == 'true4':
                function.reaction_true4(call)
            elif call.data == 'no_true4':
                function.reaction_no_true4(call)
            #5 вопрос
            elif call.data == 'test5':
                function.reaction_question5(call)
            elif call.data == 'true5':
                function.reaction_true5(call)
            elif call.data == 'no_true5':
                function.reaction_no_true5(call)
            #6 вопрос
            elif call.data == 'test6':
                function.reaction_question6(call)
            elif call.data == 'true6':
                function.reaction_true6(call)
            elif call.data == 'no_true6':
                function.reaction_no_true6(call)
            #7 вопрос
            elif call.data == 'test7':
                function.reaction_question7(call)
            elif call.data == 'true7':
                function.reaction_true7(call)
            elif call.data == 'no_true7':
                function.reaction_no_true7(call)
            #8 вопрос
            elif call.data == 'test8':
                function.reaction_question8(call)
            elif call.data == 'true8':
                function.reaction_true8(call)
            elif call.data == 'no_true8':
                function.reaction_no_true8(call)
            #9 вопрос
            elif call.data == 'test9':
                function.reaction_question9(call)
            elif call.data == 'true9':
                function.reaction_true9(call)
            elif call.data == 'no_true9':
                function.reaction_no_true9(call)
            #10 вопрос
            elif call.data == 'test10':
                function.reaction_question10(call)
            elif call.data == 'true10':
                function.reaction_true10(call)
            elif call.data == 'no_true10':
                function.reaction_no_true10(call)
            #11 вопрос
            elif call.data == 'test11':
                function.reaction_question11(call)
            elif call.data == 'true11':
                function.reaction_true11(call)
            elif call.data == 'no_true11':
                function.reaction_no_true11(call)
            #12 вопрос
            elif call.data == 'test12':
                function.reaction_question12(call)
            elif call.data == 'true12':
                function.reaction_true12(call)
            elif call.data == 'no_true12':
                function.reaction_no_true12(call)
            #13 вопрос
            elif call.data == 'test13':
                function.reaction_question13(call)
            elif call.data == 'true13':
                function.reaction_true13(call)
            elif call.data == 'no_true13':
                function.reaction_no_true13(call)
            #14 вопрос
            elif call.data == 'test14':
                function.reaction_question14(call)
            elif call.data == 'true14':
                function.reaction_true14(call)
            elif call.data == 'no_true14':
                function.reaction_no_true14(call)
            #15 вопрос
            elif call.data == 'test15':
                function.reaction_question15(call)
            elif call.data == 'true15':
                function.reaction_true15(call)
            elif call.data == 'no_true15':
                function.reaction_no_true15(call)
            #16 вопрос
            elif call.data == 'test16':
                function.reaction_question16(call)
            elif call.data == 'true16':
                function.reaction_true16(call)
            elif call.data == 'no_true16':
                function.reaction_no_true16(call)
            #17 вопрос
            elif call.data == 'test17':
                function.reaction_question17(call)
            elif call.data == 'true17':
                function.reaction_true17(call)
            elif call.data == 'no_true17':
                function.reaction_no_true17(call)
            #18 вопрос
            elif call.data == 'test18':
                function.reaction_question18(call)
            elif call.data == 'true18':
                function.reaction_true18(call)
            elif call.data == 'no_true18':
                function.reaction_no_true18(call)
            #19 вопрос
            elif call.data == 'test19':
                function.reaction_question19(call)
            elif call.data == 'true19':
                function.reaction_true19(call)
            elif call.data == 'no_true19':
                function.reaction_no_true19(call)
            #20 вопрос
            elif call.data == 'test20':
                function.reaction_question20(call)
            elif call.data == 'true20':
                function.reaction_true20(call)
            elif call.data == 'no_true20':
                function.reaction_no_true20(call)


            #Другое
            elif call.data == 'about_us':
                function.reaction_about_us(call)


    except Exception as e:
        print(e)
if __name__ == '__main__':
    bot.polling(none_stop=True)