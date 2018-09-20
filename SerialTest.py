import serial

ser = serial.Serial("/dev/cu.SLAB_USBtoUART")

ser.open()

values = [0, 255]

while True:
    #var = chr(userIn)

    shouldWrite = int(ser.read())
    print(ser.name)
    if shouldWrite == 82:
        
        for i in range(0, 5):
            ser.write(str(values[0]).encode('utf-8'))
            ser.write(str(values[1]).encode('utf-8'))
ser.close()
