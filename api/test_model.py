from database import SessionLocal
from model import *

db=SessionLocal()

# ##tester la récupération de quelques film
# movies=db.query(Movie).limit(10).all()
# movies

# for movie in movies:
#     print(movie.title)

# ##tester le rating
# ratings=db.query(Rating).limit(10).all()
# ratings

# for rating in ratings:
#     print(rating.timestamp)


# ##rester le tags
# tags=db.query(Tag).limit(10).all()
# tags

# for tag in tags:
#     print(tag.tag)

# ##rester le links
# links=db.query(Link).limit(10).all()
# links

# for link in links:
#     print(link.imdbId)


# action_movie=db.query(Movie).filter(Movie.genres.contains("Action")).limit(10).all()
# for mv in action_movie:
#     print(mv.title)


##récupération des films ayant pour notes supérieur à 4

movie_note=(
    db.query(Movie.title,Rating.rating)
    .join(Rating)
    .filter(Rating.rating >=4)
    .limit(5)
    .all()
)

for title, rating in movie_note:
    print(f"titre :{title} ,rating :{rating}")

###fermer la connexion
db.close()