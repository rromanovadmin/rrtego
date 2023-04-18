import mysql.connector
from telethon import TelegramClient, events


session_name = "cerez/Bot"
dbcon = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="116m"

)

dbcon101m = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="101m"

)
API_ID = '26135109'
API_HASH = '1833d0727270754846bb414332d10a3b'
BOT_TOKEN = '6101494933:AAFp9ywxEd-7MZYPImKahVJnHzqGOVIAYNw'

client = TelegramClient(session_name, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern="(?i)/bakiye"))
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mycursor.execute("SELECT * FROM kullanici")
    kullanici = mycursor.fetchall()
    kontrol = False
    bakiye = 0
    for i in kullanici:
        if str(SENDER) == i[0]:
            kontrol = True
            bakiye = i[1]
    if kontrol == True:
        await client.send_message(SENDER, "Mevcut Bakiyeniz: " + str(bakiye), parse_mode='html')
    else:
        await client.send_message(SENDER, "Sisteme Kayıtlı Değilsiniz. Yöneticiyle Görüşme Sağlayınız \n@RomanianR_admin" + str(bakiye),
                                  parse_mode='html')


@client.on(events.NewMessage(pattern="(?i)/kisiler"))
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    if str(SENDER) == "939646267" or str(SENDER) == "570115092" or str(SENDER) == "1566477583":
        sender = await event.get_sender()
        SENDER = sender.id

        mycursor.execute("SELECT * FROM kullanici")
        tarife = mycursor.fetchall()
        sayilan = 0
        tarifetext = ""

        for i in tarife:
            tarifetext += "Kimlik : " + tarife[sayilan][0] + " Jeton Sayısı: " + str(tarife[sayilan][1]) + " Jeton \n"
            sayilan += 1
        await client.send_message(SENDER, tarifetext)

        await client.send_message(SENDER,"Lütfen Bakiyesini Güncellemek İstediğiniz Kişinin Önce Kimlik İdsini Ardında Yüklemek İstediğiniz Jeton Mikatrını Giriniz \nÖrn:/bkguncelle id jetonmiktarı")
    else:
        await client.send_message(SENDER, "Bu Komutu Kullanmaya Yetkiniz Bulunmamaktadır.", parse_mode='html')

@client.on(events.NewMessage(pattern="(?i)/bkguncelle"))
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    if str(SENDER) == "939646267" or str(SENDER) == "570115092" or str(SENDER) == "1566477583":
        sender = await event.get_sender()
        SENDER = sender.id
        yazilan = event.message.text.split(' ')

        if yazilan.__len__() == 3:

            sndbil = yazilan[1]
            bakiyebil = yazilan[2]
            mycursor.execute("SELECT * FROM kullanici WHERE kimlik = '"+sndbil+"'")
            gel = mycursor.fetchall()

            if not gel:
                await client.send_message(SENDER, "Kimlik Bilgisi Bulunamadı Lütfen Tekrar Kontrol Ediniz",
                                          parse_mode='html')
            else:
                mycursor.execute("UPDATE kullanici SET bakiye='"+bakiyebil+"' WHERE kimlik='"+sndbil+"'")
                dbcon.commit()
                await client.send_message(SENDER, "Bakiye Güncellendi",
                                          parse_mode='html')


        else:
            await client.send_message(SENDER, "Lütfen Sadece sender id ve bakiye bilgisi giriniz.", parse_mode='html')

    else:
        await client.send_message(SENDER, "Bu Komutu Kullanmaya Yetkiniz Bulunmamaktadır.", parse_mode='html')


@client.on(events.NewMessage(pattern="(?i)/ekle"))
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mycursor = dbcon.cursor()
    yazilan = event.message.text.split(' ')

    if str(SENDER) == "939646267" or str(SENDER) == "570115092" or str(SENDER) == "1566477583":
        yazilan = event.message.text.split(' ')
        if yazilan.__len__() == 3:

            sndbil = yazilan[1]
            bakiyebil = yazilan[2]

            mycursor.execute("SELECT * FROM kullanici WHERE kimlik= '"+sndbil+"'")
            kullaniciekle = mycursor.fetchall()

            if not kullaniciekle:
                mycursor.execute("INSERT INTO kullanici (kimlik, bakiye) VALUES ('" + sndbil + "','" + bakiyebil + "')")
                dbcon.commit()
                await client.send_message(SENDER, "Kayıt Başarılı", parse_mode='html')
            else:
                await client.send_message(SENDER, "Bu Kimlik Sisteme Kayıtlı Lütfen /bkguncelle Komutu İle İşlemlerinize Devam Ediniz", parse_mode='html')
        else:
            await client.send_message(SENDER, "Lütfen Sadece sender.id ve bakiye bilgisi giriniz.", parse_mode='html')
    else:
        await client.send_message(SENDER, "Bu Komutu Kullanmaya Yetkiniz Bulunmamaktadır.", parse_mode='html')


@client.on(events.NewMessage(pattern="(?i)/start"))
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id

    text = "Sisteme Kayıt Yapabilmeniz İçin Yöneticiye ( @RomanianR_admin ) Tırnak İçindeki Kısmı  '"+str(SENDER)+"'  İletin !  \n\n/tcgsm 1111111111 Tc Bilgisi Girerek Kimlik Numarasına Kayıtlı Olan Telefon Numaralarına Rahatlıkla Erişebilirsiniz.\n\n /aile 11111111111 Tc Bilgisi Girerek Kişinin Aile Bilgilerine Ulaşabilirsiniz. \n\n/gsmtc 5555555555 Bildiğiniz Numarayı Bu Şekilde Yazarak Kime Ait Olduğunu ve Tc Bilgisine Erişebilirsiniz. \n\n/sulale 11111111111 Tc Bilgisini Girdiğiniz Kişinin Soyağacı Karşınıza Çıkacaktır.  \n\n/tcsorgu 11111111111 Tc Bilgisini Girerek Kimlik Bilgisinin Kime Ait Oluduğunu Bulabilirsiniz.  \n\n/isimsorgu İsim Soyisim İl ve İlçe Bilgilerini Girerek Merak Ettiğiniz Bir Arkadaşınızın Bilgilerini Öğrenerek Numaralarına Ulaşabilirsiniz. Yapmanız Gerekenler \nÖrn: /isimsorgu AD SOYAD İL \n\n/tarife komutunu çalıştırarak sorgu ve jeton fiyatlarını öğrenebilirsiniz \n\n/bakiye komutunu çalıştırarak kalan bakiyenizi öğrenebilirsiniz. \n\n 1 Jeton = 1 Tl"

    await client.send_message(SENDER, text)
@client.on(events.NewMessage(pattern="(?i)/tarife"))
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id

    mycursor.execute("SELECT * FROM ucrettarifesi")
    tarife = mycursor.fetchall()
    sayilan = 0
    tarifetext=""

    for i in tarife:
        tarifetext += "/"+tarife[sayilan][0] +  " Ücret: " + str(tarife[sayilan][1])  +" Jeton \n"
        sayilan += 1
    await client.send_message(SENDER, tarifetext)


@client.on(events.NewMessage(pattern="(?i)/aile"))
async def start(event):
    try:
        sender = await event.get_sender()
        SENDER = sender.id
        kontrol = False
        mycursor.execute("SELECT * FROM kullanici")
        kullanici = mycursor.fetchall()
        bakiye = 0
        gelen = False
        for i in kullanici:
            if str(SENDER) == i[0]:
                kontrol = True
                bakiye = i[1]
        if kontrol == True:

            mycursor.execute("SELECT * FROM ucrettarifesi WHERE icerik = 'aile'")
            tarifeler = mycursor.fetchall()

            tarifeAile = tarifeler[0][1]
            son = bakiye - tarifeAile
            if son >= 0:
                yazilan = event.message.text.split(' ')
                text = ""
                kuzentext = ""
                GTC = yazilan[1]
                toplamsayi = 0
                gbabatc = "0x"
                gannetc = "0x"
                mycursor101m.execute("SELECT BABATC, ANNETC FROM 101m WHERE TC='" + GTC + "' ")
                gelenbil = mycursor101m.fetchall()
                say2 = 0
                if gelenbil.__len__() != 0:
                    gbabatc = str(gelenbil[0][0])
                    gannetc = str(gelenbil[0][1])
                mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + GTC + "' ")
                gelenbil = mycursor101m.fetchall()
                if gelenbil.__len__() != 0:
                    text += "Yakınlık: Kendisi \n"
                    text += "Tc: " + str(gelenbil[0][1])
                    text += "\nAd: " + str(gelenbil[0][2])
                    text += "\nSoyad: " + str(gelenbil[0][3])
                    text += "\nDoğum Tarihi: " + str(gelenbil[0][4])
                    text += "\nİl: " + str(gelenbil[0][5])
                    text += "\nİlçe: " + str(gelenbil[0][6])
                    text += "\nAnne Adı: " + str(gelenbil[0][7])
                    text += "\nAnne Tc: " + str(gelenbil[0][8])
                    text += "\nBaba Adı: " + str(gelenbil[0][9])
                    text += "\nBaba Tc: " + str(gelenbil[0][10])
                    text += "\nUyruk: " + str(gelenbil[0][11]) + "\n --------------- \n"
                    toplamsayi += 1                    
                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + GTC + "' OR ANNETC='" + GTC + "'")
                    gelenbil = mycursor101m.fetchall()
                    if gelenbil.__len__() != 0:
                        for i in range(gelenbil.__len__()):
                            text += "Yakınlık: Çocuğu \n"
                            text += "Tc: " + str(gelenbil[i][1])
                            text += "\nAd: " + str(gelenbil[i][2])
                            text += "\nSoyad: " + str(gelenbil[i][3])
                            text += "\nDoğum Tarihi: " + str(gelenbil[i][4])
                            text += "\nİl: " + str(gelenbil[i][5])
                            text += "\nİlçe: " + str(gelenbil[i][6])
                            text += "\nAnne Adı: " + str(gelenbil[i][7])
                            text += "\nAnne Tc: " + str(gelenbil[i][8])
                            text += "\nBaba Adı: " + str(gelenbil[i][9])
                            text += "\nBaba Tc: " + str(gelenbil[i][10])
                            text += "\nUyruk: " + str(gelenbil[i][11]) + "\n --------------- \n"
                            toplamsayi += 1

                    mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gbabatc + "' ")
                    gelenbil = mycursor101m.fetchall()
                    if gelenbil.__len__() != 0:
                        text += "Yakınlık:  Babası \n"
                        text += "Tc: " + str(gelenbil[0][1])
                        text += "\nAd: " + str(gelenbil[0][2])
                        text += "\nSoyad: " + str(gelenbil[0][3])
                        text += "\nDoğum Tarihi: " + str(gelenbil[0][4])
                        text += "\nİl: " + str(gelenbil[0][5])
                        text += "\nİlçe: " + str(gelenbil[0][6])
                        text += "\nAnne Adı: " + str(gelenbil[0][7])
                        text += "\nAnne Tc: " + str(gelenbil[0][8])
                        text += "\nBaba Adı: " + str(gelenbil[0][9])
                        text += "\nBaba Tc: " + str(gelenbil[0][10])
                        text += "\nUyruk: " + str(gelenbil[0][11]) + "\n --------------- \n"
                        toplamsayi += 1

                    
                    mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gannetc + "' ")
                    gelenbil = mycursor101m.fetchall()
                    if gelenbil.__len__() != 0:
                        gannenenetc = gelenbil[0][8]
                        text += "Yakınlık: Annesi \n"
                        text += "Tc: " + str(gelenbil[0][1])
                        text += "\nAd: " + str(gelenbil[0][2])
                        text += "\nSoyad: " + str(gelenbil[0][3])
                        text += "\nDoğum Tarihi: " + str(gelenbil[0][4])
                        text += "\nİl: " + str(gelenbil[0][5])
                        text += "\nİlçe: " + str(gelenbil[0][6])
                        text += "\nAnne Adı: " + str(gelenbil[0][7])
                        text += "\nAnne Tc: " + str(gelenbil[0][8])
                        text += "\nBaba Adı: " + str(gelenbil[0][9])
                        text += "\nBaba Tc: " + str(gelenbil[0][10])
                        text += "\nUyruk: " + str(gelenbil[0][11]) + "\n --------------- \n"
                        toplamsayi += 1
                    mycursor101m.execute("SELECT * FROM 101m WHERE (BABATC='" + gbabatc + "' OR ANNETC ='"+gannetc+"') AND NOT TC='"+GTC+"'")
                    gelenbil = mycursor101m.fetchall()
                    if gelenbil.__len__() != 0:
                        for i in range(gelenbil.__len__()):
                            text += "Yakınlık: Kardeşi \n"
                            text += "Tc: " + str(gelenbil[i][1])
                            text += "\nAd: " + str(gelenbil[i][2])
                            text += "\nSoyad: " + str(gelenbil[i][3])
                            text += "\nDoğum Tarihi: " + str(gelenbil[i][4])
                            text += "\nİl: " + str(gelenbil[i][5])
                            text += "\nİlçe: " + str(gelenbil[i][6])
                            text += "\nAnne Adı: " + str(gelenbil[i][7])
                            text += "\nAnne Tc: " + str(gelenbil[i][8])
                            text += "\nBaba Adı: " + str(gelenbil[i][9])
                            text += "\nBaba Tc: " + str(gelenbil[i][10])
                            text += "\nUyruk: " + str(gelenbil[i][11]) + "\n --------------- \n"
                            toplamsayi += 1
                    await client.send_message(SENDER, text  ,parse_mode='html')

                    yenibakiye = int(bakiye) - int(tarifeAile)
                    mycursor.execute(
                        "UPDATE kullanici SET bakiye = '" + str(yenibakiye) + "' WHERE kimlik='" + str(sender.id) + "'")
                    dbcon.commit()
                    text = ""
                    text = "Eşleşen Kayıt Sayısı: " + str(toplamsayi)
                    await client.send_message(SENDER, text, parse_mode='html')
                    await client.send_message(SENDER, "Yeni Bakiyeniz: " + str(yenibakiye), parse_mode='html')

                else:
                    await client.send_message(SENDER,"Sistemde Kayıt Bulunamadı ",parse_mode='html')


            else:
                await client.send_message(SENDER,
                                          "Bu Komut İçin Bakiyeniz Yetersiz, \nSorgu İçin Gerekli Jeton: '" + str(tarifeAile) + "'\nMevcut Bakiye:'" + str(bakiye) + "'",
                                          parse_mode='html')
        else:
            sender = await event.get_sender()
            SENDER = sender.id
            await client.send_message(SENDER, "Sisteme Kayıtlı Değilsiniz. Yöneticiyle Görüşme Sağlayınız \n@RomanianR_admin",
                                  parse_mode='html')

    except Exception as e:
        print(e)
        await client.send_message(SENDER, "Lütfen Komutu Doğru Yazınız, /start Yazarak Komutları Nasıl Kullanacağınızı Öğrenebilirsiniz!", parse_mode='html')
        return    

@client.on(events.NewMessage(pattern="(?i)/tcsorgu"))
async def start(event):
    try:
        sender = await event.get_sender()
        SENDER = sender.id
        kontrol = False
        mycursor.execute("SELECT * FROM kullanici")
        kullanici = mycursor.fetchall()
        bakiye = 0
        gelen = False
        for i in kullanici:
            if str(SENDER) == i[0]:
                kontrol = True
                bakiye = i[1]
        if kontrol == True:

            mycursor.execute("SELECT * FROM ucrettarifesi WHERE icerik = 'tcsorgu'")
            tarifeler = mycursor.fetchall()

            tarifeTcsorgu = tarifeler[0][1]
            son = bakiye - tarifeTcsorgu
            if son >= 0:
                yazilan = event.message.text.split(' ')
                text = ""
                GTC = yazilan[1]
                toplamsayi = 0
                mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + GTC + "' ")
                gelenbil = mycursor101m.fetchall()
                if gelenbil.__len__() != 0:
                    text += "Tc: " + str(gelenbil[0][1])
                    text += "\nAd: " + str(gelenbil[0][2])
                    text += "\nSoyad: " + str(gelenbil[0][3])
                    text += "\nDoğum Tarihi: " + str(gelenbil[0][4])
                    text += "\nİl: " + str(gelenbil[0][5])
                    text += "\nİlçe: " + str(gelenbil[0][6])
                    text += "\nAnne Adı: " + str(gelenbil[0][7])
                    text += "\nAnne Tc: " + str(gelenbil[0][8])
                    text += "\nBaba Adı: " + str(gelenbil[0][9])
                    text += "\nBaba Tc: " + str(gelenbil[0][10])
                    text += "\nUyruk: " + str(gelenbil[0][11]) + "\n --------------- \n"
                    toplamsayi += 1
                    gelen = True
                    await client.send_message(SENDER, text  ,parse_mode='html')

                    yenibakiye = int(bakiye) - int(tarifeTcsorgu)
                    mycursor.execute(
                        "UPDATE kullanici SET bakiye = '" + str(yenibakiye) + "' WHERE kimlik='" + str(sender.id) + "'")
                    dbcon.commit()
                    text = ""
                    text = "Eşleşen Kayıt Sayısı: " + str(toplamsayi)
                    await client.send_message(SENDER, text, parse_mode='html')
                    await client.send_message(SENDER, "Yeni Bakiyeniz: " + str(yenibakiye), parse_mode='html')

                else:
                    await client.send_message(SENDER,"Sistemde Kayıt Bulunamadı ",parse_mode='html')


            else:
                await client.send_message(SENDER,
                                          "Bu Komut İçin Bakiyeniz Yetersiz, \nSorgu İçin Gerekli Jeton: '" + str(tarifeTcsorgu) + "'\nMevcut Bakiye:'" + str(bakiye) + "'",
                                          parse_mode='html')
        else:
            sender = await event.get_sender()
            SENDER = sender.id

            await client.send_message(SENDER, "Sisteme Kayıtlı Değilsiniz. Yöneticiyle Görüşme Sağlayınız \n@RomanianR_admin",
                                  parse_mode='html')

    except Exception as e:
        print(e)
        await client.send_message(SENDER, "Lütfen Komutu Doğru Yazınız, /start Yazarak Komutları Nasıl Kullanacağınızı Öğrenebilirsiniz!", parse_mode='html')
        return   


@client.on(events.NewMessage(pattern="(?i)/sulale"))
async def start(event):
    try:
        sender = await event.get_sender()
        SENDER = sender.id
        kontrol = False
        mycursor.execute("SELECT * FROM kullanici")
        kullanici = mycursor.fetchall()
        bakiye = 0
        gelen = False
        for i in kullanici:
            if str(SENDER) == i[0]:
                kontrol = True
                bakiye = i[1]
        if kontrol == True:

            mycursor.execute("SELECT * FROM ucrettarifesi WHERE icerik = 'sülale'")
            tarifeler = mycursor.fetchall()

            tarifeSülale = tarifeler[0][1]
            son = bakiye - tarifeSülale
            if son >= 0:
                yazilan = event.message.text.split(' ')
                text = ""
                kuzentext = ""
                GTC = yazilan[1]
                toplamsayi = 0
                gbabatc = "0x"
                gannetc = "0x"
                gbabadedetc ="0x"
                gbabanenetc ="0x"
                gannededetc ="0x"
                gannenenetc ="0x"
                mycursor101m.execute("SELECT BABATC, ANNETC FROM 101m WHERE TC='" + GTC + "' ")
                gelenbil = mycursor101m.fetchall()
                say2 = 0
                if gelenbil.__len__() != 0:
                    gbabatc = str(gelenbil[0][0])
                    gannetc = str(gelenbil[0][1])
                mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + GTC + "' ")
                gelenbil = mycursor101m.fetchall()
                if gelenbil.__len__() != 0:
                    text += "Yakınlık: Kendisi \n"
                    text += "Tc: " + str(gelenbil[0][1])
                    text += "\nAd: " + str(gelenbil[0][2])
                    text += "\nSoyad: " + str(gelenbil[0][3])
                    text += "\nDoğum Tarihi: " + str(gelenbil[0][4])
                    text += "\nİl: " + str(gelenbil[0][5])
                    text += "\nİlçe: " + str(gelenbil[0][6])
                    text += "\nAnne Adı: " + str(gelenbil[0][7])
                    text += "\nAnne Tc: " + str(gelenbil[0][8])
                    text += "\nBaba Adı: " + str(gelenbil[0][9])
                    text += "\nBaba Tc: " + str(gelenbil[0][10])
                    text += "\nUyruk: " + str(gelenbil[0][11]) + "\n --------------- \n"
                    toplamsayi += 1
                    gelen = True

                    mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gbabatc + "' ")
                    gelbaba = mycursor101m.fetchall()
                    if gelbaba.__len__() != 0:
                        text += "Yakınlık:  Babası \n"
                        text += "Tc: " + str(gelbaba[0][1])
                        text += "\nAd: " + str(gelbaba[0][2])
                        text += "\nSoyad: " + str(gelbaba[0][3])
                        text += "\nDoğum Tarihi: " + str(gelbaba[0][4])
                        text += "\nİl: " + str(gelbaba[0][5])
                        text += "\nİlçe: " + str(gelbaba[0][6])
                        text += "\nAnne Adı: " + str(gelbaba[0][7])
                        text += "\nAnne Tc: " + str(gelbaba[0][8])
                        text += "\nBaba Adı: " + str(gelbaba[0][9])
                        text += "\nBaba Tc: " + str(gelbaba[0][10])
                        text += "\nUyruk: " + str(gelbaba[0][11]) + "\n --------------- \n"
                        toplamsayi += 1
                        mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gelbaba[0][8]  + "' ")
                        gbabaanne = mycursor101m.fetchall()
                        if gbabaanne.__len__() != 0:
                            gbabanenetc =gbabaanne[0][8] 
                            text += "Yakınlık:  Babasının Annesi \n"
                            text += "Tc: " + str(gbabaanne[0][1])
                            text += "\nAd: " + str(gbabaanne[0][2])
                            text += "\nSoyad: " + str(gbabaanne[0][3])
                            text += "\nDoğum Tarihi: " + str(gbabaanne[0][4])
                            text += "\nİl: " + str(gbabaanne[0][5])
                            text += "\nİlçe: " + str(gbabaanne[0][6])
                            text += "\nAnne Adı: " + str(gbabaanne[0][7])
                            text += "\nAnne Tc: " + str(gbabaanne[0][8])
                            text += "\nBaba Adı: " + str(gbabaanne[0][9])
                            text += "\nBaba Tc: " + str(gbabaanne[0][10])
                            text += "\nUyruk: " + str(gbabaanne[0][11]) + "\n --------------- \n"
                            toplamsayi += 1

                        mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gelbaba[0][10]  + "' ")
                        gbabababa = mycursor101m.fetchall()
                        if gbabababa.__len__() != 0:
                            gbabadedetc = gbabababa[0][10]
                            text += "Yakınlık:  Babasının Babası \n"
                            text += "Tc: " + str(gbabababa[0][1])
                            text += "\nAd: " + str(gbabababa[0][2])
                            text += "\nSoyad: " + str(gbabababa[0][3])
                            text += "\nDoğum Tarihi: " + str(gbabababa[0][4])
                            text += "\nİl: " + str(gbabababa[0][5])
                            text += "\nİlçe: " + str(gbabababa[0][6])
                            text += "\nAnne Adı: " + str(gbabababa[0][7])
                            text += "\nAnne Tc: " + str(gbabababa[0][8])
                            text += "\nBaba Adı: " + str(gbabababa[0][9])
                            text += "\nBaba Tc: " + str(gbabababa[0][10])
                            text += "\nUyruk: " + str(gbabababa[0][11]) + "\n --------------- \n"
                        toplamsayi += 1
                    
                    

                    
                    mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gannetc + "' ")
                    gan = mycursor101m.fetchall()
                    if gan.__len__() != 0:
                        gannenenetc = gelenbil[0][8]
                        text += "Yakınlık: Annesi \n"
                        text += "Tc: " + str(gan[0][1])
                        text += "\nAd: " + str(gan[0][2])
                        text += "\nSoyad: " + str(gan[0][3])
                        text += "\nDoğum Tarihi: " + str(gan[0][4])
                        text += "\nİl: " + str(gan[0][5])
                        text += "\nİlçe: " + str(gan[0][6])
                        text += "\nAnne Adı: " + str(gan[0][7])
                        text += "\nAnne Tc: " + str(gan[0][8])
                        text += "\nBaba Adı: " + str(gan[0][9])
                        text += "\nBaba Tc: " + str(gan[0][10])
                        text += "\nUyruk: " + str(gan[0][11]) + "\n --------------- \n"
                        toplamsayi += 1

                        mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gan[0][10]  + "' ")
                        ganneanne = mycursor101m.fetchall()
                        if ganneanne.__len__() != 0:
                            gannenenetc = ganneanne[0][8]
                            text += "Yakınlık:  Annesinin Annesi \n"
                            text += "Tc: " + str(ganneanne[0][1])
                            text += "\nAd: " + str(ganneanne[0][2])
                            text += "\nSoyad: " + str(ganneanne[0][3])
                            text += "\nDoğum Tarihi: " + str(ganneanne[0][4])
                            text += "\nİl: " + str(ganneanne[0][5])
                            text += "\nİlçe: " + str(ganneanne[0][6])
                            text += "\nAnne Adı: " + str(ganneanne[0][7])
                            text += "\nAnne Tc: " + str(ganneanne[0][8])
                            text += "\nBaba Adı: " + str(ganneanne[0][9])
                            text += "\nBaba Tc: " + str(ganneanne[0][10])
                            text += "\nUyruk: " + str(ganneanne[0][11]) + "\n --------------- \n"
                            toplamsayi += 1
                        mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gan[0][10]  + "' ")
                        gannebaba = mycursor101m.fetchall()
                        if gannebaba.__len__() != 0:
                            gannededetc = gannebaba[0][10]
                            text += "Yakınlık:  Annesinin Babası \n"
                            text += "Tc: " + str(gannebaba[0][1])
                            text += "\nAd: " + str(gannebaba[0][2])
                            text += "\nSoyad: " + str(gannebaba[0][3])
                            text += "\nDoğum Tarihi: " + str(gannebaba[0][4])
                            text += "\nİl: " + str(gannebaba[0][5])
                            text += "\nİlçe: " + str(gannebaba[0][6])
                            text += "\nAnne Adı: " + str(gannebaba[0][7])
                            text += "\nAnne Tc: " + str(gannebaba[0][8])
                            text += "\nBaba Adı: " + str(gannebaba[0][9])
                            text += "\nBaba Tc: " + str(gannebaba[0][10])
                            text += "\nUyruk: " + str(gannebaba[0][11]) + "\n --------------- \n"
                            toplamsayi += 1
                    
                    mycursor101m.execute("SELECT * FROM 101m WHERE (BABATC='" + gbabatc + "' OR ANNETC ='"+gannetc+"') AND NOT TC='"+GTC+"'")
                    gelenbil = mycursor101m.fetchall()
                    if gelenbil.__len__() != 0:
                        for i in range(gelenbil.__len__()):
                            text += "Yakınlık: Kardeşi \n"
                            text += "Tc: " + str(gelenbil[i][1])
                            text += "\nAd: " + str(gelenbil[i][2])
                            text += "\nSoyad: " + str(gelenbil[i][3])
                            text += "\nDoğum Tarihi: " + str(gelenbil[i][4])
                            text += "\nİl: " + str(gelenbil[i][5])
                            text += "\nİlçe: " + str(gelenbil[i][6])
                            text += "\nAnne Adı: " + str(gelenbil[i][7])
                            text += "\nAnne Tc: " + str(gelenbil[i][8])
                            text += "\nBaba Adı: " + str(gelenbil[i][9])
                            text += "\nBaba Tc: " + str(gelenbil[i][10])
                            text += "\nUyruk: " + str(gelenbil[i][11]) + "\n --------------- \n"
                            
                            toplamsayi += 1
                    await client.send_message(SENDER, text  ,parse_mode='html')

                else:
                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + GTC + "' OR ANNETC='"+GTC+"' ")
                    gelenbil = mycursor101m.fetchall()
                    if gelenbil.__len__() != 0:
                        gelen = True
                        await client.send_message(SENDER, "Bu Tc Bilgilerine Ait Bir Veri Bulunamadı Fakat Akrabalar Çıkartıldı",parse_mode='html')
                    else:
                        await client.send_message(SENDER, "Bu Tc Bilgilerine Ait Bir Veri Bulunamadı",parse_mode='html')
                   
                
                if gelen == True:

                    text = "" 
                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + GTC + "' OR ANNETC='"+GTC+"' ")
                    evlatbil = mycursor101m.fetchall()

                    #region kendindensonrakiler

                    if evlatbil.__len__() !=0:
                        for i in range(evlatbil.__len__()):
                            toplamsayi += 1
                            text += "Yakınlık: Çocuğu \n"
                            text += "Tc: " + str(evlatbil[i][1])
                            text += "\nAd: " + str(evlatbil[i][2])
                            text += "\nSoyad: " + str(evlatbil[i][3])
                            text += "\nDoğum Tarihi: " + str(evlatbil[i][4])
                            text += "\nİl: " + str(evlatbil[i][5])
                            text += "\nİlçe: " + str(evlatbil[i][6])
                            text += "\nAnne Adı: " + str(evlatbil[i][7])
                            text += "\nAnne Tc: " + str(evlatbil[i][8])
                            text += "\nBaba Adı: " + str(evlatbil[i][9])
                            text += "\nBaba Tc: " + str(evlatbil[i][10])
                            text += "\nUyruk: " + str(evlatbil[i][11])
                            await client.send_message(SENDER, text  ,parse_mode='html')

                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + evlatbil[i][1] + "' OR ANNETC='"+evlatbil[i][1]+"' ")
                            torunu = mycursor101m.fetchall()
                            if torunu.__len__() !=0:
                                text = ""
                                for i in range(torunu.__len__()):
                                    toplamsayi += 1
                                    text += "Yakınlık: Torunu \n"
                                    text += "Tc: " + str(torunu[i][1])
                                    text += "\nAd: " + str(torunu[i][2])
                                    text += "\nSoyad: " + str(torunu[i][3])
                                    text += "\nDoğum Tarihi: " + str(torunu[i][4])
                                    text += "\nİl: " + str(torunu[i][5])
                                    text += "\nİlçe: " + str(torunu[i][6])
                                    text += "\nAnne Adı: " + str(torunu[i][7])
                                    text += "\nAnne Tc: " + str(torunu[i][8])
                                    text += "\nBaba Adı: " + str(torunu[i][9])
                                    text += "\nBaba Tc: " + str(torunu[i][10])
                                    text += "\nUyruk: " + str(torunu[i][11])
                                    await client.send_message(SENDER, text  ,parse_mode='html')
                                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + torunu[i][1] + "' OR ANNETC='"+torunu[i][1]+"' ")
                                    torununcocugu = mycursor101m.fetchall()
                                    if torununcocugu.__len__() !=0:
                                        text= "" 
                                        for i in range(torununcocugu.__len__()):
                                            toplamsayi += 1
                                            text += "Yakınlık: Torununun Çocuğu \n"
                                            text += "Tc: " + str(torununcocugu[i][1])
                                            text += "\nAd: " + str(torununcocugu[i][2])
                                            text += "\nSoyad: " + str(torununcocugu[i][3])
                                            text += "\nDoğum Tarihi: " + str(torununcocugu[i][4])
                                            text += "\nİl: " + str(torununcocugu[i][5])
                                            text += "\nİlçe: " + str(torununcocugu[i][6])
                                            text += "\nAnne Adı: " + str(torununcocugu[i][7])
                                            text += "\nAnne Tc: " + str(torununcocugu[i][8])
                                            text += "\nBaba Adı: " + str(torununcocugu[i][9])
                                            text += "\nBaba Tc: " + str(torununcocugu[i][10])
                                            text += "\nUyruk: " + str(torununcocugu[i][11])
                                            await client.send_message(SENDER, text  ,parse_mode='html')

                                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + torununcocugu[i][1] + "' OR ANNETC='"+torununcocugu[i][1]+"' ")
                                            torununcocugucocugu = mycursor101m.fetchall()
                                            if torununcocugucocugu.__len__() !=0:
                                                text = ""
                                                for i in range(torununcocugucocugu.__len__()):
                                                    toplamsayi += 1
                                                    text += "Yakınlık: Torunu Çocuğunun Çocuğu\n"
                                                    text += "Tc: " + str(torununcocugucocugu[i][1])
                                                    text += "\nAd: " + str(torununcocugucocugu[i][2])
                                                    text += "\nSoyad: " + str(torununcocugucocugu[i][3])
                                                    text += "\nDoğum Tarihi: " + str(torununcocugucocugu[i][4])
                                                    text += "\nİl: " + str(torununcocugucocugu[i][5])
                                                    text += "\nİlçe: " + str(torununcocugucocugu[i][6])
                                                    text += "\nAnne Adı: " + str(torununcocugucocugu[i][7])
                                                    text += "\nAnne Tc: " + str(torununcocugucocugu[i][8])
                                                    text += "\nBaba Adı: " + str(torununcocugucocugu[i][9])
                                                    text += "\nBaba Tc: " + str(torununcocugucocugu[i][10])
                                                    text += "\nUyruk: " + str(torununcocugucocugu[i][11])
                                                    await client.send_message(SENDER, text  ,parse_mode='html')
                    #endregion kendindensonrakiler
                    #region kardesevlatlarıvetorunları
                    mycursor101m.execute("SELECT * FROM 101m WHERE (BABATC='" + gbabatc + "' OR ANNETC ='"+gannetc+"') AND NOT TC='"+GTC+"'")
                    kardes = mycursor101m.fetchall()
                    if kardes.__len__() !=0:
                        for i in range(kardes.__len__()):
                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + kardes[i][1] + "' OR ANNETC='"+kardes[i][1]+"' ")
                            kardescocugu = mycursor101m.fetchall()
                            if kardescocugu.__len__() !=0:
                                for i in range(kardescocugu.__len__()):
                                    text = ""
                                    toplamsayi += 1
                                    text += "Yakınlık: Kardeşinin Çocuğu \n"
                                    text += "Tc: " + str(kardescocugu[i][1])
                                    text += "\nAd: " + str(kardescocugu[i][2])
                                    text += "\nSoyad: " + str(kardescocugu[i][3])
                                    text += "\nDoğum Tarihi: " + str(kardescocugu[i][4])
                                    text += "\nİl: " + str(kardescocugu[i][5])
                                    text += "\nİlçe: " + str(kardescocugu[i][6])
                                    text += "\nAnne Adı: " + str(kardescocugu[i][7])
                                    text += "\nAnne Tc: " + str(kardescocugu[i][8])
                                    text += "\nBaba Adı: " + str(kardescocugu[i][9])
                                    text += "\nBaba Tc: " + str(kardescocugu[i][10])
                                    text += "\nUyruk: " + str(kardescocugu[i][11])
                                    await client.send_message(SENDER, text  ,parse_mode='html')

                                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + kardescocugu[i][1] + "' OR ANNETC='"+kardescocugu[i][1]+"' ")
                                    kardestorun = mycursor101m.fetchall()
                                    if kardestorun.__len__() !=0:
                                        for i in range(kardestorun.__len__()):
                                            text = ""
                                            toplamsayi += 1
                                            text += "Yakınlık: Kardeşinin Torunu \n"
                                            text += "Tc: " + str(kardestorun[i][1])
                                            text += "\nAd: " + str(kardestorun[i][2])
                                            text += "\nSoyad: " + str(kardestorun[i][3])
                                            text += "\nDoğum Tarihi: " + str(kardestorun[i][4])
                                            text += "\nİl: " + str(kardestorun[i][5])
                                            text += "\nİlçe: " + str(kardestorun[i][6])
                                            text += "\nAnne Adı: " + str(kardestorun[i][7])
                                            text += "\nAnne Tc: " + str(kardestorun[i][8])
                                            text += "\nBaba Adı: " + str(kardestorun[i][9])
                                            text += "\nBaba Tc: " + str(kardestorun[i][10])
                                            text += "\nUyruk: " + str(kardestorun[i][11])
                                            await client.send_message(SENDER, text  ,parse_mode='html')

                                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + kardestorun[i][1] + "' OR ANNETC='"+kardestorun[i][1]+"' ")
                                            kardescocuktorun = mycursor101m.fetchall()
                                            if kardescocuktorun.__len__() !=0:
                                                for i in range(kardescocuktorun.__len__()):
                                                    text = ""
                                                    toplamsayi += 1
                                                    text += "Yakınlık: Kardeşinin Torununun Çocuğu \n"
                                                    text += "Tc: " + str(kardescocuktorun[i][1])
                                                    text += "\nAd: " + str(kardescocuktorun[i][2])
                                                    text += "\nSoyad: " + str(kardescocuktorun[i][3])
                                                    text += "\nDoğum Tarihi: " + str(kardescocuktorun[i][4])
                                                    text += "\nİl: " + str(kardescocuktorun[i][5])
                                                    text += "\nİlçe: " + str(kardescocuktorun[i][6])
                                                    text += "\nAnne Adı: " + str(kardescocuktorun[i][7])
                                                    text += "\nAnne Tc: " + str(kardescocuktorun[i][8])
                                                    text += "\nBaba Adı: " + str(kardescocuktorun[i][9])
                                                    text += "\nBaba Tc: " + str(kardescocuktorun[i][10])
                                                    text += "\nUyruk: " + str(kardescocuktorun[i][11])
                                                    await client.send_message(SENDER, text  ,parse_mode='html')
                                                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + kardescocuktorun[i][1] + "' OR ANNETC='"+kardescocuktorun[i][1]+"' ")
                                                    kardestoruntorun = mycursor101m.fetchall()
                                                    if kardestoruntorun.__len__() !=0:
                                                        for i in range(kardestoruntorun.__len__()):
                                                            text = ""
                                                            toplamsayi += 1
                                                            text += "Yakınlık: Kardeşinin Torununun Torunu \n"
                                                            text += "Tc: " + str(kardestoruntorun[i][1])
                                                            text += "\nAd: " + str(kardestoruntorun[i][2])
                                                            text += "\nSoyad: " + str(kardestoruntorun[i][3])
                                                            text += "\nDoğum Tarihi: " + str(kardestoruntorun[i][4])
                                                            text += "\nİl: " + str(kardestoruntorun[i][5])
                                                            text += "\nİlçe: " + str(kardestoruntorun[i][6])
                                                            text += "\nAnne Adı: " + str(kardestoruntorun[i][7])
                                                            text += "\nAnne Tc: " + str(kardestoruntorun[i][8])
                                                            text += "\nBaba Adı: " + str(kardestoruntorun[i][9])
                                                            text += "\nBaba Tc: " + str(kardestoruntorun[i][10])
                                                            text += "\nUyruk: " + str(kardestoruntorun[i][11])
                                                            await client.send_message(SENDER, text  ,parse_mode='html')
                    #endregion kardesevlatlarıvetorunları                            

                    #region amcahalavekuzen

                    mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gbabatc + "'")
                    dedetc = mycursor101m.fetchall()
                    if dedetc.__len__() !=0:
                        mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + dedetc[0][10] + "' AND NOT TC ='"+gbabatc+"'")
                        amcabil = mycursor101m.fetchall()
                        if amcabil.__len__() !=0:
                            for i in range(amcabil.__len__()):
                                toplamsayi += 1
                                text=""
                                text += "Yakınlık: Amca/Hala \n"
                                text += "Tc: " + str(amcabil[i][1])
                                text += "\nAd: " + str(amcabil[i][2])
                                text += "\nSoyad: " + str(amcabil[i][3])
                                text += "\nDoğum Tarihi: " + str(amcabil[i][4])
                                text += "\nİl: " + str(amcabil[i][5])
                                text += "\nİlçe: " + str(amcabil[i][6])
                                text += "\nAnne Adı: " + str(amcabil[i][7])
                                text += "\nAnne Tc: " + str(amcabil[i][8])
                                text += "\nBaba Adı: " + str(amcabil[i][9])
                                text += "\nBaba Tc: " + str(amcabil[i][10])
                                text += "\nUyruk: " + str(amcabil[i][11])
                                await client.send_message(SENDER, text  ,parse_mode='html')

                                mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + amcabil[i][1] + "' OR ANNETC='"+amcabil[i][1]+"' ")
                                amcahalaevlat = mycursor101m.fetchall()
                                if amcahalaevlat.__len__() !=0:
                                    for i in range(amcahalaevlat.__len__()):
                                            text = ""
                                            toplamsayi += 1
                                            text += "Yakınlık: Amca/Hala Çocuğu \n"
                                            text += "Tc: " + str(amcahalaevlat[i][1])
                                            text += "\nAd: " + str(amcahalaevlat[i][2])
                                            text += "\nSoyad: " + str(amcahalaevlat[i][3])
                                            text += "\nDoğum Tarihi: " + str(amcahalaevlat[i][4])
                                            text += "\nİl: " + str(amcahalaevlat[i][5])
                                            text += "\nİlçe: " + str(amcahalaevlat[i][6])
                                            text += "\nAnne Adı: " + str(amcahalaevlat[i][7])
                                            text += "\nAnne Tc: " + str(amcahalaevlat[i][8])
                                            text += "\nBaba Adı: " + str(amcahalaevlat[i][9])
                                            text += "\nBaba Tc: " + str(amcahalaevlat[i][10])
                                            text += "\nUyruk: " + str(amcahalaevlat[i][11])
                                            await client.send_message(SENDER, text  ,parse_mode='html')
                                            
                                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + amcahalaevlat[i][1] + "' OR ANNETC='"+amcahalaevlat[i][1]+"' ")
                                            amcahalaevlatcocugu = mycursor101m.fetchall()
                                            if amcahalaevlatcocugu.__len__()!=0:
                                                for i in range(amcahalaevlatcocugu.__len__()):
                                                    text = ""
                                                    toplamsayi += 1
                                                    text += "Yakınlık: Amca/Hala Torunu \n"
                                                    text += "Tc: " + str(amcahalaevlatcocugu[i][1])
                                                    text += "\nAd: " + str(amcahalaevlatcocugu[i][2])
                                                    text += "\nSoyad: " + str(amcahalaevlatcocugu[i][3])
                                                    text += "\nDoğum Tarihi: " + str(amcahalaevlatcocugu[i][4])
                                                    text += "\nİl: " + str(amcahalaevlatcocugu[i][5])
                                                    text += "\nİlçe: " + str(amcahalaevlatcocugu[i][6])
                                                    text += "\nAnne Adı: " + str(amcahalaevlatcocugu[i][7])
                                                    text += "\nAnne Tc: " + str(amcahalaevlatcocugu[i][8])
                                                    text += "\nBaba Adı: " + str(amcahalaevlatcocugu[i][9])
                                                    text += "\nBaba Tc: " + str(amcahalaevlatcocugu[i][10])
                                                    text += "\nUyruk: " + str(amcahalaevlatcocugu[i][11])
                                                    await client.send_message(SENDER, text  ,parse_mode='html')
                                                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + amcahalaevlatcocugu[i][1] + "' OR ANNETC='"+amcahalaevlatcocugu[i][1]+"' ")
                                                    amcahalatoruncocugu = mycursor101m.fetchall()
                                                    if amcahalatoruncocugu.__len__() !=0:
                                                        for i in range(amcahalatoruncocugu.__len__()):
                                                            text = ""
                                                            toplamsayi += 1
                                                            text += "Yakınlık: Amca/Hala Torunun Cocugu \n"
                                                            text += "Tc: " + str(amcahalatoruncocugu[i][1])
                                                            text += "\nAd: " + str(amcahalatoruncocugu[i][2])
                                                            text += "\nSoyad: " + str(amcahalatoruncocugu[i][3])
                                                            text += "\nDoğum Tarihi: " + str(amcahalatoruncocugu[i][4])
                                                            text += "\nİl: " + str(amcahalatoruncocugu[i][5])
                                                            text += "\nİlçe: " + str(amcahalatoruncocugu[i][6])
                                                            text += "\nAnne Adı: " + str(amcahalatoruncocugu[i][7])
                                                            text += "\nAnne Tc: " + str(amcahalatoruncocugu[i][8])
                                                            text += "\nBaba Adı: " + str(amcahalatoruncocugu[i][9])
                                                            text += "\nBaba Tc: " + str(amcahalatoruncocugu[i][10])
                                                            text += "\nUyruk: " + str(amcahalatoruncocugu[i][11])
                                                            await client.send_message(SENDER, text  ,parse_mode='html')
                                                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + amcahalatoruncocugu[i][1] + "' OR ANNETC='"+amcahalatoruncocugu[i][1]+"' ")
                                                            amchahalatoruntorunu = mycursor101m.fetchall()
                                                            if amchahalatoruntorunu.__len__() !=0:
                                                                for i in range(amchahalatoruntorunu.__len__()):
                                                                    text = ""
                                                                    toplamsayi += 1
                                                                    text += "Yakınlık: Amca/Hala Torununun Torunu \n"
                                                                    text += "Tc: " + str(amchahalatoruntorunu[i][1])
                                                                    text += "\nAd: " + str(amchahalatoruntorunu[i][2])
                                                                    text += "\nSoyad: " + str(amchahalatoruntorunu[i][3])
                                                                    text += "\nDoğum Tarihi: " + str(amchahalatoruntorunu[i][4])
                                                                    text += "\nİl: " + str(amchahalatoruntorunu[i][5])
                                                                    text += "\nİlçe: " + str(amchahalatoruntorunu[i][6])
                                                                    text += "\nAnne Adı: " + str(amchahalatoruntorunu[i][7])
                                                                    text += "\nAnne Tc: " + str(amchahalatoruntorunu[i][8])
                                                                    text += "\nBaba Adı: " + str(amchahalatoruntorunu[i][9])
                                                                    text += "\nBaba Tc: " + str(amchahalatoruntorunu[i][10])
                                                                    text += "\nUyruk: " + str(amchahalatoruntorunu[i][11])
                                                                    await client.send_message(SENDER, text  ,parse_mode='html')
                                            

                    #endregion amcahalavekuzen

                    #region dayıteyze
                    mycursor101m.execute("SELECT * FROM 101m WHERE TC='" + gannetc + "'")
                    annededtc = mycursor101m.fetchall()
                    if annededtc.__len__() !=0:
                        mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + annededtc[0][10] + "' AND NOT TC ='"+gannetc+"'")
                        dayibil = mycursor101m.fetchall()
                        if dayibil.__len__() !=0:
                            for i in range(dayibil.__len__()):
                                toplamsayi += 1
                                text=""
                                text += "Yakınlık: Dayı/Teyze \n"
                                text += "Tc: " + str(dayibil[i][1])
                                text += "\nAd: " + str(dayibil[i][2])
                                text += "\nSoyad: " + str(dayibil[i][3])
                                text += "\nDoğum Tarihi: " + str(dayibil[i][4])
                                text += "\nİl: " + str(dayibil[i][5])
                                text += "\nİlçe: " + str(dayibil[i][6])
                                text += "\nAnne Adı: " + str(dayibil[i][7])
                                text += "\nAnne Tc: " + str(dayibil[i][8])
                                text += "\nBaba Adı: " + str(dayibil[i][9])
                                text += "\nBaba Tc: " + str(dayibil[i][10])
                                text += "\nUyruk: " + str(dayibil[i][11])
                                await client.send_message(SENDER, text  ,parse_mode='html')

                                mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + dayibil[i][1] + "' OR ANNETC='"+dayibil[i][1]+"' ")
                                dayiteyzeevlat = mycursor101m.fetchall()
                                if dayiteyzeevlat.__len__() !=0:
                                    for i in range(dayiteyzeevlat.__len__()):
                                            text = ""
                                            toplamsayi += 1
                                            text += "Yakınlık: Dayı/Teyze Çocuğu \n"
                                            text += "Tc: " + str(dayiteyzeevlat[i][1])
                                            text += "\nAd: " + str(dayiteyzeevlat[i][2])
                                            text += "\nSoyad: " + str(dayiteyzeevlat[i][3])
                                            text += "\nDoğum Tarihi: " + str(dayiteyzeevlat[i][4])
                                            text += "\nİl: " + str(dayiteyzeevlat[i][5])
                                            text += "\nİlçe: " + str(dayiteyzeevlat[i][6])
                                            text += "\nAnne Adı: " + str(dayiteyzeevlat[i][7])
                                            text += "\nAnne Tc: " + str(dayiteyzeevlat[i][8])
                                            text += "\nBaba Adı: " + str(dayiteyzeevlat[i][9])
                                            text += "\nBaba Tc: " + str(dayiteyzeevlat[i][10])
                                            text += "\nUyruk: " + str(dayiteyzeevlat[i][11])
                                            await client.send_message(SENDER, text  ,parse_mode='html')
                                            
                                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + dayiteyzeevlat[i][1] + "' OR ANNETC='"+dayiteyzeevlat[i][1]+"' ")
                                            dayiteyzeevlatcocugu = mycursor101m.fetchall()
                                            if dayiteyzeevlatcocugu.__len__() !=0:
                                                for i in range(dayiteyzeevlatcocugu.__len__()):
                                                    text = ""
                                                    toplamsayi += 1
                                                    text += "Yakınlık: Dayı/Teyze Torunu \n"
                                                    text += "Tc: " + str(dayiteyzeevlatcocugu[i][1])
                                                    text += "\nAd: " + str(dayiteyzeevlatcocugu[i][2])
                                                    text += "\nSoyad: " + str(dayiteyzeevlatcocugu[i][3])
                                                    text += "\nDoğum Tarihi: " + str(dayiteyzeevlatcocugu[i][4])
                                                    text += "\nİl: " + str(dayiteyzeevlatcocugu[i][5])
                                                    text += "\nİlçe: " + str(dayiteyzeevlatcocugu[i][6])
                                                    text += "\nAnne Adı: " + str(dayiteyzeevlatcocugu[i][7])
                                                    text += "\nAnne Tc: " + str(dayiteyzeevlatcocugu[i][8])
                                                    text += "\nBaba Adı: " + str(dayiteyzeevlatcocugu[i][9])
                                                    text += "\nBaba Tc: " + str(dayiteyzeevlatcocugu[i][10])
                                                    text += "\nUyruk: " + str(dayiteyzeevlatcocugu[i][11])
                                                    await client.send_message(SENDER, text  ,parse_mode='html')
                                                    mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + dayiteyzeevlatcocugu[i][1] + "' OR ANNETC='"+dayiteyzeevlatcocugu[i][1]+"' ")
                                                    dayiteyztoruncocugu = mycursor101m.fetchall()
                                                    if dayiteyztoruncocugu.__len__() !=0:
                                                        for i in range(dayiteyztoruncocugu.__len__()):
                                                            text = ""
                                                            toplamsayi += 1
                                                            text += "Yakınlık: Dayı/Teyze Torunun Cocugu \n"
                                                            text += "Tc: " + str(dayiteyztoruncocugu[i][1])
                                                            text += "\nAd: " + str(dayiteyztoruncocugu[i][2])
                                                            text += "\nSoyad: " + str(dayiteyztoruncocugu[i][3])
                                                            text += "\nDoğum Tarihi: " + str(dayiteyztoruncocugu[i][4])
                                                            text += "\nİl: " + str(dayiteyztoruncocugu[i][5])
                                                            text += "\nİlçe: " + str(dayiteyztoruncocugu[i][6])
                                                            text += "\nAnne Adı: " + str(dayiteyztoruncocugu[i][7])
                                                            text += "\nAnne Tc: " + str(dayiteyztoruncocugu[i][8])
                                                            text += "\nBaba Adı: " + str(dayiteyztoruncocugu[i][9])
                                                            text += "\nBaba Tc: " + str(dayiteyztoruncocugu[i][10])
                                                            text += "\nUyruk: " + str(dayiteyztoruncocugu[i][11])
                                                            await client.send_message(SENDER, text  ,parse_mode='html')
                                                            mycursor101m.execute("SELECT * FROM 101m WHERE BABATC='" + dayiteyztoruncocugu[i][1] + "' OR ANNETC='"+dayiteyztoruncocugu[i][1]+"' ")
                                                            dayiteyzetoruntorunu = mycursor101m.fetchall()
                                                            if dayiteyzetoruntorunu.__len__() !=0:
                                                                for i in range(dayiteyzetoruntorunu.__len__()):
                                                                    text = ""
                                                                    toplamsayi += 1
                                                                    text += "Yakınlık: Dayı/Teyze Torununun Torunu \n"
                                                                    text += "Tc: " + str(dayiteyzetoruntorunu[i][1])
                                                                    text += "\nAd: " + str(dayiteyzetoruntorunu[i][2])
                                                                    text += "\nSoyad: " + str(dayiteyzetoruntorunu[i][3])
                                                                    text += "\nDoğum Tarihi: " + str(dayiteyzetoruntorunu[i][4])
                                                                    text += "\nİl: " + str(dayiteyzetoruntorunu[i][5])
                                                                    text += "\nİlçe: " + str(dayiteyzetoruntorunu[i][6])
                                                                    text += "\nAnne Adı: " + str(dayiteyzetoruntorunu[i][7])
                                                                    text += "\nAnne Tc: " + str(dayiteyzetoruntorunu[i][8])
                                                                    text += "\nBaba Adı: " + str(dayiteyzetoruntorunu[i][9])
                                                                    text += "\nBaba Tc: " + str(dayiteyzetoruntorunu[i][10])
                                                                    text += "\nUyruk: " + str(dayiteyzetoruntorunu[i][11])
                                                                    await client.send_message(SENDER, text  ,parse_mode='html')
                                            
                    #endregion dayıteyze

                    yenibakiye = int(bakiye) - int(tarifeSülale)
                    mycursor.execute("UPDATE kullanici SET bakiye = '" + str(yenibakiye) + "' WHERE kimlik='" + str(
                        sender.id) + "'")
                    dbcon.commit()
                    await client.send_message(SENDER, "Kalan Bakiye: " + str(yenibakiye), parse_mode='html')
                    text = "Toplam Sayi = " + str(toplamsayi)
                    await client.send_message(SENDER, text, parse_mode='html')
                    toplamsayi = 0
                

            else:
                await client.send_message(SENDER,
                                          "Bu Komut İçin Bakiyeniz Yetersiz, \nSorgu İçin Gerekli Jeton: '" + str(tarifeSülale) + "'\nMevcut Bakiye:'" + str(bakiye) + "'",
                                          parse_mode='html')


        else:
            sender = await event.get_sender()
            SENDER = sender.id
            await client.send_message(SENDER, "Sisteme Kayıtlı Değilsiniz. Yöneticiyle Görüşme Sağlayınız \n@RomanianR_admin",
                                  parse_mode='html')

    except Exception as e:
        print(e)
        await client.send_message(SENDER,
                                  "Lütfen Komutu Doğru Yazınız, /start Yazarak Komutları Nasıl Kullanacağınızı Öğrenebilirsiniz!",
                                  parse_mode='html')
        return


@client.on(events.NewMessage(pattern="(?i)/isimsorgu"))
async def start(event):
    try:
        sender = await event.get_sender()
        SENDER = sender.id
        kontrol = False
        mycursor.execute("SELECT * FROM kullanici")
        kullanici = mycursor.fetchall()
        bakiye = 0
        gelen = False
        for i in kullanici:
            if str(SENDER) == i[0]:
                kontrol = True
                bakiye = i[1]

        if kontrol == True:

            mycursor.execute("SELECT * FROM ucrettarifesi WHERE icerik = 'isimsorgu'")
            tarifeler = mycursor.fetchall()
            tarifeSülale = tarifeler[0][1]
            son = bakiye - tarifeSülale
            if son >= 0:
                sender = await event.get_sender()
                SENDER = sender.id
                yazilan = event.message.text.split(' ')

                if yazilan.__len__() == 4:
                    GAD = yazilan[1]
                    GSOYAD = yazilan[2]
                    GIL = yazilan[3]
                if yazilan.__len__() == 5:
                    GAD = yazilan[1] + " " + yazilan[2]
                    GSOYAD = yazilan[3]
                    GIL = yazilan[4]
                if yazilan.__len__() == 6:
                    GAD = yazilan[1] + " " + yazilan[2] + " " + yazilan[3]
                    GSOYAD = yazilan[4]
                    GIL = yazilan[5]
                if yazilan.__len__() == 7:
                    GAD = yazilan[1] + " " + yazilan[2] + " " + yazilan[3] + " " + yazilan[4]
                    GSOYAD = yazilan[5]
                    GIL = yazilan[6]
                mycursor101m.execute(
                    "SELECT * FROM 101m WHERE ADI= '" + GAD + "' AND SOYADI= '" + GSOYAD + "' AND NUFUSIL= '" + GIL + "'")
                gelenbil = mycursor101m.fetchall()
                say2 = 0
                text = ""
                if not gelenbil:
                    await client.send_message(SENDER, "Kayıt Bulunamadı, Lütfen Tekrar Deneyiniz.", parse_mode='html')
                else:
                    for i in gelenbil:
                        text = ""
                        text += "Tc: " + str(gelenbil[say2][1])
                        text += "\nAd: " + str(gelenbil[say2][2])
                        text += "\nSoyad: " + str(gelenbil[say2][3])
                        text += "\nDoğum Tarihi: " + str(gelenbil[say2][4])
                        text += "\nİl: " + str(gelenbil[say2][5])
                        text += "\nİlçe: " + str(gelenbil[say2][6])
                        text += "\nAnne Adı: " + str(gelenbil[say2][7])
                        text += "\nAnne Tc: " + str(gelenbil[say2][8])
                        text += "\nBaba Adı: " + str(gelenbil[say2][9])
                        text += "\nBaba Tc: " + str(gelenbil[say2][10])
                        text += "\nUyruk: " + str(gelenbil[say2][11]) 
                        say2 += 1
                        await client.send_message(SENDER, text, parse_mode='html')
                    yenibakiye = int(bakiye) - int(tarifeSülale)
                    mycursor.execute(
                        "UPDATE kullanici SET bakiye = '" + str(yenibakiye) + "' WHERE kimlik='" + str(sender.id) + "'")
                    dbcon.commit()
                    
                    text = ""
                    text = "Eşleşen Kayıt Sayısı: " + str(say2)
                    await client.send_message(SENDER, text, parse_mode='html')
                    await client.send_message(SENDER, "Yeni Bakiyeniz: " + str(yenibakiye), parse_mode='html')
            else:
                await client.send_message(SENDER,
                                          "Bu Komut İçin Bakiyeniz Yetersiz, \nSorgu İçin Gerekli Jeton: '" + str(tarifeSülale) + "'\nMevcut Bakiye:'" + str(bakiye) + "'",
                                          parse_mode='html')

        else:
            sender = await event.get_sender()
            SENDER = sender.id
            await client.send_message(SENDER, "Sisteme Kayıtlı Değilsiniz. Yöneticiyle Görüşme Sağlayınız \n@RomanianR_admin",
                                  parse_mode='html')
    except Exception as e:
        print(e)
        await client.send_message(SENDER,
                                  "Lütfen Komutu Doğru Yazınız, /start Yazarak Komutları Nasıl Kullanacağınızı Öğrenebilirsiniz!",
                                  parse_mode='html')
        return


@client.on(events.NewMessage(pattern="(?i)/tcgsm"))
async def select(event):
    try:
        sender = await event.get_sender()
        SENDER = sender.id
        kontrol = False
        mycursor.execute("SELECT * FROM kullanici")
        kullanici = mycursor.fetchall()
        bakiye = 0
        gelen = False
        for i in kullanici:
            if str(SENDER) == i[0]:
                kontrol = True
                bakiye = i[1]

        if kontrol == True:
            mycursor.execute("SELECT * FROM ucrettarifesi WHERE icerik = 'tcgsm'")
            tarifeler = mycursor.fetchall()
            tarifeSülale = tarifeler[0][1]
            son = bakiye - tarifeSülale
            if son >= 0:
                yazilan = event.message.text.split(' ')
                gtc = yazilan[1]

                mycursor.execute("SELECT GSM FROM gsmtelefon  where TC= '" + gtc + "'")
                mycursor101m.execute("SELECT ADI, SOYADI FROM 101m  where TC= '" + gtc + "'")
                gelenad = mycursor101m.fetchall()
                res = mycursor.fetchall()
                say = 0
                if res.__len__() != 0:
                    text = gtc + " Kimlik Numarasına Kayıtlı Gsm Bilgileri: \n"
                    for gad in gelenad:
                        text += "Adı: " + gelenad[0][0] + " Soyad: " + gelenad[0][1] + "\n \n"
                    for data in res:
                        text += "" + res[say][0] + " \n"
                        say = say + 1
                    await client.send_message(SENDER, text, parse_mode='html')
                    yenibakiye = int(bakiye) - int(tarifeSülale)
                    await client.send_message(SENDER, "Kalan Bakiyeniz: " + str(yenibakiye), parse_mode='html')
                    mycursor.execute(
                        "UPDATE kullanici SET bakiye = '" + str(yenibakiye) + "' WHERE kimlik='" + str(sender.id) + "'")
                    dbcon.commit()

                else:
                    text = gtc + "Tcsine Kayıtlı Olan Telefon Numarası Bulunamamktadır "
                    await client.send_message(SENDER, text, parse_mode='html')
            else:
                await client.send_message(SENDER,
                                          "Bu Komut İçin Bakiyeniz Yetersiz, \nSorgu İçin Gerekli Jeton: '" + str(tarifeSülale) + "'\nMevcut Bakiye:'" + str(bakiye) + "'",
                                          parse_mode='html')
        else:
            await client.send_message(SENDER, "Sisteme Kayıtlı Değilsiniz. Yöneticiyle Görüşme Sağlayınız \n@RomanianR_admin",
                                  parse_mode='html')

    except Exception as e:
        print(e)
        await client.send_message(SENDER,
                                  "Lütfen Komutu Doğru Yazınız, /start Yazarak Komutları Nasıl Kullanacağınızı Öğrenebilirsiniz!",
                                  parse_mode='html')
        return


@client.on(events.NewMessage(pattern="(?i)/gsmtc"))
async def select(event):
    try:
        mycursor = dbcon.cursor()
        sender = await event.get_sender()
        SENDER = sender.id
        kontrol = False
        mycursor.execute("SELECT * FROM kullanici")
        kullanici = mycursor.fetchall()
        bakiye = 0
        gelen = False
        for i in kullanici:
            if str(SENDER) == i[0]:
                kontrol = True
                bakiye = i[1]

        if kontrol == True:
            mycursor.execute("SELECT * FROM ucrettarifesi WHERE icerik = 'gsmtc'")
            tarifeler = mycursor.fetchall()
            tarifeSülale = tarifeler[0][1]
            son = bakiye - tarifeSülale
            if son >= 0:
                yazilan = event.message.text.split(' ')
                ggsm = yazilan[1]

                mycursor = dbcon.cursor()
                mycursor.execute("SELECT TC FROM gsmtelefon  where GSM= '" + ggsm + "'")
                res = mycursor.fetchall()

                say = 0
                if res.__len__() != 0:
                    mycursor101m.execute("SELECT ADI, SOYADI FROM 101m  where TC= '" + res[say][0] + "'")
                    gelenad = mycursor101m.fetchall()

                    text = ggsm + " GSM Numarasına Kayıtlı TC Bilgileri: \n" + "Ad: " + gelenad[0][0] + " Soyad: " + \
                           gelenad[0][1] + "\n \n"
                    text += "TC: " + res[say][0] + " \n"
                    yenibakiye = int(bakiye) - int(tarifeSülale)
                    mycursor.execute(
                        "UPDATE kullanici SET bakiye = '" + str(yenibakiye) + "' WHERE kimlik='" + str(sender.id) + "'")
                    dbcon.commit()
                    await client.send_message(SENDER, text, parse_mode='html')
                    await client.send_message(SENDER, "Kalan Bakiyeniz: " + str(yenibakiye), parse_mode='html')
                else:
                    text = ggsm + " Telefon Numarasına Kayıtlı Olan Telefon TC Bilgisi Bulunamamktadır "
                    await client.send_message(SENDER, text, parse_mode='html')

            else:
                await client.send_message(SENDER,
                                          "Bu Komut İçin Bakiyeniz Yetersiz, \nSorgu İçin Gerekli Jeton: '" + str(tarifeSülale) + "'\nMevcut Bakiye:'" + str(bakiye) + "'",
                                          parse_mode='html')


        else:
            await client.send_message(SENDER, "Sisteme Kayıtlı Değilsiniz. Yöneticiyle Görüşme Sağlayınız \n@RomanianR_admin",
                                  parse_mode='html')

    except Exception as e:
        print(e)
        await client.send_message(SENDER, "Lütfen Komutu Doğru Yazınız, /start Yazarak Komutları Nasıl Kullanacağınızı Öğrenebilirsiniz!", parse_mode='html')
        return


mycursor = dbcon.cursor()
mycursor101m = dbcon101m.cursor()

print("Bot Başladı.")
client.run_until_disconnected()