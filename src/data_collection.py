import requests
import pandas as pd
import time
from tqdm import tqdm
from datetime import datetime

class ModernEnglishBookCollector:
    def __init__(self, batch_size=100, delay=1):
        self.base_url = "https://openlibrary.org/search.json"
        self.batch_size = batch_size
        self.delay = delay
        
    def fetch_books(self, offset, limit):
        """
        Fetch English books from 1900-2022
        """
        params = {
            'q': 'language:eng',
            'limit': limit,
            'offset': offset,
            'fields': 'key,title,author_name,first_publish_year,language,subject,cover_i',
            'sort': 'random',
            # Filter for English books in our date range
            'language': 'eng',
            'year_min': 1900,
            'year_max': 2022
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def process_book(self, book):
        """
        Process a single book record with validation
        """
        # Validate publication year
        year = book.get('first_publish_year', None)
        if not year or year < 1900 or year > 2022:
            return None
            
        # Validate language
        languages = book.get('language', [])
        if not languages or 'eng' not in languages:
            return None
            
        return {
            'title': book.get('title', ''),
            'author_name': book.get('author_name', [''])[0] if book.get('author_name') else '',
            'first_publish_year': year,
            'subject': book.get('subject', []),
            'cover_i': book.get('cover_i', None),
            'subject_count': len(book.get('subject', [])),
            'decade': (year // 10) * 10
        }

    def collect_data(self, total_books=10000):
        """
        Collect specified number of valid English books
        """
        all_books = []
        offset = 0
        pbar = tqdm(total=total_books, desc="Collecting books")
        
        while len(all_books) < total_books:
            # Fetch batch of books
            result = self.fetch_books(offset, self.batch_size)
            
            if result and 'docs' in result:
                # Process and validate each book
                for book in result['docs']:
                    processed_book = self.process_book(book)
                    if processed_book:  # Only add valid books
                        all_books.append(processed_book)
                        pbar.update(1)
                        
                        # Check if we have enough books
                        if len(all_books) >= total_books:
                            break
                
                offset += self.batch_size
                time.sleep(self.delay)  # Rate limiting
            else:
                print(f"\nFailed to fetch batch at offset {offset}")
                time.sleep(self.delay * 2)  # Wait longer after failure
            
        pbar.close()
        return all_books

    def save_data(self, books, filename):
        """
        Save collected books with statistics
        """
        df = pd.DataFrame(books)
        
        # Additional data validation
        df = df[
            (df['first_publish_year'] >= 1900) & 
            (df['first_publish_year'] <= 2022)
        ].copy()
        
        # Save to CSV
        df.to_csv(filename, index=False)
        
        # Print dataset statistics
        print("\nDataset Statistics:")
        print(f"Total books: {len(df)}")
        print(f"Publication years: {df['first_publish_year'].min()} - {df['first_publish_year'].max()}")
        print(f"Books per decade:")
        print(df['decade'].value_counts().sort_index())
        print(f"\nMost common subjects:")
        all_subjects = []
        for subjects in df['subject']:
            if isinstance(subjects, str):
                try:
                    subject_list = eval(subjects)
                    all_subjects.extend(subject_list)
                except:
                    continue
        
        subject_counts = pd.Series(all_subjects).value_counts()
        print(subject_counts.head(10))
        
        return df

def main():
    # Initialize collector
    collector = ModernEnglishBookCollector(batch_size=100, delay=1)
    
    # Collect books
    print("Starting collection of 10,000 English books from 1900-2022...")
    books = collector.collect_data(total_books=10000)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'modern_english_books_{timestamp}.csv'
    
    # Save data and get dataframe
    df = collector.save_data(books, filename)
    
    return df

if __name__ == "__main__":
    df = main()