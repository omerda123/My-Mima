from django.test import TestCase
from django.utils import timezone

from .models import Artist
from .models import Song
from .models import Fact


class QuestionModelTests(TestCase):
    def setUp(self):
        king = Artist.objects.create(name="King Crimson", mima_id=1)
        epitaph = Song.objects.create(name="Epitaph", artist=king, mima_id=2)
        fact = Fact.objects.create(song=epitaph,
                                   fact="This song title as well as the lyrics of this song refer to the message that is displayed on a gravestone. In this song, the singer is facing a struggle and fears that his epitaph will be \"confusion.\" Greg Lake, who was the bass player with the group for the In the Court of The Crimson King album (his only album with the band, as he left to form Emerson, Lake & Palmer), explained: 'Epitaph' is basically a song about looking with confusion upon a world gone mad. King Crimson had a strange ability to write about the future in an extremely prophetic way and the messages this song contains are even more relative today than they were when the song was originally written.",
                                   author="Omer Daniel",
                                   date_created=timezone.now())

    def test_add_fact(self):
        artist = Artist.objects.get(name="King Crimson")
        song = Song.objects.get(name="Epitaph")
        fact = Fact.objects.get(author="Omer Daniel")

        self.assertEqual(artist.name , "King Crimson")
        self.assertEqual(song.name, "Epitaph")
        self.assertEqual(song.artist.name, "King Crimson")
        self.assertEqual(
            fact.fact,
            "This song title as well as the lyrics of this song refer to the message that is displayed on a gravestone. In this song, the singer is facing a struggle and fears that his epitaph will be \"confusion.\" Greg Lake, who was the bass player with the group for the In the Court of The Crimson King album (his only album with the band, as he left to form Emerson, Lake & Palmer), explained: 'Epitaph' is basically a song about looking with confusion upon a world gone mad. King Crimson had a strange ability to write about the future in an extremely prophetic way and the messages this song contains are even more relative today than they were when the song was originally written.",
        )
        self.assertEqual(fact.song.name, "Epitaph")
        self.assertEqual(fact.song.artist.name, "King Crimson")
        self.assertEqual(fact.author, "Omer Daniel")
