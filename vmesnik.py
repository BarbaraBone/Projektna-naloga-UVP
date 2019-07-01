import bottle
from model import *

@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.html')

@bottle.post('/informacije/')
def informacije():
    b = eval(bottle.request.forms['stevilo'])
    info_o = Stevilo(b)
    # if type(b) == str:
    #     return bottle.template('problem.html')
    return bottle.template('osnovne_informacije.html',izbira=info_o)
    
@bottle.get('/razlaga/')
def razlaga():
    return bottle.template('razlaga.html')

bottle.run(debug=True, reloader=True)