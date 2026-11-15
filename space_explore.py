
import streamlit as st
import pandas as pd

# App title
st.title("🚀 Space Explorer Adventure")

# Sidebar navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Navigate to:", ["Home", "Space Quiz", "Mission Planner"])

# Home Section
if choice == "Home":
    st.header("🌌 Welcome to Space Explorer Adventure!")
    st.write("""
        Embark on an interstellar journey!  
        - Take a fun Space Quiz.  
        - Plan your Space Mission.  
        Navigate through the sections using the sidebar.  
    """)

# Space Quiz Section
elif choice == "Space Quiz":
    st.header("🧑‍🚀 Test Your Space Knowledge")
    
    # Quiz questions
    st.subheader("Answer the following questions:")
    q1 = st.radio("Q1: What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars"])
    q2 = st.radio("Q2: Who was the first human to travel into space?", ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin"])
    q3 = st.radio("Q3: What galaxy do we live in?", ["Milky Way Galaxy","Andromeda Galaxy",  "Whirlpool Galaxy"])
    
    # Submit quiz answers
    if st.button("Submit Quiz"):
        score = 0
        score += 1 if q1 == "Jupiter" else 0
        score += 1 if q2 == "Yuri Gagarin" else 0
        score += 1 if q3 == "Milky Way Galaxy" else 0
        
        st.info(f"Your score is {score}/3. Great job!")
        
        # Display results in a table
        results = pd.DataFrame({
            "Question": ["Q1", "Q2", "Q3"],
            "Your Answer": [q1, q2, q3],
            "Correct Answer": ["Jupiter", "Yuri Gagarin", "Milky Way Galaxy"]
        })
        st.write("Quiz Results:")
        st.table(results)

# Mission Planner Section
elif choice == "Mission Planner":
    st.header("🛰️ Plan Your Space Mission")
    
    # Spacecraft name input
    spacecraft = st.text_input("Name your spacecraft:", "Star Explorer")
    
    # Space mission launch date
    launch_date = st.date_input("Select your mission launch date:")
    
    # Space mission launch time
    launch_time = st.time_input("Select your mission launch time:")
    
    # Select a spaceship type
    spaceship_type = st.selectbox("Choose your spaceship type:", ["Rocket", "Shuttle", "Space Station"])
    
    # Motivational space quote
    category = st.selectbox("Pick a motivational space quote:", ["Exploration", "Discovery", "Adventure"])
    quotes = {
        "Exploration": "To explore the universe is to explore ourselves.",
        "Discovery": "Discovery is seeing what everybody else has seen, and thinking what nobody else has thought.",
        "Adventure": "Space is an adventure worth taking."
    }
    st.write(f"Motivational Quote: '{quotes[category]}'")
    
    # Save Mission Button
    if st.button("Save Mission"):
        st.success(f"Your space mission '{spacecraft}' is planned for {launch_date} at {launch_time} on a {spaceship_type}!")

