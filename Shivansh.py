import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    # Use the raw URL for Shiv.jpeg
    st.image("https://raw.githubusercontent.com/ShraddhaDarade/ShivanshPortfolio/main/Shiv.jpeg")

with col2:
    st.title("Shivansh Khedkar")
    content = """
    Hi! My name is Shivansh, and I’m 5 years old. I love playing with my toys, dancing to my favorite songs, and going on adventures while traveling. Music makes me so happy, and I even sing along sometimes! I love my mom and dad so much—they’re my superheroes and make everything extra fun. Life is amazing, and I enjoy every moment! 😊
    """
    st.info(content)

col3, col4 = st.columns(2)

with col3:
    # Use the raw URL for aaibaba.jpeg
    st.image("https://raw.githubusercontent.com/ShraddhaDarade/ShivanshPortfolio/main/aaibaba.jpeg")

with col4:
    st.title("My Mom and Dad")
    content2 = """
    My Aai is a computer engineer, and she works at IBM. She’s so smart and always helps me learn new things. Aai also cooks the yummiest food for me—I love everything she makes! She gives me the best hugs, and I love her so much. 💖
    My Baba works at Alfa Laval. He’s super fun, and I love playing with him. We laugh a lot together, and he always makes me feel happy. Baba is so kind and the best dad ever. 💙
    I’m the luckiest kid to have such awesome parents! 😊
    """
    st.info(content2)
