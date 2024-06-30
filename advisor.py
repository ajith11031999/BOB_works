# advisor.py

import os
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class FinancialAdvisor:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=os.environ['OPENAI_API_KEY'])
        self.loader = DirectoryLoader('/content/drive/MyDrive/financial_data', glob="*.pdf", loader_cls=PyPDFLoader)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=2048)
        self.docsearch = None  # Will be initialized later

    def load_documents(self):
        documents = self.loader.load()
        texts = self.text_splitter.split_documents(documents)
        self.docsearch = Chroma.from_documents(texts, self.embeddings, persist_directory='financial_embeds')

    def generate_advisory(self, query):
        qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model="gpt-4", temperature=0.7),
            chain_type='stuff',
            retriever=self.docsearch.as_retriever(search_type="similarity", search_kwargs={'k': 5}, return_source_documents=True)
        )
        response = qa(query)
        return response
