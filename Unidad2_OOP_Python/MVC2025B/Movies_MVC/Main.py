from Model import *
from Movies_MVC.Repositories.movie_repository import *
from Movies_MVC.Repositories.mongodb_repository import *


# Principio "L": Principio de sustitución de Liskov: puede usarse una subclase en reemplazo de su superclase
# sin afectar el funcionamiento del módulo o del sistemas completo:
repo: IMovieRepository = MongoDB_MovieRep()
lista_todas_peliculas = repo.getAll()
