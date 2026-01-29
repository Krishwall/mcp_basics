from fastmcp   import FastMCP
import feedparser

mcp=FastMCP(name="FeedFetcher"
            )

@mcp.tool()
def fcc_news_search(query: str, max_results: int = 5) -> dict:
    """Fetches the latest news articles from FreeCodeCamp via RSS by title/description
    
    args:
        query (str): The search query to look for in FCC news.
        max_results (int): The maximum number of news articles to return.
    returns:
        str: A formatted string containing the titles and links of the news articles."""
    
    feed_url = f"https://www.freecodecamp.org/news/rss/"
    feed = feedparser.parse(feed_url)
    
    if not feed.entries:
        return "No news articles found for the given query."
    
    results = []
    for entry in feed.entries :
        title=entry.get("title","")
        description=entry.get("description","")
        if query.lower() in title.lower() or query.lower() in description.lower():
            results.append({"title":title, "url":entry.get("link","")})

        if len(results) >= max_results:
            break

    return {"results":results} or [{"message":"No news articles found for the given query."}]
@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 5) -> dict:
    """Fetches the latest YouTube videos from FreeCodeCamp via RSS by title/description
    
    args:
        query (str): The search query to look for in FCC YouTube videos.
        max_results (int): The maximum number of videos to return.
    returns:
        str: A formatted string containing the titles and links of the videos."""
    
    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    feed = feedparser.parse(feed_url)
    
    if not feed.entries:
        return "No YouTube videos found for the given query."
    
    results = []
    for entry in feed.entries :
        title=entry.get("title","")
        description=entry.get("description","")
        if query.lower() in title.lower() or query.lower() in description.lower():
            results.append({"title":title, "url":entry.get("link","")})

        if len(results) >= max_results:
            break

    return {"results":results} or [{"message":"No YouTube videos found for the given query."}]
@mcp.tool()
def fcc_secret_message() -> str:
    """Returns a secret message """
    return "Keep pushing your limits ! 🚀"
if __name__ == "__main__":
    mcp.run(transport="http") #STDIO by default 