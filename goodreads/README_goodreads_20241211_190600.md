# Analysis Report

### Summary of the Dataset

The dataset consists of 10,000 entries and 23 columns, capturing various attributes related to books on Goodreads. Key columns include identifiers (book_id, goodreads_book_id), publication data (original_publication_year, original_title), author information, ratings (average_rating, ratings_count), and metadata (image URLs). 

### Key Insights

1. **Missing Values**:
   - The dataset has missing values in several critical columns:
     - `isbn` (700 missing)
     - `isbn13` (585 missing)
     - `original_publication_year` (21 missing)
     - `original_title` (585 missing)
     - `language_code` (1084 missing)
   - This suggests a need for data cleaning, particularly in these areas, to enhance the dataset's usability.

2. **Authors**:
   - There are 4,664 unique authors, with Stephen King being the most frequently featured author (60 entries). This indicates a potential popularity bias towards certain authors.

3. **Publication Years**:
   - The mean original publication year is approximately 1982, with a range extending from as far back as -1750 to 2017. This highlights the inclusion of both historical and contemporary works.

4. **Ratings Analysis**:
   - The average rating across all books is approximately 4.00, with a relatively small standard deviation (0.25), indicating a general trend towards positive ratings among the books.
   - Ratings count ranges significantly, with a minimum of 2,716 to a maximum of 4,780,653, suggesting a substantial disparity in popularity and reader engagement across the dataset.

5. **Language Distribution**:
   - The `language_code` column has 25 unique values but shows a significant number of missing entries (1,084). The most common language appears to be English (`eng`), which suggests the dataset is primarily focused on English-language books.

6. **Image Availability**:
   - There are 6,669 unique image URLs for book covers, indicating a robust visual representation of the dataset, which can be beneficial for user engagement and marketing.

### Recommendations

1. **Data Cleaning and Imputation**:
   - Address the missing values in key columns, particularly for ISBNs and publication years. Imputation strategies could involve using the mode for categorical variables and the mean or median for numerical fields.

2. **Exploratory Data Analysis (EDA)**:
   - Conduct EDA to visualize the distribution of ratings, publication years, and authors. Histograms and box plots can provide insights into the data distribution and potential outliers.

3. **Author and Genre Analysis**:
   - Analyze the most prolific authors and their associated genres to identify trends. This could help in targeting marketing efforts or curating reading lists.

4. **Language Diversity**:
   - Explore the potential for expanding the dataset to include more non-English books, which could attract a broader audience.

5. **User Engagement Strategies**:
   - Leverage the availability of images to create visually appealing book recommendations or social media posts to engage users.

6. **Recommendation System Development**:
   - Utilize the average ratings and ratings count to develop a recommendation system that highlights popular books, enhancing user experience on the platform.

By implementing these recommendations, the dataset can be transformed into a more robust resource for both analysis and user engagement in the book community.

![Chart](./goodreads_heatmap_20241211_190543.png)
![Chart](./goodreads_barplot_20241211_190545.png)

## Sample Data

|   book_id |   goodreads_book_id |   best_book_id |   work_id |   books_count |      isbn |      isbn13 | authors                     |   original_publication_year | original_title                           | title                                                    | language_code   |   average_rating |   ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |   ratings_4 |   ratings_5 | image_url                                                  | small_image_url                                            |
|----------:|--------------------:|---------------:|----------:|--------------:|----------:|------------:|:----------------------------|----------------------------:|:-----------------------------------------|:---------------------------------------------------------|:----------------|-----------------:|----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|------------:|------------:|:-----------------------------------------------------------|:-----------------------------------------------------------|
|         1 |             2767052 |        2767052 |   2792775 |           272 | 439023483 | 9.78044e+12 | Suzanne Collins             |                        2008 | The Hunger Games                         | The Hunger Games (The Hunger Games, #1)                  | eng             |             4.34 |         4780653 |              4942365 |                    155254 |       66715 |      127936 |      560092 |     1481305 |     2706317 | https://images.gr-assets.com/books/1447303603m/2767052.jpg | https://images.gr-assets.com/books/1447303603s/2767052.jpg |
|         2 |                   3 |              3 |   4640799 |           491 | 439554934 | 9.78044e+12 | J.K. Rowling, Mary GrandPré |                        1997 | Harry Potter and the Philosopher's Stone | Harry Potter and the Sorcerer's Stone (Harry Potter, #1) | eng             |             4.44 |         4602479 |              4800065 |                     75867 |       75504 |      101676 |      455024 |     1156318 |     3011543 | https://images.gr-assets.com/books/1474154022m/3.jpg       | https://images.gr-assets.com/books/1474154022s/3.jpg       |
|         3 |               41865 |          41865 |   3212258 |           226 | 316015849 | 9.78032e+12 | Stephenie Meyer             |                        2005 | Twilight                                 | Twilight (Twilight, #1)                                  | en-US           |             3.57 |         3866839 |              3916824 |                     95009 |      456191 |      436802 |      793319 |      875073 |     1355439 | https://images.gr-assets.com/books/1361039443m/41865.jpg   | https://images.gr-assets.com/books/1361039443s/41865.jpg   |
|         4 |                2657 |           2657 |   3275794 |           487 |  61120081 | 9.78006e+12 | Harper Lee                  |                        1960 | To Kill a Mockingbird                    | To Kill a Mockingbird                                    | eng             |             4.25 |         3198671 |              3340896 |                     72586 |       60427 |      117415 |      446835 |     1001952 |     1714267 | https://images.gr-assets.com/books/1361975680m/2657.jpg    | https://images.gr-assets.com/books/1361975680s/2657.jpg    |
|         5 |                4671 |           4671 |    245494 |          1356 | 743273567 | 9.78074e+12 | F. Scott Fitzgerald         |                        1925 | The Great Gatsby                         | The Great Gatsby                                         | eng             |             3.89 |         2683664 |              2773745 |                     51992 |       86236 |      197621 |      606158 |      936012 |      947718 | https://images.gr-assets.com/books/1490528560m/4671.jpg    | https://images.gr-assets.com/books/1490528560s/4671.jpg    |
