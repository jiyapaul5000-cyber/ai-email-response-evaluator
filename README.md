# AI Email Response Evaluator

## Overview
An AI-powered application that generates professional email replies and evaluates their quality using Google Gemini.

## Features
- Generate professional email responses
- AI-based evaluation
- Accuracy score
- Tone analysis
- Completeness analysis
- Suggestions for improvement

## Tech Stack
- Python
- Streamlit
- Google Gemini API
- dotenv

## Project Structure
AI_Email_Response_Evaluator/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables (Gemini API Key)
├── .gitignore                  # Git ignored files
│
├── data/
│   └── emails.json             # Email dataset
│
├── prompts/
│   └── prompts.py              # Prompt templates for AI
│
├── services/
│   ├── gemini_service.py       # Handles Gemini API integration
│   └── evaluator.py            # Evaluates AI-generated responses
│
├── utils/
│   └── helper.py               # Utility/helper functions
│
└── README.md                   # Project documentation

## Installation
### 1. Clone the repository

bash
git clone https://github.com/jiyapaul5000-cyber/ai-email-response-evaluator.git


### 2. Navigate to the project directory

bash
cd ai-email-response-evaluator


### 3. Create a virtual environment

bash
python -m venv venv


### 4. Activate the virtual environment

**Windows**

bash
venv\Scripts\activate
### 5. Install the required dependencies

bash
pip install -r requirements.txt


### 6. Configure the API Key

Create a `.env` file in the project root and add:

env
GEMINI_API_KEY=your_api_key_here

## How to Run
Run the Streamlit application:

bash
streamlit run app.py


The application will start on your local machine.

Open your browser and visit:


http://localhost:8501

## Screenshots
<img width="1107" height="942" alt="image" src="https://github.com/user-attachments/assets/82374be7-3039-4a79-9334-f65244ab9ff3" />
<img width="1027" height="790" alt="image" src="https://github.com/user-attachments/assets/f5257002-ce42-4d60-b7c8-e6da293f14a6" />


