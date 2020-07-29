# from @RY-Givenchy

#
# Copyright: 2020 niedong
# Raw frame operation scene for manim
#

from manimlib.scene.scene import Scene
from manimlib.constants import *
import threading
import time


class RawFrameScene(Scene):
    CONFIG = {
        "num_frames": 0,
        "msg_flag": True
    }

    def write_frame(self, frame):
        self.file_writer.write_frame(frame)
        self.num_frames += 1

    def write_current_frame(self):
        self.write_frame(self.get_frame())

    def capture(self, mobjects, write_current_frame=True):
        """
        Capture mobjects on the current frame, write to movie if possible.

        :param mobjects: instance of Mobject to be captured.
        :param write_current_frame: boolean value, whether to write current frame to movie.
        """
        self.update_frame(mobjects, self.get_frame())
        if write_current_frame:
            self.write_current_frame()
        return self

    def print_frame_message(self, msg_end="\r"):
        sec = int(self.num_frames / self.camera.frame_rate)
        print("Capturing raw frame: {}. Video duration: {} min {:2d} sec".format(
            self.num_frames, sec // 60, sec % 60), end=msg_end)

    def setup_thread(self):
        def thread_func():
            while self.msg_flag:
                self.print_frame_message()
                time.sleep(1)

        thread = threading.Thread(target=thread_func, daemon=True)
        setattr(self, "msg_thread", thread)

    # Normally, 'self.setup' method is called automatically before 'self.construct'.
    # However, if 'self.setup' method is override, call 'super().setup' manually.
    def setup(self):
        """
        Setup method for RawFrameScene. A must call before using this scene.
        """
        self.file_writer.open_movie_pipe()
        self.setup_thread()
        self.msg_thread.start()

    # Normally, 'self.tear_down' method is called automatically after 'self.construct'.
    # However, if 'self.tear_down' method is override, call 'super().tear_down' manually.
    def tear_down(self):
        """
        Finish method for RawFrameScene. A must call after using this scene.
        """
        self.file_writer.close_movie_pipe()
        setattr(self, "msg_flag", False)
        self.msg_thread.join()
        self.print_frame_message(msg_end="\n")
        self.num_plays += 1

    def play(self, *args, **kwargs):
        """
        'self.play' method fails in this scene. Do not use it.
        """
        raise Exception("""
            'self.play' method is not allowed to use in this scene
            Use 'self.capture(...)' instead
        """)

    def wait(self, duration=DEFAULT_WAIT_TIME, stop_condition=None):
        for i in range(int(duration * self.camera.frame_rate)):
            self.write_current_frame()

    def clear(self):
        self.reset_camera()
