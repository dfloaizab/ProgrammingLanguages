from Model.movie import Movie
from View.MovieView import MovieView
from Repositories.movie_repository import IMovieRepository


class MovieController:

    def __init__(this, repository:IMovieRepository, view: MovieView):
        this.repo = repository
        this.view = MovieView

    # Implementación de una función de CRUD que sería llamada desde la vista
    # O le reportaría a la vista:
    def listAllMovies(this):
        moviesData = this.repo.getAll()
        #Visualiza la información a través del view:
        this.view.showMovies(moviesData)
