import os
import unittest
from auto_video_gen import gif_finder

class GifFinderTest(unittest.TestCase):
    def test_find_gifs_no_api_key(self):
        os.environ.pop('GIPHY_API_KEY', None)
        urls = gif_finder.find_gifs(['test line'])
        self.assertEqual(urls, [None])

if __name__ == '__main__':
    unittest.main()
