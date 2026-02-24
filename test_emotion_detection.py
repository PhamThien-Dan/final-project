import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Kiểm tra cảm xúc Joy
        res1 = emotion_detector("I am glad this happened")
        self.assertEqual(res1['dominant_emotion'], 'joy')
        
        # Kiểm tra cảm xúc Anger
        res2 = emotion_detector("I am really mad about this")
        self.assertEqual(res2['dominant_emotion'], 'anger')

if __name__ == "__main__":
    unittest.main()
