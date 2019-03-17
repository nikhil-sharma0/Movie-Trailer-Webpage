import media
import movie_webpage

avengers = media.Movie("Avengers: The Endgame", "Avengers end game, Thanos will lose.", "https://i.redd.it/u0hdkuizkz611.jpg", "https://www.youtube.com/watch?v=hA6hldpSTF8&t=3s")
print(avengers.storyline)

batman = media.Movie("Batman: The Dark Knight Rises", "Batman saving the Gotham as always.", "https://cdn.europosters.eu/image/750/posters/batman-dark-knight-rises-batman-rise-i12714.jpg", "https://www.youtube.com/watch?v=GokKUqLcvD8")
print(batman.storyline)
#dragon.show_tailer()

john_wick = media.Movie("John Wick 3", "He will kill everyone with a pencil.", "https://i.pinimg.com/originals/1b/03/a1/1b03a1a68c4616f8fb203d00a2849a9a.jpg", "https://www.youtube.com/watch?v=udnZjEIVwDs")
print(john_wick.storyline)
#john_wick.show_tailer()

toy_story = media.Movie("Toy Story 4", "Toys will come to life again.", "https://oyster.ignimgs.com/wordpress/stg.ign.com/2018/11/TS4_MIN_TSR_1s_WOODY_v5.0_Mech3.jpg", "https://www.youtube.com/watch?v=LDXYRzerjzU")
print(toy_story.storyline)

bohemian_rhapsody = media.Movie("Bohemian Rhapsody", "Watch Freddie Mercury live again.", "https://m.media-amazon.com/images/M/MV5BNDg2NjIxMDUyNF5BMl5BanBnXkFtZTgwMzEzNTE1NTM@._V1_SY1000_CR0,0,629,1000_AL_.jpg", "https://www.youtube.com/watch?v=mP0VHJYFOAU")
print(bohemian_rhapsody.storyline)

deadpool = media.Movie("Deadpool 2", "He's back with a bang.", "https://cdn.images.express.co.uk/img/dynamic/36/590x/secondary/DEADPOOL-2-1223473.jpg", "https://www.youtube.com/watch?v=D86RtevtfrA")
print(deadpool.storyline)

movies = [avengers, bohemian_rhapsody, toy_story, deadpool, batman, john_wick]

movie_webpage.open_movies_page(movies)