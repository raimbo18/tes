import ErrorLinepy
from ErrorLinepy import *
from ErrorAkad.ttypes import *
from multiprocessing import Pool, Process
import datetime, pafy, time, timeit, pytz, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, urllin, wikipedia, ctypes
from time import sleep
from datetime import datetime
from datetime import timedelta, date
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

err = ERR0R()
err = ERR0R(authToken='EwjA7BGA87lPrc4L0zU9.grzYgOnTdKvSkrQ7FTsKMq.TmsMcUZV6F1pLmV4TxQ5RDSN8NwxUg/x9iFFmCoYF6s=')
err.log("yAuthToken: "+str(err.authToken))
channel = LineChannel(err)
err.log("yChannelToken: "+str(channel.getChannelResult))

poll = LinePoll(err)
call = err
mid = err.getProfile().mid
devlist = ['uac8e3eaf1eb2a55770bf10c3b2357c33']

errProfile = err.getProfile()
myProfile["displayName"] = errProfile.displayName
myProfile["statusMessage"] = errProfile.statusMessage
myProfile["pictureStatus"] = errProfile.pictureStatus

errspawn = err.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

errkuh = {
    'ErrautoJoin':True,
    'ErrautoAdd':True,
    'ErrautoLeave':False,
    'ErrautoLeave1':False,
    'ErrautoJoinTicket':True,
    }

readerz = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "lurkt":{},
    "lurkp":{},
    "ROM":{}
}
cctvz = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

#with open('devlist.json', 'r') as fp:
#    devlist = json.load(fp)
    
#ErrSettingz = codecs.open("setting.json","r","utf-8")
#Errmain = json.load(ErrSettingz)
#ErrSettingzz = codecs.open("settings.json","r","utf-8")
#settings = json.load(ErrSettingzz)
#ErrSettingzzz = codecs.open("wait.json","r","utf-8")
#wait = json.load(ErrSettingzzz)

errstart = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

####### ERR0R DEF LIST ########
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
    
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def terjadiError(text):
    err.log("Problem : " + str(text))
    time_ = datetime.now()
    with open("errorlog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items
    
def mengulangBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit' % (days, hours, mins)
    #return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit' % (days, hours, mins)

def untuk_tag_anggota(to, mid):
    try:
        arrData = ""
        textx = "「 Mention 」\n Mentioning to {} Member\n\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n" + " //"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n< {} >".format(str(err.getGroup(to).name))
                except:
                    no = "\n*Mentioned*"
        err.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        err.sendMessage(to, "[ ERR0R ] Terjadi kesalahan :\n" + str(error))

def anggota_baru(to, mid):
    try:
        arrData = ""
        textx = "  「 Member Joined 」\n" #.format(str(len(mid))+"」")
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = err.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nSelamat Datang di : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n {}".format(str(err.getGroup(to).name))
                except:
                    no = "\n *yeayea"
        err.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        err.sendMessage(to, "[ ERR0R ] Terjadi kesalahan :\n" + str(error))

def anggota_keluar(to, mid):
    try:
        arrData = ""
        textx = "  「 Member Leaved 」\n" #.format(str(len(mid))+"」")
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = err.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"] #+" da: "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n {}".format(str(err.getGroup(to).name))
                except:
                    no = "\n Yeayea"
        err.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        err.sendMessage(to, "[ ERR0R ] Terjadi kesalahan  :\n" + str(error))

def melihat_sider(to, mid):
    try:
        arrData = ""
        textx = "Sider User 「 {} 」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(err.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        err.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        err.sendMessage(to, "[ ERR0R ] Terjadi kesalahan :\n" + str(error))

def kirim_mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Lost Time")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Lost Time")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def kirim_mention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = err.getAllContactIds()
        gid = err.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nTeman : "+str(len(teman))+"\nAktif dalam : \n < "+bot+" >"
        err.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        err.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Errmain["keyCommand"]):
        cmd = pesan.replace(Errmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def perintah():
    key = Errmain["keyCommand"]
    key = key.title()
    helpMessage = " " + "\n" + \
    return helpMessage

def errBot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            print ("「 0 」 Sepi :(")
            return

        if op.type == 5:
            print ("「 5 」 Di Add :)")
            if settings["autoAdd"] == True:
                err.findAndAddContactsByMid(op.param2)
                err.sendMessage(op.param1, "Thx for add!")

        if op.type == 13:
            if mid in op.param3:
                if wait["ErrautoJoin"] == True:
                    #if op.param2 not in Bots and op.param2 not in admin:
                        err.acceptGroupInvitation(op.param1)
                        ginfo = err.getGroup(op.param1)
                        err.sendMessage(op.param1," " +str(ginfo.name) + ">")
                    else:
                        err.acceptGroupInvitation(op.param1)
                        ginfo = err.getGroup(op.param1)
                        err.sendMessage(op.param1," " +str(ginfo.name) + ">")

        if op.type == 13:
            if mid in op.param3:
                if wait["ErrautoLeave"] == True:
                    #if op.param2 not in Bots and op.param2 not in admin:
                        err.acceptGroupInvitation(op.param1)
                        ginfo = err.getGroup(op.param1)
                        err.sendMessage(op.param1," " +str(ginfo.name))
                        err.leaveGroup(op.param1)
                    else:
                        err.acceptGroupInvitation(op.param1)
                        ginfo = err.getGroup(op.param1)
                        err.sendMessage(op.param1," " + str(ginfo.name))

        if op.type in [22, 24]:
            print ("[ 22 And 24 ] Diundang ke Room & Out dari Room")
            if wait["ErrautoLeave"] == True:
                kirim_mentions(op.param2, "@! hmm?")
                err.leaveRoom(op.param1)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://leert.corrykalam.gq/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               err.sendMessage(msg.to, str(data["answer"]))
                   except Exception as error:
                       pass

        if op.type == 26:
            try:
                print ("[ 26 ] PUBLIC")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                prefix = Errmain["keyCommand"].title()
                if settings["prefix"] == False:
                    prefix = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != puy.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                              if wait["selfbot"] == True:
                                helpMessage = helpmessage()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = err.getContact(poey)
                                kirim_mentions(to, str(helpMessage), [poey])

#============================================================  QR JOINING ===========================================================#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if wait["ErrautoJoinTicket"] == True:
                                 link_re = re.compile('(:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     aditmadzs.sendMessage(msg.to, "%s" % str(group.name))

    except Exception as error:
        print (error)
#=======================================================  QR JOINING FINISHED ===========================================================#

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        




