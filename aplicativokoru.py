#Instalando o Pandas no terminal: pip install pandas
#Instalando o Streamlit no terminal: pip install streamlit
#Instalando o matplotlib no terminal: pip install matplotlib

#Importando Streamlit, Pandas, Numpy e Matplotlib:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Criando nosso aplicativo no terminal: streamlit run aplicativokoru.py

#Chamando todas as bases
df1 = pd.read_csv('DataSet_brazilian-ecommerce/olist_customers_dataset.csv')
df2 = pd.read_csv('DataSet_brazilian-ecommerce/olist_geolocation_dataset.csv')
df3 = pd.read_csv('DataSet_brazilian-ecommerce/olist_order_items_dataset.csv')
df4 = pd.read_csv('DataSet_brazilian-ecommerce/olist_order_payments_dataset.csv')
df5 = pd.read_csv('DataSet_brazilian-ecommerce/olist_order_reviews_dataset.csv')
df6 = pd.read_csv('DataSet_brazilian-ecommerce/olist_orders_dataset.csv')
df7 = pd.read_csv('DataSet_brazilian-ecommerce/olist_products_dataset.csv')
df8 = pd.read_csv('DataSet_brazilian-ecommerce/olist_sellers_dataset.csv')

#Abaixo criamos um join (MERGE) das tabelas para podermos cruzar dados com mais facilidade
df9_merge = pd.merge(df1, df6, on='customer_id')
df10_merge = pd.merge(df9_merge, df3, on='order_id')
df11_merge = pd.merge(df10_merge, df4, on='order_id')
df12_merge = pd.merge(df11_merge, df5, on='order_id')
df13_merge = pd.merge(df12_merge, df7, on='product_id')
tabela_unica = pd.merge(df13_merge, df8, on='seller_id')

#Título do Projeto:
st.markdown("<h1 style='color: #edf388; font-family: Arial;font-size: 30px;'>Estudo de dados da Base Olist - Projeto Koru</h1>", unsafe_allow_html=True)

#01-Pergunta número 01
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>01 - Os dados dessa base se refere a qual período?</p>", unsafe_allow_html=True)

#01-Transformando a coluna "ORDER APPROVED AT" de "object" para "datetime"
tabela_unica['order_approved_at'] = pd.to_datetime(tabela_unica['order_approved_at'])
tipo_dados = tabela_unica['order_approved_at'].dtype

#01-Resposta
data_mais_antiga = tabela_unica['order_approved_at'].min()
data_mais_recente = tabela_unica['order_approved_at'].max()

#01-Exibindo os resultados
st.write("R: As informações da base Olist estudada nesse projeto referem-se ao período de", data_mais_antiga, "a", data_mais_recente)

#02-Pergunta número 02
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>02 - Quantidade de vendas aprovadas por mês?</p>", unsafe_allow_html=True)

#02-Criei uma nova coluna contendo o mês e ano
tabela_unica['MesAno'] = tabela_unica['order_approved_at'].dt.strftime('%B-%Y')

#02-Contando linha de compras aprovadas por mês e ano respectivos
resumo_tabela = tabela_unica['MesAno'].value_counts().reset_index()
resumo_tabela.columns = ['MesAno', 'Vendas Aprovadas']

#02-Exibindo os resultados
st.write(resumo_tabela)

#02-Gráfico para a tabela.
fig, ax = plt.subplots()
ax.bar(resumo_tabela['MesAno'], resumo_tabela['Vendas Aprovadas'])

#02-Aqui criei os nomes dos rótulos
ax.set_title('Quantidade de Vendas Aprovadas por Mês/Ano')
ax.set_xlabel('Mês e Ano')
ax.set_ylabel('Quantidade')

#02-Esse código abaixo inclina os rótulos para melhor visualização
plt.xticks(rotation=45, ha='right')

#02-Exibindo o gráfico
st.pyplot(fig)

#03-Pergunta número 03
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>03 - Qual o dia da semana que mais vende?</p>", unsafe_allow_html=True)

#03-Criei duas colunas. Uma de dia da semana e a outra horário das vendas aprovadas
tabela_unica['dia_da_semana'] = tabela_unica['order_approved_at'].dt.day_name()
tabela_unica['horario'] = tabela_unica['order_approved_at'].dt.time

#03-Fiz uma contagem para saber qual o dia que mais vende.
tabela_contagem_dia = tabela_unica['dia_da_semana'].value_counts().reset_index()
tabela_contagem_dia.columns = ['Dia da Semana', 'Quantidade']

#03-Mostrando a tabela em streamlit
st.write(tabela_contagem_dia)

#03-Mostrando o gráfico em streamlit
st.bar_chart(tabela_contagem_dia.set_index('Dia da Semana'))

#04-Pergunta número 04
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>04 - Quais as categoria de produtos mais vendidos?</p>", unsafe_allow_html=True)

#04-Fiz uma contagem para saber qual a categoria que mais vende.
tabela_contagem_categoria = tabela_unica['product_category_name'].value_counts().reset_index()
tabela_contagem_categoria.columns = ['Categoria do Produto', 'Quantidade']

#04-Mostrando a tabela em streamlits
st.write(tabela_contagem_categoria)

#04-Selecionar os 10 primeiros itens
top_10 = tabela_contagem_categoria.head(10)

#04-Gráfico de barras para os 10 primeiros itens
st.bar_chart(top_10.set_index('Categoria do Produto'))

#05-Pergunta número 05
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>05 - Quais os estados que mais compraram nesse período?</p>", unsafe_allow_html=True)

#05-Fiz uma contagem para saber quais estados mais comoraram
tabela_contagem_estado = tabela_unica['customer_state'].value_counts().reset_index()
tabela_contagem_estado.columns = ['Estado', 'Quantidade']

#05-Mostrando a tabela em streamlits
st.write(tabela_contagem_estado)

#05-Selecionar os 10 primeiros itens
top_10_estado = tabela_contagem_estado.head(10)

#05-Gráfico de barras para os 10 primeiros itens
st.bar_chart(top_10_estado.set_index('Estado'))

#06-Pergunta número 06
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>06 - Quais as cidades que mais compraram nesse período?</p>", unsafe_allow_html=True)

#06-Fiz uma contagem para saber quais estados mais comoraram
tabela_contagem_cidade = tabela_unica['customer_city'].value_counts().reset_index()
tabela_contagem_cidade.columns = ['Cidade', 'Quantidade']

#06-Mostrando a tabela em streamlits
st.write(tabela_contagem_cidade)

#06-Selecionar os 10 primeiros itens
top_10_cidade = tabela_contagem_cidade.head(10)

#06-Gráfico de barras para os 10 primeiros itens
st.bar_chart(top_10_cidade.set_index('Cidade'))

#07-Pergunta número 07
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>07 - Quais os meios de pagamento mais utilizados?</p>", unsafe_allow_html=True)

#07-Fiz uma contagem para saber quais estados mais comoraram
tabela_contagem_pagamento = tabela_unica['payment_type'].value_counts().reset_index()
tabela_contagem_pagamento.columns = ['Meios de Pagamento', 'Quantidade']

#07-Mostrando a tabela em streamlits
st.write(tabela_contagem_pagamento)

#07-Gráfico de pizza
fig, ax = plt.subplots()
wedges, _, autopct = ax.pie(tabela_contagem_pagamento['Quantidade'], autopct='%1.1f%%', startangle=90)
ax.axis('equal') 

#07-Adicionando legendas
ax.legend(wedges, tabela_contagem_pagamento['Meios de Pagamento'], title='Meios de Pagamento', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

#07-exibindo o gráfico
st.pyplot(fig)

#08-Pergunta número 08
st.markdown("<p style='color: #75a8f3; font-family: Arial;font-size: 20px;'>08 - Qual a média de avaliação dos clientes sendo que 1 é a nota menor e 5 é a nota maior?</p>", unsafe_allow_html=True)

#08-Fiz uma contagem para saber quais estados mais comoraram
tabela_contagem_estrelas = tabela_unica['review_score'].value_counts().reset_index()
tabela_contagem_estrelas.columns = ['Estrelas', 'Quantidade']

#08-Mostrando a tabela em streamlits
st.write(tabela_contagem_estrelas)

#08-Calculando a média
media_estrelas = tabela_unica['review_score'].mean()

st.write("R: A média de estrelas é: ", media_estrelas)

#08-Gráfico de pizza
fig, ax = plt.subplots()
wedges, _, autopct = ax.pie(tabela_contagem_estrelas['Quantidade'], autopct='%1.1f%%', startangle=90)
ax.axis('equal') 

#08-Adicionando legendas
ax.legend(wedges, tabela_contagem_estrelas['Estrelas'], title='Estrelas', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

#08-exibindo o gráfico
st.pyplot(fig)