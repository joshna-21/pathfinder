import streamlit as st
from logic import get_recommendations

st.set_page_config(page_title="PathFinder", page_icon="🧭")
st.title("🧭 PathFinder — Career & Migration Assistant")
st.markdown("Welcome! I’ll help you discover job opportunities and migration paths based on your skills and goals.")

with st.sidebar:
    st.title("About")
    st.markdown("""
    PathFinder is an AI chatbot that gives:
    - 🎯 Career suggestions
    - ✈️ Visa guidance
    - 📚 Learning resources
    - 🤖 Smart replies based on your profile
    """)

st.subheader("🌍 Select Your Target Country")
country = st.selectbox("Choose a country you're interested in:", ["UK", "Canada", "Germany"])

st.subheader("🛠️ Select Your Skills")
skills = st.multiselect(
    "Pick your current skills:",
    ["Python", "SQL", "Power BI", "Excel", "Docker", "Django", "Figma", "German A2", "CAD", "HTML/CSS"]
)

if st.button("🔍 Find Recommendations"):
    if country and skills:
        result = get_recommendations(country, skills)
        st.markdown(result)
    else:
        st.warning("Please select a country and at least one skill.")
