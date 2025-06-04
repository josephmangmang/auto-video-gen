import os
import unittest
from auto_video_gen import script_generator

class ScriptGeneratorTest(unittest.TestCase):
    def test_generate_script_fallback(self):
        os.environ.pop('OPENAI_API_KEY', None)
        lines = script_generator.generate_script('hope', lines=4)
        self.assertEqual(len(lines), 4)
        self.assertTrue(all(isinstance(l, str) for l in lines))

if __name__ == '__main__':
    unittest.main()
