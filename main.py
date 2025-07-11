import streamlit as st
import PyPDF2
import io
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"], #for safer use
    openai_api_base="https://api.groq.com/openai/v1",
    model="llama3-8b-8192"  
)

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume in PDF format and get feedback on how to improve it.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_role = st.text_input("Enter the job role you're targetting (optional)")
analyze = st.button("Analyse Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(file.read()))
    return file.read().decode("utf-8")

if analyze and uploaded_file is not None:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations."""

        response = llm.invoke([
            SystemMessage(content="You are an expert resume reviewer."),
            HumanMessage(content=prompt)
        ])


        st.markdown("### Analysis Result")
        st.markdown(response.content)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")
