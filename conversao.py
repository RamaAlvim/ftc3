import itertools

class AFD:

    def __init__(self, estados, simbolos, transicoes, comeco, fim):

        self.Q=estados
        self.sigma=simbolos
        self.delta=transicoes#EO -> ED:s
        self.q1=comeco
        self.F=fim

def conversao(afn):

    afd=AFD(estados, simbolos, transicoes, comeco, fim)
    afd.q1=afn.q1
    afd.Q=afn.q1
    for x in afn.Q:
        for a in afn.sigma:
            y={}
            for delta in afn.iter(a):
                y.push({(delta.x,delta.a)})
                if y not in afd.Q:
                    afn.Q.push(y)
                afn.delta.push({x,a,y})



estados = {}
simbolos= {}
transicoes= {}
comeco ={}
fim= {}

afn = AFD(estados, simbolos, transicoes, comeco, fim)


conversao(afn)