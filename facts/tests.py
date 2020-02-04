from django.test import TestCase
from django.utils import timezone

from .models import Artists
from .models import Songs
from .models import Facts


class QuestionModelTests(TestCase):
    def test_add_artist(self):
        king = Artists(name="King Crimson")
        self.assertIs(king.name == "King Crimson", True)

    def test_add_song(self):
        king = Artists(name="King Crimson")
        epitaph = Songs(name="Epitaph", artist_id=king)
        self.assertIs(king.name == "King Crimson", True)
        self.assertIs(epitaph.name == "Epitaph", True)
        self.assertIs(epitaph.artist_id.name == "King Crimson", True)

    def test_add_fact(self):
        king = Artists(name="King Crimson")
        epitaph = Songs(name="Epitaph", artist_id=king)
        fact = Facts(song_id=epitaph, fact="This song title as well as the lyrics of this song refer to the message that is displayed on a gravestone. In this song, the singer is facing a struggle and fears that his epitaph will be \"confusion.\" Greg Lake, who was the bass player with the group for the In the Court of The Crimson King album (his only album with the band, as he left to form Emerson, Lake & Palmer), explained: 'Epitaph' is basically a song about looking with confusion upon a world gone mad. King Crimson had a strange ability to write about the future in an extremely prophetic way and the messages this song contains are even more relative today than they were when the song was originally written.")
        self.assertIs(king.name == "King Crimson", True)
        self.assertIs(epitaph.name == "Epitaph", True)
        self.assertIs(epitaph.artist_id.name == "King Crimson", True)
        self.assertIs(fact.fact == "This song title as well as the lyrics of this song refer to the message that is displayed on a gravestone. In this song, the singer is facing a struggle and fears that his epitaph will be \"confusion.\" Greg Lake, who was the bass player with the group for the In the Court of The Crimson King album (his only album with the band, as he left to form Emerson, Lake & Palmer), explained: 'Epitaph' is basically a song about looking with confusion upon a world gone mad. King Crimson had a strange ability to write about the future in an extremely prophetic way and the messages this song contains are even more relative today than they were when the song was originally written.", True)
        self.assertIs(fact.song_id.name == "Epitaph", True)
        self.assertIs(fact.song_id.artist_id.name == "King Crimson", True)

