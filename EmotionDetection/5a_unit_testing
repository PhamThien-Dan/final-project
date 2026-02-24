import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Kiểm tra trường hợp văn bản vui vẻ (Joy)
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Kiểm tra trường hợp văn bản giận dữ (Anger)
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(res2['dominant_emotion'], 'anger')
        
        # Kiểm tra trường hợp văn bản chán ghét (Disgust)
        result_3 = emotion_detector('I am feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # Kiểm tra trường hợp văn bản buồn bã (Sadness)
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        # Kiểm tra trường hợp văn bản sợ hãi (Fear)
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
