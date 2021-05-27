import pandas as pd
import os


path = "/home/vni/Labora/Programação/Python Software/Raizes/cruzamento/"
temp_file_names = os.listdir(path + 'DB')
emails = []

def check_email( email_address, file ):
    for row in range(0, len( file )):
        if email_address == file.iloc[row][1]:
            return [True, row]
    return False

def get_email_addresses( temp_file_name, emails ):
    temp_file = pd.read_excel( path + 'DB/' + temp_file_name )
    for row_number in range(0, len(temp_file)):
        if ('@' in temp_file.iloc[row_number][1]):
            if (temp_file.iloc[row_number][1] in emails) == False:
                emails.append(temp_file.iloc[row_number][1])

def parse_forms(a, b):
    for file_number in range(a, b):
        get_email_addresses(temp_file_names[file_number], emails)

# this fills up the emails list.
parse_forms(0, len(temp_file_names))
# parse_forms(0, 6)

file_name = "clientes-2021-04-23-13-45-94849d87f4.xlsx"
file = pd.read_excel(path + file_name)
final_list = []

def check_client_email_address( row_number ):
    email_address = file.iloc[row_number][1]
    if email_address in emails:
        final_list.append([file.iloc[row_number][2], file.iloc[row_number][1], 'antigo', file.iloc[row_number][15], file.iloc[row_number][20]])
    else:
        final_list.append([file.iloc[row_number][2], file.iloc[row_number][1], 'novo', file.iloc[row_number][15], file.iloc[row_number][20]])

# print( [file.iloc[4][15], file.iloc[4][20]])


for row_number in range(0, len(file)):
    check_client_email_address( row_number )
df = pd.DataFrame(final_list)
df.to_excel('cruzamento de info de cestantes.xlsx')

# print(final_list)

# for email in emails:


# print(len(emails))
# temp_file_name = temp_file_names[0]
# print(temp_file_name)
# print( check_email( "cristinavallereal@gmail.com", file ) )
# print(file_names)

# print( file.iloc[3][1] )