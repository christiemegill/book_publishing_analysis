# Publishing Industry Evolution Analysis (1900-2022)
## Overview
This project analyzes the evolution of English-language book publishing from 1900 to 2022, focusing on five key research questions:

How has the volume of book publishing changed across decades?
Are there notable spikes or dips in publishing that correlate with historical events?
What are the dominant trends in modern publishing?
How has genre distribution changed in the 21st century?
Are certain subjects/genres showing rapid growth or decline?

## Key Features
* Historical publishing volume analysis
* Correlation analysis with major historical events
* Genre trend analysis and evolution
* Growth rate calculations by decade
* Genre diversity measurements
* Advanced genre categorization and cleaning

## Technologies Used
* Python 3.x
* pandas: Data manipulation and analysis
* Matplotlib: Data visualization
* seaborn: Enhanced visualizations
* NumPy: Numerical computing
* Tableau: Advanced visualization and interactive dashboards

## Project Structure
book_publishing_analysis/
├── data/
│   ├── modern_english_books.csv
│   └── historical_events.csv
├── notebooks/
│   └── publishing_evolution_analysis.ipynb
└── README.md


## Data Cleaning Methodology

* Standardized publication years (1900-2022)
* Implemented comprehensive genre mapping system
* Consolidated children's literature categories
* Removed format-based categories (e.g., congresses, proceedings)
* Enhanced genre cleaning with custom mapping

## Analysis Methods
* analyze_publishing_volume(): Decade-by-decade publication trends
* analyze_historical_events_impact(): Correlation with major events
* analyze_genre_trends(): Modern genre distribution analysis
* analyze_growth_rates(): Decade-over-decade growth calculation
* analyze_genre_diversity(): Genre variety analysis
* analyze_filtered_genre_evolution(): Filtered genre trend analysis

## Key Findings

* Publishing Volume Trends

    * Tracked volume changes across decades
    * Identified growth patterns and significant shifts
    * Visualized decade-by-decade comparisons

* Historical Event Correlations

* Analyzed impact of major events:

    * World Wars
    * Great Depression
    * 9/11
    * 2008 Financial Crisis
    * COVID-19

* Genre Evolution

    * Tracked emergence and decline of genres
    * Identified dominant categories
    * Analyzed genre diversity trends

## Visualizations

* The project includes several key visualizations:

  *  Publication volume by decade (1900-2022)
  *  Genre dominance trends
  *  Top 10 most common genres
  *  Evolution of top 5 genres over time

## Usage
* analyzer = LibraryDataAnalyzer('../data/modern_english_books.csv')

* volume_trends = analyzer.analyze_publishing_volume()

* historical_analysis = analyzer.analyze_historical_events_impact()

* genre_trends = analyzer.analyze_genre_trends()

## Tableau Integration

* The project includes prepared datasets for Tableau visualization:

  tableau_timeline.csv: Decade-wise publication volumes
  
  tableau_genres.csv: Genre distribution across decades

## Future Development

* Planned enhancements include:

  * Regional analysis expansion
  * Additional historical event correlation
  * Enhanced genre categorization
  * Temporal pattern analysis
  * Market segment analysis

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
