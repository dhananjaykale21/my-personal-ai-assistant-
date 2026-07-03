import streamlit as st
from difflib import get_close_matches
from datetime import datetime, date
from zoneinfo import ZoneInfo
import random

from knowledge import knowledge


# ==========================
# BASIC ASSISTANT RESPONSES
# ==========================
def get_basic_response(question):

    q = question.lower().strip()

    # Greetings
    if q in [
        "hi",
        "hello",
        "hey",
        "hello assistant",
        "hello ai",
        "hello pa",
        "good morning",
        "good afternoon",
        "good evening"
    ]:

        return random.choice([
            "Hello Dhananjay! 👋 How can I help you today?",
            "Hi Dhananjay! 🚀 What would you like to work on today?",
            "Welcome back, Dhananjay! 😊 How may I assist you?",
            "Hey Dhananjay! Ready to build something awesome today?"
        ])

    # How are you
    if "how are you" in q:

        return (
            "I'm doing great, Dhananjay! 😊\n\n"
            "Ready to help with cloud, AI, coding, "
            "projects, learning, or anything else."
        )

    # Date
    if q in ["date", "today date", "what is today's date"]:

        return datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).strftime(
            "📅 Today is %A, %d %B %Y."
        )

    # Time
    if q in ["time", "what time is it", "current time"]:

        return datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).strftime(
            "🕒 The current time is %I:%M %p IST."
        )

    # Day
    if q in ["day", "what day is today"]:

        return datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).strftime(
            "📆 Today is %A."
        )

    # Age
    if "how old am i" in q or "my age" in q:

        birth = date(2000, 1, 4)
        today = date.today()

        age = (
            today.year
            - birth.year
            - ((today.month, today.day) < (birth.month, birth.day))
        )

        return f"You are {age} years old."

    # About me
    if q in ["who am i", "tell me about me"]:

        return knowledge.get(
            "bio",
            "You are Dhananjay Kale."
        )

    # Hobbies
    if "hobbies" in q:

        return (
            "🎯 Your hobbies:\n\n• "
            + "\n• ".join(knowledge["hobbies"])
        )

    # Goals
    if "goals" in q:

        return (
            "🚀 Your goals:\n\n• "
            + "\n• ".join(knowledge["goals"])
        )

    # Skills
    if "skills" in q:

        return (
            "💻 Your skills:\n\n• "
            + "\n• ".join(knowledge["skills"])
        )

    # Projects
    if "projects" in q:

        return (
            "🛠️ Your projects:\n\n• "
            + "\n• ".join(knowledge["projects"])
        )

    # Certifications
    if "certifications" in q:

        return (
            "🏆 Your certifications:\n\n• "
            + "\n• ".join(knowledge["certifications"])
        )

    # Thanks
    if q in ["thanks", "thank you"]:

        return "You're welcome, Dhananjay! 😊"

    # Bye
    if q in ["bye", "goodbye", "see you"]:

        return "Goodbye Dhananjay! 👋 Have a wonderful day."

    # Help
    if q in ["help", "what can you do"]:

        return """
I can help you with:

• Personal information
• Skills and certifications
• Hobbies and goals
• Projects
• Date and time
• Friendly conversations

Soon, I'll be connected to GPT or Gemini so I can answer almost anything naturally.
"""

    return None


# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Dhananjay AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================
# CSS
# ==========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(
        circle at center,
        #101a40 0%,
        #050816 70%
    );
    color: white;
}

section[data-testid="stSidebar"] {
    background: rgba(18,18,25,0.9);
    border-right: 1px solid #2a2d35;
}

.chat-title {
    font-size: 52px;
    text-align: center;
    margin-top: 120px;
    font-weight: 300;
}

.gradient-text {
    background: linear-gradient(
        90deg,
        #79b8ff,
        #9b8cff,
        #ff8fd8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #a0a0a0;
    font-size: 20px;
    margin-bottom: 40px;
}

</style>
""", unsafe_allow_html=True)


# ==========================
# SIDEBAR
# ==========================
with st.sidebar:

    st.title("✨ Dhananjay AI")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### Recent")

    chats = [
        "Personal AI",
        "Cloud Learning",
        "Kubernetes",
        "Terraform",
        "Projects"
    ]

    for chat in chats:
        st.button(chat, use_container_width=True)

    st.divider()

    st.caption("Dhananjay Kale")
    st.caption("Cloud DevOps Engineer")


# ==========================
# SESSION STATE
# ==========================
if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================
# HOME PAGE
# ==========================
if len(st.session_state.messages) == 0:

    st.markdown("""
    <div class='chat-title'>
        Hello,
        <span class='gradient-text'>
            Dhananjay
        </span>
    </div>

    <div class='subtitle'>
        How can I help you today?
    </div>
    """, unsafe_allow_html=True)

else:

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


# ==========================
# USER INPUT
# ==========================
question = st.chat_input(
    "Ask me anything..."
)


# ==========================
# CHAT LOGIC
# ==========================
if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    answer = get_basic_response(question)

    if answer is None:

        q = question.lower().strip()

        if q in knowledge:

            answer = knowledge[q]

            if isinstance(answer, list):
                answer = "• " + "\n• ".join(answer)

            elif isinstance(answer, dict):
                answer = "\n".join(
                    [f"**{k}:** {v}" for k, v in answer.items()]
                )

        else:

            match = get_close_matches(
                q,
                knowledge.keys(),
                n=1,
                cutoff=0.5
            )

            if match:

                answer = knowledge[match[0]]

                if isinstance(answer, list):
                    answer = "• " + "\n• ".join(answer)

                elif isinstance(answer, dict):
                    answer = "\n".join(
                        [f"**{k}:** {v}" for k, v in answer.items()]
                    )

            else:

                answer = (
                    "I don't know that yet, Dhananjay. "
                    "Teach me something new! 😊"
                )

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()