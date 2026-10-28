import random
from math import trunc


#Tapşırıq: Python-da bir ədəd təxmin etmə oyunu yaz.

# Şərtlər:
#
# Kompüter 1 ilə 100 arasında təsadüfi bir ədəd seçsin.
#
# İstifadəçi ədədi təxmin etsin.
#
# Ədəd böyükdürsə, "Daha kiçik ədəd daxil et" yazılsın.
#
# Ədəd kiçikdirsə, "Daha böyük ədəd daxil et" yazılsın.
#
# Düz tapdıqda neçə cəhd etdiyini göstərsin.


def eded_texmin_et():
    eded = random.randint(1,10)

    ceht = 0

    while True:
        try:
            eded_tap = int(input("Zehmet olmasa 1-100 arasi bir eded girin : "))
            ceht +=1
            #print(eded)

            if eded_tap > eded:
                print("Sizin {} yazdiginiz eded gizledilen ededen boyukdur:".format(eded_tap))
            elif eded_tap < eded:
                print("Sizin {} yazdiginiz eded gizledilen ededen kicikdir:".format(eded_tap))

            else:
                print("Dogrudur Siz ededi tapdiniz Gizledilen eded {} yazdiginiz eded {}".format(eded,eded_tap))
                print("Cehd sayi", ceht)
                break

        except ValueError:
            print("Zehmet olmasa eded girin")

eded_texmin_et()





