# chatbot.py
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from faqs import faq_data

# Step 1: Load a small, open-source model
# You can replace this with any model like "google/flan-t5-base" or "mistralai/Mistral-7B-Instruct" (via Ollama)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

# Step 2: Load embedding model for semantic matching
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Step 3: Convert FAQ questions into embeddings
faq_questions = list(faq_data.keys())
faq_embeddings = embedder.encode(faq_questions, convert_to_tensor=True)

def find_best_match(user_question):
    """Find the most similar FAQ question using cosine similarity"""
    query_embedding = embedder.encode(user_question, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(query_embedding, faq_embeddings)
    best_match_idx = similarity.argmax().item()
    return faq_questions[best_match_idx], faq_data[faq_questions[best_match_idx]]

def answer_query(question):
    matched_q, matched_a = find_best_match(question)
    prompt = f"Question: {question}\nAnswer based on college FAQ: {matched_a}"
    result = generator(prompt, max_length=128, do_sample=False)
    return result[0]["generated_text"]
