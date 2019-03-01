import top100_spotify
import unittest


class TestSong(unittest.TestCase):
    def test1(self):
        with self.assertRaises(ValueError):
            song = top100_spotify.Song("Ed Sheeran", "Shape of You", 8.9, 0.7, -8, 0.8, 0.6, 0.1, 0.7, 100, 500000)
            song.danceability = 90
