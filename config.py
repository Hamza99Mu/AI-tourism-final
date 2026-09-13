import os
import streamlit as st

def get_secret(key: str, default=None):
    val = None
    try:
        val = st.secrets.get(key)
    except Exception:
        pass
    if not val:
        try:
            for sec in st.secrets.values():
                if isinstance(sec, dict) and key in sec:
                    val = sec[key]
        except Exception:
            pass
    if not val:
        val = os.getenv(key, default)
    
    if val:
        os.environ[key] = str(val)
    return val

get_secret("GROQ_API_KEY")
