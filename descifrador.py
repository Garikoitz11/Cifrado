textoEn = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXVITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE."""

#frecuencias = [["E", 16.78], ["A", 11.96], ["O", 8.69], ["L", 8.37], ["S", 7.88], ["N", 7.01], ["D", 6.87], ["R", 4.94], ["U", 4.8], ["I", 4.15], ["T", 3.31], ["C", 2.92], ["P", 2.776], ["M", 2.12], ["Y", 1.54], ["Q", 1.53], ["B", 0.92], ["H", 0.89], ["G", 0.73], ["F", 0.52], ["V", 0.39], ["J", 0.3], ["", 0.29], ["Z", 0.15], ["X", 0.6], ["K", 0], ["W", 0]]
frecuencias = ["E", "A", "O", "L","S","N","D","R","U","I","T","C","P","M","Y","Q","B","H","G","F","V","J","Z","X","K","W"]
listaLetras = []
contarLetras = textoEn.count("")

for i in range(contarLetras-1):
    if textoEn[i] != " " and textoEn[i] != "\n" and textoEn[i] != "." and textoEn[i] != "," and textoEn[i] != "1" and textoEn[i] != "2" and textoEn[i] != "3" and textoEn[i] != "4" and textoEn[i] != "5" and textoEn[i] != "6" and textoEn[i] != "7" and textoEn[i] != "8" and textoEn[i] != "9" and textoEn[i] != "0" and textoEn[i].islower() == False:
        listaLetras.append(textoEn[i])

frecuenciaLetras = []

for letra in listaLetras:
    frecuenciaLetras.append(listaLetras.count(letra))

nuevaLista = []
nuevaListaFrecuencias = []

def calcularValor(letra):
    for l in range(len(listaLetras)):
        if listaLetras[l] == letra:
            return frecuenciaLetras[l]
    return 0

for letra in listaLetras:
    valor = True
    for letra2 in nuevaLista:
        if letra == letra2:
            valor = False
    if valor == True:
        nuevaLista.append(letra)
        nuevaListaFrecuencias.append(calcularValor(letra))

listaAlto = []
count = 0
nuevasFrecuencias = []
while 0 < len(nuevaListaFrecuencias):
    result = False
    h = 0
    alto= 0
    for j in nuevaListaFrecuencias:
        if listaAlto is None or j > alto:
            alto = j
    while result == False and h<len(nuevaListaFrecuencias)-1:
        if nuevaListaFrecuencias[h] == alto:
            result = True 
        else:
            h = h+1
    nuevasFrecuencias.append(nuevaLista[h])
    del nuevaListaFrecuencias[h]
    del nuevaLista[h]

y = 0
for z in frecuencias:
    if len(nuevasFrecuencias) > y:
        textoNuevo = textoEn.replace(nuevasFrecuencias[y], z.swapcase())
        textoEn = textoNuevo
        y = y+1

print(textoNuevo)