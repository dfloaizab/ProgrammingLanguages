from Controller.movie_controller import MovieController
from View.MovieView import MovieView
from Repositories.mongodb_repository import MongoDB_MovieRep


if __name__ == "__main__":
    repo = MongoDB_MovieRep()
    view = MovieView()
    controller = MovieController(repo, view)
    controller.listAllMovies()