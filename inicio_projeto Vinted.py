
# import pandas as pd
# import numpy as np
# from tabulate import tabulate

# df = pd.read_excel(r"C:\Users\Lucas Santos\OneDrive\Desktop\ProjetoPython\Projeto Vinted\usuarios-VINTED.xlsx")
# # print(tabulate(df, headers= 'keys', tablefmt= 'grid'))

# # df_3 = df.loc[df['pais'] == 'Estados Unidos']
# # print(tabulate(df_3, headers= 'keys', tablefmt= 'grid'))

# # df_false = df.loc[df['pais'] == False]
# # print(tabulate(df_false, headers= 'keys', tablefmt= 'grid'))

# df.loc[(df['id'].between(1, 150)) & (df['pais'] == False), 'pais'] = 'Franca'


# df.loc[(df['id'].between(151 , 299)) & (df['pais'] == False), 'pais'] = 'Lituania'
# # print(tabulate(df, headers= 'keys', tablefmt= 'grid'))



# ids = [15, 28, 31, 36, 45, 52, 60, 64, 76, 88, 93, 99, 100, 106, 114, 117, 118, 123, 132, 139, 147, 150, 157]
# nomes = ['Louis Martin', 'Pierre Dupont', 'Paul Laurent', 'Luc Moreau', 'Nicolas Lefevre', 'Julien Robert', 'Antoine Richard', 'Thomas Petit', 'Hugo Roux', 'Gabriel Faure', 'Alexandre Giraud', 'Benjamin Noel', 'Matthieu Blanchard', 'Sebastien Marchand', 'Florian Guerin', 'Victor Lemoine', 'Damien Fontaine', 'Maxime Perrot', 'Kevin Renault', 'Romain Barbier', 'Quentin Menard', 'Gregory Charles', 'Loic Morin']

# df.loc[(df['id'].isin(ids)) & (df['nome_completo'] == False), 'nome_completo'] = nomes
# # print(tabulate(df, headers= 'keys', tablefmt= 'grid'))

# df_n_false = df.loc[df['nome_completo'] == False]

# # print(tabulate(df_n_false, headers= 'keys', tablefmt= 'grid'))

# ids_2 = [127,160,174,175,177,180,193,195,205,214,223,232,234,237,250,255,265,273,282,283,285,296]
# nomes2 = ['Jonas Kazlauskas', 'Edy Putbre','Tomas Petrauskas', 'Mantas Jankauskas', 'Vytautas Zukauskas', 'Andrius Kavaliauskas', 'Dainius Janavicius', 'Gediminas Valanciunas', 'Linas Balciunas', 'Mindaugas Stankevicius', 'Rokas Jakubauskas', 'Egidijus Sabonis', 'Giedrius Vaitkus', 'Arvydas Matulionis', 'Saulius Vitkauskas', 'Vilius Lapinskas', 'Domas Grigaitis', 'Paulius Zilinskas', 'Laurynas Pukis', 'Simas Kupstas', 'Evaldas Jurevicius', 'Arturas Ramonas']

# df.loc[(df['id'].isin(ids_2)) & (df['nome_completo'] == False), 'nome_completo'] = nomes2


# df_loca_car =df.loc[df['id'] == 37]


# df_erroN = df.loc[df['nome_completo'].str.contains('\?', na=False)]


# df.loc[df['nome_completo'].str.contains('\?', na=False), 'nome_completo'] = df['nome_completo'].str.replace('\?', 'e', regex=True)

# df = df.drop(columns='id')

# print(tabulate(df, headers= 'keys', tablefmt= 'grid'))

# df.to_excel(r"C:\Users\Lucas Santos\OneDrive\Desktop\ProjetoPython\Projeto Vinted\Usuarios_Vinted_ok.xlsx", index=False)


import pandas as pd
import numpy as np
from tabulate import tabulate

df = pd.read_excel(r"C:\Users\Lucas Santos\OneDrive\Documentos\produtos.xlsx")


# print(tabulate(df_false, headers= 'keys', tablefmt= 'grid'))

ids3 = [299,15,92,99,204,21]
cat = ['Blusas','Casacos','Blusas','Casacos','Blusas', 'Blusas']


df.loc[(df['id_usuario'].isin(ids3)) & (df['categoria'] == False), 'categoria'] = cat

df_false = df.loc[df['categoria'] == False]


ids4 = [171,94,289,33,154,73,213,22,139,81,260,11,182]
cat_2 = ['Blusas','Casacos','Blusas','Casacos','Blusas', 'Blusas', 'Blusas','Casacos','Blusas','Casacos','Blusas', 'Blusas', 'Blusas']

# df.loc[(df['id'].isin(ids_2)) & (df['nome_completo'] == False), 'nome_completo'] = nomes2
df.loc[(df['id_usuario'].isin(ids4)) & (df['categoria'] == False), 'categoria'] = cat_2
print(tabulate(df, headers= 'keys', tablefmt= 'grid'))

df.to_excel(r"C:\Users\Lucas Santos\OneDrive\Documentos\produtos_ok.xlsx")