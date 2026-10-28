#Tapşırıq: Python-da tələbələrin qiymətlərini idarə edən proqram yaz.

# Şərtlər:
#
# İstifadəçi neçə tələbə olduğunu daxil etsin.
#
# Hər tələbənin adını və 3 fənn üzrə qiymətini daxil etsin.
#
# Hər tələbənin orta balını hesabla.
#
# Orta balı 90 və yuxarıdırsa, Əla;
#
# 70–89 arasındadırsa, Yaxşı;
#
# 50–69 arasındadırsa, Kafi;
#
# 50-dən aşağıdırsa, Kəsildi yazılsın.
#
# Bütün tələbələri orta bala görə böyükdən kiçiyə sırala.
#
# Ən yüksək orta bala sahib tələbəni göstər.


def telebeler():

    telebeler = []
    while True:
        try:

            say = int(input("Siyahida nece telebe var: "))

            if say <=0:
                print("Secimi duzgun edin!")
                break


            for i in range(say):
                print(f"\n {i+1}- telebe")

                ad = input("Telebenin adi: ").capitalize()

                qiymet_1 = float(input("Birinci fenden bali: "))
                qiymet_2 = float(input("Ikinci fenden bali: "))
                qiymet_3 = float(input("Ucuncu fenden bali: "))

                orta = (qiymet_1+qiymet_2+qiymet_3) / 3

                if orta >= 90:
                    netice = 'Ela'

                elif orta >= 70:
                    netice = 'Yaxsi'

                elif orta >= 50:
                    netice = "Kafi"

                else:
                    netice = "Kesildi"



                telebe = {
                    'ad': ad,
                    'orta': orta,
                    'netice': netice
                }

                telebeler.append(telebe)

                # Tələbələri orta bala görə azalan sıra ilə düzürük
            telebeler.sort(key=lambda x: x['orta'], reverse=True)

            print("\n--------Telebelerin neticeleri---------")
            for telebe in telebeler:
                print(
                    f'Ad: {telebe['ad']} |'
                    f'Orta bal {telebe ['orta']:.2f} |'
                    f'Netice {telebe['netice']}'
                )

            # Ən yüksək orta bala sahib tələbə
            if telebeler:

                print("\n --------En yuksek necite ---------")
                print("Telebe",telebeler[0]['ad'])
                print("Orta bal",round(telebeler[0]["orta"],2))



        except ValueError:
            print("Xəta! Zəhmət olmasa, tam ədəd daxil edin.")


telebeler()
