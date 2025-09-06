
**Medical Chatbot (Student Project)**

This project is a **basic medical chatbot** created in Python. The chatbot is designed to help students and users learn about **common medical terms and diseases** in a simple, easy-to-understand way. It does not replace doctors or professional medical advice but serves as an **educational tool**.

The chatbot contains a **small knowledge base** with two main parts:

1. **Medical Terms** – simple explanations of words like *acute, chronic, biopsy, tachycardia,* and *dyspnea*.
2. **Common Diseases** – short descriptions of diseases such as *Diabetes, Hypertension, Asthma, and Influenza (Flu)*. For each disease, the chatbot can provide:

   * A **summary** of what the disease is.
   * **Common symptoms** that people might notice.
   * **Basic advice** like checking with a doctor or resting.

The chatbot works in two modes:

* **Flask API Mode**: You can send a message to the chatbot through an API (for example, using Postman or cURL) and get a JSON response. This makes it useful for integrating into web apps or mobile apps.
* **Simple Question & Answer**: The chatbot looks for keywords or close matches in your message. For example:

  * If you type *“What is asthma?”* it will reply with a short description, symptoms, and advice.
  * If you type *“Explain biopsy”*, it will give you the meaning of the term.
  * If you ask about something not in the knowledge base, it politely says it cannot understand.

This project is **easy to run** and uses only **basic Python** and the **Flask library**, making it beginner-friendly. The goal is to **practice chatbot development, medical terminology handling, and simple text processing**.

           -------------------------IMPORTANT-------------------------

(***Finally, the chatbot always includes a **safety disclaimer**: it is for learning purposes only and not meant for real diagnosis ****)
