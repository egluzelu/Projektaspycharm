pajamos = []
islaidos = []
islaidu_eilute = []
pajamu_eilute = []
pajamu_suma = []
islaidu_suma = []

while True:
    print("Pasirinkite operacija: \n"
        "1. Iveskite pajamas: \n"
        "2. Iveskite islaidas: \n"
        "3. Pajamu eilutes: \n"       
        "4. Islaidu eilutes: \n" 
        "5. Statistika: \n"
        "6. Iseiti. \n")

    ivestis = input("Pasirinkite komanda: ")

    if ivestis == "6":
        print("End")
        break

    if ivestis not in ("1", "2", "3", "4", "5"):
        print ("Blogai pasirinkote ivesti")
        continue

    if ivestis == "1":
        menuo = int(input("Iveskite menesi skaiciumi: "))
        pajamu_tipas = input("Iveskite pajamu tipa: ")
        pajamu_suma = int(input("Iveskite pajamu suma: "))
        pajamu_eilute = [menuo, pajamu_tipas, pajamu_suma]
        pajamos.append(pajamu_eilute)
        print(f"Per {menuo} men. jusu pajamos uz {pajamu_tipas} buvo {pajamu_suma} eur.")
        print("-----------------------------------------")
    if ivestis == "2":
        menuo = int(input("Iveskite menesi skaiciumi: "))
        islaidu_tipas = input("Iveskite islaidu tipa: ")
        islaidu_suma = int(input("Iveskite islaidu suma:"))
        islaidu_eilute = [menuo, islaidu_tipas, islaidu_suma]
        islaidos.append(islaidu_eilute)
        print(f"Per {menuo} men. jusu islaidos uz {islaidu_tipas} buvo {islaidu_suma} eur.")
        print("-----------------------------------------")
    if ivestis == "3":
        print(pajamos)
        print("-----------------------------------------")
    if ivestis == "4":
        print(islaidos)
        print("-----------------------------------------")


