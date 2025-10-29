# Last updated: 28/10/2025, 19:43:30
class Solution(object):
    def lengthOfLIS(self, nums):
        #caso 1 = [2,1,2,4,5] 
        # R/ 4 = [1,2,4,5]
        # len = 5
        longitud = len(nums) # 5
        if longitud == 0:
            return 0

        dp = [1] * longitud 

        # [1,1,1,1,1] por si esta completamente decreciente la lista 
        # aqui podriamos ir reemplazando los 1 por cada valor i en la lista nums
        for i in range(longitud):
            for j in range(i):
            # creo que lo ideal seria buscar el numero mas bajo y empezar a agregar a dp desde ahi 
                if nums[j] < nums[i]:
                # si en a[2,1,2,3] por ejemplo si 2 < 1, luego se iria comparndo con los demas y agregarlo a dp
                    if dp[j] + 1 > dp[i]: # agregamos el valor minimo a la lista 
                        dp[i] = dp[j] +1
        return max(dp)





    
        