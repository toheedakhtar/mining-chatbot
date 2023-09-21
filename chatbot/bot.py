# import os
# from langchain.chains.question_answering import load_qa_chain 
# from langchain.text_splitter import CharacterTextSplitter
# from langchain import PromptTemplate
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.llms import OpenAI
# # from langchain.chat_models import ChatOpenAI
# from dotenv import load_dotenv
# from PyPDF2 import PdfReader
# # import time



# load_dotenv()

# def get_text_from_pdf(pdf):
#     with open(pdf, "rb") as file:
#         pdf_reader = PdfReader(file)
#         text = ""
#         for i in range(len(pdf_reader.pages)):    # i = page num
#             text += pdf_reader.pages[i].extract_text()
#         return text

# def get_text(file):
#     with open(file, "r") as file:
#         text = file.read()
#     return text

# def get_text_from_all_files(dir):
#     text_all = ""
#     for files in os.listdir(dir):
#         file_path = os.path.join(dir, files)
#         if files.endswith(".pdf"):
#             text_all += get_text_from_pdf(file_path)
#         elif files.endswith(".txt"):
#             text_all += get_text(file_path)
        
#     return text_all

# def answer(question):
#     files_dir = 'chatbot/docs/'    #data to train on (pdfs or text)
#     text = get_text_from_all_files(files_dir)  

#     # splitting text into chunks as OpenAI has limit of ~4100 tokens
#     text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
#     text_chunks = text_splitter.split_text(text)

#     embeddings = OpenAIEmbeddings()
#     vector_text = FAISS.from_texts(text_chunks, embeddings)
#     # time.sleep(4)

#     llm = OpenAI()
#     chain = load_qa_chain(llm, chain_type="stuff")

#     docs = vector_text.similarity_search(question)
#     response = chain.run(input_documents=docs, question=question)
#     return response