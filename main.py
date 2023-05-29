import os
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAIChat
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

llm = OpenAIChat()
embeddings = OpenAIEmbeddings()

loader = PyPDFLoader("terms.pdf")
pages = loader.load_and_split()

text ="""You are Nifty Bridge AI assistant. You have to introduce yourself as Nifty Bridge AI assistent. Use the following pieces of context to answer the users question. 
If you cannot answer, just say ""I don't know please contact with support by email support@nifty-bridge.com", don't try to make up an answer."""
for page in pages:
    text += f'{page.page_content}\n'

text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
chunks = text_splitter.split_text(text)


knowledge_base = FAISS.from_texts(chunks, embeddings)


def openai_answers(message):
    user_question = message
    docs = knowledge_base.similarity_search(user_question)
    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=user_question)
    
    return response






