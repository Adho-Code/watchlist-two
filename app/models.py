class Movie:
    '''
    Movie class to define Movie objects
    '''

    def __init__(self,id,title,overview,poaster,vote_average,vote_count):
        self.id =id
        self.title =title
        self.overview =overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poaster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,reviews):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = reviews

    def save_review(self):
        Review.all_reviews.clear()

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response