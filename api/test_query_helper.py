from database import SessionLocal
from query_helpers import *

db=SessionLocal()

#######Test  table Movies
###test 1
# movie= get_movie(db,1)
# print(movie.title)

#test 2
# movies=get_movies(db,limit=5)
# for film in movies:
#     print(film.title)

#######Test table rating
##test1 :récuperation de l'évaluation du film 1 par l'utilisateur 1
# rating =get_rating(db,movie_id=1,user_id=1)
# print(f"user id :{rating.userId} movie: {rating.movie.title} évaluation: {rating.rating}")

##test2: récupération des 10 premiers films ayant une valeur minimum d'évaluation de 3.5
# ratings=get_ratings(db,min_rating=3.5, limit=10)
# for rating in ratings:
#     print(f"film :{rating.movie.title} évaluation: {rating.rating}")

####"table tags"
# tag=get_tag(db,user_id=2,movie_id=60756,tag_text="funny")
# print(tag)
# print(f"user id: {tag.userId}, movie_id: {tag.movieId}, tag :{tag.tag}")


###test sur le nombre de film
nb_film=get_movie_count(db)
print(nb_film)

###test sur le nombre de links
nb_links=get_link_count(db)
print(nb_links)
db.close()
