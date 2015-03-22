import ppi
class decoder:
    def __init__(self,opcode):
        self.dict = {'nop':'00',
				'lxi_b':'01',
				'stax_b':'02',
				'inx_b':'03',
				'inr_b':'04',
				'dcr_b':'05',
				'mvi_b':'06',
				'rlc':'07',
				'dad_b':'09',
				'ldax_b':'0a',
				'dcx_b':'0b',
				'inr_c':'0c',
				'dcr_c':'0d',
				'mvi_c':'0e',
				'rrc':'0f',
				'lxi_d':'11',
				'stax_d':'12',
				'inx_d':'13',
				'inr_d':'14',
				'dcr_d':'15',
				'mvi_d':'16',
				'ral':'17',
				'dad_d':'19',
				'ldax_d':'1a',
				'dcx_d':'1b',
				'inr_e':'1c',
				'dcr_e':'1d',
				'mvi_e':'1e',
				'rar':'1f',
				'rim':'20',
				'lxi_h':'21',
				'shld':'22',
				'inx_h':'23',
				'inr_h':'24',
				'dcr_h':'25',
				'mvi_h':'26',
				'daa':'27',
				'dad_h':'29',
				'lhld':'2a',
				'dcx_h':'2b',
				'inr_l':'2c',
				'dcr_l':'2d',
				'mvi_l':'2e',
				'cma':'2f',
				'sim':'30',
				'lxi_sp':'31',
				'sta':'32',
				'inx_sp':'33',
				'inr_m':'34',
				'dcr_m':'35',
				'mvi_m':'36',
				'stc':'37',
				'dad_sp':'39',
				'lda':'3a',
				'dcx_sp':'3b',
				'inr_a':'3c',
				'dcr_a':'3d',
				'mvi_a':'3e',
				'cmc':'3f',
				'mov_b_b':'40',
				'mov_b_c':'41',
				'mov_b_d':'42',
				'mov_b_e':'43',
                                'mov_b_h':'44',
                                'mov_b_l':'45',
                                'mov_b_m':'46',
                                'mov_b_a':'47',
                                'mov_c_b':'48',
                                'mov_c_c':'49',
                                'mov_c_d':'4a',
                                'mov_c_e':'4b',
                                'mov_c_h':'4c',
                                'mov_c_l':'4d',
                                'mov_c_m':'4e',
                                'mov_c_a':'4f',
                                'mov_d_b':'50',
                                'mov_d_c':'51',
                                'mov_d_d':'52',
                                'mov d_e':'53',
                                'mov_d_h':'54',
                                'mov_d_l':'55',
                                'mov_d_m':'56',
                                'mov_d_a':'57',
                                'mov_e_b':'58',
                                'mov_e_c':'59',
                                'mov_e_d':'5a',
                                'mov_e_e':'5b',
                                'mov_e_h':'5c',
                                'mov_e_l':'5d',
                                'mov_e_m':'5e',
                                'mov_e_a':'5f',
                                'mov_h_b':'60',
                                'mov_h_c':'61',
                                'mov_h_d':'62',
                                'mov_h_e':'63',
                                'mov_h_h':'64',
                                'mov_h_l':'65',
                                    
    'mov_l_b':'68',
    'mov_l_c':'69',
    'mov_l_d':'6a',
    'mov_l_e':'6b',
    'mov_l_h':'6c',
    'mov_l_l':'6d',
    'mov_l_m':'6e',
    'mov_l_a':'6f',

'mov_m_b':'70',
'mov_m_c':'71',
'mov_m_d':'72',
'mov_m_e':'73',
'mov_m_h':'74',
'mov_m_l':'75',
'hlt':'76',
'mov_m_a':'77',

'mov_a_b':'78',
'mov a_c':'79',
'mov a_d':'7a',
'mov_a_e':'7b',
'mov_a_h':'7c',
'mov_a_l':'7d',
'mov_a_m':'7e',
'mov_a_a':'7f',

'add_b':'80',
'add_c':'81',
'add_d':'82',
'add_e':'83',
'add_h':'84',
'add_l':'85',
'add_m':'86',
'add_a':'87',

'adc_b':'88',
'adc_c':'89',
'adc_d':'8a',
'adc_e':'8b',
'adc_h':'8c',
'adc_l':'8d',
'adc_m':'8e',
'adc_a':'8f',

'sub_b':'90',
'sub_c':'91',
'sub_d':'92',
'sub_e':'93',
'sub_h':'94',
'sub_l':'95',
'sub_m':'96',
'sub_a':'97',

'sbb_b':'98',
'sbb_c':'99',
'sbb_d':'9a',
'sbb_e':'9b',
'sbb_h':'9c',
'sbb_l':'9d',
'sbb_m':'9e',
'sbb_a':'9f',

'ana_b':'a0',
'ana_c':'a1',
'ana_d':'a2',
'ana_e':'a3',
'ana_h':'a4',
'ana_l':'a5',
'ana_m':'a6',
'ana_a':'a7',

'xra_b':'a8',
'xra_c':'a9',
'xra_d':'aa',
'xra_e':'ab',
'xra_h':'ac',
'xra_l':'ad',
'xra_m':'ae',
'xra_a':'af',

'ora_b':'b0',
'ora_c':'b1',
'ora_d':'b2',
'ora_e':'b3',
'ora_h':'b4',
'ora_l':'b5',
'ora_m':'b6',
'ora_a':'b7',

'cmp_b':'b8',
'cmp_c':'b9',
'cmp_d':'ba',
'cmp_e':'bb',
'cmp_h':'bc',
'cmp_l':'bd',
'cmp_m':'be',
'cmp_a':'bf',

'rnz':'c0',
'pop_b':'c1',
'jnz':'c2',
'jmp':'c3',
'cnz':'c4',
'push_b':'c5',
'adi':'c6',
'rst_0':'c7',
'rz':'c8',
'ret':'c9',
'jz':'ca',
'cz':'cc',
'call':'cd',
'aci':'ce',
'rst_1':'cf',
'rnc':'d0',
'pop_d':'d1',
'jnc':'d2',
'out':'d3',
'cnc':'d4',
'push_d':'d5',
'sui':'d6',
'rst_2':'d7',
'rc':'d8',
'jc':'da',
'ini':'db',
'cc':'dc',
'sbi':'de',
'rst_3':'df',
'rpo':'e0',
'pop_h':'e1',
'jpo':'e2',
'xthl':'e3',
'cpo':'e4',
'push_h':'e5',
'ani':'e6',
'rst_4':'e7',
'rpe':'e8',
'pchl':'e9',
'jpe':'ea',
'xchg':'eb',
'cpe':'ec',
'xri':'ee',
'rst_5':'ef',
'rp':'f0',
'pop_psw':'f1',
'jp':'f2',
'di':'f3',
'cp':'f4',
'push_psw':'f5',
'ori':'f6',
'rst_6':'f7',
'rm':'f8',
'sphl':'f9',
'jm':'fa',
'ei':'fb',
'cm':'fc',
'cpi':'fe',
'rst_7':'ff'
            
				}

        self.opc = opcode
        self.list = self.opc.keys()
        self.listfunc = self.dict.keys()
        self.listop = self.dict.values()
        self.list.sort()
        self.PC = self.list[0]
        self.PC = hex(int(self.PC))

        #registers
        self.SP='0xff00'
        self.A = ""
        self.B = ""
        self.C = ""
        self.D = ""
        self.E = ""
        self.H = ""
        self.L = ""
        self.M = ""
        self.FLAG = "00000000"

        #PPI
        self.ppi = ppi.PPI()

        #interrupt flag
        self.INTFLAG = '0'

        #interrupt services
        self.int7_5 = '0x8fbf'
        self.int6_5 = '0x8fb9'
        self.int5_5 = '0x8fb3'
        self.intVector = ''
        self.intFlipFlop = '0'

    def show(self):
        print self.A,self.B,self.C
        for i in self.list:
            print hex(int(i)),self.opc[i]
    def decode(self):
       # print type(self.mov_a_a)

        while self.opc[str(int(self.PC,0))] != '76':
            getattr(self,self.listfunc[self.listop.index(self.opc[str(int(self.PC,0))])])()
            print self.opc[str(int(self.PC,0))] 

    #data transfer
    #mov a,x functions
    def mov_a_a(self):
        print "hello chitra"
        self.A = self.A
        
        self.PC = int(self.PC,0)
        self.PC += 1
        self.PC = hex(self.PC)


    def mvi_a(self):
        print "mane"
        self.PC = int(self.PC,0)
        self.PC += 1
        self.PC = hex(self.PC)
        self.A = self.opc[str(int(self.PC,0))]
        self.PC = int(self.PC,0)
        self.PC += 1
        self.PC = hex(self.PC)

    def lxi_b(self):
        self.PC = int(self.PC,0)
        self.PC += 1
        self.PC = hex(self.PC)
        self.B = self.opc[str(int(self.PC,0))]
        self.PC = int(self.PC,0)
        self.PC += 1
        self.PC = hex(self.PC)
        self.C = self.opc[str(int(self.PC,0))]
        self.PC = int(self.PC,0)
        self.PC += 1
        self.PC = hex(self.PC)

    def add_b(self):
        sum=hex(int('0x'+self.A,0)+int('0x'+self.B,0))[2:]
        print sum,"sum"
        if(len(sum)>2):
            self.A=sum[-2:]
            if bin(int('0x'+self.A,0)).count('1') % 2 == 0:
                self.setParity()
            else:
                self.setParity(False)
            self.setCarry()
            
        else:
            self.A=sum
            if bin(int('0x'+self.A,0)).count('1') % 2 == 0:
                self.setParity()
            else:
                self.setParity(False)
            self.setCarry(False)
        print self.FLAG,'flag',self.A
        self.incPC()

    def incPC(self,i = 1):
            for x in range(0,i):
                    self.PC = int(self.PC,0)
                    self.PC += 1
                    self.PC = hex(self.PC)

    def rlc(self):
        temp = bin(int('0x'+self.A,0))  
        if(len(temp)<10):
            temp2 = temp[:2] + '0'*(10 -len(temp)) + temp[2:]
            temp = temp2
        binfirst = temp[2:3]
        if(binfirst == '1'):
              self.setCarry()
        else:
              self.setCarry(False)
        binpart = temp[3:]
        binrotate = '0b'+binpart + binfirst
        self.A = hex(int(binrotate,2))[2:] 
        print temp,binrotate,"rotated",self.A,self.FLAG
        self.incPC()

    def jmp(self):
        self.incPC()
        low = self.opc[str(int(self.PC,0))]
        self.incPC()
        high = self.opc[str(int(self.PC,0))]
        add = '0x'+high+low
        self.PC=add

    def jnz(self):
        if(self.FLAG[1] != '1'):
            self.jmp()
        else:
            self.incPC(3)

    def ldax_b(self):
        low = self.B
        high = self.C
        addr = '0x'+high+low
        self.A = self.loadFromMemory(addr)
        self.incPC()
    def stax_b(self):
        low = self.B
        high = self.C
        addr = '0x'+high + low
        self.saveToMemory(addr,self.A)
        self.incPC()
    def push_b(self):
        self.saveToMemory(self.SP,self.C)
        self.SP = int(self.SP,0)-1
        self.SP = hex(self.SP)
        self.saveToMemory(self.SP,self.B)
        self.SP = int(self.SP,0)-1
        self.SP = hex(self.SP)
        self.incPC()

    def pop_b(self):
        self.SP = int(self.SP,0)+1
        self.SP = hex(self.SP)
        if(self.opc.has_key(str(int(self.SP,0)))):
               self.B = self.opc.pop(str(int(self.SP,0))) 
        self.SP = int(self.SP,0)+1
        self.SP = hex(self.SP)
        if(self.opc.has_key(str(int(self.SP,0)))):
               self.C = self.opc.pop(str(int(self.SP,0))) 
        self.incPC()
    def push_psw(self):
        flag='0b'+self.FLAG
        flag=hex(int(flag,2))[2:]
        print flag,"rock psw",self.FLAG
        self.saveToMemory(self.SP,self.A)
        self.SP = int(self.SP,0)-1
        self.SP = hex(self.SP)
        self.saveToMemory(self.SP,flag)
        self.SP = int(self.SP,0)-1
        self.SP = hex(self.SP)
        self.incPC()
    def pop_psw(self):
        self.SP = int(self.SP,0)+1
        self.SP = hex(self.SP)
        if(self.opc.has_key(str(int(self.SP,0)))):
               flag= self.opc.pop(str(int(self.SP,0))) 
        self.SP = int(self.SP,0)+1
        self.SP = hex(self.SP)
        if(self.opc.has_key(str(int(self.SP,0)))):
               self.A = self.opc.pop(str(int(self.SP,0))) 
        flag = bin(int('0x'+flag,0))[2:]
        if(len(flag)<8):
            flag = '0'*(8 - len(flag)) + flag
        self.FLAG = flag
        print self.FLAG,'refined flag'         
        self.incPC()

#for interrupt handling
    def sim(self):
        vari = bin(int('0x'+self.A,0))[2:]
        if(len(vari)<8):
            varii = '0'*(8 - len(vari)) + vari
            vari = varii
        vari = vari[4:]
        if(vari[0] == '1'):
            if(vari[1] == '0'):
                self.intVector = self.int7_5
            elif(vari[2] == '0'):
                self.intVector = self.int6_5
            elif(vari[3] == '0'):
                self.intVector = self.int5_5
            else:
                print "none"
        self.incPC()
    def ei(self):
        self.intFlipFlop = '1'
        self.incPC()

    def di(self):
        self.intFlipFlop = '0'
        self.incPC()

#for the 8255 PPI
    def out(self):
        self.incPC()
        print "hello"
        control = self.opc[str(int(self.PC,0))]
        if control == '40':
                self.out_40()
        elif control == '41':
                self.out_41()
        elif control =='42':
                self.out_42()
        elif control == '43':
                self.out_43()
        else:
                print "there was an error"
        self.incPC()

    def out_40(self):
        if(self.ppi.PORTA.direction=='1'):
            self.ppi.PORTA.input(self.A)
        else:
            print("illigal out")
        self.ppi.showCW()
        print "out_40"

    def out_41(self):
        if(self.ppi.PORTA.mode !='2'):
            if(self.ppi.PORTB.direction=='1'):
                self.ppi.PORTB.input(self.A)
            else:
                print("illigal out")
        else:
             print "illegal out port a is in mode 2"
        print "out_42"

    def out_42(self):
        if(self.ppi.PORTA.mode == '0'):
            if(self.ppi.PORTA.direction=='1'):
                self.ppi.PORTA.input(self.A)
            else:
                print("illigal out")
        else:
            print "illegal out for porta in mode 1 or 2"
        print "out_43"

    def out_43(self):
        self.ppi.setCW(self.A)
        self.ppi.showCW()
        print "out_43"        

    def ini(self):
        self.incPC()
        control = self.opc[str(int(self.PC,0))]
        if control == '40':
                self.in_40()
        elif control == '41':
                self.in_41()
        elif control =='42':
                self.in_42()
        elif control == '43':
                self.in_43()
        else:
                print "there was an error"
        self.incPC()

    def in_40(self):
        if(self.ppi.PORTA.direction=='0'):
            self.A=self.ppi.PORTA.output()
        else:
            print("illigal in")
        self.ppi.showCW()
        print "in_40"
        print self.A,"23 aaunu paro"

    def in_41(self):
        if(self.ppi.PORTA.mode !='2'):
            if(self.ppi.PORTB.direction=='0'):
                self.A=self.ppi.PORTB.output()
            else:
                print("illigal in")
        else:
             print "illegal out port a is in mode 2"
        print "out_42"

    def in_42(self):
        if(self.ppi.PORTA.mode == '0'):
            if(self.ppi.PORTA.direction=='0'):
                self.A=self.ppi.PORTC.output()
            else:
                print("illigal in")
        else:
             print "illegal out for porta in mode 1 or 2"
        print "out_43"

    def in_43(self):
        print "in_43 is illigal"        



#memory related operation
#always takes the addr in '0xXXXX' format        
    def saveToMemory(self,addr,value):
        addr = str(int(addr,0))
        if(self.opc.has_key(addr)):
                print "cannot allocate"
        else:
             self.opc[addr] = value
             print self.opc[addr],"to memory"

    def loadFromMemory(self,addr):
        if(self.opc.has_key(str(int(addr,0)))):
             print self.opc[str(int(addr,0))],"from memory"
             return self.opc[str(int(addr,0))]


# set or reset FLAGS
    def setParity(self,set = True):
        if set:
            temp = self.FLAG[:-3]+'1'+self.FLAG[-2:]
        else:
            temp = self.FLAG[:-3] + '0' + self.FLAG[-2:]
        self.FLAG = temp

    def setCarry(self,set = True):
        if set:
            temp = self.FLAG[:-1]+'1'
        else:
            temp = self.FLAG[:-1] + '0' 
        self.FLAG = temp

    def setAC(self,set = True):
        if set:
            temp = self.FLAG[:3]+'1'+self.FLAG[4:]
        else:
            temp = self.FLAG[:3] + '0' + self.FLAG[4:]
        self.FLAG = temp

    def setZero(self,set = True):
        if set:
            temp = self.FLAG[:1]+'1'+self.FLAG[2:]
        else:
            temp = self.FLAG[:1] + '0' + self.FLAG[2:]
        self.FLAG = temp

    def setSign(self,set = True):
        if set:
            temp = '1'+self.FLAG[1:]
        else:
            temp = '0'+self.FLAG[1:]
        self.FLAG = temp

    
# d7 d6 d5 d4 d3 d2 d1 d0
# S  Z  XX AC XX P  XX CY          



