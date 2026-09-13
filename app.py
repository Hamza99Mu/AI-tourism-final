import streamlit as st
from rag import answer_with_rag
from itinerary import generate_itinerary
from weather_api import get_weather
from maps_api import search_places

st.set_page_config(page_title="AI Tourism Assistant", page_icon="🏔️", layout="wide")
st.title("🏔️ AI Tourism Assistant")
st.caption("AI-powered travel planning for Pakistan — starting with KPK.")

with st.sidebar:
    st.header("Trip Preferences")
    destination = st.text_input("Destination", "Swat")
    days = st.number_input("Number of days", 1, 14, 3)
    budget = st.number_input("Budget (PKR)", 0, 10000000, 25000, step=1000)
    travel_type = st.selectbox("Travel type", ["Family", "Solo", "Friends", "Students"])
    language = st.selectbox("Language", ["English", "Urdu"])
    include_weather = st.checkbox("Include weather", True)
    include_places = st.checkbox("Include nearby places", True)

tab1, tab2, tab3 = st.tabs(["💬 Ask AI", "📅 Plan My Trip", "🌤️ Live Info"])

with tab1:
    question = st.text_area("Your question",
        placeholder="Example: What are good family-friendly places in Swat?")
    if st.button("Ask AI", type="primary"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Searching the tourism knowledge base..."):
                result = answer_with_rag(question, language)
            st.markdown(result["answer"])
            if result["sources"]:
                st.markdown("### 📚 Sources")
                for source in result["sources"]:
                    st.write(f"- {source}")

with tab2:
    if st.button("Generate Itinerary", type="primary"):
        with st.spinner("Creating your travel plan..."):
            context = answer_with_rag(
                f"Give useful tourism information about {destination}.", "English"
            )
            itinerary = generate_itinerary(
                destination, int(days), int(budget), travel_type, language,
                context["answer"]
            )
        st.markdown(itinerary)

with tab3:
    st.subheader(f"Live information for {destination}")
    if include_weather:
        st.markdown("### 🌤️ Weather")
        weather = get_weather(destination)
        if weather["ok"]:
            st.write(f"Temperature: {weather['temperature']} °C")
            st.write(f"Condition: {weather['description']}")
            st.caption(weather["source"])
        else:
            st.info(weather["message"])

    if include_places:
        st.markdown("### 📍 Places")
        places = search_places(destination)
        if places:
            for place in places:
                st.write(f"- **{place['name']}**")
        else:
            st.info("Maps/Places API is not configured yet.")

st.divider()
st.caption("Verify important travel information with official sources before travel.")
