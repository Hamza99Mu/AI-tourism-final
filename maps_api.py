from .config import get_secret

def search_places(location):
    # Extension point for the Maps/Places provider selected for your project.
    # The app fails gracefully until a provider/key is configured.
    if not get_secret("GOOGLE_MAPS_API_KEY"):
        return []
    return []
