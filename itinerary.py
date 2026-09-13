from config import get_secret
def generate_itinerary(destination, days, budget, travel_type, language, tourism_context):
    key = get_secret("OPENAI_API_KEY")
    if not key:
        return (f"### 🏔️ {destination} — {days}-Day Starter Plan\n\n"
                f"- Travel type: {travel_type}\n- Budget: PKR {budget:,}\n\n"
                "Configure OPENAI_API_KEY for AI-generated personalized planning.")
    try:
        from openai import OpenAI
        client = OpenAI(api_key=key)
        prompt = f"""Create a practical {days}-day itinerary for {destination}, Pakistan.
Travel type: {travel_type}
Budget: PKR {budget:,}
Use the supplied tourism context. Do not invent unsupported facts.
Include daily activities, approximate budget categories and verification notes.
Respond in {language}.

Tourism context:
{tourism_context}"""
        response = client.chat.completions.create(
            model=get_secret("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": "You are a careful travel planner."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as exc:
        return f"Could not generate itinerary: {exc}"
