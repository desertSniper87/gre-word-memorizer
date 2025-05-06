import requests
import json
from config import DICTIONARY_API_BASE_URL

def get_word_definition(word):
    """Fetch word definition from the Dictionary API
    
    Args:
        word (str): The word to look up
        
    Returns:
        dict: Word information including definition, part of speech, etc.
             or None if word not found
    """
    url = f"{DICTIONARY_API_BASE_URL}{word}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        if not data or not isinstance(data, list) or len(data) == 0:
            return None
            
        # Extract relevant information
        result = {
            'word': word,
            'phonetics': '',
            'part_of_speech': '',
            'definition': '',
            'example': ''
        }
        
        # Get phonetics if available
        if data[0].get('phonetics') and len(data[0]['phonetics']) > 0:
            for phonetic in data[0]['phonetics']:
                if phonetic.get('text'):
                    result['phonetics'] = phonetic.get('text')
                    break
        
        # Get the first meaning
        if data[0].get('meanings') and len(data[0]['meanings']) > 0:
            meaning = data[0]['meanings'][0]
            result['part_of_speech'] = meaning.get('partOfSpeech', '')
            
            if meaning.get('definitions') and len(meaning['definitions']) > 0:
                definition = meaning['definitions'][0]
                result['definition'] = definition.get('definition', '')
                result['example'] = definition.get('example', '')
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching definition: {e}")
        return None
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error parsing definition response: {e}")
        return None