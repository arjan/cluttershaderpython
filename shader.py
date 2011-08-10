import sys
from gi.repository import Clutter

class Test:

    def __init__(self):
        self.stage = Clutter.Stage()

        r = Clutter.Texture.new_from_file("/home/arjan/Desktop/arjan.jpg")
        r.set_size(640, 480)
        self.stage.add_actor(r)
        shader = Clutter.Shader()
        source = open(__file__.replace(".py", ".glsl"), "r").read()
        shader.set_fragment_source(source, len(source))
        shader.set_uniform("image", 0)
        r.set_shader(shader)
        self.stage.show()


def main():
    Clutter.init(sys.argv)
    Test()
    Clutter.main()


if __name__ == "__main__":
    main()

