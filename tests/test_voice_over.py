import unittest
from auto_video_gen import voice_over

class VoiceOverTest(unittest.TestCase):
    def test_estimate_duration(self):
        dur = voice_over._estimate_duration('three words here', words_per_minute=60)
        # 3 words at 60 wpm -> 3 seconds
        self.assertAlmostEqual(dur, 3.0, places=2)

if __name__ == '__main__':
    unittest.main()
