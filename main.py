import streamlit as st
import os
import openai
import PyPDF2
from langchain.embeddings import OpenAIEmbeddings
from pdfminer.utils import open_filename
from langchain.vectorstores import Chroma
from langchain import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import VectorDBQA
from langchain.document_loaders import UnstructuredFileLoader, UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import nltk
from streamlit_chat import message


nltk.download("punkt")


def run_query_app():
    #openai_api_key = st.sidebar.text_input("OpenAI API Key", key="openai_api_key_input", type="password")

    # uploaded_file = st.file_uploader("Upload a file", type=['txt', 'pdf'], key="file_uploader")
    # if uploaded_file:
    #     # Save the uploaded file
    #     file_path = os.path.join('./uploaded_files', uploaded_file.name)
    #     with open(file_path, "wb") as f:
    #         f.write(uploaded_file.read())

        # Initialize OpenAIEmbeddings

        #os.environ['OPENAI_API_KEY'] = openai_api_key
        apiKey = "API_KEY"
        # Initialize OpenAIEmbeddings
        embeddings = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=apiKey)

        # Load the file as document
        # _, ext = os.path.splitext(file_path)
        # if ext == '.txt':
        #     loader = UnstructuredFileLoader(file_path)
        # elif ext == '.pdf':
        #     loader = UnstructuredPDFLoader(file_path)
        # else:
        #     st.write("Unsupported file format.")
        #     return
        loader = UnstructuredFileLoader("/1706.03762.pdf")
        documents = loader.load()

        # Split the documents into texts
        text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)

        # Create Chroma vectorstore from documents
        doc_search = Chroma.from_documents(texts, embeddings)

        # Initialize VectorDBQA
        chain = VectorDBQA.from_chain_type(llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=apiKey), chain_type="stuff", vectorstore=doc_search)

        input = st.text_input("Say anything")
        output = chain.run(input)
        print(output)
if __name__ == '__main__':
    run_query_app()
