<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Serenify - Mental Well-Being Platform</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f4f8f8;
            color: #333;
            line-height: 1.6;
        }

        /* Navbar */
        header {
            background-color: #2c5e55;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        header h1 {
            font-size: 1.5rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 1.5rem;
            font-weight: 500;
        }

        nav a:hover {
            text-decoration: underline;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #e0f2f1, #b2dfdb);
            padding: 4rem 2rem;
            text-align: center;
        }

        .hero h2 {
            font-size: 2.5rem;
            color: #1b4d3e;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 1.5rem auto;
            color: #444;
        }

        .btn {
            background-color: #2c5e55;
            color: white;
            padding: 0.7rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            text-decoration: none;
        }

        .btn:hover {
            background-color: #1e403a;
        }

        /* Main Container */
        .container {
            max-width: 1100px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        section {
            background: white;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        section h2 {
            color: #2c5e55;
            margin-bottom: 1rem;
            border-bottom: 2px solid #e0f2f1;
            padding-bottom: 0.5rem;
        }

        /* Card Grid */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-top: 1rem;
        }

        .card {
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            padding: 1.5rem;
            background-color: #fafafa;
        }

        .card h3 {
            color: #1b4d3e;
            margin-bottom: 0.5rem;
        }

        /* Search Input */
        .search-box {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-bottom: 1rem;
            font-size: 1rem;
        }

        /* Helpline Alert */
        .helpline-box {
            background-color: #ffebee;
            border-left: 5px solid #e53935;
            padding: 1rem;
            margin-top: 1rem;
            border-radius: 4px;
        }

        footer {
            text-align: center;
            padding: 1.5rem;
            background-color: #2c5e55;
            color: white;
            margin-top: 2rem;
        }
    </style>
</head>
<body>

    <!-- Header / Navigation -->
    <header>
        <h1>Serenify</h1>
        <nav>
            <a href="#home">Home</a>
            <a href="#info">Information</a>
            <a href="#directory">Find Support</a>
            <a href="#music">Calming Music</a>
            <a href="#helpline">Helplines</a>
        </nav>
    </header>

    <!-- Hero Section -->
    <div class="hero" id="home">
        <h2>A Safe Space for Your Mental Well-Being</h2>
        <p>Simple, reliable information and accessible mental health support resources whenever you need them.</p>
        <a href="#directory" class="btn">Find Professional Help</a>
    </div>

    <div class="container">

        <!-- Mental Health Information Section -->
        <section id="info">
            <h2>Mental Health Information</h2>
            <p>Understand your emotional well-being with basic, verified information.</p>
            <div class="grid">
                <div class="card">
                    <h3>Understanding Stress</h3>
                    <p>Stress is a normal body reaction to challenges. Learn healthy ways to manage day-to-day pressure.</p>
                </div>
                <div class="card">
                    <h3>Managing Anxiety</h3>
                    <p>Anxiety involves feeling fearful or nervous. Deep breathing and grounding exercises can help.</p>
                </div>
                <div class="card">
                    <h3>Overcoming Loneliness</h3>
                    <p>Feeling disconnected is common. Building small daily social routines can improve your mood.</p>
                </div>
            </div>
        </section>

        <!-- Find a Professional Section -->
        <section id="directory">
            <h2>Find Support</h2>
            <p>Search verified counselors, psychologists, and health clinics.</p>
            <input type="text" id="searchInput" class="search-box" placeholder="Search by city or specialty (e.g., Counselor, Delhi)..." onkeyup="filterDirectory()">
            
            <div class="grid" id="directoryGrid">
                <div class="card professional-card">
                    <h3>Dr. Ananya Sharma</h3>
                    <p><strong>Role:</strong> Clinical Psychologist</p>
                    <p><strong>Location:</strong> Delhi / Online</p>
                    <p><strong>Focus:</strong> Anxiety, Stress Management</p>
                </div>
                <div class="card professional-card">
                    <h3>Counselor Rahul Verma</h3>
                    <p><strong>Role:</strong> Student Counselor</p>
                    <p><strong>Location:</strong> Mumbai / Online</p>
                    <p><strong>Focus:</strong> Academic Stress, Career Guidance</p>
                </div>
                <div class="card professional-card">
                    <h3>Serene Mind Clinic</h3>
                    <p><strong>Role:</strong> Wellness Center</p>
                    <p><strong>Location:</strong> Ahmedabad</p>
                    <p><strong>Focus:</strong> General Counseling & Therapy</p>
                </div>
            </div>
        </section>

        <!-- Calming Music / Audio Section -->
        <section id="music">
            <h2>Calming Activities & Audio</h2>
            <p>Listen to relaxing sounds to soothe your mind during stressful moments.</p>
            <div class="grid">
                <div class="card">
                    <h3>Ocean Waves</h3>
                    <audio controls style="width: 100%; margin-top: 10px;">
                        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </div>
                <div class="card">
                    <h3>Rainfall Sound</h3>
                    <audio controls style="width: 100%; margin-top: 10px;">
                        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </div>
            </div>
        </section>

        <!-- Support & Helplines Section -->
        <section id="helpline">
            <h2>Emergency Support & Helplines</h2>
            <p>If you or someone you know needs immediate assistance, please reach out to these resources.</p>
            <div class="helpline-box">
                <h3>KIRAN Mental Health Helpline (India)</h3>
                <p><strong>Toll-Free Number:</strong> 1800-599-0019 (24/7 Available)</p>
            </div>
            <div class="helpline-box" style="margin-top: 10px;">
                <h3>Tele-MANAS</h3>
                <p><strong>Toll-Free Number:</strong> 14416 or 1800-891-4416</p>
            </div>
        </section>

    </div>

    <footer>
        <p>&copy; 2026 Serenify. Designed for Mental Well-Being Support.</p>
    </footer>

    <!-- JavaScript Filter Functionality -->
    <script>
        function filterDirectory() {
            let input = document.getElementById('searchInput').value.toLowerCase();
            let cards = document.getElementsByClassName('professional-card');

            for (let i = 0; i < cards.length; i++) {
                let cardText = cards[i].innerText.toLowerCase();
                if (cardText.includes(input)) {
                    cards[i].style.display = "";
                } else {
                    cards[i].style.display = "none";
                }
            }
        }
    </script>
</body>
</html>

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
