import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análise", layout="wide")

dadosbov = pd.read_csv('Evolucao_Mensal.csv', sep=';', skiprows=1, encoding='latin-1')
st.session_state["data"] = dadosbov


st.sidebar.markdown("Desenvolvido por Júlio Zequin")


st.title("📑Apresentação dos dados e tipos de variáveis")
st.write("O conjunto de dados reúne informações mensais, no período de janeiro de 2014 a agosto de 2025, relacionando dois indicadores econômicos relevantes no Brasil: o Índice Bovespa (IBOVESPA) e a taxa SELIC. Além dos valores absolutos, " \
"também foram calculadas suas variações percentuais mensais, permitindo comparar oscilações no mercado acionário e na política monetária.")
    
# Remove pontos de milhar e troca vírgula por ponto
dadosbov["Valor"] = (dadosbov["Valor"].astype(str).str.replace(".", "", regex=False).str.replace(",", ".", regex=False).astype(float))

    # Série da SELIC mensal (código 4189 no SGS)
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=csv"

selic = pd.read_csv(url, sep=';', decimal=',')
selic['data'] = pd.to_datetime(selic['data'], dayfirst=True)
selic['valor'] = selic['valor'].astype(float)

# Filtra o mesmo período do seu IBOVESPA (2014–2025)
selic = selic[(selic['data'] >= "2014-01-01") & (selic['data'] <= "2025-12-31")]

    # Cria coluna de data no IBOVESPA
dadosbov['Data'] = pd.to_datetime(dadosbov['Ano'].astype(str) + '-' + dadosbov['Mês'].astype(str) + '-01')

    # Junta IBOVESPA e SELIC pela data
df = pd.merge(dadosbov[['Data','Valor']], selic[['data','valor']], left_on='Data', right_on='data')

df = df.rename(columns={'Valor': 'IBOVESPA', 'valor': 'SELIC'})
df = df[['Data','IBOVESPA','SELIC']]

# Variação mensal percentual
df['IBOVESPA_pct'] = df['IBOVESPA'].pct_change() * 100
df['SELIC_pct'] = df['SELIC'].pct_change() * 100

df

st.markdown("""
- **Data: Qualitativa ordinal (período temporal da observação)**
- **IBOVESPA: Quantitativa contínua (valor absoluto do índice Bovespa no período)**
- **SELIC: Quantitativa contínua (Taxa básica de juros da economia brasileira (%) no período)**
- **IBOVESPA_pct: Quantitativa contínua (variação percentual do IBOVESPA em relação ao período anterior)**  
- **SELIC_pct: Quantitativa contínua (variação percentual da taxa SELIC em relação ao período anterior.)**                  
""")

st.subheader("📌O objetivo do conjunto de dados é comparar o comportamento do mercado de capitais (IBOVESPA) com a política monetária (SELIC), no intuito de responder as seguintes perguntas:")

st.markdown("""
- **Oscilações na taxa de juros influenciam (ou não) a performance do índice de ações?**
- **Existe correlação entre a variação da SELIC e a variação do IBOVESPA?**
- **O IBOVESPA tende a subir em ciclos de queda da SELIC?**
- **Durante períodos de juros altos, o IBOVESPA fica estagnado ou cai?**  
            """)

st.write("Será usado apenas as colunas de variações percentuais porque elas colocam IBOVESPA e SELIC em mesma base de comparação, " \
"destacam os movimentos relativos e permitem uma análise estatística e econômica mais justa e consistente")

# Seleciona apenas as colunas numéricas
numericas = df[['IBOVESPA_pct',	'SELIC_pct']]

# resumo
resumo = pd.DataFrame({
    'count': numericas.count(),
    'min': numericas.min(),
    'max': numericas.max(),
    'mean': numericas.mean(),
    'median': numericas.median(),
    'std': numericas.std(),
    'var': numericas.var()
})

resumo

st.markdown("""
- **O IBOVESPA apresenta retorno médio positivo, mas com quedas muito mais intensas do que as altas, o que indica alto risco.**

- **A SELIC varia menos e passa longos períodos sem alteração, mas em certos momentos sofre ajustes fortes, o que gera dispersão parecida com a do IBOVESPA.**

- **Resumo estatístico sugere que o mercado acionário compensa seu risco com crescimento médio positivo, enquanto a SELIC reflete decisões pontuais da política monetária.**
             
""")

st.title("📈Verificando distribuição dos dados")

def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)


plt.figure(figsize=(13, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['IBOVESPA_pct'].dropna(), kde=True, bins=20, color='skyblue')
plt.title('Distribuição de Frequência da Variação Percentual Mensal do IBOVESPA')
plt.xlabel('Variação Percentual Mensal (%)')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.histplot(df['SELIC_pct'].dropna(), kde=True, bins=20, color='salmon')
plt.title('Distribuição de Frequência da Variação Percentual Mensal da SELIC')
plt.xlabel('Variação Percentual Mensal (%)')
plt.ylabel('Frequência')


plt.tight_layout()
st.pyplot(plt)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['IBOVESPA_pct', 'SELIC_pct']].dropna())
plt.title('Boxplot da Variação Percentual Mensal do IBOVESPA e SELIC')
plt.ylabel('Variação Percentual Mensal (%)')
st.pyplot(plt)

st.write("**Conclusão dos gráficos:**")


st.markdown("""
- **O IBOVESPA mostra comportamento muito mais volátil e instável.**

- **A SELIC apresenta mudanças discretas na maioria do tempo, mas quando muda, pode gerar impactos significativos**

- **Isso reforça a ideia de que a política monetária é mais gradual e o mercado de capitais mais sensível e reativo.**
             
""")

st.write("Outliers não serão levadas em consideração pois representam uma pequena fração do dataframe.")
st.write("Necessário um gráfico de tendência para comparar a variação dos índices ao longo do tempo.")

plt.figure(figsize=(12, 6))
sns.lineplot(x='Data', y='IBOVESPA_pct', data=df, label='IBOVESPA_pct')
sns.lineplot(x='Data', y='SELIC_pct', data=df, label='SELIC_pct')
plt.title('Tendência da Variação Percentual Mensal do IBOVESPA e SELIC ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Variação Percentual Mensal (%)')
plt.legend()
plt.grid(True)
st.pyplot(plt)

st.markdown("""
- **O IBOVESPA é muito mais volátil e reativo, enquanto a SELIC muda em passos mais controlados.**

- **Há momentos de correlação, mas não é uma regra fixa — o mercado de capitais responde a um conjunto mais amplo de variáveis além da política monetária.**    
             
""")

st.title("🧪Correlação, IC, e Teste de Hipótese")

# 1. Seleção das variáveis

x = df['IBOVESPA_pct'].dropna()
y = df['SELIC_pct'].dropna()

# 2. Cálculo da correlação de Pearson

r, p_value = stats.pearsonr(x, y)
print(f"Correlação de Pearson: r = {r:.4f}, p-valor = {p_value:.4f}")

# 3. Intervalo de Confiança para r (usando transformação de Fisher)

n = len(x)

# Transformação de Fisher Z
z = np.arctanh(r)
se = 1 / np.sqrt(n - 3)  # erro padrão

# Intervalo de confiança 95%
z_crit = stats.norm.ppf(0.975)  # valor crítico z para 95%
lo_z, hi_z = z - z_crit * se, z + z_crit * se
lo, hi = np.tanh([lo_z, hi_z])  # voltando da escala Z para r

st.subheader(f"IC 95% para r: [{lo:.4f}, {hi:.4f}]")


# 4. Visualização 1 - Dispersão com linha de regressão e IC

plt.figure(figsize=(10,6))
sns.regplot(x=x, y=y, ci=95, line_kws={'color':'red'})
plt.title(f"Correlação IBOVESPA x SELIC\nr = {r:.4f}, p = {p_value:.4f}", fontsize=12)
plt.xlabel("IBOVESPA - Variação Percentual Mensal (%)")
plt.ylabel("SELIC - Variação Percentual Mensal (%)")
st.pyplot(plt)

st.markdown("""
- **A correlação entre variações percentuais mensais de IBOVESPA e SELIC é muito fraca e praticamente irrelevante (r ≈ -0,09).**

- **Isso sugere que, no curto prazo, o IBOVESPA não responde de forma direta às mudanças percentuais na SELIC.**    
             
""")

st.write("O intervalo de confiança vai de -0.25 até +0.07.")
st.write("Isso significa que, com 95% de confiança, a correlação verdadeira pode ser negativa, nula ou levemente positiva.")

st.markdown("""
- **Não há evidências estatísticas de uma relação linear consistente entre variação percentual do IBOVESPA e variação percentual da SELIC.**

- **O efeito pode ser nulo ou muito fraco em qualquer direção.**    
             
""")

# 5. Visualização 2 - Distribuição bootstrap das correlações
# ------------------------------------------------------------
n_boot = 5000
boot_corrs = []
rng = np.random.default_rng(42)

for _ in range(n_boot):
    sample_idx = rng.choice(n, n, replace=True)
    r_boot, _ = stats.pearsonr(x.iloc[sample_idx], y.iloc[sample_idx])
    boot_corrs.append(r_boot)

plt.figure(figsize=(10,6))
sns.histplot(boot_corrs, bins=30, kde=True, color="skyblue")
plt.axvline(r, color='red', linestyle='--', label=f"r observado = {r:.4f}")
plt.axvline(lo, color='black', linestyle='--', label=f"IC95% [{lo:.2f}, {hi:.2f}]")
plt.axvline(hi, color='black', linestyle='--')
plt.title("Distribuição Bootstrap da Correlação de Pearson", fontsize=12)
plt.xlabel("Coeficiente de Correlação r")
plt.ylabel("Frequência")
plt.legend()
st.pyplot(plt)

st.write("A correlação de Pearson entre IBOVESPA e SELIC apresentou valor de 𝑟=−0.0906 com p=0.2889. O teste de hipótese" \
" realizado indicou que não há evidências estatísticas para rejeitar a hipótese nula de ausência de correlação " \
"linear entre as variáveis, uma vez que o p-valor é superior ao nível de significância de 5%. Para reforçar esse resultado, " \
"foi aplicado o método de reamostragem bootstrap, que gerou a distribuição empírica dos coeficientes de correlação. " \
"O intervalo de confiança de 95% estimado para 𝑟 r foi [-0.25, 0.08], contendo o valor zero, o que confirma a " \
"ausência de significância estatística. Assim, tanto o teste de hipótese formal quanto a análise bootstrap apontam " \
"para a inexistência de uma relação linear robusta entre IBOVESPA e SELIC no período analisado.")

st.title("💡Conclusão")

st.write("Com base nas análises estatísticas, " \
"não foi possível comprovar uma relação estatisticamente significativa entre as variações da SELIC e o desempenho do IBOVESPA no período estudado.")
st.write("Ou seja: embora a teoria econômica sugira que cortes de juros favorecem o mercado acionário, os dados não sustentam essa relação de forma isolada," \
" indicando que outros fatores macroeconômicos e conjunturais têm peso relevante sobre o comportamento da bolsa.")




