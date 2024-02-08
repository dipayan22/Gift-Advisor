from flask import Flask, render_template, request, jsonify
import google.generativeai as genai 
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')

    response=model.generate_content(input)

    return response.text


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_gift', methods=['POST'])
def suggest_gift():
    occasion = request.form.get('occasion')
    recipient = request.form.get('recipient')
    favorite_thing = request.form.get('favoriteThing')
    budget = request.form.get('budget')

    input_text = f'''Imagine you are an AI-powered Gift Advisor, assisting a user in finding the perfect gift for their {recipient} on the occasion of {occasion}. The user is looking for something sentimental, related to a shared hobby, {favorite_thing}, and within a budget of Rupees {budget}.

Give me some idea for the my {recipient} like this format:
1. Gift Idea 1:
    - Gift Idea: Description of the first gift idea.
    - Sentimentality: Explain why this gift idea is sentimental.
    - Budget: Estimated cost of the first gift idea.

2. Gift Idea 2:
    - Gift Idea: Description of the second gift idea.
    - Sentimentality: Explain why this gift idea is sentimental.
    - Budget: Estimated cost of the second gift idea.
    
3. Gift Idea 3:
    - Gift Idea: Description of the third gift idea.
    - Sentimentality: Explain why this gift idea is sentimental.
    - Budget: Estimated cost of the third gift idea.

4. Gift Idea 4:
    - Gift Idea: Description of the third gift idea.
    - Sentimentality: Explain why this gift idea is sentimental.
    - Budget: Estimated cost of the third gift idea.

5. Gift Idea 5:
    - Gift Idea: Description of the third gift idea.
    - Sentimentality: Explain why this gift idea is sentimental.
    - Budget: Estimated cost of the third gift idea.

---
---
Provide personalized and thoughtful gift suggestions, explaining the reasoning behind each recommendation.'''

    response = get_gemini_response(input_text)

    # Perform your logic here to extract and format the suggestions

    # For now, returning a simple message
    suggestion = response.split('---')[0]  # Extracting the suggestions

    # Splitting the suggestions into individual items
    formatted_suggestions = [item.strip() for item in suggestion.split('\n\n')]

    
    # print(formatted_suggestions)
    return render_template('suggestion.html', suggestion=formatted_suggestions)


if __name__ == '__main__':
    app.run(debug=True)
