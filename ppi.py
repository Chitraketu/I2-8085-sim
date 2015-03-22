class ports:
    def __init__(self):
            self.mode = "0"
            self.direction = "0"
            self.data = "00000000"
    def input(self,dataval):
            self.data = bin(int('0x'+dataval,0))[2:]
            if len(self.data)<8:
                temp='0'*(8-len(self.data))+self.data
                self.data=temp
            print self.data
    def output(self):
            return hex(int('0b'+self.data,2))[2:]
class PPI:
    def __init__(self):
        self.CW = "00000000"
        self.PORTA = ports()
        self.PORTB = ports()
        self.PORTC = ports()
        self.PORTC.datalow = self.PORTC.data[4:]
        self.PORTC.datahigh = self.PORTC.data[:4]
        self.PORTC.lowdirection = "0"
        self.PORTC.hihgdirection = "0"

    def setCW(self,cw):
        self.CW = bin(int('0x'+cw,0))[2:]
        print self.CW,len(self.CW)
        if(len(self.CW)<8):
                vari = '0'*(8 - len(self.CW))+self.CW
                self.CW = vari
        if(self.CW[0] == '0'):
                self.bsr()
        else:
                self.iomode()

    def showCW(self):
            print self.CW,"self.CW"
            print self.PORTA.mode,"mode"
            print self.PORTA.data,"data"
            print self.PORTC.mode

    def bsr(self):
            cbits = self.CW[4:]
            cpos = cbits[:-1]
            setc = cbits[-1:]
            cpos = int('0b'+cpos,2)
            cpos = 7 - cpos
            tempC = self.PORTC.data
            tempCC = tempC[:cpos]+setc+tempC[cpos+1:]
            self.PORTC.data = tempCC
            print self.PORTC.data,"portc"

    def iomode(self):
        if(self.CW[1]=='1'):
            self.PORTA.mode = '2'
        elif(self.CW[2]=='1'):
            self.PORTA.mode = '1'
        elif(self.CW[2]=='0'):
            self.PORTA.mode = '0'
        if(self.CW[3]=='0'):
            self.PORTA.direction = '0'
        else:
            self.PORTA.direction = '1'
             
        if self.CW[4]=='0':    
            self.PORTC.lowdirection = '0'
        else:
            self.PORTC.lowdirection = '1'
        if self.CW[7]=='0':    
            self.PORTC.highdirection = '0'
        else:
            self.PORTC.highdirection = '1'
        if(self.CW[6]=='0'):
            self.PORTB.direction = '0'
        else:
            self.PORTB.direction = '1'
        if(self.CW[5] == '0'):
            self.PORTB.mode ='0'
        else:
            self.PORTB.mode ='1'


             
    
