import streamlit as st 
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, DuckDuckGoSearchRun, WikipediaQueryRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Set up page configuration
st.set_page_config(page_title="LangChain - AI Chatbot with Search", page_icon="🤖", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .assistant-bubble {
            background-color: #e8f5fe;
            padding: 10px;
            border-radius: 15px;
            margin-bottom: 10px;
            font-size: 1.1em;
            color: #2C3E50;
        }
        .user-bubble {
            background-color: #ffe8e8;
            padding: 10px;
            border-radius: 15px;
            margin-bottom: 10px;
            font-size: 1.1em;
            color: #2C3E50;
            text-align: right;
        }
        .title {
            font-size: 2.5em;
            color: #2E86C1;
            font-weight: bold;
        }
        .sidebar-title {
            font-size: 1.5em;
            color: #2E86C1;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for settings and information
st.sidebar.markdown("<div class='sidebar-title'>Settings</div>", unsafe_allow_html=True)
st.sidebar.markdown("Configure your API key and search preferences here.")
api_key = st.sidebar.text_input("Enter your Groq_API_Key:", type="password")

# Add a model selection dropdown in the sidebar
model_name = st.sidebar.selectbox(
    "Select a Model:",
    options=["Llama3-8b-8192", "GPT-3.5-turbo", "GroqL-2b", "ChatGroq-v1"], # Replace with actual model options available in Groq
    index=0
)

st.sidebar.markdown("---")

# Initialize API wrappers for Arxiv and Wikipedia
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Title and banner
st.markdown("<div class='title'>LangChain - Chat With Enhanced Search</div>", unsafe_allow_html=True)
st.image("https://source.unsplash.com/featured/?technology,ai", use_column_width=True)  # Add a tech-related banner image
st.markdown("""
### 🤖 Discover academic papers and general knowledge!
This interactive chatbot provides a seamless way to access Arxiv papers and Wikipedia information. Ask away and explore new insights!
""")
st.markdown("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I'm here to help you explore information. What can I assist you with today?"}
    ]

# Display chat history with custom styles
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.markdown(f"<div class='assistant-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# Handle user input
if prompt := st.chat_input(placeholder="Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user input with custom style
    st.markdown(f"<div class='user-bubble'>{prompt}</div>", unsafe_allow_html=True)
    
    # Set up language model and agent
    llm = ChatGroq(groq_api_key=api_key, model_name=model_name, streaming=True)
    tools = [arxiv, wiki]

    search_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True
    )

    # Run the search agent and display response
    with st.container():
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role': 'assistant', "content": response})

        # Display the assistant's response with custom style
        st.markdown(f"<div class='assistant-bubble'>{response}</div>", unsafe_allow_html=True)
