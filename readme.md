## MetroMoneyLovesMe
Cracking metro money

### Requirments 
- Arduino (preferably Uno), 
- RFID-RC522, some cables
- MetroMoney card

### Running

Assemble the arduino and the sensor using the datasheet of rfid-rc522 (Put reset on pin 7 and SS on 5), get the serial output and paste it into some sort of txt file. Run hexdump.py. You can continue to process the data using [mfread](https://github.com/zhovner/mfdread)
