"""
Seed script — Populate the database with Mohamed's projects and experience.
Run with:  python seed.py
"""

import json
import os

from app import create_app, db
from app.models import Experience, Project

app = create_app(os.environ.get("FLASK_ENV", "development"))

EXPERIENCES = [
    {
        "role": "Data Scientist",
        "company": "zeroG – AI in Aviation (Lufthansa Group)",
        "location": "Frankfurt, Germany",
        "date_range": "Dec 2022 — Present",
        "description": (
            "Lead the innovation, design, and implementation of advanced AI systems "
            "to drive customer engagement and strategic business initiatives. "
            "Serve as a key resource for Generative and Agentic AI."
        ),
        "highlights": json.dumps(
            [
                "Keynote on Agentic AI with live multi-agent system demo at Data Community Day",
                "Pioneered first generative AI 'categories model' for city destination scoring",
                "Engineered ancillary recommender → 3-15% purchase increase across airlines",
                "Optimised recommender APIs for up to 20× performance gain",
                "Built AB testing pipeline from scratch for rigorous model validation",
            ]
        ),
        "sort_order": 1,
    },
    {
        "role": "AI Engineer (Freelance)",
        "company": "Freelance",
        "location": "Remote",
        "date_range": "Apr 2021 — Oct 2022",
        "description": (
            "Delivered end-to-end AI solutions for diverse clients, "
            "managing every stage from scoping to deployment and maintenance."
        ),
        "highlights": json.dumps(
            [
                "'Virtual Patient' simulation for interactive medical training",
                "Automated Dark Web Auto-Labelling & Classification system",
            ]
        ),
        "sort_order": 2,
    },
    {
        "role": "Engineering Lecturer (Part-Time)",
        "company": "Arab International University",
        "location": "Damascus, Syria",
        "date_range": "Feb 2022 — Jun 2022",
        "description": (
            "Instructed undergraduate students in Algorithms & Data Structures. "
            "Developed curriculum, projects, and assessments."
        ),
        "highlights": json.dumps(
            [
                "Algorithms & Data Structures lab instructor",
                "Delivered Reinforcement Learning workshop (Smart Tech Institute, 2021)",
            ]
        ),
        "sort_order": 3,
    },
    {
        "role": "Data Scientist",
        "company": "Damascus-based Start-Up",
        "location": "Damascus, Syria",
        "date_range": "Apr 2020 — Jun 2021",
        "description": (
            "Owned the full data science pipeline — from web scraping and cleaning "
            "to modelling and deployment of predictive systems."
        ),
        "highlights": json.dumps(
            [
                "Foreign Exchange Forecasting (JPY/CAD) — time-series model",
                "Emotion Prediction from Voice — deep learning classifier",
                "Arabic Tweets Classifier — NLP sentiment analysis",
            ]
        ),
        "sort_order": 4,
    },
    {
        "role": "BSc/MSc Informatics Engineering — AI Major",
        "company": "Arab International University",
        "location": "Damascus, Syria",
        "date_range": "Sep 2015 — Mar 2021",
        "description": (
            "Thesis: Human Behavior Simulation — a multi-modal AI system combining "
            "voice cloning, 3D avatar reconstruction, and deep RL agent training."
        ),
        "highlights": json.dumps(
            [
                "Voice Cloning via Zero-Shot Learning from 5-20s audio samples",
                "3D Avatar Reconstruction using Facebook's PIFu from a single image",
                "RL Agent trained to walk in Blender/Unity via PPO",
            ]
        ),
        "sort_order": 5,
    },
]

PROJECTS = [
    {
        "title": "Multi-Agent Voice System",
        "short_description": "Voice-activated autonomous business analysis.",
        "description": (
            "Designed and built a live, multi-agent system demo presented as a keynote "
            "at the Lufthansa Group Data Community Day 2025. The system processes voice "
            "commands, transcribes them, and uses an LLM orchestrator to delegate tasks "
            "to specialised search and data analysis agents — solving complex business "
            "queries in real-time."
        ),
        "technologies": "Python,LangChain,Whisper,Azure OpenAI,FastAPI",
        "category": "genai",
        "year": "2025",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 1,
    },
    {
        "title": "Ancillary Recommender System",
        "short_description": "Production recommendation engine driving 3-15% purchase uplift.",
        "description": (
            "Engineered and deployed a production-grade ancillary recommender system "
            "across multiple Lufthansa Group airline partners. The system scores and "
            "ranks ancillary products in real-time, resulting in a measurable 3-15% "
            "increase in purchase rates. Included API refactoring that achieved a 20× "
            "performance gain."
        ),
        "technologies": "Python,Scikit-Learn,Azure ML,REST APIs,AB Testing",
        "category": "recsys",
        "year": "2023",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 2,
    },
    {
        "title": "Generative AI City Recommender",
        "short_description": "First GenAI model for destination scoring & diversity.",
        "description": (
            "Pioneered the first generative AI-based 'categories model' to score city "
            "destinations. The model significantly improved the diversity and relevance "
            "of travel recommendations by combining category embeddings with frequency- "
            "based signals, serving the 95%+ non-logged-in customer base."
        ),
        "technologies": "Python,GPT-4,Azure OpenAI,Pandas,NumPy",
        "category": "genai",
        "year": "2024",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 3,
    },
    {
        "title": "AB Testing Framework",
        "short_description": "End-to-end experimentation pipeline for model validation.",
        "description": (
            "Architected and built a comprehensive AB testing framework from the ground "
            "up. Handles segmentation for both logged-in (ID-based) and non-logged-in "
            "(market-behaviour clusters) users, with automated statistical analysis and "
            "reporting to drive data-informed model iteration."
        ),
        "technologies": "Python,Pandas,SciPy,Azure Data Factory,SQL",
        "category": "recsys",
        "year": "2024",
        "client": "Lufthansa Group",
        "featured": False,
        "sort_order": 4,
    },
    {
        "title": "Human Behavior Simulation",
        "short_description": "Multi-modal AI: voice cloning + 3D avatar + RL agent.",
        "description": (
            "Master's thesis project combining three AI modalities: (1) Zero-Shot "
            "voice cloning from 5-20s audio samples, (2) 3D avatar reconstruction "
            "from a single image using Facebook's PIFu, and (3) a deep RL agent "
            "trained via PPO to walk in a Blender/Unity virtual environment."
        ),
        "technologies": "Python,TensorFlow,Blender,Unity,C#,PPO",
        "category": "rl cv",
        "year": "2021",
        "client": "Arab International University",
        "featured": False,
        "sort_order": 5,
    },
    {
        "title": "Virtual Patient Simulation",
        "short_description": "Interactive AI patient for medical training scenarios.",
        "description": (
            "Developed an AI-powered 'Virtual Patient' simulation for use in interactive "
            "clinical training. The system models patient symptoms, responds to medical "
            "questions, and adapts its state based on treatment decisions."
        ),
        "technologies": "Python,NLP,TensorFlow,Flask",
        "category": "nlp",
        "year": "2022",
        "client": "Freelance Client",
        "featured": False,
        "sort_order": 6,
    },
    {
        "title": "Dark Web Auto-Labelling",
        "short_description": "Automated classification of dark web content.",
        "description": (
            "Built an automated system for scraping, labelling, and classifying dark web "
            "content. Used NLP-based text classification pipelines to categorise content "
            "at scale with minimal human annotation."
        ),
        "technologies": "Python,Scikit-Learn,BeautifulSoup,Selenium,NLP",
        "category": "nlp",
        "year": "2022",
        "client": "Freelance Client",
        "featured": False,
        "sort_order": 7,
    },
    {
        "title": "Emotion from Voice",
        "short_description": "Deep learning classifier for vocal emotion detection.",
        "description": (
            "Designed and trained a deep learning model to predict human emotions from "
            "raw voice data. Feature extraction leveraged mel-frequency cepstral "
            "coefficients (MFCCs) fed into a convolutional + recurrent neural network."
        ),
        "technologies": "Python,TensorFlow,Keras,Librosa,NumPy",
        "category": "cv",
        "year": "2021",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 8,
    },
    {
        "title": "Arabic Tweets Classifier",
        "short_description": "Sentiment analysis for Arabic social media text.",
        "description": (
            "Developed an NLP pipeline for classifying Arabic tweets by sentiment. "
            "Addressed the challenges of Arabic morphology and dialectal variation "
            "through custom tokenisation and pre-processing."
        ),
        "technologies": "Python,NLTK,Scikit-Learn,Pandas",
        "category": "nlp",
        "year": "2021",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 9,
    },
    {
        "title": "Forex Forecasting (JPY/CAD)",
        "short_description": "Time-series model for foreign exchange prediction.",
        "description": (
            "Engineered a time-series forecasting model to predict JPY/CAD exchange "
            "rates. Incorporated feature engineering on macroeconomic signals and "
            "evaluated multiple architectures including LSTM and ARIMA."
        ),
        "technologies": "Python,TensorFlow,Pandas,Statsmodels",
        "category": "nlp",
        "year": "2020",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 10,
    },
    {
        "title": "RAG Pipeline with Smart Segmentation",
        "short_description": "Retrieval-Augmented Generation with Anthropic-inspired chunking.",
        "description": (
            "Implemented a Retrieval-Augmented Generation (RAG) pipeline with smart "
            "document segmentation inspired by Anthropic's recent research. The system "
            "dynamically chunks documents based on semantic boundaries for more accurate "
            "context retrieval."
        ),
        "technologies": "Python,LangChain,FAISS,Azure OpenAI",
        "category": "genai",
        "year": "2024",
        "client": "Personal Project",
        "featured": False,
        "sort_order": 11,
    },
    {
        "title": "AI Search & Reasoning Agents",
        "short_description": "Multi-step reasoning agents inspired by OpenAI O-series.",
        "description": (
            "Built multi-step reasoning AI agents inspired by OpenAI's O-model "
            "architecture. Agents assess source credibility, perform chain-of-thought "
            "reasoning, and execute autonomous tool use for complex research tasks."
        ),
        "technologies": "Python,LangChain,OpenAI,Tool Use,Agents",
        "category": "genai",
        "year": "2024",
        "client": "Personal Project",
        "featured": False,
        "sort_order": 12,
    },
]


def seed():
    with app.app_context():
        db.create_all()

        # Clear existing data
        Project.query.delete()
        Experience.query.delete()
        db.session.commit()

        for exp_data in EXPERIENCES:
            db.session.add(Experience(**exp_data))

        for proj_data in PROJECTS:
            db.session.add(Project(**proj_data))

        db.session.commit()
        print(f"✓ Seeded {len(EXPERIENCES)} experiences and {len(PROJECTS)} projects.")


if __name__ == "__main__":
    seed()
