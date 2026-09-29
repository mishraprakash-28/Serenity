import importlib

st = importlib.import_module("streamlit")
from google import genai
import os

# Page Configuration
st.set_page_config(
    page_title="Serenify - Mental Well-Being Platform",
    page_icon="🌿",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main-title {
        color: #2c5e55;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .sub-title {
        text-align: center;
        color: #555;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #2c5e55;
        color: white;
        border-radius: 8px;
    }
    .helpline-box {
        background-color: #ffebee;
        border-left: 5px solid #e53935;
        padding: 1rem;
        margin-top: 1rem;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 class='main-title'>🌿 Serenify</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>A Safe Space for Your Mental Well-Being</p>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🤖 AI Assistant (SereneBot)", 
    "📚 Information", 
    "👨‍⚕️ Find Support", 
    "🎧 Calming Music", 
    "🚨 Helplines"
])

# ---------------------------------------------------------
# TAB 1: AI Assistant
# ---------------------------------------------------------
with tab1:
    st.header("AI Mental Health Companion")
    st.write("Apne stress, anxiety, ya thoughts share karein. Yeh AI ek supportive companion ki tarah guide karega.")
    
    api_key = os.getenv("GEMINI_API_KEY") or st.sidebar.text_input("Enter Gemini API Key:", type="password")

    if api_key:
        try:
            client = genai.Client(api_key=api_key)

            if "messages" not in st.session_state:
                st.session_state.messages = [
                    {"role": "assistant", "content": "Namaste! Main Serenify ka AI assistant hoon. Aaj aap kaisa feel kar rahe hain?"}
                ]

            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])

            if user_prompt := st.chat_input("Apni baat yahan likhein..."):
                st.session_state.messages.append({"role": "user", "content": user_prompt})
                st.chat_message("user").write(user_prompt)

                system_instruction = (
                    "You are Serenify AI, a compassionate and empathetic mental health companion. "
                    "Provide gentle, supportive, and practical wellness advice. "
                    "Do NOT give official medical diagnoses or prescribe medication. "
                    "Always remind users that you are an AI and encourage them to seek professional help if needed."
                )

                full_prompt = f"{system_instruction}\n\nUser: {user_prompt}"

                with st.spinner("SereneBot soch raha hai..."):
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=full_prompt
                    )
                    bot_reply = response.text
                    
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                st.chat_message("assistant").write(bot_reply)

        except Exception as e:
            st.error(f"Error initializing Gemini API: {e}")
    else:
        st.info("AI Chatbot use karne ke liye sidebar me Gemini API Key enter karein.")

# ---------------------------------------------------------
# TAB 2: Mental Health Information
# ---------------------------------------------------------
with tab2:
    st.header("Mental Health Information")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Understanding Stress")
        st.write("Stress ek normal reaction hai. Regular breaks aur breathing exercises se isse balance kiya ja sakta hai.")
        
    with col2:
        st.subheader("Managing Anxiety")
        st.write("Anxiety feel hone par deep breathing aur grounding techniques try karein.")
        
    with col3:
        st.subheader("Overcoming Loneliness")
        st.write("Doston ya trusted logo se connect rahein aur self-care routines follow karein.")

# ---------------------------------------------------------
# TAB 3: Professional Support Directory
# ---------------------------------------------------------
with tab3:
    st.header("Find Professional Support")
    
    professionals = [
        {"Name": "Dr. Ananya Sharma", "Role": "Clinical Psychologist", "City": "Delhi", "Specialty": "Anxiety & Stress"},
        {"Name": "Counselor Rahul Verma", "Role": "Student Counselor", "City": "Mumbai", "Specialty": "Academic Stress"},
        {"Name": "Serene Mind Clinic", "Role": "Wellness Center", "City": "Ahmedabad", "Specialty": "Therapy & Counseling"},
        {"Name": "Dr. Pooja Mehta", "Role": "Psychiatrist", "City": "Bangalore", "Specialty": "Depression & Mood Shifts"}
    ]
    search_query = st.text_input("City ya Specialty dwara search karein:")

    if search_query:
        query = search_query.casefold()
        filtered_professionals = [
            professional
            for professional in professionals
            if any(query in str(value).casefold() for value in professional.values())
        ]
        st.dataframe(filtered_professionals, use_container_width=True)
    else:
        st.dataframe(professionals, use_container_width=True)

# ---------------------------------------------------------
# TAB 4: Calming Audio & Activities
# ---------------------------------------------------------
with tab4:
    st.header("Calming Activities & Audio")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("🌊 Ocean Waves")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    with col_b:
        st.subheader("🌧️ Rainfall Sounds")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")

# ---------------------------------------------------------
# TAB 5: Emergency Helplines
# ---------------------------------------------------------
with tab5:
    st.header("Emergency Support & Helplines")
    st.markdown("""
        <div class="helpline-box">
            <h3>KIRAN Mental Health Helpline (India)</h3>
            <p><b>Toll-Free Number:</b> 1800-599-0019 (24/7 Available)</p>
        </div>
        <br>
        <div class="helpline-box">
            <h3>Tele-MANAS</h3>
            <p><b>Toll-Free Number:</b> 14416 or 1800-891-4416</p>
        </div>
    """, unsafe_allow_html=True)

st.sidebar.title("About Serenify")
st.sidebar.info("Serenify ek educational aur supportive platform hai. Yeh kisi medical diagnosis ya emergency line ka replacement nahi hai.")