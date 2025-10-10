from movie_repository import IMovieRepository

# SE APLICA LA "O" DE SOLID: cada repositorio concreto, implementa las operaciones para un store 
# específico
class MongoDB_MovieRep(IMovieRepository):

    def getAll(this):
        #return super().getAll()
        return[
            {"title":"Inception","year":"2010","genre":"SciFi","Director":"Chistopher Nolan"},
            {"title":"1917","year":"2021","genre":"Historical","Director":"Sam Mendes"},
        ]