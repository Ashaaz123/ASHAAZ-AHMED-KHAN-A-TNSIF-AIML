# Install once:
# pip install transformers torch sentence-transformers

from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# 1. Load a pre-trained LLM
generator = pipeline("text-generation", model="distilgpt2")

# 2. Prompt Engineering + Text Generation
prompt = "Explain Artificial Intelligence in simple words:"
result = generator(
    prompt,
    max_new_tokens=40,
    do_sample=True,
    temperature=0.7
)

print("GENERATED TEXT:")
print(result[0]["generated_text"])


# 3. Embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Machine Learning allows computers to learn from data.",
    "Deep Learning uses neural networks with multiple layers.",
    "Generative AI creates new text, images and other content."
]

query = "What is Generative AI?"

doc_embeddings = model.encode(documents)
query_embedding = model.encode(query)

# 4. Simple RAG-style Retrieval
scores = util.cos_sim(query_embedding, doc_embeddings)[0]

best_index = scores.argmax()

print("\nRETRIEVED INFORMATION:")
print(documents[best_index])


# 5. Generate an answer using retrieved information
context = documents[best_index]

final_prompt = f"""
Answer the question using the information below.

Information: {context}

Question: {query}

Answer:
"""

answer = generator(
    final_prompt,
    max_new_tokens=50,
    do_sample=True,
    temperature=0.5
)

print("\nRAG ANSWER:")
print(answer[0]["generated_text"])