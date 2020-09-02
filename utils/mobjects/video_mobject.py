# from @pdcxs
# A VideoMobject to import videos, just like ImageMobject
# put videos into assets/videos folder

from manimlib.mobject.mobject import Mobject
from manimlib.mobject.types.image_mobject\
     import ImageMobject
from manimlib.utils.images import \
    get_full_video_path
from manimlib.constants import *
from manimlib.utils.config_ops import digest_config
from manimlib.utils.file_ops import seek_full_path_from_defaults

from math import floor
import cv2
import numpy as np

def get_full_video_path(video_file_name):
    return seek_full_path_from_defaults(
        video_file_name,
        default_dir=os.path.join("assets", "videos"),
        extensions=[".mp4", ".avi", ".wmv"]
    )

class VideoMobject(Mobject):
    CONFIG = {
        # need some information of the scene
        "scene": None
    }

    def __init__(self, filename, **kwargs):
        digest_config(self, kwargs)
        Mobject.__init__(self, **kwargs)
        path = get_full_video_path(filename)
        self.cap = cv2.VideoCapture(path)

        self.is_start = False

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        # Total frame num of the video
        self.frame_count = int(self.cap.get(
            cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps
        
        self.start_time = 0
        self.current_time = 0
        self.offset = 0

        r, i = self.cap.read()
        self.img = ImageMobject(i, **kwargs)
        self.add_updater(lambda v, dt: v.update_pixel())
        self.add(self.img)

    def start(self):
        self.is_start = True
        self.start_time = self.scene.get_time()

    def stop(self):
        self.is_start = False
        self.offset = self.current_time

    def update_pixel(self):
        if not self.is_start:
            return
        scene = self.scene

        scene_time = float(scene.get_time())
        self.current_time = scene_time - \
            self.start_time + self.offset

        frame_index = floor(self.current_time\
            / self.duration * self.frame_count)
        
        if frame_index >= self.frame_count:
            frame_index = self.frame_count - 1
            return

        self.cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            frame_index)
        
        returned, img = self.cap.read()

        self.img.pixel_array[:, :, :3] = np.array(img)
        self.img.pixel_array[:, :, 3] = 255

          
# A video named zhang.mp4 is placed in assets/videos folder
class VideoTest(Scene):
    def construct(self):
        video = VideoMobject("zhang", scene=self)
        video.start()

        self.add(video)
        self.wait(video.duration/2)
        video.stop()
        
        text = Text("现在停顿1秒",
            font='Microsoft YaHei')
        text.scale(0.8)
        text.move_to(UP*2)

        self.play(Write(text))
        self.wait()
        
        video.start()
        self.wait(video.duration/2)
