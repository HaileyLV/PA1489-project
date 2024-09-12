# Inlämningsuppgift 1: Samarbete och Konfigurationshantering

## 1. Forma utvecklingsteam:
- Planera hur ni vill arbeta: Vi sitter tillsammans minst två gånger i veckan: tisdag (efter lektionen) och torsdag (efter labben)

# 2. Bestäm utvecklingsmiljö
- Vi använder VS code.

# 3. Bestäm vilken git-server ni vill använda
- Github
- Vi har alla våra egna konton på Github

# 4. Skapa projektet. Se till att ge det ett bra namn och beskriv det ordentligt.
- Hailey skapade ett projekt och delade till alla.

# 5. Vi behöver svara minst på dessa frågor för att hitta en bra design för vår produkt:
- Våra produkter tillåter eller inte funktioner nedan:
  + många användare åt gången (Kan flera kunder beställa samtidigt?)
  + ha användarbehörighetsfunktion (Till exempel är det bara köksanvändaren som kan kontrollera de hamburgare som kunderna väljer och markera hamburgarna som färdiga)
  + använda en relationsdatabases eller en NoSQL - database
- Vilka varutyper (menyer, hamburgare, tillbehör, dricka, osv.) som skall finnas? Vem tar ansavar får någon typ av vara?
  + Ebba och Hailey: Hamburgare och tillbehör
  + Wilma:dricka
  + Sabor: Burger Orderer
  + Thanh: Administratör

# 7. Språk:
- Python?

# 6. De här funktionerna måste våra produkter ha:
- En containerbaserad platform, med separata containers för BurgerOrderer, KitchenView, och MenuStore. 

**BurgerOrderer:** Det huvudsakliga webgränssnittet. Behöv inte göra det snyggt. Funktionalitet är viktigaste.
- Presenterar de olika varutyperna
- Kunden kan välja vad de vill ha med i sin beställning
- Kunden **kan anpassa sin beställning** (t.ex. ta bort “lök” från sin “Metric Ton Bacon Burger”)
- Hämtar information om de olika varutyperna från databasen MenuStore
- När beställningen är klar skickas den via ett REST-anrop till KitchenView

**MenuStore**: En databas som innehåller information om varje typ av vara.
- Information om de olika varutyperna och hur man kan anpassa dem kan skötas via ett separat gränssnitt såsom **adminer**

**KitchenView**: Tar emot beställningar från BurgerOrderer och visar dem för kökspersonalen.
- När en beställning är mottagen via ett REST-API skall den skrivas ut på skärmen.
- Behöv bara en enkel textbaserad utskrift.
