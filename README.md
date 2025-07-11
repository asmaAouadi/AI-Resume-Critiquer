# AI-Resume-Critiquer
<img width="914" height="425" alt="image" src="https://github.com/user-attachments/assets/d3d02b31-072c-4c65-915f-785dde2713d0" />

A modern, interactive AI-powered app that reviews and improves resumes. Built with **Streamlit**, **LangChain**, and **Groq’s LLaMA 3**, featuring a 3D animated agent via **Spline** for a more engaging user experience.

---

### 🚀 Features

* 📤 Upload your resume in PDF format
* 🧠 Get detailed AI feedback on:

  * Clarity and impact
  * Skills and experience presentation
  * Tailored advice for specific job roles
* 🌍 Multilingual feedback support *(coming soon)*
* 🤖 Interactive 3D agent (Spline)
* ⚡ Powered by [Groq](https://groq.com/) LLMs for blazing-fast responses

---

### 🛠 Tech Stack

| Technology    | Usage                        |
| ------------- | ---------------------------- |
| **Streamlit** | Web UI                       |
| **Groq API**  | LLaMA 3 inference            |
| **LangChain** | LLM message handling         |
| **PyPDF2**    | Resume (PDF) text extraction |
| **Spline**    | 3D assistant embedded        |

---

### 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/asmaAouadi/AI-Resume-Critiquer.git
cd AI-Resume-Critiquer
```

2. **(Optional) Create a virtual environment**:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set your secrets**
   Create a `.streamlit/secrets.toml` file with your Groq API key:

```toml
OPENAI_API_KEY = "your_groq_api_key_here"
```

---

### ▶️ Run the App

```bash
streamlit run main.py
```

---

### 🌐 Deployment

You can deploy it to:

* **Streamlit Cloud** (recommended)
* **Netlify** (via CLI and serverless setup)
* **Render** or **Vercel**

---

### 🧪 Coming Features

* 🌍 Language selector for multilingual feedback
* 📁 Support for DOCX files
* 🪄 Resume improvement suggestions
* 💡 Smart job-matching tips

---

### 📃 License

This project is licensed under the [MIT License](LICENSE).
© 2025 MorenaDev

---
