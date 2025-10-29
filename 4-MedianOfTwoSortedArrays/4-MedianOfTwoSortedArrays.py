# Last updated: 29/10/2025, 10:23:38
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        listaCompletaORD = []
        j = 0
        i = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                listaCompletaORD.append(nums1[i])
                i+=1 
            else: 
                listaCompletaORD.append(nums2[j])
                j+=1
            # como estan ordenadas y si ya terminamos una como i por ejemplo 
            # agregamos el resto de la lista j (que ya esta ordenada)
        listaCompletaORD.extend(nums1[i:])
        listaCompletaORD.extend(nums2[j:])
        
        
        long = len(listaCompletaORD)
        if len(listaCompletaORD) % 2 == 0: # si es par se saca la media entre los dos del medio
            a = int(long/2)
            b = int(long/2-1)
            x = listaCompletaORD[a]
            z = listaCompletaORD[b]
            return((x+z)/2.0)
        else: 
            a = int(long/2.0)
            return(listaCompletaORD[a])