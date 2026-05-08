import pandas as pd 

# importando os dados csv
df_dados = pd.read_csv('./aula11/base1.csv', sep=';')
print(df_dados.head())

print('\nMaior Preço:')
print(df_dados['preco'].max())

print('\nMenor Preço:')
print(df_dados['preco'].min())

print('\nMédia dos Preço:')
print(round(df_dados['preco'].mean(),2)) # round(x,2)

print('\nTotal dos Preço:')
print(df_dados['preco'].sum())
