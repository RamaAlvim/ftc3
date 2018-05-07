





class AFD:

    def __init__(self, estados, simbolos, transicoes, comeco, fim):

        self.Q=estados
        self.sigma=simbolos
        self.delta=transicoes#EO -> ED:s
        self.q1=comeco
        self.F=fim




estados = {}
simbolos= {}
transicoes= {}
comeco ={}
fim= {}

#le cada AF nesse ponto



#prox linha salva o AF
D=AFD(estados, simbolos, transicoes, comeco, fim)




def executarAFD(self,str):

    estadoatual=self.q1

    for i in str:
        estadoatual=self.delta[(estadoatual,i)]

        if estadoatual in self.F:
            aceita=True

        else:
            aceita=False

    return aceita



str="12121"

print("{0} FOI ACEITA EM D: {1}" .format(str, executarAFD(str)))







