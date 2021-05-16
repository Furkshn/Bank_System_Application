import time
import datetime

zaman = datetime.datetime.ctime(datetime.datetime.now())



class BankAccount():


    banka_faiz = 15.0                                                    # Class Methods & Attributes

    dolar_tl = 8.20

    bitcoin = 60000

    ethereum = 4000

    @classmethod
    def calculating_price(cls):

        price_btc = cls.bitcoin * cls.dolar_tl

        price_eth = cls.ethereum * cls.dolar_tl

        return price_btc,price_eth


    @classmethod
    def current_prices(cls):

        return f"""    --- Faiz Oranı: %{cls.banka_faiz}
    ------ Dolar: {cls.dolar_tl} TL
    --------- Bitcoin: {cls.calculating_price()[0]} TL
    ------------ Ethereum: {cls.calculating_price()[1]} TL"""


    def __init__(self,kullanıcı_adı,kullanıcı_şifre):                               # Instances Methods

        self.owner = kullanıcı_adı
        self.balance = 500.0
        self.şifre = kullanıcı_şifre
        self.crypto_balance = 5.0        # In Btc
        self.crypto_balance_eth = 5.0    # In Eth


    def getBalance(self):

        return f"Sayın {self.owner}, hesabınızdaki toplam miktar: {self.balance} TL'dir."



    def getBalance_crypto_btc(self):

            return f"Sayın {self.owner}, kripto para cüzdanınızdaki toplam BTC miktarı: {self.crypto_balance} BTC'dir."


    def getBalance_crypto_eth(self):


        return f"Sayın {self.owner}, kripto para cüzdanınızdaki toplam ETH miktarı: {self.crypto_balance_eth} ETH'dur."



    def deposit(self,amount):

        if amount > 0:
            self.balance += amount
            return self.getBalance()

        else:
            return "Uyarı ! Yatırıcağınız Para Miktarı En Az 1 Tl Olmalıdır."


    def withdraw(self,amount):

        if self.balance >= amount and self.balance >0:

            self.balance -= amount

            return f"Banka hesabınızdan çektiğiniz miktar: {amount} TL'dir."

        else:

            return "Uyarı ! Bakiyenizdeki Miktar Kadar Para Çekebilirsiniz !"



    def invest_interest(self,amount):

        if  self.balance > 0 and  self.balance >= amount:

            self.balance += (amount * BankAccount.banka_faiz) / 100

            return f"Faize yatırdığınız toplam para {amount} TL'dir. Toplam alacağınız faiz getirisi: {(amount * BankAccount.banka_faiz) / 100} TL'dir."

        else:

            return "Hesabınızda Yeterince Para Bulunmamaktadır."


    def buy_btc(self,amount):


        if self.balance > 0 and self.balance >= amount:

            self.balance -= amount

            self.crypto_balance += amount / BankAccount.calculating_price()[0]   # BTC FİYATI

            return f"Toplam alınan Bitcoin(BTC) miktarı: {amount / BankAccount.calculating_price()[0]}"

        else:

            return "Hesabınızda Yeterince Para Bulunmamaktadır."


    def buy_eth(self, amount):

        if self.balance > 0 and self.balance >= amount:

            self.balance -= amount

            self.crypto_balance_eth += amount / BankAccount.calculating_price()[1]   # ETH FİYATI

            return f"Toplam alınan Ethereum(ETH) miktarı: {amount / BankAccount.calculating_price()[1]}"

        else:

            return "Hesabınızda Yeterince Para Bulunmamaktadır."


    def withdraw_btc(self,amount):

        if self.crypto_balance > 0 and self.crypto_balance >= amount:

            self.crypto_balance -= amount

            self.balance += amount * BankAccount.calculating_price()[0]

            print(f"Çekeceğiniz Bitocin(BTC) miktarının TL cinsinden değeri: {amount * BankAccount.calculating_price()[0]} TL'dir.")

            return f"Bitcoin cüzdanınızdan çektiğiniz miktar: {amount} BTC"

        else:

            return "Uyarı ! Cüzdanınızdaki Miktar Kadar Bitcoin(BTC) Çekebilirsiniz !"


    def withdraw_eth(self,amount):

        if self.crypto_balance_eth > 0 and self.crypto_balance_eth >= amount:

            self.crypto_balance_eth -= amount

            self.balance += amount * BankAccount.calculating_price()[1]

            print(f"Çekeceğiniz Ethereum(ETH) miktarının TL cinsinden değeri: {amount * BankAccount.calculating_price()[1]} TL'dir.")

            return f"Ethereum cüzdanınızdan çektiğiniz miktar: {amount} ETH"

        else:

            return "Uyarı ! Cüzdanınızdaki Miktar Kadar Ethereum(ETH) Çekebilirsiniz !"





işlem_sayısı = 3

while True:          # Genel Uygulama Döngüsü


    kullanıcı_adı = input(""" -----   Banka Uygulamasına Hoşgeldiniz :)     ----- 

    Lütfen Adınızı ve Soyadınızı Giriniz:""")
    şifre = input("Lütfen Banka Hesabı Şifrenizi Giriniz:")

    if len(şifre) == 11:

        hesap = BankAccount(kullanıcı_adı, şifre)
        print(f"Sayın {kullanıcı_adı} Banka Hesabınıza Başarılı Bir Şekilde Giriş Yaptınız." + "\n")

    else:

        if işlem_sayısı > 0:

            işlem_sayısı -= 1
            print("Uyarı ! Eksik veya Yanlış Şifre Girdiniz !")
            print("Kalan Şifre Girme Hakkı:", işlem_sayısı, "\n")
            continue

        elif işlem_sayısı == 0:

            print("Size Tanınan Şifre Girme Hakkı Limitinizi Doldurdunuz !")
            print("Banka Hesabınızı Güvenliğiniz İçin Kitledik ! Lütfen Müşteri Hizmetlerine Bağlanın.")
            break


    while True:          # Bankacılık İşlemlerinin While Döngüsü


        islem = input("""Lütfen Aşağıdaki Seçeneklerden İşlem Türünü Seçiniz:

         - Banka Hesabınıza Para Yatırmak İçin: 1
         -- Banka Hesabınızdan Para Çekmek İçin: 2
         --- Banka Hesabınızdaki Bakiyeyi Görüntülemek İçin: 3
         ---- Faiz Yatırımı Yapmak İçin: 4
         ----- Kripto Para İşlemleri Yapmak İçin 5'e Basınız... 

         Lütfen Banka İşleminizi Seçiniz: """)

        if islem == "1":

            amount = int(input("Lütfen Yatırmak İstediğiniz Miktarı Giriniz:"))
            print(hesap.deposit(amount))
            print("")


        elif islem == "2":

            amount = int(input("Lütfen Çekmek İstediğiniz Miktarı Giriniz:"))
            print(hesap.getBalance() + "\n")
            print(hesap.withdraw(amount))
            print(hesap.getBalance())
            print("")



        elif islem == "3":

            print(hesap.getBalance())
            print("")



        elif islem =="4":

            amount = int(input("Lütfen Yatırmak İstediğiniz Miktarı Giriniz:"))
            print(hesap.getBalance())
            print("")
            print(hesap.invest_interest(amount))
            print(hesap.getBalance())
            print("")


        while True:  # Kripto Para İşlemleri İçin Oluşturulan Döngü

            if islem == "5":

                crypto_process = input("""Lütfen Aşağıdaki Seçeneklerden Yapacağınız İşlemi Seçiniz:
                      Kripto Para Almak İçin: 1
                      Kripto Para Çekmek İçin: 2
                      Kripto Para Cüzdanınızı Görüntülemek İçin: 3'e Basınız...

                      Lütfen İşlem Seçiniz:""")

                if crypto_process == "1":

                    crypto_choices = input("""Lütfen Alacağınız Kripto Parayı Seçiniz:

                    --- Bitcoin İçin: 1

                    --- Ethereum İçin: 2'ye Basınız...

                    Lütfen Seçeneklerden En Az Birini Seçiniz:""")

                    if crypto_choices == "1":

                        print(hesap.getBalance())
                        print(hesap.getBalance_crypto_btc() + "\n")
                        amount = int(input("Lütfen Yatıracağınız Para Miktarını Giriniz:"))
                        print(hesap.buy_btc(amount))
                        print(hesap.getBalance() + "\n")

                        print("Hesap Özeti: ", hesap.getBalance_crypto_btc())
                        print("")



                    elif crypto_choices == "2":

                        print(hesap.getBalance())
                        print(hesap.getBalance_crypto_eth() + "\n")
                        amount = int(input("Lütfen Yatıracağınız Para Miktarını Giriniz:"))
                        print(hesap.buy_eth(amount))
                        print(hesap.getBalance() + "\n")

                        print("Hesap Özeti: ", hesap.getBalance_crypto_eth())
                        print("")



                elif crypto_process == "2":

                    crypto_choices = input("""Lütfen Çekeceğiniz Kripto Parayı Seçiniz:

                                        --- Bitcoin İçin: 1

                                        --- Ethereum İçin: 2'ye Basınız...

                                        Lütfen Seçeneklerden En Az Birini Seçiniz:""")

                    if crypto_choices == "1":

                        print(hesap.getBalance())
                        print(hesap.getBalance_crypto_btc() + "\n")
                        amount = int(input("Lütfen Çekeceğiniz Bitcoin(BTC) Miktarını Giriniz:"))
                        print("")
                        print(hesap.withdraw_btc(amount))
                        print(hesap.getBalance() + "\n")

                        print("Hesap Özeti: ", hesap.getBalance_crypto_btc())
                        print("")



                    elif crypto_choices == "2":

                        print(hesap.getBalance())
                        print(hesap.getBalance_crypto_eth() + "\n")
                        amount = int(input("Lütfen Çekeceğiniz Ethereum(ETH) Miktarını Giriniz:"))
                        print("")
                        print(hesap.withdraw_eth(amount))
                        print(hesap.getBalance() + "\n")

                        print("Hesap Özeti: ", hesap.getBalance_crypto_eth())
                        print("")



                elif crypto_process == "3":

                    crypto_choices = input("""Lütfen Görüntülemek İstediğiniz Kripto Para Cüzdanını Seçiniz:

                                        --- Bitcoin İçin: 1

                                        --- Ethereum İçin: 2'ye Basınız...

                                        Lütfen Seçeneklerden En Az Birini Seçiniz:""")

                    if crypto_choices == "1":

                        print(hesap.getBalance())
                        print("")
                        print("Hesap Özeti: ", hesap.getBalance_crypto_btc())
                        print("")



                    elif crypto_choices == "2":

                        print(hesap.getBalance())
                        print("")
                        print("Hesap Özeti: ", hesap.getBalance_crypto_eth())
                        print("")


                işlem_devam = input("Başka Bir Kripto Para İşlemi Yapmak İster Misiniz ?(E / H)")
                if işlem_devam == "E" or işlem_devam =="e":
                    continue

                else:
                    time.sleep(0.5)
                    print("Yönlendiriliyor...")
                    print("")
                    break

            break



        işlem_devam = input("Başka Bir İşlem Yapmak İster Misiniz ?(E / H)")

        if işlem_devam == "E" or işlem_devam =="e":
            continue

        else:

            time.sleep(0.5)
            print("Banka Uygulamasından Çıkılıyor...")
            print("")
            break


    print("Yine Bekleriz...")
    print(zaman)
    break
































