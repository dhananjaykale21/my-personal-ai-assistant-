import streamlit as st
from difflib import get_close_matches
from knowledge import knowledge

st.set_page_config(
    page_title="Dhananjay AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
    background:
        radial-gradient(circle at center,
        rgba(27,48,115,.45),
        #050816 65%);
    color:white;
}

section[data-testid="stSidebar"]{
    background:#16181d;
    border-right:1px solid #2a2d35;
}

.chat-title{
    font-size:52px;
    text-align:center;
    margin-top:120px;
    color:#f4f4f4;
    font-weight:300;
}

.gradient-text{
    background:linear-gradient(
        90deg,
        #79b8ff,
        #9b8cff,
        #ff8fd8
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    text-align:center;
    color:#a0a0a0;
    font-size:20px;
    margin-bottom:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:

    st.title("✨ Dhananjay AI")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []

    st.text_input(
        "Search chats",
        placeholder="Search..."
    )

    st.divider()

    st.markdown("### Recent")

    chats = [
        "Cloud Automation",
        "AKS Setup",
        "Backup Strategy",
        "Terraform Notes",
        "AI Assistant"
    ]

    for c in chats:
        st.button(c, use_container_width=True)

    st.divider()

    st.caption("Dhananjay Kale")
    st.caption("Cloud DevOps Engineer")

# ---------- MAIN ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:

    st.markdown(
        """
        <div class='chat-title'>
        Hello, <span class='gradient-text'>
        Dhananjay
        </span>
        </div>

        <div class='subtitle'>
        What would you like to build today?
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

question = st.chat_input(
    "Ask about life, cloud, projects, DevOps or anything..."
)

if question:

    st.session_state.messages.append(
        {"role":"user","content":question}
    )

    q = question.lower()

    if q in knowledge:
        answer = knowledge[q]

    else:
        match = get_close_matches(
            q,
            knowledge.keys(),
            n=1
        )

        answer = (
            knowledge[match[0]]
            if match
            else "I don't know that yet. Upload a document or teach me something new."
        )

    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

    st.rerun()