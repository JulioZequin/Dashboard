# 📊 Análise IBOVESPA x SELIC

Este projeto tem como objetivo analisar a relação entre o **Índice Bovespa (IBOVESPA)** e a **taxa SELIC**, no período de **jan/2014 a ago/2025**.  
A aplicação foi desenvolvida em **Python** com **Streamlit** e integra dados econômicos do mercado financeiro e da política monetária.

### Link do site: https://juliozequin.streamlit.app/ 
---

## 🚀 Tecnologias utilizadas
- [Streamlit](https://streamlit.io/) – Interface interativa
- [Pandas](https://pandas.pydata.org/) – Manipulação dos dados
- [NumPy](https://numpy.org/) – Cálculos numéricos
- [Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/) – Visualizações
- [Plotly](https://plotly.com/python/) – Gráficos interativos
- [SciPy](https://scipy.org/) – Estatística
- [Plotnine](https://plotnine.readthedocs.io/) – Visualização estilo ggplot

---

## 📑 Descrição dos dados
- **IBOVESPA:** valor absoluto do índice (mensal)  
- **SELIC:** taxa básica de juros da economia brasileira (%)  
- **IBOVESPA_pct:** variação percentual mensal do IBOVESPA  
- **SELIC_pct:** variação percentual mensal da SELIC  

Fonte dos dados:
- IBOVESPA: Arquivo `Evolucao_Mensal.csv`
- SELIC: API do Banco Central do Brasil (série 4189)

---

## 📌 Objetivos da análise
- Investigar se oscilações na SELIC influenciam a performance do IBOVESPA.  
- Avaliar a correlação entre variações percentuais mensais.  
- Testar hipóteses estatísticas sobre a relação entre os indicadores.  

---

## 🔍 Principais resultados
- O **IBOVESPA** apresenta maior **volatilidade** e oscilações intensas.  
- A **SELIC** muda em ciclos mais lentos, mas pode gerar impactos significativos.  
- A correlação de Pearson encontrada foi **r ≈ -0,09 (p > 0.05)** → não significativa.  
- Bootstrap e IC95% confirmaram a ausência de relação linear consistente.  
- Conclusão: **não há evidência estatística de que cortes/altas da SELIC expliquem isoladamente o comportamento do IBOVESPA.**

---


