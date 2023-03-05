import openai
import telebot

openai.api_key = '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'
bot = telebot.TeleBot('6188761136:AAGE5eltrvTjJ-Upx0XiHwdCoHgls1_9nGU')


@bot.messagehandler(func=lambda: True)
def handler_messag(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,

    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.polling()
