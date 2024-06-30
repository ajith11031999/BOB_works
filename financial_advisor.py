# financial_advisor.py

import os
import yfinance as yf
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.chains import RetrievalQA

# Initialize OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "sk-proj-DfbTcn0Kc02holTywnR7T3BlbkFJcLbLxaeCKWSrtpnXPOwr")

# Load financial documents
def load_financial_documents():
    loader = DirectoryLoader('/path/to/financial_data', glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2048)
    texts = text_splitter.split_documents(documents)

    return texts

# Create embeddings and vector store
def create_vector_store(texts):
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=openai_api_key)
    persist_dir = 'financial_embeds'
    docsearch = Chroma.from_documents(texts, embeddings, persist_directory=persist_dir)
    return docsearch

# Build QA system
def build_qa_system(docsearch):
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4", temperature=0.7),
        chain_type='stuff',
        retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={'k': 5}, return_source_documents=True)
    )
    return qa

# Fetch real-time stock data using yfinance
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data

# Generate advisory based on customer and stock data
def generate_advisory(customer_data, stock_data):
    # Placeholder: Implement analysis logic based on customer and stock data
    advice = f"Based on your risk tolerance and current market trends, consider investing in {customer_data['investment_amount']} worth of {stock_data['symbol']}."
    explanation = f"This advice is generated considering the market volatility and your {customer_data['risk_tolerance']} risk tolerance."
    return advice, explanation
