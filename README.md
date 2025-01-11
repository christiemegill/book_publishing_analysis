# Publishing Industry Evolution Analysis (1900-2022)
## Overview
This project analyzes the evolution of English-language book publishing over more than a century, from 1900 to 2022. Using Python, Jupyter, and data visualization techniques, it explores publishing volumes, genre trends, and historical correlations to provide insights into the industry's development and adaptation to technological changes.

## Key Features
* Comprehensive analysis of publishing volume trends across three major historical periods
* Genre dominance analysis by decade
* Interactive visualizations using Matplotlib
* Data preparation for Tableau integration
* Advanced data cleaning and standardization of genre categories
* Statistical analysis of growth patterns and historical event correlations

## Technologies Used
* Python 3.x
* pandas: Data manipulation and analysis
* Matplotlib: Data visualization
* NumPy: Numerical computing
* Tableau: Advanced visualization and interactive dashboards
  
## Installation

# Clone the repository
git clone https://github.com/yourusername/publishing-analysis.git

# Navigate to project directory
cd publishing-analysis

## Project Structure
publishing-analysis/

│

├── data/

│   ├── modern_english_books.csv

│   ├── tableau_timeline.csv

│   └── tableau_genres.csv

│

├── notebooks/

│   └── publishing_analysis.ipynb

│

├── src/

│   ├── data_cleaning.py

│   └── analysis_utils.py

│

└── visualizations/
│
    ├── decade_trends.png
│ 
    ├── genre_evolution.png
│
    └── top_genres.png

## Key Findings
* Publishing Volume Analysis

* Identified three distinct growth periods:

  *  Pre-War Era (1900-1940): Modest growth rates of 10-15% per decade
  *  Post-War Expansion (1940-1990): Peak growth rates of 50-70% per decade
  *  Digital Revolution (1990-2022): Sustained high volumes with modified growth patterns

* Genre Evolution

 * Tracked the emergence and dominance of different genres across decades
 *  Revealed significant shifts in reader interests and market demands
 *  Identified the rise of Young Adult literature and consistent growth in Children's literature

* Historical Correlations

  * Analyzed impact of major world events on publishing volumes
  * Tracked influence of technological disruptions
  * Documented industry resilience and adaptation patterns

## Data Cleaning Methodology

* Implemented comprehensive genre mapping system
* Standardized category names and hierarchies
* Separated format designations from genre classifications
* Handled overlapping categories (e.g., juvenile/children's fiction)

## Visualizations

* The project includes several key visualizations:

  *  Publication volume by decade (1900-2022)
  *  Genre dominance trends
  *  Top 10 most common genres
  *  Evolution of top 5 genres over time

## Usage
Example usage of core analysis functions
from src.analysis_utils import analyze_publication_trends, analyze_genre_dominance

Analyze publication trends
decade_counts = analyze_publication_trends()

Analyze genre dominance
decade_genres = analyze_genre_dominance()

## Tableau Integration

* The project includes prepared datasets for Tableau visualization:

  tableau_timeline.csv: Decade-wise publication volumes
  
  tableau_genres.csv: Genre distribution across decades

## Future Development

* Planned enhancements include:

  *  Regional variation analysis
  *  Format-specific growth rate analysis
  *  Price point evolution tracking
  *  Market concentration analysis
  *  Distribution channel impact assessment

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
 This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
 github.com/christiemegill/book_publishing_analysis

## Acknowledgments
 Data source: Open Library API


# Install required packages
pip install -r requirements.txt
