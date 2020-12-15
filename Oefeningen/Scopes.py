

class MijnClass : 

    varOpenbaar = "Dit is openbaar toegankelijk"
    __varPrive = "Deze is prive"

    Opvragen = 0

    #Mag er wel bij van binnenuit 
    def Voorbeeld (self):
        print(self.__varPrive)

    #Getter
    def getVarPrive(self):
        self.Opvragen += 1 
        return self.__varPrive

    def setVarPrive(self, value):
        self.__varPrive = value

instClass = MijnClass()
print( instClass.varOpenbaar)


#Mag er niet bij van buitenaf!
#print (instClass.__varPrive)

instClass.Voorbeeld()