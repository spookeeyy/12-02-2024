def failistSõnejärjendisse(fail):
    järjend = []
    for rida in fail:
        järjend += [rida.strip()]
        # järjed.append(rida.strip())
        fail.close()
        return järjend
    
failinimi = input("Sisestage failinimi"   ) + " txt"
fail = open(failinimi, encoding="UTF-8")
sõned = failistSõnejärjendisse(fail)
print(sõned)
print(sõned[3])