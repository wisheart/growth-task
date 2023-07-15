from moviepy.editor import *

clip = (VideoFileClip("./video/dance.mp4")
          .subclip(1,3)
          .resize(0.5))
clip.write_gif("./video/dance.gif")