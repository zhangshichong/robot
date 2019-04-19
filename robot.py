from wxpy import *
bot = Bot(cache_path=True)

tuling = Tuling(api_key='a20ff4cbfc814f379b347d3d9d934feb')

renhaolan = ensure_one(bot.search('跑山猪'))
wangjianke = ensure_one(bot.search('王剑'))
ydbf = bot.groups().search('原地暴富')[0]
# ydbf = bot.groups().search('原地暴富')[0]
# print(type(chats))
# g = chats['原地暴富']
renhaolan.send('今晚来么')
wangjianke.send('今晚来么')
# ydbf.send('今晚来么')
@bot.register(renhaolan)
def reply_re(msg):
    tuling.do_reply(msg)
@bot.register(wangjianke)
def reply_re(msg):
    tuling.do_reply(msg)
@bot.register(ydbf)
def reply_re(msg):
    tuling.do_reply(msg)
embed()