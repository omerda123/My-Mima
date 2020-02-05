from django.test import TestCase
from django.utils import timezone

from .models import Artist
from .models import Song
from .models import Fact


class QuestionModelTests(TestCase):
    def test_add_artist(self):
        king = Artist(name="King Crimson")
        self.assertEqual(king.name, "King Crimson")

    def test_add_song(self):
        king = Artist(name="King Crimson")
        epitaph = Song(name="Epitaph", artist_id=king)
        self.assertEqual(king.name, "King Crimson")
        self.assertEqual(epitaph.name, "Epitaph")
        self.assertEqual(epitaph.artist_id.name, "King Crimson")

    def test_add_fact(self):
        king = Artist(name="King Crimson")
        epitaph = Song(name="Epitaph", artist_id=king)
        fact = Fact(song_id=epitaph,
                    fact="This song title as well as the lyrics of this song refer to the message that is displayed on a gravestone. In this song, the singer is facing a struggle and fears that his epitaph will be \"confusion.\" Greg Lake, who was the bass player with the group for the In the Court of The Crimson King album (his only album with the band, as he left to form Emerson, Lake & Palmer), explained: 'Epitaph' is basically a song about looking with confusion upon a world gone mad. King Crimson had a strange ability to write about the future in an extremely prophetic way and the messages this song contains are even more relative today than they were when the song was originally written.",
                    author="Omer Daniel",
                    date_created=timezone.now())

        self.assertEqual(king.name == "King Crimson")
        self.assertEqual(epitaph.name, "Epitaph")
        self.assertEqual(epitaph.artist_id.name, "King Crimson")
        self.assertEqual(
            fact.fact,
            "This song title as well as the lyrics of this song refer to the message that is displayed on a gravestone. In this song, the singer is facing a struggle and fears that his epitaph will be \"confusion.\" Greg Lake, who was the bass player with the group for the In the Court of The Crimson King album (his only album with the band, as he left to form Emerson, Lake & Palmer), explained: 'Epitaph' is basically a song about looking with confusion upon a world gone mad. King Crimson had a strange ability to write about the future in an extremely prophetic way and the messages this song contains are even more relative today than they were when the song was originally written.",
        )
        self.assertEqual(fact.song_id.name, "Epitaph")
        self.assertEqual(fact.song_id.artist_id.name, "King Crimson")
        self.assertEqual(fact.author, "Omer Daniel")
