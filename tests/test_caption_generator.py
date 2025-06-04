import os
import tempfile
import unittest
from auto_video_gen import caption_generator

class CaptionGeneratorTest(unittest.TestCase):
    def test_format_timestamp(self):
        self.assertEqual(caption_generator.format_timestamp(1.5), '00:00:01,500')

    def test_generate_srt(self):
        lines = ['line one', 'line two']
        timestamps = [(0, 1), (1, 2)]
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, 'captions.srt')
            result = caption_generator.generate_srt(lines, timestamps, path)
            self.assertTrue(os.path.exists(result))
            with open(result, 'r', encoding='utf-8') as f:
                content = f.read()
            self.assertIn('line one', content)
            self.assertIn('00:00:00,000 --> 00:00:01,000', content)

if __name__ == '__main__':
    unittest.main()
