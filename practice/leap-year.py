class Solution:
    leap_year=int(input("enter the year"))
    leap_year=FALSE

    if leap_year>=100:
        if leap_year>=400:
            print("True")
    else:
        print("False")