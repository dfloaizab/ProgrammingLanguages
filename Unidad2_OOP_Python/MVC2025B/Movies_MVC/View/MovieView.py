class MovieView:
    
    def showMovies(this,movies):
        print("Esta es la lista de todas las películas en la BD:\n")
        for m in movies:
            print(f"-{m.title} ({m.year}, {m.genre})")