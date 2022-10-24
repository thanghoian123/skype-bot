from skypebot import SkypeBot

skype_bot = SkypeBot('+84769144735', 'thangprohoian123')

id_room_order = '19:95c27d40c4cb480987e24ae1fc8cb4f4@thread.skype'

room = skype_bot.sk.chats[id_room_order]
# 'http://shopeefood.vn/da-nang/tiem-com-ca-men-ga-nuong-muoi-ot-la-chanh-pham-van-nghi',
skype_bot.loop()
