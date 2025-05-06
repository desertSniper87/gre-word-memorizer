import sqlite3
import os
from config import DATABASE_PATH

def initialize_db():
    """Initialize the SQLite database with required tables"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create table for GRE words
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gre_words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE NOT NULL,
        phonetics TEXT,
        part_of_speech TEXT,
        definition TEXT NOT NULL,
        example TEXT,
        image_url TEXT,
        image_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()
    
def save_word(word_data):
    """Save word information to the database
    
    Args:
        word_data (dict): Dictionary containing word information
    
    Returns:
        int: ID of the inserted/updated row
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Check if the word already exists
    cursor.execute('SELECT id FROM gre_words WHERE word = ?', (word_data['word'],))
    existing_id = cursor.fetchone()
    
    if existing_id:
        # Update existing record
        cursor.execute('''
        UPDATE gre_words SET 
            phonetics = ?,
            part_of_speech = ?,
            definition = ?,
            example = ?,
            image_url = ?,
            image_path = ?
        WHERE id = ?
        ''', (
            word_data.get('phonetics', ''),
            word_data.get('part_of_speech', ''),
            word_data.get('definition', ''),
            word_data.get('example', ''),
            word_data.get('image_url', ''),
            word_data.get('image_path', ''),
            existing_id[0]
        ))
        row_id = existing_id[0]
    else:
        # Insert new record
        cursor.execute('''
        INSERT INTO gre_words 
            (word, phonetics, part_of_speech, definition, example, image_url, image_path)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            word_data['word'],
            word_data.get('phonetics', ''),
            word_data.get('part_of_speech', ''),
            word_data.get('definition', ''),
            word_data.get('example', ''),
            word_data.get('image_url', ''),
            word_data.get('image_path', '')
        ))
        row_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    return row_id

def get_word(word):
    """Retrieve word information from the database
    
    Args:
        word (str): The word to retrieve
        
    Returns:
        dict: Word information or None if not found
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM gre_words WHERE word = ?', (word,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return dict(result)
    return None

def get_all_words():
    """Retrieve all words from the database
    
    Returns:
        list: List of word dictionaries
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM gre_words ORDER BY word')
    results = cursor.fetchall()
    
    conn.close()
    
    return [dict(row) for row in results]