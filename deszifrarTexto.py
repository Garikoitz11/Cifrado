texto = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXVITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE."""

from collections import Counter #Importa la funcion

x = Counter(texto) #Mira cuanto aparece cada caracter, de mas a menos
print(x) #Lo muestra por pantalla

texto = texto.replace("X", "e") #Intercambia las letras del mensaje por las mas frecuentes de nuestro idioma
texto = texto.replace("E", "a")
texto = texto.replace("K", "r")
texto = texto.replace("I", "o")
texto = texto.replace("C", "i")
texto = texto.replace("J", "n")
texto = texto.replace("T", "l")
texto = texto.replace("A", "d")
texto = texto.replace("R", "c")
texto = texto.replace("Z", "u")
texto = texto.replace("H", "t")
texto = texto.replace("N", "s")
texto = texto.replace("P", "m")
texto = texto.replace("D", "p")
texto = texto.replace("O", "f")
texto = texto.replace("Q", "b")
texto = texto.replace("S", "q")
texto = texto.replace("V", "y")
texto = texto.replace("G", "j")
texto = texto.replace("U", "g")
texto = texto.replace("M", "h")
texto = texto.replace("F", "x")
texto = texto.replace("L", "z")

print(texto) #Imprime el mensaje desencriptado