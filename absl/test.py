import logging as py_logging
from absl import app
from absl import flags
from absl import logging

flags.DEFINE_integer('in_height', 10, 'The height of input.', lower_bound=1, short_name='h')
flags.DEFINE_integer('in_width', 3, 'The width of input.', lower_bound=1, short_name='w')
flags.DEFINE_integer('out_width', 7, 'The width of input.', lower_bound=1, short_name='o')

FLAGS = flags.FLAGS

formatter = py_logging.Formatter('[%(levelname)s %(asctime)s %(filename)s:%(lineno)s] %(message)s')
logging.get_absl_handler().setFormatter(formatter)


def demo(in_height, in_width, out_width):
    print(f"{in_height},{in_width},{out_width}")
    pass


def main(argv):
    demo(FLAGS.in_height, FLAGS.in_width, FLAGS.out_width)


if __name__ == "__main__":
    app.run(main)
