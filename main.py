import os
import PyPDF2
from openai import OpenAI
import langchain.chains as lc
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI as LangChainOpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY","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")

# Initialize the LangChain OpenAI model
openai_model = LangChainOpenAI(api_key=OPENAI_API_KEY)

# Set up memory
memory = ConversationBufferMemory()
# Create a ConversationChain with the OpenAI model and memory
conversation_chain = lc.ConversationChain(llm=openai_model, memory=memory)

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def chunk_pdf_text(pdf_text, max_length=2000):
    words = pdf_text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 > max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            current_chunk.append(word)
            current_length += len(word) + 1

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
# Function to estimate the token count
def estimate_token_count(text):
    return len(text.split())
# Function to ask OpenAI a question based on the PDF text
def ask_openai_with_pdf_context(question, pdf_text_chunks, conversation_chain):
    for chunk in pdf_text_chunks:
        if estimate_token_count(question + chunk) < 4097:
            prompt = f"Question about Rowan University: {question}\n\nPDF Content:\n{chunk}\n\nAnswer:"
            response = conversation_chain.run(prompt).strip()
            if is_response_adequate(response, chunk):
                return response

    return "I don't have information about that."
# Function to check if the response is adequately addressing the question
def is_response_adequate(response, pdf_text):
    # Simple heuristic: check if response contains some keywords from the PDF
    # This logic can be improved for better accuracy
    keywords = pdf_text.split()[:100]  # Example: Use the first 100 words of the PDF as keywords
    return any(keyword.lower() in response.lower() for keyword in keywords)

# Modified conversation function
def chat_with_gpt_langchain(prompt, pdf_text, conversation_chain):
    response = ask_openai_with_pdf_context(prompt, pdf_text, conversation_chain)
    return response

if __name__ == "__main__":
    # Extract text from the PDF file
    pdf_file_path = "/Users/blenbegashaw/PycharmProjects/pythonProject1/Scraped Articles.pdf"
    pdf_text = extract_text_from_pdf(pdf_file_path)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt_langchain(user_input, pdf_text, conversation_chain)
        print("Chatbot: ", response)
