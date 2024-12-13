import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Carregar o dataset (substitua o caminho pelo arquivo baixado do Kaggle)
data = pd.read_csv("superstore_sales.csv")

# Converter colunas para o tipo numérico (substituir erros por NaN)
data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')
data['Profit'] = pd.to_numeric(data['Profit'], errors='coerce')

# Verificar se há valores ausentes e removê-los
data.dropna(subset=['Sales', 'Profit'], inplace=True)

# Exibir informações básicas sobre os dados
print(data.info())
print(data.head())

# Análise 1: Performance contra valores esperados
total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum()
expected_sales = 500000  # Exemplo de valor esperado
expected_profit = 70000  # Exemplo de valor esperado

print(f"Total Sales: {total_sales}, Expected Sales: {expected_sales}")
print(f"Total Profit: {total_profit}, Expected Profit: {expected_profit}")

# Análise 2: Análise por categoria
category_summary = data.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'})
category_summary['Profit Margin (%)'] = (category_summary['Profit'] / category_summary['Sales']) * 100
print(category_summary)

# Visualização
plt.figure(figsize=(10, 6))
sns.barplot(data=category_summary.reset_index(), x='Category', y='Sales', palette='Blues')
plt.title('Total Sales by Category')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=category_summary.reset_index(), x='Category', y='Profit', palette='Greens')
plt.title('Total Profit by Category')
plt.show()

# Análise 3: Top e Bottom produtos
subcategory_summary = data.groupby('Sub-Category').agg({'Sales': 'sum'}).sort_values(by='Sales', ascending=False)
print("Top 5 Products by Sales:")
print(subcategory_summary.head(5))

print("Bottom 5 Products by Sales:")
print(subcategory_summary.tail(5))

# Análise 4: Tendências mensais
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month'] = data['Order Date'].dt.to_period('M')
monthly_sales = data.groupby('Month').agg({'Sales': 'sum'}).reset_index()

# Ajustar formato de Month para compatibilidade com o gráfico
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o')
plt.title('Monthly Sales Trends')
plt.xticks(rotation=45)
plt.show()

# Análise 5: Análise geográfica
state_sales = data.groupby('State').agg({'Sales': 'sum'}).reset_index()
fig = px.scatter_geo(state_sales, locationmode='USA-states', locations='State', size='Sales',
                     title='Sales by State', scope='usa')
fig.show()

print(recommendations)

