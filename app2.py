import os
from langchain.chains.question_answering import load_qa_chain 
from langchain.text_splitter import CharacterTextSplitter
from langchain import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from dotenv import load_dotenv
from PyPDF2 import PdfReader


load_dotenv()

def get_text_from_pdf(pdf):
    with open(pdf, "rb") as file:
        pdf_reader = PdfReader(file)
        text = ""
        for i in range(len(pdf_reader.pages)):    # i = page num
            text += pdf_reader.pages[i].extract_text()
        return text

def get_text(file):
    with open(file, "r") as file:
        text = file.read()
    return text

def get_text_from_all_files(dir):
    text_all = ""
    for files in os.listdir(dir):
        file_path = os.path.join(dir, files)
        if files.endswith(".pdf"):
            text_all += get_text_from_pdf(file_path)
        elif files.endswith(".txt"):
            text_all += get_text(file_path)
        
    return text_all


files_dir = './docs/'    #data to train on (pdfs or text)
text = get_text_from_all_files(files_dir)  

# splitting text into chunks as OpenAI has limit of ~4100 tokens
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
text_chunks = text_splitter.split_text(text)
# print(text_chunks)

embeddings = OpenAIEmbeddings()

docsearch = FAISS.from_texts(text_chunks, embeddings)
# print(docsearch)

llm = OpenAI()
chain = load_qa_chain(llm, chain_type="stuff")

# template = """ Answer the question based on the context below. If the
# question cannot be answered using the information provided answer
# with "Sorry, I don't know."

# Context: In this question is being asked by a someone working in the mining
# industry. he/she asks a query and according to data provided you have to answer the query 

# Question: {question}

# Answer: """

# prompt = PromptTemplate(
#     input_variables=["question"],
#     template=template

# )

question = input("Enter your question: \n")


docs = docsearch.similarity_search(question)
response = chain.run(input_documents=docs, question=question)
print(response)