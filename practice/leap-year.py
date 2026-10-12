class Solution:
    def is_leap_year(is_leap_year):
        if  year % 400 ==0:
        return True
        elif year % 100 ==0:
            return False
        elif year % 4 ==0:
            return True
         else:
            return False

         year=int(input())   
         print("leap_year(year)")


                  
