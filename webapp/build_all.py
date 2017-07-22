import build_models
import build_library
import build_nltk
import logging


def build_files():
    logging.debug("Begin library building process.")
    build_nltk.main()
    build_library.main()
    build_models.main()
    logging.debug("Finish library building process.")


def main():
    build_files()


if __name__ == '__main__':
    main()
