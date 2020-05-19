#import urllib2
import BeautifulSoup4


e = urllib2.urlopen("http://es.wikipedia.org/wiki/Paraguay").read()

soup = BeautifulSoup(e, 'html.parser')

# Ejemplo de como imprimir todo
# print soup.prettify()

# Obtenemos la tabla

tabla_paraguay = soup.find_all('table', 'wikitable')[1]

# Obtenemos todas las filas
rows = tabla_paraguay.find_all("tr")

for row in rows:
    # obtenemos todas las columns
    cells = row.find_all("td")
    linea = ""
    for cell in cells:
        linea += cell.get_text() + '\t'
        
    #imprimos la fila
    print (linea)