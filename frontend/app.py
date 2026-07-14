import streamlit as st
import requests
#backend BASE_URL
BASE_URL="http://127.0.0.1:8000"
# ------------------------------
# Session State Initialization
# ------------------------------

if "conversation" not in st.session_state:
    st.session_state.conversation = None

if "themes" not in st.session_state:
    st.session_state.themes = None

# ------------------------------
# Title
# ------------------------------

st.title("🤝 Personalized Networking Assistant")

# ------------------------------
# User Input
# ------------------------------

event_description = st.text_area(
    "Event Description",
    placeholder="Example: AI Conference focusing on Healthcare and Machine Learning"
)

user_interests = st.text_input(
    "Your Interests (comma separated)",
    placeholder="AI, Machine Learning, Healthcare"
)

# ------------------------------
# Generate Button
# ------------------------------

if st.button("Generate Conversation Starters"):

    # Clean user interests
    interests = [
        interest.strip()
        for interest in user_interests.split(",")
        if interest.strip()
    ]
    #json serialisation

    payload={
        "event_description":event_description,
        "user_interests":interests
    }
    #api call
    response = requests.post(f"{BASE_URL}/generate-conversation",json=payload)
    data = None
    if(response.status_code==200):
        data = response.json()
    else:
        st.error("Backend error")

    if(data!=None):
        # Save into session state
        st.session_state.themes = data["themes"]   
        st.session_state.conversation = data["conversation_starters"]

# ------------------------------
# Display Previous Results
# -----------------------------

if st.session_state.conversation:

    st.subheader("🎯 Detected Themes")

    for theme in st.session_state.themes:
        st.success(theme)

    st.divider()

    st.subheader("💬 Conversation Starters")

    for i, suggestion in enumerate(st.session_state.conversation):

        st.write(f"**{i+1}. {suggestion}**")

        col1, col2 = st.columns([1, 1])

        # -----------------------
        # Like Button
        # -----------------------

        with col1:

            if st.button("👍 Like", key=f"like_{i}"):

                payload = {
                    "suggestion": suggestion,
                    "action": "like"
                }

                response = requests.post(
                    f"{BASE_URL}/feedback",
                    json=payload
                )

                if response.status_code == 200:
                    st.success("Thanks for your feedback!")

                else:
                    st.error("Couldn't save feedback.")

        # -----------------------
        # Dislike Button
        # -----------------------

        with col2:

            if st.button("👎 Dislike", key=f"dislike_{i}"):

                payload = {
                    "suggestion": suggestion,
                    "action": "dislike"
                }

                response = requests.post(
                    f"{BASE_URL}/feedback",
                    json=payload
                )

                if response.status_code == 200:
                    st.success("Thanks for your feedback!")

                else:
                    st.error("Couldn't save feedback.")

        st.divider()
    # ----------------------------------------
# Fact Checking Section
# ----------------------------------------

st.markdown("---")

st.subheader("🔍 Wikipedia Fact Check")

statement = st.text_input(
    "Enter a statement to verify",
    placeholder="Example: TensorFlow was released in 2019"
)

if st.button("Verify Fact"):

    if statement.strip() == "":
        st.warning("Please enter a statement.")

    else:

        payload = {
            "input_text": statement
        }

        response = requests.post(
            f"{BASE_URL}/fact-check",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            st.success(result["verification_status"])

            if result["summary"]:
                st.write(result["summary"])

        else:

            st.error("Unable to verify the statement.")
# ---------------------------------------
# History Section
# ---------------------------------------

st.markdown("---")

st.subheader("📜 Previous Conversations")

if st.button("View Previous Conversations"):

    response = requests.get(f"{BASE_URL}/history")

    if response.status_code == 200:

        history = response.json()
        

        if not history:
            st.info("No conversation history available.")

        else:

            # Display only the last 5 conversations (newest first)
            for session in reversed(history[-5:]):

                st.markdown(f"### 📅 {session['timestamp']}")

                st.write("**Event Description:**")
                st.write(session["event-desc"])

                st.write("**User Interests:**")
                st.write(", ".join(session["user_interests"]))

                st.write("**Detected Themes:**")
                for theme in session["themes"]:
                    st.write(f"• {theme}")

                st.write("**Conversation Starters:**")
                for starter in session["conversation_Starters"]:
                    st.success(starter)

                st.markdown("---")

    else:

        st.error("Unable to load conversation history.")
# ---------------------------------------
# Feedback History
# ---------------------------------------

st.markdown("---")

st.subheader("📝 Feedback History")

if st.button("View Feedback History"):

    response = requests.get(f"{BASE_URL}/feedback")

    if response.status_code == 200:

        feedback = response.json()

        if not feedback:

            st.info("No feedback available.")

        else:

            # Show only last 10 feedback entries
            for item in reversed(feedback[-10:]):

                # Like / Dislike icon
                icon = "👍" if item["action"] == "like" else "👎"

                st.write(f"{icon} **{item['suggestion']}**")

                # Small timestamp
                st.caption(item["timestamp"])

                st.markdown("---")

    else:

        st.error("Unable to load feedback history.")