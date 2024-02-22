
import sys
import os

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'src')))

from ocr_watchdog import ImageHandler

def test_extract_text():
    handler = ImageHandler()
    # Correct the method name from 'process_image_path' to 'process_image'
    result = handler.process_image("./data/HelloWorld.jpeg")
    expected = "Hello, World|\n"
    print(result)
    assert result == expected
