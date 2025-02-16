import streamlit as st

# Sidebar with profile links
st.sidebar.title("About")
st.sidebar.write("## Google Play Store Analytics")
st.sidebar.write(
    "This application provides insights into the Google Play Store, "
    "visualizing various trends such as app categories, user ratings, sentiment distribution, and revenue generation."
)
st.sidebar.write("### Connect with Me:")
st.sidebar.markdown(
    "[![GitHub](https://img.shields.io/badge/GitHub-Profile-informational?style=flat&logo=github)](https://github.com/s1reyash)"
)
st.sidebar.markdown(
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/shreyash8421/)"
)

# Main App Title
st.title("📊 Google Play Store Review Insights")
st.write(
    "This dashboard provides an analytical view of the Google Play Store, "
    "focusing on key metrics such as category distribution, revenue, ratings, and update trends."
)
st.markdown("---")

# List of HTML files and their descriptions
plots = [
    {"file": "plotes/top_10_categories.html","title":"Top Categories with the Highest Number of Apps","description":"The distribution of top categories on the Play Store reveals that Tools, Entertainment, and Productivity apps dominate in terms of popularity and prevalence. Tools consistently occupy the largest share, reflecting the high demand for utility apps that enhance functionality and user convenience."},
    {"file": "plotes/category_pie_Graph2.html","title":"Categories Represented through Pie Chart","description":"The pie chart illustrates the percentage distribution of the top categories on the Play Store. Tools apps lead, followed by Entertainment and Productivity apps, showcasing user preferences."},
    {"file": "plotes/type_Graph3.html","title":"Type Distribution","description":"Most apps on the Play Store are free, following a strategy of user acquisition through free access and later monetizing via ads or premium features."},
    {"file": "plotes/Rating_Graph4.html","title":"Rating Distribution","description":"Ratings on the Play Store are mostly high, indicating user satisfaction. This suggests that well-rated apps tend to deliver a good user experience."},
    {"file": "plotes/Sentiment_Distribution.html","title":"Sentiment Distribution","description":"Sentiment analysis of reviews shows a mix of positive and negative feedback, with a generally positive sentiment dominating."},
    {"file": "plotes/Install_graph6.html","title":"Mostly Installed Categories","description":"Games are among the most installed apps, reflecting the high demand for entertainment and leisure activities on mobile devices."},
    {"file": "plotes/Updates_over_the_year_graph07.html","title":"Updates over the Years","description":"Over time, apps are receiving more frequent updates, indicating developers' commitment to bug fixes, feature enhancements, and improved user experience."},
    {"file": "plotes/Revenue_by_category graph6.html","title":"Revenue By Category","description":"Business and Productivity apps generate the most revenue, often through subscription models and premium features."},
    {"file": "plotes/Genres_Graph9.html","title":"Top Genres","description":"Genres like Action, Casual, and Tools are popular, reflecting user preferences for engaging games and utility apps."},
    {"file": "plotes/updates_vs_rating_graph.html","title":"Updates Vs Rating","description":"A weak correlation exists between update frequency and app ratings, suggesting that frequent updates do not always guarantee higher ratings."},
    {"file": "plotes/PaidFree_rating_graph11.html","title":"Type Vs Rating","description":"Paid apps generally have higher ratings than free apps, indicating that users expect premium-quality features from paid applications."},
]

# Loop through the plots and display each with its description
for i, plot in enumerate(plots):
    st.subheader(f"📌 {plot['title']}")
    st.write(plot["description"])
    with open(plot["file"], "r", encoding="utf-8") as file:
        html_content = file.read()
        st.components.v1.html(html_content, height=400)  # Display HTML visualization

st.markdown("---")
st.markdown("### Made by [Shreyash](https://github.com/s1reyash)")
