# Last updated: 28/10/2025, 19:43:30
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        visitados = []
        lista = []
        resultado = []
        cuenta = 0
        long = 0
        maxLong = 0
        indice = 0
        longitudes = []
        inicio = 0          # inicio de la ventana actual
        inicio_mejor = 0    # inicio de la mejor subcadena

        
        for letra in s:
            lista.append(letra)

        while indice < len(lista):
            ch = lista[indice]
            while ch in visitados:
                visitados.pop(0)   
                inicio += 1
            visitados.append(ch)
            long = indice - inicio + 1
            if long > maxLong:
                maxLong = long
                inicio_mejor = inicio
            longitudes.append(maxLong)
            resultado.append(maxLong)
            indice += 1
        return (maxLong)
                