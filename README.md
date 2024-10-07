LangChain - AI Chatbot with Enhanced Search

This project is a Streamlit-based chatbot application powered by LangChain, which integrates various APIs, including Arxiv and Wikipedia, to provide users with quick access to academic papers and general knowledge. The chatbot leverages Groq's language models to respond interactively to user queries.
Features

    API Integration: Access Arxiv papers and Wikipedia articles in real-time.
    Model Selection: Choose from available Groq models (e.g., Llama3-8b-8192, GPT-3.5-turbo, GroqL-2b, and ChatGroq-v1).
    Customizable UI: Styled user and assistant chat bubbles for a better user experience.
    Streamlined Search: Execute searches and receive academic and general knowledge insights seamlessly.

Requirements

    Python 3.7+
    Streamlit
    LangChain
    dotenv (for managing API keys securely)

    Setup Instructions
1. Create a Virtual Environment

Set up a virtual environment using Conda or the Python venv module.
Using Conda:

conda create -n langchain-chatbot python=3.8
conda activate langchain-chatbot

Or using venv:
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

2. Install Dependencies

Ensure you have all the required packages by running:

pip install -r requirements.txt

Here's a README.md file for the code:
LangChain - AI Chatbot with Enhanced Search

This project is a Streamlit-based chatbot application powered by LangChain, which integrates various APIs, including Arxiv and Wikipedia, to provide users with quick access to academic papers and general knowledge. The chatbot leverages Groq's language models to respond interactively to user queries.
Features

    API Integration: Access Arxiv papers and Wikipedia articles in real-time.
    Model Selection: Choose from available Groq models (e.g., Llama3-8b-8192, GPT-3.5-turbo, GroqL-2b, and ChatGroq-v1).
    Customizable UI: Styled user and assistant chat bubbles for a better user experience.
    Streamlined Search: Execute searches and receive academic and general knowledge insights seamlessly.

Requirements

    Python 3.7+
    Streamlit
    LangChain
    dotenv (for managing API keys securely)

Setup Instructions
1. Create a Virtual Environment

Set up a virtual environment using Conda or the Python venv module.

Using Conda:

bash

conda create -n langchain-chatbot python=3.8
conda activate langchain-chatbot

Or using venv:

bash

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

2. Install Dependencies

Ensure you have all the required packages by running:

bash

pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file in the project directory and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here
4. Run the Application

Start the Streamlit application by running:
streamlit run app.py

Usage

    Enter your API key and select a model from the sidebar.
    Type your query into the chat input box, and the assistant will provide relevant information from Arxiv and Wikipedia.

Enjoy exploring academic knowledge and general information through a responsive, interactive chatbot!




    
