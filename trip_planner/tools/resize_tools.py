from langchain.tools import tool
import io
from PIL import Image

class ResizeTools():

  @tool("resize_image")
  def resize_image(self,input_url):
    """Resize an image from a given URL to a new width while maintaining aspect ratio."""
    new_width = 800
    try:
        response = requests.get(input_url)
        img = Image.open(io.BytesIO(response.content))
        print(img)

        width_percent = (new_width / float(img.size[0]))
        new_height = int((float(img.size[1]) * float(width_percent)))

        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        return resized_img
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None
