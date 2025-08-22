# PDF RAG Hugging Face and Langchain

A simple Retrieval-Augmented Generation (RAG) app that lets you upload PDFs, indexes them into a local ChromaDB using Sentence-Transformer embeddings, retrieves the most relevant chunks, and generates answers with a Hugging Face text2text model.

## Features
- Multiple PDF upload and parsing via `pypdf`
- Character-based chunking with overlap
- Embeddings from `sentence-transformers` (default: `all-MiniLM-L6-v2`)
- Generation via Hugging Face `pipeline("text2text-generation")` (default: `facebook/bart-large-cnn`)
- Gradio UI 

## Quickstart

### 1) Create and activate a virtual environment (optional but recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

> **Tip:** If PyTorch wheels fail to install automatically on your system, please follow the official instructions for your platform: https://pytorch.org/get-started/locally/

Then open the local URL shown in the terminal.

### 4) Use it
- Upload one or more PDF files
- Click **Index PDFs**
- Type a question and click **Get Answer**
- Inspect retrieved chunks to validate grounding

## Notes & Options

- **Embedding model**: Change in the Streamlit sidebar (e.g., `sentence-transformers/all-MiniLM-L6-v2`, `all-mpnet-base-v2`, etc.).
- **Generation model**: Also configurable (e.g., `facebook/bart-large-cnn`). Larger models may require a GPU and more RAM/VRAM.
- **Security**: This is a local demo. Do not expose it to the public without proper hardening.

## Troubleshooting

- **Torch install issues**: See the PyTorch website for platform-specific wheel commands.
- **CUDA/CPU mismatch**: If you do not have a GPU, everything should still run on CPU (slower). Consider smaller models.
- **Poor answers**: Increase Top-K, adjust chunk size/overlap, try a better embedding model, or switch to a stronger generator.

## License
MIT
