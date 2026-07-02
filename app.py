import streamlit as st
from difflib import get_close_matches

st.set_page_config(
    page_title="Dhananjay AI",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0b0f19;
}

.stChatMessage {
    border-radius: 18px;
    padding: 12px;
}

.user-msg {
    background: #1f2937;
    color: white;
    padding: 12px;
    border-radius: 16px;
    margin: 8px 0;
}

.bot-msg {
    background: linear-gradient(90deg,#4f46e5,#7c3aed);
    color: white;
    padding: 12px;
    border-radius: 16px;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

knowledge = {
    "who is dhananjay":
        "Dhananjay Kale is a Cloud DevOps Engineer at Henkel dx with 4.5 years of experience in Azure, GCP, Kubernetes, Terraform, and DevOps automation.",

    "who is Nanjaiyan":
        "He is best brother of Dhananjay kale and soul mate of him lovely friend who add valaue in his every phase of life !!.",

    "azure":
        "Dhananjay works extensively with Azure Landing Zones, AKS, ACR, Private Endpoints, Backup, Monitoring, and Infrastructure Automation.",

    "skills":
        "Azure, GCP, Kubernetes, Docker, Terraform, Python, Bash, PowerShell, GitLab CI/CD, Prometheus, Grafana.",

    "experience":
        "Dhananjay has around 4.5 years of Cloud DevOps experience.",

    "projects":
        "Cloud Portal Automation, Backup Automation, IOC AI Assistant, Hostname Generator, and AI-powered internal tools."
}

st.title("🤖 Dhananjay AI")
st.caption("Your personal AI assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask me anything about Dhananjay...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    q = question.lower()

    if q in knowledge:
        answer = knowledge[q]
    else:
        match = get_close_matches(q, knowledge.keys(), n=1)
        answer = knowledge[match[0]] if match else "I don't know that yet."

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()