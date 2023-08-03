from countryinfo import CountryInfo

# input1 = str(input("Enter your country:-"))
# country = CountryInfo(input1)
# A = country.info()
# B = country.provinces()
# C = country.wiki()
# D = country.region()
#
#
# print(A)
# print(B)
# print(C)
# print(D)

def countryinfo(input1):
    country = CountryInfo(input1)
    A = country.wiki()
    B = country.population()
    C = country.region()
    D = country.provinces()
    E = country.borders()
    F = country.area()
    G = country.capital()
    H = country.currencies()
    I = country.languages()
    all_info(A,B,C,D,E,F,G,H,I)


def all_info(A,B,C,D,E,F,G,H,I):
    print("This is wiki links of your country: ",A)
    print("country Populations: ",B)
    print("country Region: ",C)
    print("country provinces,states: ",D)
    print("country borders with connect: ",E)
    print("country area: ",F)
    print("country capital: ",G)
    print("country currencies: ",H)
    print("country languages: ",I)

countryinfo(input1 = input("Enter Your Country: "))