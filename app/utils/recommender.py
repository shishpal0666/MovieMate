
from app.models.models import UserSearch
from app.utils.tmdb import fetch_tmdb_results
from app.utils.history_recommender import recommend_from_history

def get_user_recommendations(user_id, top_n=32):
    user_searches = UserSearch.objects(user=user_id).order_by('-timestamp').limit(15)
    movie_titles = [r.movie_title for r in user_searches]

    if not movie_titles:
        return []

    recommended_df = recommend_from_history(movie_titles, top_n=top_n)

    rec_movies = []
    if not recommended_df.empty:
        for _, row in recommended_df.iterrows():
            results = fetch_tmdb_results(row['title'])
            if results:
                rec_movies.append(results[0])

    return rec_movies
