import pandas as pd

def get_price(row, neighb):
    for row in range(0, len(freightprices)):
        if freightprices.iloc[row][0].replace(" ", "") in neighb.replace(" ", ""):
            return freightprices.iloc[row][1]

def namemaker(dia):
    return "Cesta camponesa " + dia

def get_freightprice(file, row):
    neighb=file.iloc[row][2]
    if "Niterói" in neighb:
        return 17
    else:
        return get_price(row, neighb)

def find_Format(column):
    if "R$" in file.columns[column]:
        price_part=file.columns[column][file.columns[column].find("R$")+2:]
        if "/" in price_part:
            return 1
        else:
            return 2
    else:
        return 3

def getPrice(column):
    n=find_Format(column)
    try:
        if n == 1:
            price_part=file.columns[column][file.columns[column].find("R$")+2:]
            b=price_part.find("/")
            return float(price_part[:b].replace(",", "."))
            # return float(file.columns[column][a+3:b].replace(",", "."))
        elif n==2:
            a=file.columns[column].find("R$")
            return float(file.columns[column][a + 2 : a + 7].replace(",", "."))
            # return float(file.columns[column][a+3:-1].replace(",", "."))
        else:
            return 0
    except ValueError:
        print(n, a, file.columns[column], "oops, column " + str(column))

def get_pedido(row):
    data1=file.iloc[row]
    col=7
    rows=[]
    while col < len(file.columns):
        if data1[col]>0:
            if (type(getPrice(col)) == type(1.2) or type(getPrice(col)) == type(1+'')):
            # cols.append(col)
            # print(col, data1[col], getPrice(col) )
            # print(data1[col])
            # print(getPrice(col))
            # print(find_Format(col))
                rows.append([data1[col], file.columns[col], getPrice(col),  data1[col] * getPrice(col)])
            else:
                rows.append([data1[col], file.columns[col], getPrice(col),  ""])
        col+=1
    return rows

def sum_total3(rows):
    sum=0
    for row in rows:
        sum+=row[-1]
    return sum

def get_rows(bairro):
    rows=[]
    row=0
    # print(bairro==file.iloc[row][1])
    while row<len(file):
        if file.iloc[row][1]==bairro:
            rows.append(row)
        row+=1
    return rows

def bairro_list(bairro):
    bairro_list=[]
    rows=get_rows(bairro)
    for row in rows:
        bairro_list.append(get_pedido(row))
    return bairro_list

def lista_taxistas(file):
    file2 = file.sort_values(by=['NÚCLEO'])
    file3 = file2[['NÚCLEO','NOME COMPLETO', "ENDEREÇO", "Endereço de e-mail", "TELEFONE"]]
    file3.to_excel("lista taxistas.xlsx")
    return file3

def get_infocestante(row):
    info=[]
    for col in [3,2,6]:
        info.append(file.iloc[row][col])
    info.append("")
    # print(info[2])
    return info

def make_pedidoscestante(row):
    info=get_infocestante(row)
    pedidos=get_pedido(row)
    return [info,pedidos]

def make_lista(row):
    lista1=[get_infocestante(row)]
    lista2=[get_infocestante(row)]
    for pedido in get_pedido(row):
        lista1.append(pedido)
        # lista_taxi[-1].append(pedido)

    # total = 0
    # for row1 in range(1, len(lista1)):
    #     total+=lista1[row1][3]
    #     lista1[row1][3] =  lista1[row1][3]

    lista1.append([ "Frete", "", "", "" ])

    # if type(get_freightprice(file, row)) == type(1):
    #     lista1.append([ "Frete", "", "", "R$" + str(get_freightprice(file, row))])
    # else:
    #     lista1.append([ "Frete", "", "", get_freightprice(file, row)])

    lista1.append(["Total","","", ""])
    lista1.append(["", "", "", ""])
    lista1.append(["", "", "", ""])
    lista2[0].append('')
    return [lista1,lista2]

def make_final(rows):
    listafinal=[]
    Column_names = ["ENDEREÇO", "NOME", "NÚCLEO", "TELEFONE", "TOTAL"]
    lista_taxi=[]
    for row in rows:
        print(row)
        info = make_lista(row)
        print(info[0][0])
        listafinal+=info[0]
        lista_taxi+=info[1]
    df=pd.DataFrame(listafinal)
    df1=pd.DataFrame(lista_taxi)
    # df2 = df1.sort_values(by=['NÚCLEO'])

    df.to_excel("Lista de Pedidos Marica" + dia + ".xlsx")
    df1.to_excel("Lista de Entrega Marica" + dia + ".xlsx")

    # df2.to_excel("Lista de Entrega " + dia + ".xlsx")
    # return df

def place_rs(file):
    file=file.rename(columns={"Doação MPA":"Doação MPA R$1,00"})
    return file

dia="11_04_2021"
# filename="Cesta Camponesa "+ dia + " (respostas).xlsx"
# filename="Cesta Camponesa 13_03_21 (respostas).xlsx"
filename="Respostas 08_04 (2).xlsx"
# filetestename="Cesta Camponesa " + dia + " (respostas).xlsx"
path = "/home/vni/Labora/Programação/Python Software/Raizes/"
file = pd.read_excel(path + filename).rename(columns={"Doação MPA":"Doação MPA R$1,00"})
# fileteste = pd.read_excel(path + filetestename)
freightprices = pd.read_excel("Freight Prices.xlsx")
# make_final()
# print(lista_taxistas(file))
# lista_taxistas(file)

# print(file.columns[6])
# print(place_rs(file).columns[6])

# rows = [i for i in range(0, 59)]

# print(getPrice(54))

# FAZER LISTA
rows = [i for i in range(0, len(file))]
make_final(rows)

# for col in range(0, 400):
#     print(getPrice(col))


# print(file)
# for row in range(0, len(file)):
#     print(get_infocestante(row))

