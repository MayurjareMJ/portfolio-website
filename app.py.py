import streamlit as st

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Blog", "Contact"])

# Home Page
if page == "Home":
    st.title("👋 Hi, I'm Mayur Jare")
    st.write("AI Engineer | Generative AI | RAG Pipelines | Computer Vision")
    st.download_button("📄 Download Resume", "resume.pdf")

# Skills Page
elif page == "Skills":
    st.header("⚡ Skills")
    st.progress(95)
    st.text("Python: Expert")
    st.progress(90)
    st.text("Deep Learning: Advanced")

# Projects Page
elif page == "Projects":
    st.header("🚀 Featured Projects")
    st.subheader("1. RAG Chatbot")
    st.write("Built a chatbot with LangChain + ChromaDB for document Q&A.")
    if st.button("Demo RAG Chatbot"):
        st.write("👉 (Embed your demo here)")

# Blog Page
elif page == "Blog":
    st.header("📝 Latest Blog Posts")
    st.write("- [Building RAG with LangChain](https://medium.com/)")
    st.write("- [Vector DBs Compared](https://medium.com/)")

# Contact Page
elif page == "Contact":
    st.header("📬 Contact Me")
    st.write("📧 Email: yourmail@gmail.com")
    st.write("💼 [LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("🐙 [GitHub](https://github.com/yourprofile)")
