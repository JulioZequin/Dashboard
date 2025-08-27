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

# Configuração inicial da página
st.set_page_config(
    page_title="Portfólio - Júlio Zequin",
    page_icon="📊",
    layout="wide"
)

# =============================
# SEÇÃO HOME
# =============================

# Título de boas-vindas
st.title("👋 Olá, eu sou Júlio Zequin")
st.subheader("Estudante de Engenharia de Software (FIAP)")




# Foto/Avatar (opcional: troque pelo caminho da sua foto)
st.image("WhatsApp Image 2025-08-27 at 10.55.02.jpeg", width=180)


st.markdown(
        """
        ### Sobre mim  
        Sou estudante de Engenharia de Software na FIAP (4º semestre) e já acumulo experiência em projetos acadêmicos e pessoais com linguagens como Python, Java, C++, HTML, CSS, JavaScript e SQL.
        Tenho familiaridade com metodologias ágeis, especialmente Scrum, além de utilizar ferramentas como Git, GitHub, Google Colab, IntelliJ IDEA e VS Code no desenvolvimento dos trabalhos.

        Atuei em iniciativas de análise de dados e participei do projeto Fórmula E em parceria com a Tech Mahindra, aplicando soluções em Python, C++ e tecnologias web.
        Busco minha primeira experiência profissional na área de programação, destacando minha facilidade em aprender, boa comunicação e dedicação ao aprimoramento contínuo. 

 
        """
    )

st.markdown("""
- 📧 **Email:** [juliozequin2003@gmail.com](mailto:juliozequin2003@gmail.com)  
- 📱 **Telefone:** +55 (11) 99866-0139  
- 💻 **GitHub:** [github.com/JulioZequin](https://github.com/JulioZequin)  
- 🔗 **LinkedIn:** [Júlio Zequin](https://www.linkedin.com/in/j%C3%BAlio-zequin-b660142b7/)
""")

# Pequeno destaque final
st.success("💡 Use o menu lateral para navegar pelas seções!")





