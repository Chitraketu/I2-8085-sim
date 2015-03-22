import decoder
class parser:
	def __init__ (self,nm):
		#file read
		#self.name=nm
		self.__dict__ = {'nop':'00',
				'lxi b':'01',
				'stax b':'02',
				'inx b':'03',
				'inr b':'04',
				'dcr b':'05',
				'mvi b':'06',
				'rlc':'07',
				'dad b':'09',
				'ldax b':'0a',
				'dcx b':'0b',
				'inr c':'0c',
				'dcr c':'0d',
				'mvi c':'0e',
				'rrc':'0f',
				'lxi d':'11',
				'stax d':'12',
				'inx d':'13',
				'inr d':'14',
				'dcr d':'15',
				'mvi d':'16',
				'ral':'17',
				'dad d':'19',
				'ldax d':'1a',
				'dcx d':'1b',
				'inr e':'1c',
				'dcr e':'1d',
				'mvi e':'1e',
				'rar':'1f',
				'rim':'20',
				'lxi h':'21',
				'shld':'22',
				'inx h':'23',
				'inr h':'24',
				'dcr h':'25',
				'mvi h':'26',
				'daa':'27',
				'dad h':'29',
				'lhld':'2a',
				'dcx h':'2b',
				'inr l':'2c',
				'dcr l':'2d',
				'mvi l':'2e',
				'cma':'2f',
				'sim':'30',
				'lxi sp':'31',
				'sta':'32',
				'inx sp':'33',
				'inr m':'34',
				'dcr m':'35',
				'mvi m':'36',
				'stc':'37',
				'dad sp':'39',
				'lda':'3a',
				'dcx sp':'3b',
				'inr a':'3c',
				'dcr a':'3d',
				'mvi a':'3e',
				'cmc':'3f',
				'mov b,b':'40',
				'mov b,c':'41',
				'mov b,d':'42',
				'mov b,e':'43',
                                'mov b,h':'44',
                                'mov b,l':'45',
                                'mov b,m':'46',
                                'mov b,a':'47',
                                'mov c,b':'48',
                                'mov c,c':'49',
                                'mov c,d':'4a',
                                'mov c,e':'4b',
                                'mov c,h':'4c',
                                'mov c,l':'4d',
                                'mov c,m':'4e',
                                'mov c,a':'4f',
                                'mov d,b':'50',
                                'mov d,c':'51',
                                'mov d,d':'52',
                                'mov d,e':'53',
                                'mov d,h':'54',
                                'mov d,l':'55',
                                'mov d,m':'56',
                                'mov d,a':'57',
                                'mov e,b':'58',
                                'mov e,c':'59',
                                'mov e,d':'5a',
                                'mov e,e':'5b',
                                'mov e,h':'5c',
                                'mov e,l':'5d',
                                'mov e,m':'5e',
                                'mov e,a':'5f',
                                'mov h,b':'60',
                                'mov h,c':'61',
                                'mov h,d':'62',
                                'mov h,e':'63',
                                'mov h,h':'64',
                                'mov h,l':'65',
                                    
    'mov l,b':'68',
    'mov l,c':'69',
    'mov l,d':'6a',
    'mov l,e':'6b',
    'mov l,h':'6c',
    'mov l,l':'6d',
    'mov l,m':'6e',
    'mov l,a':'6f',

'mov m,b':'70',
'mov m,c':'71',
'mov m,d':'72',
'mov m,e':'73',
'mov m,h':'74',
'mov m,l':'75',
'hlt':'76',
'mov m,a':'77',

'mov a,b':'78',
'mov a,c':'79',
'mov a,d':'7a',
'mov a,e':'7b',
'mov a,h':'7c',
'mov a,l':'7d',
'mov a,m':'7e',
'mov a,a':'7f',

'add b':'80',
'add c':'81',
'add d':'82',
'add e':'83',
'add h':'84',
'add l':'85',
'add m':'86',
'add a':'87',

'adc b':'88',
'adc c':'89',
'adc d':'8a',
'adc e':'8b',
'adc h':'8c',
'adc l':'8d',
'adc m':'8e',
'adc a':'8f',

'sub b':'90',
'sub c':'91',
'sub d':'92',
'sub e':'93',
'sub h':'94',
'sub l':'95',
'sub m':'96',
'sub a':'97',

'sbb b':'98',
'sbb c':'99',
'sbb d':'9a',
'sbb e':'9b',
'sbb h':'9c',
'sbb l':'9d',
'sbb m':'9e',
'sbb a':'9f',

'ana b':'a0',
'ana c':'a1',
'ana d':'a2',
'ana e':'a3',
'ana h':'a4',
'ana l':'a5',
'ana m':'a6',
'ana a':'a7',

'xra b':'a8',
'xra c':'a9',
'xra d':'aa',
'xra e':'ab',
'xra h':'ac',
'xra l':'ad',
'xra m':'ae',
'xra a':'af',

'ora b':'b0',
'ora c':'b1',
'ora d':'b2',
'ora e':'b3',
'ora h':'b4',
'ora l':'b5',
'ora m':'b6',
'ora a':'b7',

'cmp b':'b8',
'cmp c':'b9',
'cmp d':'ba',
'cmp e':'bb',
'cmp h':'bc',
'cmp l':'bd',
'cmp m':'be',
'cmp a':'bf',

'rnz':'c0',
'pop b':'c1',
'jnz':'c2',
'jmp':'c3',
'cnz':'c4',
'push b':'c5',
'adi':'c6',
'rst 0':'c7',
'rz':'c8',
'ret':'c9',
'jz':'ca',
'cz':'cc',
'call':'cd',
'aci':'ce',
'rst 1':'cf',
'rnc':'d0',
'pop d':'d1',
'jnc':'d2',
'out':'d3',
'cnc':'d4',
'push d':'d5',
'sui':'d6',
'rst 2':'d7',
'rc':'d8',
'jc':'da',
'in':'db',
'cc':'dc',
'sbi':'de',
'rst 3':'df',
'rpo':'e0',
'pop h':'e1',
'jpo':'e2',
'xthl':'e3',
'cpo':'e4',
'push h':'e5',
'ani':'e6',
'rst 4':'e7',
'rpe':'e8',
'pchl':'e9',
'jpe':'ea',
'xchg':'eb',
'cpe':'ec',
'xri':'ee',
'rst 5':'ef',
'rp':'f0',
'pop psw':'f1',
'jp':'f2',
'di':'f3',
'cp':'f4',
'push psw':'f5',
'ori':'f6',
'rst 6':'f7',
'rm':'f8',
'sphl':'f9',
'jm':'fa',
'ei':'fb',
'cm':'fc',
'cpi':'fe',
'rst 7':'ff'
            
				}
                self.index = 0x8000
                self.dick = dict()
                self.postlabel = dict()
                self.label = dict()
		self.file = open(nm,'r')
	def read(self):
		self.a = self.file.read().split('\n')
		self.file.close()
	def showcode(self):
		#print self.__dict__[self.a[4]]
		print self.a
        def parsecode(self):
            self.index = 0x8000
            #print self.arr[0]
            #parsing begins here
            for line in self.a:
                line = " ".join(line.split())
                print line
                #first check for the ':' for the label
                if(line.find(':')!= -1):
                    sal = line.split(':')
                    print hex(self.index)
                    self.label[sal[0]] = str(self.index)
                    line = sal[1]
                #first check whether there is any space in the line or not
                line = " ".join(line.split())
                if line.find(' ')<0 or line.find(' ')>len(line):
                    #if there is no space then check in the dictionary for the key
                    if(self.__dict__.has_key(line)):
                        print self.__dict__[line]
                        self.dick[str(self.index)] = self.__dict__[line]
                else:
                    #else split the line into the two words and check for the 'h' in the second word
                    #if there is not any h in the second word then search for the entire line in the dictionary
                    #split the line in two if there is any ',' in between
                    if(line.find(',')!= -1):
                        strs = line.split(',')
                        if(self.__dict__.has_key(line)):
                                print self.__dict__[line]
                                self.dick[str(self.index)] = self.__dict__[line]
                        else:
                            if(strs[1].find('h')<0 or strs[1].find('h')>len(strs[1])):
                                #if there is 'h' in the second word it must be the value but not the opcode 
                                if(self.__dict__.has_key(line)):
                                    print self.__dict__[line]
                                    self.dick[str(self.index)] = self.__dict__[line]
                            else:
                                if(self.__dict__.has_key(strs[0])):
                                    self.opcode = self.__dict__[strs[0]]
                                    print self.__dict__[strs[0]]
                                    self.dick[str(self.index)] = self.__dict__[strs[0]]
                                    
                            if(len(strs[1]) >= 4):
                                if(strs[1].find('h') != -1):
                                    vals = strs[1].split('h');
                                    self.index += 1
                                    self.dick[str(self.index)] = vals[0][2:]
                                    print vals[0][2:]
                                    self.index += 1
                                    self.dick[str(self.index)] = vals[0][:2]
                                    print vals[0][:2]
                       	    else: 
				    self.index += 1
				    print strs[1][:2],"bi"
				    self.dick[str(self.index)] = strs[1][:2]

                    else:
                        #if there is no ',' in between even then there can exist any value for example out 40h
                        #so again split it with ' ' and check for the 'h' in the second word
                        strs = line.split(' ');
                        if(self.label.has_key(strs[1])):
                            if self.__dict__.has_key(strs[0]):
                                print self.__dict__[strs[0]]
                                self.dick[str(self.index)] = self.__dict__[strs[0]]
                                vals = hex(int(self.label[strs[1]]))[2:]
                                print vals[2:],"vals"
                                self.index += 1
                                self.dick[str(self.index)] = vals[2:]
                                print vals[:2],"vsals"
                                self.index += 1
                                self.dick[str(self.index)] = vals[:2]
                        elif(strs[1].find('h') !=-1):
                                if(self.__dict__.has_key(strs[0])):
                                        print self.__dict__[strs[0]]
                                        self.dick[str(self.index)] = self.__dict__[strs[0]]
                                if(len(strs[1]) >= 4):
                                    if(strs[1].find('h') != -1):
                                        vals = strs[1].split('h');
                                        self.index += 1
                                        self.dick[str(self.index)] = vals[0][2:]
                                        print vals[0][2:]
                                        self.index += 1
                                        self.dick[str(self.index)] = vals[0][:2]
                                        print vals[0][:2]
                                else:
                                    self.index += 1
                                    self.dick[str(self.index)] = strs[1][:2]
                                    print strs[1][:2]
                        else:
                                if(self.__dict__.has_key(line)):
                                    self.dick[str(self.index)] = self.__dict__[line]
                                    print self.__dict__[line]
                                elif self.__dict__.has_key(strs[0]):
                                         self.dick[str(self.index)] = self.__dict__[strs[0]]
                                         self.index += 1
                                         self.postlabel[strs[0]] = self.index
                                         self.dick[str(self.index)] = '00'
                                         self.index += 1
                                         self.dick[str(self.index)] = '00'
                self.index = self.index + 1                                         
        def show(self):
            i = 0x8000
            self.parsecode()
            list = self.dick.keys()
            list.sort()
            listvalues = self.dick.values()
            for i in list:
                vari = int(i)
                print hex(vari),self.dick[i]

p = parser("file")
p.read()
p.showcode()
p.parsecode()
p.show()
d = decoder.decoder(p.dick)
d.decode()
d.show()
