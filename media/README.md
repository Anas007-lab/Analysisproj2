# Analysis Report

### Dataset Summary

The dataset, `media.csv`, consists of 2,652 entries and 8 columns, capturing various attributes related to media items, including their publication date, language, type, title, author, and ratings on overall quality, quality, and repeatability. The columns include:

- **date**: Publication date of the media item (99 missing values)
- **language**: Language of the media (no missing values)
- **type**: Type of media (no missing values)
- **title**: Title of the media (no missing values)
- **by**: Author or creator of the media (262 missing values)
- **overall**: Overall rating (no missing values)
- **quality**: Quality rating (no missing values)
- **repeatability**: Repeatability rating (no missing values)

### Key Insights

1. **Missing Values**: The dataset contains missing values in the `date` (99) and `by` (262) columns. This could impact analyses that rely on these fields, particularly in time-based or author-based studies.

2. **Language**: The dataset includes media in 11 different languages, with a predominant frequency for English (1,306 instances). This suggests a significant bias towards English-language media.

3. **Media Type**: The majority of entries are classified as 'movie' (2,211 entries), indicating a focus on this type of media. This could limit the insights drawn for other types.

4. **Rating Distributions**:
   - **Overall Ratings**: The mean overall rating is approximately 3.05, with a standard deviation of 0.76, indicating a generally positive reception but with variability.
   - **Quality Ratings**: The average quality rating is around 3.21, again suggesting positive feedback from users.
   - **Repeatability Ratings**: The average repeatability rating is lower (1.49), suggesting that media items are not commonly revisited by viewers, which could influence marketing strategies or content development.

5. **Title and Author Popularity**: The most frequent title is "Kanda Naal Mudhal," with 9 occurrences, while "Kiefer Sutherland" is the most frequent author with 48 occurrences, indicating that a small number of titles and authors dominate the dataset.

### Recommendations

1. **Address Missing Data**: Consider strategies to fill in missing values for `date` and `by`. For instance, if the data is time-sensitive, imputation based on other similar records could enhance the dataset.

2. **Expand Media Types**: To provide a more comprehensive analysis, future data collection could include additional media types beyond movies, such as TV shows, documentaries, or online content.

3. **Analyze Language Distribution**: Conduct further analysis on language-related trends to understand the audience better. This could involve examining ratings by language to see if there are significant differences in audience reception.

4. **Investigate Ratings Correlations**: A more detailed analysis could be done to explore the relationships between overall, quality, and repeatability ratings. Understanding these correlations can help identify what aspects of media content viewers value most.

5. **Marketing Strategy**: Given the lower repeatability ratings, consider strategies to increase viewer engagement, such as promotional campaigns, sequels, or spin-offs of popular titles.

By addressing these insights and recommendations, stakeholders can enhance the dataset's utility and derive richer insights for decision-making.

![Chart](./media_heatmap.png)
![Chart](./media_barplot.png)

## Sample Data

| date      | language   | type   | title       | by                            |   overall |   quality |   repeatability |
|:----------|:-----------|:-------|:------------|:------------------------------|----------:|----------:|----------------:|
| 15-Nov-24 | Tamil      | movie  | Meiyazhagan | Arvind Swamy, Karthi          |         4 |         5 |               1 |
| 10-Nov-24 | Tamil      | movie  | Vettaiyan   | Rajnikanth, Fahad Fazil       |         2 |         2 |               1 |
| 09-Nov-24 | Tamil      | movie  | Amaran      | Siva Karthikeyan, Sai Pallavi |         4 |         4 |               1 |
| 11-Oct-24 | Telugu     | movie  | Kushi       | Vijay Devarakonda, Samantha   |         3 |         3 |               1 |
| 05-Oct-24 | Tamil      | movie  | GOAT        | Vijay                         |         3 |         3 |               1 |
