Temperaturmätning med Raspberry Pi Pico och DS18B20

För att använda koden så måste du utföra följande steg:

1. En Raspberry Pi Pico
2. En DS18B20-temperatursensor

Detta projektet går ut på att skapa ett program som läser av en temperatursensor (DS18B20) och skriver ut mätvärden i terminalen i formatet <unit id> <sensor id> <measurement>. Exempel på hur utskriften kan se ut är: e6614103e71d8d2e 28d6445c090000da 23.75. Programmet ska även ha förmågan att upptäcka hur många temperatursensorer som är anslutna. Det ska även finnas en konfigurationsfil, config.json, som specificerar vilken pinne vi ska använda för anslutningen och hur långt intervallet ska vara mellan varje mätning.

Installation:
För att köra koden på din Raspberry Pi Pico, så måste du utföra följande steg:

1. Ladda ner MicroPython till din Raspberry Pi Pico.
2. Håll in BOOTSEL-knappen på Picon samtidigt som du ansluter den till datorn.
3. Ladda ner MicroPython och överför den till Picon.

Kör koden med Thonny
För att köra  koden på din Raspberry Pi Pico, utför följande steg:

1. Anslut din Raspberry Pi Pico till din datorn via USB.
2. Använd Thonny eller liknande verktyg för att ladda upp och köra koden på din Raspberry Pi Pico.

Nu är Raspberry Pi Pico redo att användas för temperaturmätning med DS18B20-temperatursensorn. Utskrifterna kommer att visas i terminalen med hjälp av den angivna konfigurationsfilen.
