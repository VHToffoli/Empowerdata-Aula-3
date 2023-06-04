#!/usr/bin/env python
# coding: utf-8

# # Biblioteca (Library)

# In[69]:


import pandas as pd


# # Carregando Dados (Uploading data)

# In[79]:


dados = pd.read_excel("vendas.xlsx")


# # Análise Exploratória (Exploratory Analysis)

# In[80]:


#Listar primeiras linhas (List first lines)

dados.head()


# In[78]:


#Listar as últimas linhas (List last lines)

dados.tail()


# In[66]:


#Tamanho da tabela de dados (Data tab size)

dados.shape


# In[67]:


#Tipo de dados (Data types)

dados.dtypes


# # Estatisticas (Data Stats)

# In[17]:


#Gerando estatísticas (Generating Statistics)
dados.describe()


# # Análises (Analysis)

# In[14]:


# Total de vendas por loja (Total sales per store)
dados.loja.value_counts()


# In[68]:


#Total de pedidos de Açaí por tamanho (total Açaí meal orders per size)
dados.tamanho.value_counts()


# In[16]:


#Total de vendas por forma de pagamento (Total sales per payment method)
dados.forma_pagamento.value_counts()


# # Agrupamento de dados (Data grouping)

# In[8]:


#faturamento por loja (biliing per store)
dados.groupby("loja").preco.sum()


# In[7]:


#Faturamento médio por loja  (Average biliing per store)
dados.groupby("loja").preco.mean()


# In[ ]:


#Faturamento por Estado/Cidade (Biliing per State/City)
dados.groupby(["estado", "cidade"]).preco.sum().to_excel("Faturamento-estado-cidade.xlsx")


# In[ ]:


#Preço médio agrupado por Estado/Cidade(Average price grouped per State/City)
dados.groupby(["estado", "cidade"]).preco.mean().to_frame()


# # Visualização de dados (Data Visualization)

# In[ ]:


get_ipython().system('pip install plotly==5.14.1')
get_ipython().system('pip install plotly.express')
get_ipython().system('pip install prophet')


# In[83]:


import plotly.express as px
from prophet.plot import plot_plotly


# # Criando Gráficos (Creating Graphics)

# In[92]:


grafico = px.histogram(dados, x="loja", y= "preco", text_auto=True, color="forma_pagamento")
grafico.show()
grafico.write_html("Grafico_forma_pagamento.html")


# # Listas - Estrutura de Dados (List - Data Structure)

# In[102]:


lista_colunas=["loja", "cidade", "estado", "regiao", "tamanho", "local_consumo"]


# # Estrutura de Repetição (For Loop)

# In[103]:


for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna, y="preco", text_auto=True, color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"Grafico-{coluna}.html")


# In[ ]:





# In[ ]:





# In[ ]:




