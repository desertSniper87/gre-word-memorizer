import os
import urllib.parse
import webbrowser


def search_image(word):
    """Open a browser window with Google Images search for the word

    Args:
        word (str): The word to search for

    Returns:
        dict: Information about the search
    """
    try:
        # Format the search query
        search_query = f"{word} meaning"
        encoded_query = urllib.parse.quote_plus(search_query)

        # Create the Google Images search URL
        google_images_url = (
            f"https://www.google.com/search?q={encoded_query}&tbm=isch"
        )

        # Open the URL in the default web browser
        webbrowser.register(
            "qutebrowser",
            None,
            webbrowser.BackgroundBrowser("/opt/homebrew/bin/qutebrowser"),
            preferred=True,
        )
        webbrowser.open(google_images_url)

        print(f"Opened browser with Google Images search for '{word}'")

        # Return information about the search
        return {
            "url": google_images_url,
            "source": "Google Images",
            "search_query": search_query,
        }

    except Exception as e:
        print(f"Error opening browser: {e}")
        return None


def download_image(url, word):
    """This function is now a placeholder since we're using the browser

    With the browser-based approach, the user will need to manually save images.
    This function remains for API compatibility with the rest of the code.

    Args:
        url (str): The image search URL (not used)
        word (str): The word associated with the image

    Returns:
        str: A placeholder message instead of a file path
    """
    # Create images directory if it doesn't exist (for potential future use)
    images_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "images"
    )
    os.makedirs(images_dir, exist_ok=True)

    # Instead of downloading an image, just return a message
    return f"Browser opened for manual image selection for '{word}'"
