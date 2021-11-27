
syotetty_luku = int(input('Syota jokin positiivinen kokonaisluku: '))

on_alkuluku = True
kasvava_luku = int("2")

while kasvava_luku < syotetty_luku:
    if(syotetty_luku % kasvava_luku == 0):
        on_alkuluku = False

    kasvava_luku += 1


if on_alkuluku == True:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")

