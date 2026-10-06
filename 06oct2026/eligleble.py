performance_rating=4
years=2

user_performance_rating=int(input())
user_years=int(input())

if user_performance_rating > performance_rating and user_years > years:
    print("eligible")
else:
    print("not eligible")    