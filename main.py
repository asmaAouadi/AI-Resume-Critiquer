import streamlit as st
import streamlit.components.v1 as components
import PyPDF2
import io
from langchain.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# ==== PAGE CONFIG + CUSTOM FONT ====
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="wide")
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}
/* Page background */
body {
    background-color: #f5f5f5;
}
/* Titles */
.title {
    font-size: 2.5rem;
    font-weight: bold;
    color: #3a3a3a;
    margin-bottom: 20px;
}
/* Subtitle */
.subtitle {
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 30px;
}
/* Upload + input fields */
section[data-testid="stFileUploader"] > label > div {
    background: #fafafa;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 15px;
}
input, textarea {
    border-radius: 8px !important;
    padding: 10px !important;
}
/* Buttons */
button[kind="primary"] {
    background-color: #6a0dad;
    border: none;
    border-radius: 10px;
    padding: 0.75rem 1.5rem;
    color: white;
    font-weight: 600;
}
button[kind="primary"]:hover {
    background-color: #8e44ad;
}
</style>
""", unsafe_allow_html=True)


llm = ChatOpenAI(
    openai_api_key = st.secrets["OPENAI_API_KEY"],
    openai_api_base="https://api.groq.com/openai/v1",
    model="llama3-8b-8192"
)

st.markdown("<div class='title'>📄 AI Resume Critiquer + 3D Experience</div>", unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])


with col1:
    st.markdown("### 🤖 AI Agent")
    spline_scene_url = "https://my.spline.design/genkubgreetingrobot-V26vBhza9Svv8xlUkmTPhsaF"
    components.html(
        f"""<iframe src="{spline_scene_url}" width="100%" height="450px" frameborder="0"></iframe>""",
        height=450
    )


with col2:
    st.markdown("### 📄 Resume Analysis Tool")
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    job_role = st.text_input("Enter the job role you're targeting (optional)")
    analyze = st.button("🔍 Analyze Resume")

    def extract_text_from_pdf(pdf_file):
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    def extract_text_from_file(file):
        if file.type == "application/pdf":
            return extract_text_from_pdf(io.BytesIO(file.read()))
        return file.read().decode("utf-8")

    if analyze and uploaded_file is not None:
        try:
            file_content = extract_text_from_file(uploaded_file)

            if not file_content.strip():
                st.error("❌ File does not have any content.")
                st.stop()

            prompt = f"""
            Please analyze this resume and provide constructive feedback. 
            Focus on:
            1. Content clarity and impact
            2. Skills presentation
            3. Experience descriptions
            4. Specific improvements for {job_role if job_role else 'general job applications'}
            
            Resume content:
            {file_content}
            """

            with st.spinner("⏳ Analyzing your resume..."):
                response = llm.invoke([
                    SystemMessage(content="You are an expert resume reviewer."),
                    HumanMessage(content=prompt)
                ])

            st.markdown("""
            <div style="background-color: #ffffff; border-radius: 10px; padding: 20px; 
                        box-shadow: 0px 0px 10px rgba(0,0,0,0.05); margin-top: 20px;">
                <h4 style="color: #6a0dad;">🧠 AI Feedback</h4>
                <div style="color: #333; line-height: 1.6;">
                    {}
                </div>
            </div>
            """.format(response.content), unsafe_allow_html=True)

            st.success("✅ Resume analyzed successfully!")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


st.markdown("""
<hr style="margin-top: 50px;">
<div style="text-align: center; color: gray;">
    Made with ❤️ by MorenaDev | Powered by Groq + Streamlit + Spline
</div>
""", unsafe_allow_html=True)
