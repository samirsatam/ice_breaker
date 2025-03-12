from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn or Twitter profile page."""
    search = TavilySearchResults()
    # res = search.run(f"{name}") , does not work and returns wrong results.
    # res = search.run(f"{name} linkedin") works but seems to be less precise
    res = search.run(f"{name} Raft linkedin") # with company name is more accurate.
    # res = search.run(f"{name} Linkedin profile") # with company name is more accurate.
    return res