
import re

from scrapy.crawler import CrawlerProcess
from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent

from spiders.skypespider import SkypeBotSpider

# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# }) 
process = CrawlerProcess()

class SkypeBot(SkypeEventLoop):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sk = Skype(self.username, self.password)
        super(SkypeBot, self).__init__(username, password)

    def onEvent(self, event):
        # print("wait........")
        if isinstance(event, SkypeNewMessageEvent) \
                and not event.msg.userId == self.userId:
                # and "ping" in event.msg.content:
            regex_order = r"\*order (.+)"
            regex_store = r"\*store (.+)"

            matches_store = re.finditer(regex_store, event.msg.content, re.MULTILINE)
            text = event.msg.content.split()
            link_store = event.msg.content.split('*store')[1]

            print(event.msg.content,"=====content")
            if len(text)>0:
                cmd = text[0]
                cmd_info = text[1]
                print(cmd_info,"----------cmd")
                if cmd.lower() == '*order':
                    event.msg.chat.sendMsg("ok picked {}".format(link_store))
                if cmd.lower() == '*store':
                    print("---------matches_store",matches_store)
                    process.crawl(SkypeBotSpider,url = link_store)
                    process.start() 
                    print("---------finish")
                    
                    # the script will block here until the crawling is finished
                    # event.msg.chat.sendMsg("store {}".format(cmd_info))
        
    def connect(self):
        return Skype(self.username, self.password)

    def create_room(self, group_members):
        sk = self.connect()
        user = sk.user  # you
        contacts = sk.contacts  # your contacts
        chats = sk.chats  # your conversations
        print('======group_members', group_members)

        # if len(group_members)==0:
        #     return None
        ch = chats.create(group_members)
        print('======vaoday', ch)
        if ch:
            return ch
        return None

    def send_message(self, ch, mess):
        ch.sendMsg(mess)

    def retrieve_message(self, ch):
        return ch.getMsgs()
