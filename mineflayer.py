from javascript import require, On, Once, AsyncTask, once, off, console
import time
minefalyer = require('mineflayer')
 
ipserv = input('Введите айпи сервера: ')
loginserv = input('Введите логин: ')
versserv = input('Введите версию: ')
qslot = int(input('Введите слот хотбара на который нужно нажать: '))
qslotc = qslot - 1
wclick = int(input('Введите на какой слот в меню нужно нажать: '))
wclickc = wclick - 1
 
bot = minefalyer.createBot({
    'host': ipserv,
    'username': loginserv,
    'version': versserv,
 
})
@On(bot, 'login')
def botsetQuickBarSlot(slot):
    bot.setQuickBarSlot(qslotc)
    print('Я выбрал', qslot, 'слот в хотбаре')
    time.sleep(5)
    bot.swingArm()
    print('Я нажал на компас')
    time.sleep(5)
    bot.clickWindow(wclickc, 0, 0)
    print('Я зашел на сервер')
 
@On(bot, "messagestr")
def handleMsg(this, sender, message, *args):
  if sender:
      print('[CHAT LOGS] -', sender)
 
bot.on('kicked', console.log)
bot.on('error', console.log)
while True:
    pass
