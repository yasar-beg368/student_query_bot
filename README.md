# 🎓 Student Query Bot — Domain-Specific College Chatbot

A simple **AI-powered chatbot** built for handling **college-related FAQs** such as admission, courses, placements, hostel, and campus life.  
This chatbot uses **local open-source models** for natural language understanding — no OpenAI API needed.

---

## 🧠 **Overview**

The **Student Query Bot** helps students and visitors quickly find answers to common college-related questions such as:

- 📚 Courses offered  
- 📝 Admission requirements  
- 🏫 Campus & facilities  
- 💰 Fees and scholarships  
- 💼 Placement opportunities  
- 🎉 Student activities  
- 📞 Contact information  

It uses **semantic search with Sentence Transformers** to find the most relevant answer from a predefined FAQ dataset.

---

## ⚙️ **Tech Stack**

| Component | Technology Used |
|------------|----------------|
| 🧩 Framework | Streamlit |
| 🗣️ NLP Model | Sentence Transformers (all-MiniLM-L6-v2) |
| 💬 Logic | Python (LangChain-style retrieval approach) |
| 📁 Dataset | Custom-built FAQ dataset (`faq_data.py`) |
| 🧠 Embeddings | Cosine similarity using `sentence-transformers` |

---

## 🧰 **Project Structure**

student_query_bot/
│
├── app.py # Streamlit UI
├── chatbot.py # Query handling + NLP logic
├── faq_data.py # FAQ knowledge base
├── requirements.txt # Dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 **Setup Instructions**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yasar-beg368/student_query_bot.git
cd student_query_bot
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # (on Windows)
# OR
source venv/bin/activate  # (on Mac/Linux)
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the App
bash
Copy code
streamlit run app.py
Then open the link shown in the terminal (usually http://localhost:8501) in your browser.

💬 Usage
Type a question like:

“What courses are offered?”

“Do you provide hostel facilities?”

“What is the average placement package?”

The chatbot responds instantly based on your FAQ dataset.

🧩 How It Works
User enters a query in the Streamlit chat UI.

The chatbot encodes the query using SentenceTransformer embeddings.

It compares the query vector with precomputed FAQ vectors using cosine similarity.

The best-matching answer is displayed to the user.

This makes the chatbot context-aware and accurate, even if the user’s question wording differs slightly.

🧾 Example Queries
Question	Example Answer
What are the hostel facilities?	“Separate hostels for boys and girls with WiFi, gym, and 24x7 security.”
Does the college offer placements?	“Yes! Our top recruiters include TCS, Infosys, and Wipro with 90% placement rate.”
How can I pay my fees?	“Fees can be paid online through our student portal or via bank transfer.”

<img width="1168" height="668" alt="Screenshot 2025-11-02 000355" src="https://github.com/user-attachments/assets/c542895d-dce8-4c82-97e9-4a0d5701df7b" />


🧑‍💻 Future Enhancements
Integrate a vector database (FAISS) for scalable retrieval.

Add speech-to-text for voice queries.

Create a student portal chatbot that integrates live API data.

🏷️ License
This project is open source under the MIT License.

💖 Contributors
👤 Yasar Beg
💡 Designed & Developed the Student Query Bot
📬 Contact: admissions@college.edu
