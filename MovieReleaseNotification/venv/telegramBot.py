# import telegram
import telepot

token = '963319881:AAE-EQDUlm5QrxuLYCqE0TbfBKem0xsZ73E'
# bot = telegram.Bot(token='963319881:AAE-EQDUlm5QrxuLYCqE0TbfBKem0xsZ73E')
bot = telepot.Bot(token)

# for i in bot.getUpdates():
#     print(i.message)
# print(bot.getMe())
bot.getUpdates()
