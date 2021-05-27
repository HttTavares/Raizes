import pandas as pd

file = pd.read_excel("Cesta Camponesa 16_01 (respostas).xlsx")
freightprices = pd.read_excel("Freight Prices.xlsx")

# def get_price(row, neighb):
#     for row in range(0, len(freightprices)):
#         if freightprices.iloc[row][0].replace(" ", "") in neighb.replace(" ", ""):
#             return freightprices.iloc[row][1]
#
# def namemaker(dia):
#     return "Cesta camponesa " + dia
#
# def get_freightprice(file, row):
#     neighb=file.iloc[row][2]
#     if "Niterói" in neighb:
#         return 17
#     else:
#         return get_price(row, neighb)

lista_cestantes=[]
class Cestantes:
    def __init__(self, lista_cestantes):
        self.lista_cestantes=lista_cestantes

    # def getcestante_byinfo(self, info):
    #     for thing in self.lista_cestantes:
    #         if thing.

class Cestante:
    def __init__(self, name, id, address, nucleus, phone, email, history):
        self.name=name
        self.id=id
        self.address=address
        self.nucleus=nucleus
        self.phone=phone
        self.email=email
        self.history=history
        Cestantes.append(self)

Cestantes1 = Cestantes(lista_cestantes)

print(Cestantes1.lista_cestantes)

# for row in range(5,35):
#     print(file.iloc[row][2], get_freightprice(file,row))
