import math
import cmath

#def je_prast(n):
#    if n == 1:
#        return = "Ni praštevilo."
#    if n == 2:
#        return "Je praštevilo."
#    elif n % 2 == 0:
#        return "Ni praštevilo."
#    else:
#        d = 3
#        while d ** 2 <= n:
#            if n % d == 0:
#                return "Ni praštevilo."
#            d += 2
#        return "Je praštevilo."

def najdi_delitelje(n):
    seznam = []
    for x in range(1, n + 1):
        if n % x == 0:
            seznam.append(x)
    return seznam

def je_prast(n):
    delitelji = najdi_delitelje(n)
    return len(delitelji) == 2

def gcd(m, n):
    #največji supni delitelj
    while n != 0:
        (m, n) = (n, m % n)
    return int(m)

def lcm(a, b):
    #najmanjši skupni večkratnik
    return int(a * b / gcd(a, b))

def prast_razcep(n):
    seznam = [] #v seznamu bomo imeli pare (prastevilo, potenca)
    delitelji = najdi_delitelje(n)
    prastevila = [x for x in delitelji if je_prast(x) == True]
    for stevilo in prastevila:
        i = 0
        while n % stevilo == 0:
            i += 1
            n = n // stevilo
        seznam.append((stevilo, i))
    if seznam == []:
        return [(n, 1)]
    else:
        return seznam

def naredi_produkt(seznam):
    razcep = ''
    for (osnova, potenca) in seznam:
        razcep += '{}^{}'.format(osnova, potenca) + ' * '
    return razcep[:-3]


RIMSKA_STEVILA = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def po_rimljansko(n):
    rimljansko = ''
    while n > 0:
        for i, r in RIMSKA_STEVILA:
            while n >= i:
                rimljansko += r
                n -= i
    return rimljansko

def je_trikotno(n):
    for x in range(1, n):
        if x * (x + 1) == 2 * n:
            return (True, x)
    return (False, None)

def mersennova_prastevila(n): #uporaba Lucas-Lehmerjevega algoritma
    if n == 1:
        return "Ni Mersennovo praštevilo."
    if n == 2:
        return "Je Mersennovo praštevilo."
    else:
        s = 4
        m = 2**n - 1 #tako število bo zagotovo Marsennovo
        i = 0
        while i <= n - 2:
            o = s % m
            s = o**2 - 2
            i = i + 1
        if o == 0:
            return "Je Mersennovo praštevilo."
        else:
            return "Ni Mersennovo praštevilo."

################################

class Stevilo:
    def __init__(self, n):
        self.stevilo = n
    
    
    ### ZA VSE ###

    def vrsta(self):
        tip =  str(type(self.stevilo))[8:-2]
        if tip == 'int':
            return 'To je celo število.'
        elif tip == 'float':
            return 'To je decimalno število.'
        elif tip == 'complex':
            return 'To je kompleksno število.'
        else:
            return 'Tega števila ne prepoznam. Preveri, ali si uporabil piko kot ločilo. Preveri, ali si vpisal število. Imaginarno število je v Pythonu označeno z "j".'        
    
    def absolutna_vrednost(self):
        return 'Absolutna vrednost števila je: {}'.format(abs(self.stevilo))

    def zanimivosti(self):
        n = self.stevilo
        if n == 18:
            return 'Oseba z osemnajstimi leti je polnoletna v Sloveniji.'
        if str(n) in str(math.pi):
            return 'Ej, a veš da je tako zaporedje v iracionalnem številu pi!!'
        if n == 45:
            return 'To število je uporabljeno v opisu projektne naloge.' 
        else:
            pass
    
    ##Vse razen kompleksna: 

    def pozitivnost(self):
        if self.vrsta() != 'To je kompleksno število.':
            if self.stevilo < 0:
                return "To je negativno število."
            elif self.stevilo == 0:
                return "To je nič. Ni ne pozitivno, ne negativno."
            else:
                return "To je pozitivno število."
    
    ### CELA ŠTEVILA ### 

    def sodost(self):
        if self.vrsta == 'To je celo število.':
            if self.stevilo % 2 == 0:
                return 'To je sodo število.'
            else:
                return 'To je liho število'  
        
    def predhodnik_naslednik(self):
        if self.vrsta() == 'To je celo število.':
            return 'Predhodnik števila je {}, naslednik pa {}.'.format(self.stevilo - 1, self.stevilo + 1)

    def je_prastevilo(self):
        if self.vrsta() == 'To je celo število.' and self.pozitivnost() == True:
            if je_prast(self.stevilo) == True:
                return 'Je praštevilo.'
            else:
                return 'Ni praštevilo.'


    def delitelji(self):
        if self.vrsta() == 'To je celo število.':
            delitelji = najdi_delitelje(self.stevilo)
            return 'Seznam deliteljev: {}'.format(delitelji)
    
    def prastevilski_razcep(self):
        if self.vrsta() == 'To je celo število.':
            seznam = prast_razcep(self.stevilo)
            return 'Praštevilski razcep števila: {}'.format(naredi_produkt(seznam))
    
    def mersennova_prastevila(self):
         if self.vrsta == 'To je celo število.':
            a = mersennova_prastevila(self.stevilo) 
            return a

    def binarni_zapis(self):
        if self.vrsta() == 'To je celo število.':
            b = bin(self.stevilo)
            return 'To je binarni zapis: {}'.format(b)
    
    def rimski_zapis(self):
        if self.vrsta() == 'To je celo število.':
            r = po_rimljansko(self.stevilo)
            return 'To je rimski zapis: {}'. format(r)

    def je_kvadratno_stevilo(self):
        if self.vrsta() == 'To je celo število.':
            razcep = prast_razcep(self.stevilo)
            for (osnova, potenca) in razcep:
                if potenca % 2 != 0:
                    return 'Ne obstaja celo število, ki bi ga kvadrirali, da dobimo {}.'.format(self.stevilo)
            return 'Je kvadratno število.'
    
    def je_kvadrat_od(self):
        if self.je_kvadratno_stevilo() == 'Je kvadratno število.':
            return 'Če števili {0} in -{0} kvadriramo, dobimo {1}'.format(int(math.sqrt(self.stevilo)), self.stevilo)        
    
    def je_trikotno_stevilo(self):
        if self.vrsta == 'To je celo število.':
            pravilnost, dolzina_stranice = je_trikotno(self.stevilo)
            if pravilnost == True:
                return 'Je trikotno število. Stranica trikotnika je dolga {}.'.format(dolzina_stranice)
            else:
                return 'Ni trikotno število.'
        
    
    ### DECIMALNA ŠTEVILA ###

    def celi_decimalni_del(self):
        if self.vrsta() == 'To je decimalno število.':
            vse_stevke = len(str(self.stevilo))
            celi_del = int(self.stevilo)
            cele_stevke = len(str(celi_del))
            decimalni_del = round(self.stevilo - celi_del, vse_stevke - cele_stevke)
            return [celi_del, decimalni_del]

    # def zaokrozi(self, k=1):
    #     # k = na katero deicmalno mesto želimo zaokrožiti
    #     if self.vrsta() == 'To je decimalno število.':
    #         a = round(self.stevilo, k)
    #         return a
    
    def ulomek(self):
        if self.vrsta() == 'To je decimalno število.':
            dec_del = self.celi_decimalni_del()[1]
            b = len(str(dec_del)[2:])#ker je je vejica in 0 na začetku
            im = 10**b
            st = int(self.stevilo * im)
            delitelj = gcd(st, im)
            stevec = int(st / delitelj)
            imenovalec = int(im / delitelj)
            return '{}/{}'.format(stevec, imenovalec)

    ### KOMPLEKSNA ŠTEVILA ### 
    
    def konjugiraj(self):
        if self.vrsta() == 'To je kompleksno število.':
            return self.stevilo.conjugate()
    
    def kompleksni_imaginarni_del(self):
        return 'Realni del je {}, imaginarni pa {}.'.format(self.stevilo.real, self.stevilo.imag)
    
    def cisto_stevilo(self):
        if self.vrsta() == 'To je kompleksno število.':
            konjugirano = self.stevilo.conjugate()
            if self.stevilo == - konjugirano:
                return 'To je pravo imaginarno število.'
            
