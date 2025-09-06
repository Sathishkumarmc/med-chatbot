# Simple Medical Chatbot using Dictionary

def medical_chatbot():
    responses = {
        "fever": "You might have a viral infection. Stay hydrated and rest. If it persists, consult a doctor.",
        "headache": "Try drinking water and resting in a quiet room. If it’s severe, consider taking a mild pain reliever.",
        "cough": "It could be a common cold. Drink warm fluids and take honey with ginger. If it worsens, see a doctor.",
        "cold": "Stay warm, drink hot soups, and take vitamin C-rich foods.",
        "stomach pain": "Avoid spicy food and drink plenty of water. If pain persists, visit a doctor.",
        "vomiting": "You may have food poisoning. Drink ORS solution and rest.",
        "sore throat": "Gargle with warm salt water and drink herbal tea.",
        "diarrhea": "Stay hydrated with ORS and avoid solid foods until it improves.",
        "back pain": "Maintain a good posture and do light stretching. Apply a warm compress if necessary.",
        "chest pain": "This can be serious. If it's severe or persistent, seek medical attention immediately.",
        "fatigue": "Ensure you're getting enough sleep and a balanced diet. Exercise can also help.",
        "insomnia": "Try reducing screen time before bed, drinking warm milk, or meditating.",
        "anxiety": "Practice deep breathing exercises and talk to someone if it persists.",
        "allergy": "Avoid known allergens and take antihistamines if needed. If symptoms are severe, seek medical help.",
        "high blood pressure": "Reduce salt intake, exercise regularly, and consult a doctor for medication.",
        "low blood pressure": "Increase fluid intake and eat small, frequent meals.",
        "indigestion": "Avoid greasy food, eat slowly, and try ginger tea.",
        "constipation": "Increase fiber intake, drink more water, and exercise regularly.",
        "skin rash": "Apply a soothing lotion and avoid scratching. If it worsens, consult a dermatologist.",
        "toothache": "Rinse with warm salt water and use a cold compress. See a dentist if the pain persists.",
        "ear pain": "Avoid loud noises and use a warm compress. Consult a doctor if the pain is severe.",
        "eye irritation": "Wash with clean water and avoid rubbing. Use artificial tears if necessary.",
        "exit": "Thank you for using the medical chatbot. Stay healthy!"
    }
    
    print("Hello! I am a medical chatbot. How can I assist you today?")
    print("Type 'exit' to stop the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        for key in responses:
            if key in user_input:
                print("Chatbot:", responses[key])
                if key == "exit":
                    return
                break
        else:
            print("Chatbot: I'm not sure about that. Please consult a doctor for more information.")

medical_chatbot()
