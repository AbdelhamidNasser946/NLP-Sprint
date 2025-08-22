from transformers import pipeline


def load_qa_model():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")


def answering_questions(qa_model, question, context):
    answer = qa_model(question=question, context=context)
    return answer['answer'], answer['score']


if __name__ == '__main__':
    context_ex = """
    Artificial Intelligence (AI) is a branch of computer science that aims to build machines
    capable of performing tasks that typically require human intelligence.
    These tasks include reasoning, learning from experience, making decisions,
    understanding natural language, and recognizing patterns.

    In healthcare, AI is used to analyze medical images, predict patient outcomes,
    and even assist in surgeries with robotic systems.
    For example, AI algorithms can detect early signs of diseases such as cancer
    from radiology scans with accuracy comparable to expert doctors.

    In finance, AI helps banks and institutions detect fraud,
    analyze risks, and provide personalized recommendations to customers.
    It is also widely used in stock market predictions and algorithmic trading.

    In transportation, AI powers self-driving cars,
    optimizes traffic management systems in smart cities,
    and improves logistics by predicting the best delivery routes.

    However, AI also raises ethical concerns such as job displacement,
    privacy issues, and the possibility of bias in automated decision-making.
    Governments and organizations are working on policies and regulations
    to ensure that AI is developed responsibly and benefits society as a whole.
    """
    qa = load_qa_model()
    print(answering_questions(qa, 'What are some ethical concerns of AI?', context_ex))
