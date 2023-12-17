from pyfirmata import Arduino


def led_islemleri(deger):
    board=Arduino("COM3")
    board.get_pin("d:7:o")
    if(deger==1):
        board.digital[7].write(1)
        board.exit()
    elif(deger==0):
        board.digital[7].write(0)
        board.exit()

def ampul_islemleri(deger,pin_numarasi):
    board=Arduino("COM3")
    board.get_pin("d:8:o")
    board.get_pin("d:9:o")
    if(deger==1):
        board.digital[pin_numarasi].write(1)
        board.exit()
    elif(deger==0):
        board.digital[pin_numarasi].write(0)
        board.exit()

def klima_islemleri(deger,pin_numarasi):

    board=Arduino("COM4")
    board.get_pin("d:{}:o".format(pin_numarasi))

    if deger==1:
        board.digital[pin_numarasi].write(1)
        board.exit()

    elif deger==0:
        board.digital[pin_numarasi].write(0)
        board.exit()