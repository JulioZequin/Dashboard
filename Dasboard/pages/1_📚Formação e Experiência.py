import streamlit as st

st.title("🎓 Formação e Experiência")

# Formação
with st.expander("📘 Formação Acadêmica", expanded=True):
    st.markdown("""
    - **Engenharia de Software** – 4º semestre (cursando)  
    - **Ensino Médio** – Colégio Domus Sapiens
    """)

# Certificações
with st.expander("🎓 Certificações", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Alura**")
        st.markdown("""
        - Python para Data Science — 40h  
        - Formação Excel — 50h  
        - SQL — 16h  
        - Git e GitHub
        """)

    with col2:
        st.markdown("**FIAP — NanoCourses**")
        st.markdown("""
        - Engenharia de Software — 100h  
        - Design Thinking — Process
        """)

# Projetos
with st.expander("💻 Projetos", expanded=True):
    st.markdown("### ⚡ Projeto Fórmula E – FIAP + Tech Mahindra")
    with st.container():
        st.markdown("""
        Plataforma interativa para corridas da Fórmula E.  
        - Tecnologias: Python, HTML, CSS, C++  
        - Funcionalidades: transmissão interativa, sistema de palpites e engajamento com prêmios  
        """)

    st.markdown("### 📊 Análise de Dados sobre Homicídios no Brasil")
    with st.container():
        st.markdown("""
        Exploração estatística e visual de dados de criminalidade.  
        🔗 [GitHub](https://github.com/JulioZequin/AnaliseHomicidiosBrasil)  
        """)

    st.markdown("### 🔥 Análise de Dados sobre Incêndios nos EUA")
    with st.container():
        st.markdown("""
        Estudo dos padrões de queimadas com Python e bibliotecas de análise de dados.  
        🔗 [GitHub](https://github.com/JulioZequin/AnaliseIncendiosEUA)  
        """)

# Tecnologias e Ferramentas
with st.expander("🛠️ Tecnologias e Ferramentas", expanded=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("- 🐍 Python")
        st.markdown("- ☕ Java")
        st.markdown("- ⚙️ C++")
        st.markdown("- 🚀 IntelliJ IDEA")

    with col2:
        st.markdown("- 🗄️ SQL")
        st.markdown("- 📓 Google Colab")
        st.markdown("- 💻 VS Code")
        st.markdown("- 📊 Scrum")

    with col3:
        st.markdown("- 📐 Astah")
        st.markdown("- 🧩 Oracle SQL Developer")
        st.markdown("- 🏢 Excel")


# Idiomas
with st.expander("🌍 Idiomas", expanded=True):
    st.markdown("""
    - 🇺🇸 Inglês — Intermediário
    """)
