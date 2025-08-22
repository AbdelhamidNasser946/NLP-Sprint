# Text Summarization & Question-Answering Web App

An interactive web application for text summarization and question answering, powered by state-of-the-art language models and a user-friendly Gradio interface.

---

## ​​ Features

- **Text Summarization**: Generate concise and coherent summaries of input text.
- **Question Answering**: Ask questions about the text and receive accurate responses.
- **Interactive Web Interface**: Built using **Gradio** to provide a smooth, web-based user experience.
- **Support for Multiple Models**: Choose between different language models depending on your GPU/CPU resources and performance needs.

---

##  Interactive Web Interface (Gradio)

The app uses **Gradio** to:

- Offer a responsive and intuitive UI
- Accept both **plain text** and **file inputs**
- Provide configuration options (like model selection or summary length)
- Display results immediately within the browser, without needing users to run Python scripts locally

A typical Gradio layout might include:
- A text input box
- Model selection dropdown
- “Submit” button
- Output display area for both summary and answered questions

---

##  Getting Started

### Prerequisites

Make sure you have:

- Python 3.8+
- Installed dependencies: `transformers`, `openai`, `gradio` (if applicable), etc.

### Installation

```bash
git clone https://github.com/AbdelhamidNasser946/Text-Summarization.git
cd Text-Summarization/Text_summarize_QA/code
pip install -r requirements.txt
```

### Project Structure
```
Text_summarize_QA/
└── code/
├── app.py # Main entry point for the Gradio web app
├── summarizer.py # Summarization model logic
├── qa.py # Question Answering model logic
├── utils.py # Helper functions (if applicable)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
