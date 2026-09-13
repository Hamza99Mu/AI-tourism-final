import os
import streamlit as st
from groq import Groq
from config import get_secret

def _get_groq_client():
    api_key = get_secret("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("Configure GROQ_API_KEY for AI-generated personalized planning.")
        st.stop()
    return Groq(api_key=api_key)

def generate_itinerary(destination: str, duration: int = 3, preferences: str = "general sightseeing") -> str:
    client = _get_groq_client()
    prompt = f"""
    Create a practical, day-by-day travel itinerary for {destination} lasting {duration} days.
    Traveler preferences: {preferences}.
    Include morning, afternoon, and evening activities, plus practical local tips.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional travel planner and local tourism guide."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2048
    )
    return response.choices[0].message.content
