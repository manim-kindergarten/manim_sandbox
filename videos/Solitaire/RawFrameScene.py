# from @RY-Givenchy

#
# Copyright: 2020 niedong
# Raw frame operation scene for manim
#
# Originally written to accelerate the
# process of writing each frame for
# my solitaire video. It would be about
# 1000-10000 times slower without
# acceleration, due to how manim handles
# each frame.
#

from manimlib.imports import *


class RawFrameScene(Scene):
    CONFIG = {
        "objects_buffer": []
    }

    def open_pipe(self):
        self.file_writer.open_movie_pipe()

    def close_pipe(self):
        self.file_writer.close_movie_pipe()

    def print_frame_message(self):
        print("Capturing raw frame: {}\r".format(self.num_plays), end="")

    def add_plays(self):
        self.num_plays += 1

    def write_frame(self, frame):
        self.file_writer.write_frame(frame)
        self.add_plays()

    def append_to_buffer(self, objects):
        self.objects_buffer.append(objects)

    def capture_on_frame(self, capture_objects):
        self.update_frame(capture_objects, self.get_frame())
        self.append_to_buffer(capture_objects)
        self.write_frame(self.get_frame())
        self.print_frame_message()

    def capture(self, capture_objects):
        self.open_pipe()
        self.capture_on_frame(capture_objects)
        self.close_pipe()
        return self

    def clear_objects_buffer(self):
        self.objects_buffer.clear()

    def append_to_mobjects(self, clear=True):
        self.add(*self.objects_buffer)
        if clear:
            self.clear_objects_buffer()
