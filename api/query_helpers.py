"""SQLAlchemy Query Functions for MovieLens API"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import Optional

import model

# --- Films ---
def get_movie(db: Session, movie_id: int):
    """Récupère un film par son ID."""
    return db.query(model.Movie).filter(model.Movie.movieId == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genre: str = None):
    """Récupère une liste de films avec filtres optionnels."""
    query = db.query(model.Movie)
    
    if title:
        query = query.filter(model.Movie.title.ilike(f"%{title}%"))
    if genre:
        query = query.filter(model.Movie.genres.ilike(f"%{genre}%"))
    
    return query.offset(skip).limit(limit).all()

# --- Évaluations ---
def get_rating(db: Session, user_id: int, movie_id: int):
    """Récupère une évaluation en fonction du couple (userId, movieId)."""
    return db.query(model.Rating).filter(
        model.Rating.userId == user_id,
        model.Rating.movieId == movie_id
    ).first()


def get_ratings(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None, min_rating: float = None):
    """Récupère une liste d'évaluations avec filtres optionnels."""
    query = db.query(model.Rating)
    
    if movie_id:
        query = query.filter(model.Rating.movieId == movie_id)
    if user_id:
        query = query.filter(model.Rating.userId == user_id)
    if min_rating:
        query = query.filter(model.Rating.rating >= min_rating)
    
    return query.offset(skip).limit(limit).all()

# --- Tags ---
def get_tag(db: Session, user_id: int, movie_id: int, tag_text: str):
    """Récupère un tag par userId, movieId et le texte du tag."""
    return (
        db.query(model.Tag)
        .filter(
            model.Tag.userId == user_id,
            model.Tag.movieId == movie_id,
            model.Tag.tag == tag_text
        )
        .first()
    )


def get_tags(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    movie_id: Optional[int] = None, 
    user_id: Optional[int] = None
):
    """Récupère une liste de tags avec filtres optionnels."""
    query = db.query(model.Tag)

    if movie_id is not None:
        query = query.filter(model.Tag.movieId == movie_id)
    if user_id is not None:
        query = query.filter(model.Tag.userId == user_id)

    return query.offset(skip).limit(limit).all()


# --- Liens ---
def get_link(db: Session, movie_id: int):
    """Retourne le lien IMDB et TMDB associé à un film spécifique."""
    return db.query(model.Link).filter(model.Link.movieId == movie_id).first()

def get_links(db: Session, skip: int = 0, limit: int = 100):
    """Retourne une liste paginée de liens IMDB et TMDB de films."""
    return db.query(model.Link).offset(skip).limit(limit).all()

# --- Requêtes analytiques ---
def get_movie_count(db: Session):
    """Retourne le nombre total de films."""
    return db.query(model.Movie).count()

def get_rating_count(db: Session):
    """Retourne le nombre total d'évaluations."""
    return db.query(model.Rating).count()

def get_tag_count(db: Session):
    """Retourne le nombre total de tags."""
    return db.query(model.Tag).count()

def get_link_count(db: Session):
    """Retourne le nombre total de liens."""
    return db.query(model.Link).count()