from countryinfo import CountryInfo

input1 = str(input("Enter your country:-"))
country = CountryInfo(input1)
A = country.info()
B = country.provinces()
C = country.wiki()
D = country.region()


print(A)
print(B)
print(C)
print(D)