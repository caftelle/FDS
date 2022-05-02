
###########################################################################
########################## DEVELOPED BY CAFTELLE ##########################
########################## DEVELOPED BY CAFTELLE ##########################
########################## DEVELOPED BY CAFTELLE ##########################
###########################################################################
#################################  FDS  ###################################
######################## V E R S I O N  1 . 0 . 0 #########################
###########################################################################
###########################################################################
################## Caftelle Created by Furkan ARINCI ######################
###########################################################################


def bolgekontrol():
    print('##################################################################################')
    print('## Bölge ayarları kontrol ediliyor...')
    alkabolgefile = open("alkabolge.txt", "r")
    alkabolgefilelist = ''.join(alkabolgefile)

    orjinbolgefile = open("orjinbolge.txt", "r")
    orjinbolgefilelist = ''.join(orjinbolgefile)

    metrobilbolgefile = open("metrobilbolge.txt", "r")
    metrobilbolgefilelist = ''.join(metrobilbolgefile)

    ccfile = open("cc.txt", "r")
    ccfilelist = ''.join(ccfile)

    if not '@turksat.com.tr' in ccfilelist:
        print('##################################################################################')
        print('## Lütfen Mail Ekini girin.')
        print('##################################################################################')
        cc = input('## Eke koymak istediginiz Mail adresini yazınız : ')
        print('## Eke koymak istediginiz Mail adresi : ' + cc)
        with open('cc.txt', 'w', encoding="utf-8") as f:
            f.write(cc)
            print('## Dosyaya Kaydedildi.')

    if not '@turksat.com.tr' in alkabolgefilelist:
        print('##################################################################################')
        print('## Lütfen Al-Ka Bölge Sorumlusu Kişileri Tanımlayın.')
        print('##################################################################################')
        alkabolge = input('## Al-Ka Bölgesi Sorumlusu Mail adresini yazınız : ')
        print('## Al-Ka Bölgesi sorumlusu mail adresi : ' + alkabolge)
        with open('alkabolge.txt', 'w', encoding="utf-8") as f:
            f.write(alkabolge)
            print('## Dosyaya Kaydedildi.')

    if not '@turksat.com.tr' in orjinbolgefilelist:
        print('##################################################################################')
        print('## Lütfen Orjin Bölge Sorumlusu Kişileri Tanımlayın.')
        print('##################################################################################')
        orjinbolge = input('## Orjin Bölgesi Sorumlusu Mail adresini yazınız : ')
        print('Orjin Bölgesi sorumlusu mail adresi : ' + orjinbolge)
        with open('orjinbolge.txt', 'w', encoding="utf-8") as f:
            f.write(orjinbolge)
            print('Dosyaya Kaydedildi.')

    if not '@turksat.com.tr' in metrobilbolgefilelist:
        print('##################################################################################')
        print('## Lütfen Metrobil Bölge Sorumlusu Kişileri Tanımlayın.')
        print('##################################################################################')
        metrobilbolge = input('## Metrobil Bölgesi Sorumlusu Mail adresini yazınız : ')
        print('## Metrobil Bölgesi sorumlusu mail adresi : ' + metrobilbolge)
        with open('metrobilbolge.txt', 'w', encoding="utf-8") as f:
            f.write(metrobilbolge)
            print('## Dosyaya Kaydedildi.')


    print('## Bölge Ayarları Tamamlandı.')
    print('##################################################################################')

def bolgeduzenleme():

        print('##################################################################################')
        print('## Bölge Ayarları Düzenleme sihirbazı başlatılıyor...')
        print('[1] Al-Ka Bölgesi | [2] Orjin Bölgesi | [3] Metrobil Bölgesi | [4] Mail Eki' )
        duzenleme= input('## Düzenlemek istediğiniz bölgeyi seçiniz : ')
        print('##################################################################################')
        duzenlemelist = ''.join(duzenleme)


        if '1' in duzenlemelist:
            alkabolgefile = open("alkabolge.txt", "r")
            alkabolge = ''.join(alkabolgefile)
            print('##################################################################################')
            print('## Al-Ka Bölgesi Güncel Sorumlu Mail Adresi : ' + alkabolge)
            print('Lütfen Al-Ka Bölge Sorumlusu Güncel Kişileri Tanımlayın.')
            print('##################################################################################')
            alkabolge = input('## Al-Ka Bölgesi Sorumlusu Mail adresini yazınız : ')
            print('## Al-Ka Bölgesi sorumlusu mail adresi : ' + alkabolge)
            with open('alkabolge.txt', 'w', encoding="utf-8") as f:
                f.write(alkabolge)
                print('## Dosyaya Güncellendi ve Kaydedildi.')

        if '2' in duzenlemelist:
            orjinbolgefile = open("orjinbolge.txt", "r")
            orjinbolge = ''.join(orjinbolgefile)
            print('##################################################################################')
            print('## Orjin Bölgesi Güncel Sorumlu Mail Adresi : ' + orjinbolge)
            print('## Lütfen Orjin Bölge Sorumlusu Güncel Kişileri Tanımlayın.')
            print('##################################################################################')
            orjinbolge = input('## Orjin Bölgesi Sorumlusu Mail adresini yazınız : ')
            print('## Al-Ka Bölgesi sorumlusu mail adresi : ' + orjinbolge)
            with open('orjinbolge.txt', 'w', encoding="utf-8") as f:
                f.write(orjinbolge)
                print('## Dosyaya Güncellendi ve Kaydedildi.')

        if '3' in duzenlemelist:
            metrobilbolgefile = open("metrobilbolge.txt", "r")
            metrobilbolge = ''.join(metrobilbolgefile)
            print('##################################################################################')
            print('## Metrobil Bölgesi Güncel Sorumlu Mail Adresi : ' + metrobilbolge)
            print('## Lütfen Metrobil Bölge Sorumlusu Güncel Kişileri Tanımlayın.')
            print('##################################################################################')
            metrobilbolge = input('## Metrobil Bölgesi Sorumlusu Mail adresini yazınız : ')
            print('## Al-Ka Bölgesi sorumlusu mail adresi : ' + metrobilbolge)
            with open('metrobilbolge.txt', 'w', encoding="utf-8") as f:
                f.write(metrobilbolge)
                print('## Dosyaya Güncellendi ve Kaydedildi.')

        if '4' in duzenlemelist:
            ccfile = open("cc.txt", "r")
            cc = ''.join(ccfile)
            print('##################################################################################')
            print('## Eke koymak istediginiz Mail adresi :  ' + cc)
            print('## Lütfen Al-Ka Bölge Sorumlusu Güncel Kişileri Tanımlayın.')
            print('##################################################################################')
            cc = input('## Eke koymak istediginiz Mail adresini yazınız : ')
            print('## Eke koymak istediginiz Güncel Mail adresi :  ' + cc)
            with open('cc.txt', 'w', encoding="utf-8") as f:
                f.write(cc)
                print('## Dosyaya Güncellendi ve Kaydedildi.')

def sistemegiris():

    print('##################################################################################')
    print('## Fatura Düzeltme Sihirbazı Başlatılıyor...')
    bolgekontrol()
    print('##################################################################################')
    print('Fatura Düzeltme Sihirbazına Hoşgeldiniz. \nCaftelle Created by Furkan ARINCI')
    print('##################################################################################')
    print('[1] Al-Ka Bölgesi | [2] Orjin Bölgesi | [3] Metrobil Bölgesi | [4] Bölge Sorumlusu Düzenleme')

    bolgesecim = input('## Faturasını düzeltmek istediğiniz Bölgeyi Seçiniz : ')
    print('##################################################################################')
    bolgesecimlist = ''.join(bolgesecim)

    if '4' in bolgesecimlist :

        bolgeduzenleme()

    hizmetno = input('## Hizmet Numarasını Giriniz : ')
    print('##################################################################################')
    modemdetay=''
    stbdetay=''
    smartcarddetay=''
    ikutudetay=''
    conaxmoduldetay=''

    print('[1] Modem | [2] HD STB | [3] Smart Card | [4] i-Kutu | [5] Conax Modül')
    cihazsecim = input('## Lütfen İade Aldığınız Cihazları seçiniz : ')
    cihazsecimlist = ''.join(cihazsecim)

    if  '1' in cihazsecimlist:
        print('##################################################################################')
        print('## MODEM')
        print('##################################################################################')
        modemdetay= ' MODEM '
        print('[1] Adaptör | [2] RJ-45 | [3] RJ-11')
        modemaksesuar = input('Lütfen iade aldığınız aksesuarları seçiniz : ')
        modemaksesuarlist = ''.join(modemaksesuar)


        if not '1' in modemaksesuarlist:
            print('## MODEM Adaptör iade alınmadı.')
            modemdetay = modemdetay + '(Adaptör Eksik)'
        if not '2' in modemaksesuarlist:
            print('## MODEM R-45 iade alınmadı.')
            modemdetay = modemdetay + '(RJ-45 Eksik)'
        if not '3' in modemaksesuarlist:
            print('## MODEM R-11 iade alınmadı.')
            modemdetay = modemdetay + '(RJ-11 Eksik)'


    if '2' in cihazsecimlist:
        print('##################################################################################')
        print('## HD STB ')
        print('##################################################################################')
        stbdetay = ', HD STB '
        print('[1] Adaptör | [2] Kumanda | [3] HDMI')
        stbaksesuar = input('## Lütfen iade aldığınız aksesuarları seçiniz : ')
        stbaksesuarlist = ''.join(stbaksesuar)


        if not '1' in stbaksesuarlist:
            print('## HD STB Adaptör iade alınmadı.')
            stbdetay = stbdetay + '(Adaptör Eksik)'
        if not '2' in stbaksesuarlist:
            print('## HD STB Kumanda iade alınmadı.')
            stbdetay = stbdetay + '(Kumanda Eksik)'
        if not '3' in stbaksesuarlist:
            print('## HD STB HDMI iade alınmadı.')
            stbdetay = stbdetay + '(HDMI Eksik)'

    if '3' in cihazsecimlist:
        print('##################################################################################')
        print('## SMART CARD İade alındı.')
        print('##################################################################################')
        smartcarddetay = ', SMART CARD'

    if '4' in cihazsecimlist:
        print('##################################################################################')
        print('## i-Kutu')
        print('##################################################################################')
        ikutudetay = ', i-Kutu '
        print('[1] Adaptör | [2] i-Kutu Kumanda | [3] Ethernet 1.5 Mt. | [4] HDMI')
        ikutuaksesuar = input('## Lütfen iade aldığınız aksesuarları seçiniz : ')
        ikutuaksesuarlist = ''.join(ikutuaksesuar)

        if not '1' in ikutuaksesuarlist:
            print('## i-Kutu Adaptör iade alınmadı.')
            ikutudetay = ikutudetay + '(Adaptör Eksik)'
        if not '2' in ikutuaksesuarlist:
            print('## i-Kutu Kumanda iade alınmadı.')
            ikutudetay = ikutudetay + '(Kumanda Eksik)'
        if not '3' in ikutuaksesuarlist:
            print('## i-Kutu Ethernet 1.5 Mt. iade alınmadı.')
            ikutudetay = ikutudetay + '(Ethernet 1.5 Mt. Eksik)'
        if not '4' in ikutuaksesuarlist:
            print('## i-Kutu HDMI iade alınmadı.')
            ikutudetay = ikutudetay + '(HDMI Eksik)'

    if '5' in cihazsecimlist:
        print('##################################################################################')
        print('## Conak Modül İade alındı. ')
        print('##################################################################################')
        conaxmoduldetay = ', CONAX MODUL '

    mailtext = 'Merhabalar, \n\n' + hizmetno + ' hizmet numaralı abonemizin' + modemdetay + stbdetay + smartcarddetay + ikutudetay + conaxmoduldetay + ' cihazları iade alındı.\nFatura güncelenmesi konusunda yardımlarınızı bekliyoruz. \n\niyi calısmalar.\n| Developed by Caftelle'

    with open('mailmanuel.txt', 'w', encoding="utf-8") as f:
        f.write(mailtext)

    try:
        import win32com.client as win32
        print('##################################################################################')
        print("## Outlook Uygulamasını Açıyorum...")

        if '1' in bolgesecimlist:
            alkabolgefile = open("alkabolge.txt", "r")
            alkabolge = ''.join(alkabolgefile)

            ccfile = open("cc.txt", "r")
            cc = ''.join(ccfile)

            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = alkabolge
            mail.CC = cc
            mail.Subject = hizmetno + ' Al-Ka Bölge Fatura Düzeltmesi hk.'
            mail.HtmlBody = mailtext
            mail.Display(True)
            print('##################################################################################')
            print('## Fatura Düzeltme Sihirbazını kullandıgınız için teşekkür ederiz.')
            print('##################################################################################')

        if '2' in bolgesecimlist:
            orjinbolgefile = open("orjinbolge.txt", "r")
            orjinbolge = ''.join(orjinbolgefile)

            ccfile = open("cc.txt", "r")
            cc = ''.join(ccfile)

            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = orjinbolge
            mail.CC = cc
            mail.Subject = hizmetno + ' Orjin Bölge Fatura Düzeltmesi hk.'
            mail.HtmlBody = mailtext
            mail.Display(True)
            print('##################################################################################')
            print('## Fatura Düzeltme Sihirbazını kullandıgınız için teşekkür ederiz.')
            print('##################################################################################')

        if '2' in bolgesecimlist:

            metrobilbolgefile = open("metrobilbolge.txt", "r")
            metrobilbolge = ''.join(metrobilbolgefile)
            ccfile = open("cc.txt", "r")
            cc = ''.join(ccfile)

            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = metrobilbolge
            mail.CC = cc
            mail.Subject = hizmetno + ' Metrobil Bölge Fatura Düzeltmesi hk.'
            mail.HtmlBody = mailtext
            mail.Display(True)
            print('##################################################################################')
            print('## Fatura Düzeltme Sihirbazını kullandıgınız için teşekkür ederiz.')
            print('##################################################################################')
    except:

        import webbrowser
        print('##################################################################################')
        print("## Outlook Uygulaması Zaten Açık ve Arkaplanda Bekliyor yada Kurulumu Yapılmamış Olabilir...")
        print("## Posta Uygulamasını Açıyorum...")

        if '1' in bolgesecimlist:
            alkabolgefile = open("alkabolge.txt", "r")
            alkabolge = ''.join(alkabolgefile)

            ccfile = open("cc.txt", "r")
            cc = ''.join(ccfile)

            mailTo = alkabolge
            mailCC = cc
            mailSubject = hizmetno + ' Al-Ka Bölge Fatura Düzeltmesi hk.'
            mailHtmlBody = mailtext
            webbrowser.open("mailto:" + mailTo + '?cc=' + mailCC + '&subject=' + mailSubject + '&body=' + mailHtmlBody,
                            new=1)
            print('## Fatura Düzeltme Sihirbazını kullandıgınız için teşekkür ederiz.')

        if '2' in bolgesecimlist:
            orjinbolgefile = open("orjinbolge.txt", "r")
            orjinbolge = ''.join(orjinbolgefile)

            ccfile = open("cc.txt", "r")
            cc = ''.join(ccfile)

            mailTo = orjinbolge
            mailCC = cc
            mailSubject = hizmetno + ' Orjin Bölge Fatura Düzeltmesi hk.'
            mailHtmlBody = mailtext
            webbrowser.open("mailto:" + mailTo + '?cc=' + mailCC + '&subject=' + mailSubject + '&body=' + mailHtmlBody,
                            new=1)
            print('## Fatura Düzeltme Sihirbazını kullandıgınız için teşekkür ederiz.')

        if '2' in bolgesecimlist:
            metrobilbolgefile = open("metrobilbolge.txt", "r")
            metrobilbolge = ''.join(metrobilbolgefile)
            ccfile = open("cc.txt", "r")
            cc = ''.join(ccfile)

            mailTo = metrobilbolge
            mailCC = cc
            mailSubject = hizmetno + ' Metrobil Bölge Fatura Düzeltmesi hk.'
            mailHtmlBody = mailtext
            webbrowser.open("mailto:" + mailTo + '?cc=' + mailCC + '&subject=' + mailSubject + '&body=' + mailHtmlBody,
                            new=1)
            print('##################################################################################')
            print('## Fatura Düzeltme Sihirbazını kullandıgınız için teşekkür ederiz.')
            print('##################################################################################')

        with open('mailmanuel.txt', 'w', encoding="utf-8") as f:
            f.write(mailtext)
            print('##################################################################################')
            print('## Dosya mailmanuel adıyla kaydedildi.')

            print('## Fatura Düzeltme Sihirbazını kullandıgınız için teşekkür ederiz.')
            print('##################################################################################')


sistemegiris()


###########################################################################
########################## DEVELOPED BY CAFTELLE ##########################
########################## DEVELOPED BY CAFTELLE ##########################
########################## DEVELOPED BY CAFTELLE ##########################
###########################################################################
#################################  FDS  ###################################
######################## V E R S I O N  1 . 0 . 0 #########################
###########################################################################
###########################################################################
################## Caftelle Created by Furkan ARINCI ######################
###########################################################################