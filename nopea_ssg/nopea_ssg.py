#!/usr/bin/env python3
"""
Nopea static site generator
"""

import argparse
import os
import pathlib
import sys
import shutil

from jinja2 import Environment, FileSystemLoader
from markdown import markdown
from PIL import Image
import files
import mdyml
import sass


class Page:
    """
    Page info.

    Attributes
    ----------
    title: str
        Title of the page.
    link: str
        Relative link to the page from the site root
    """

    def __init__(self, title, link):
        """Create page with title and link"""
        self.title = title
        self.link = link


class Site:
    """
    The whole website info.

    Attributes
    ----------
    path_to_root: str
        Path to the root of the website.
    """

    def __init__(self, root_dir, path_file_in):
        """Creat site and calculate SITE.path_to_root"""
        path = os.path.relpath(root_dir, os.path.dirname(path_file_in))
        path = os.path.join(path, "")
        self.path_to_root = path


def generate_one_file(env, base_dir, input_filename, destination_filename):
    """
    Generate one HTML file from Markdown source.

    Parameters
    ----------
    env: Environment
        Environment for template loading.
    base_dir: str
        Base directory with content
    input_filename: str
        Filename to process.
    destination_filename: str
        Where to store the converted file.
    """

    print(f"{input_filename} => {destination_filename}")
    (meta, content) = mdyml.load_markdown_with_yaml_header_from_file(input_filename)

    meta["SITE"] = Site(base_dir, input_filename)
    meta["content"] = content
    template = env.get_template(meta["layout"] + ".html")
    rendered = template.render(meta)

    with open(destination_filename, "w", encoding="UTF-8") as out:
        out.write(rendered)


def get_html_filename(relative_markdown_filename):
    """
    Get HTML filename from given Markdown filename.
    """

    return os.path.splitext(relative_markdown_filename)[0] + ".html"


def markdownify(content):
    """Define filter to be passed to jinja2 rendering engine"""
    return markdown(content)


def copy_static(static_dir, destination_dir):
    """
    Copy static files. For the .jpg images also create their compressed version.

    Parameters
    ----------
    static_dir: str
        The source directory.
    destination_dir: str
        The destination directory.
    """
    for file_in, file_in_rel, relative_dirname in files.relative_paths_walk(static_dir):
        dir_out = os.path.join(destination_dir, relative_dirname)
        file_out = os.path.join(destination_dir, file_in_rel)
        pathlib.Path(dir_out).mkdir(parents=True, exist_ok=True)
        shutil.copy(file_in, file_out)
        _, file_extension = os.path.splitext(file_in)
        if file_extension in [".jpg", ".jpeg"]:
            file_out_compressed = file_out + "-compressed.jpg"
            if not os.path.exists(file_out_compressed):
                compress_photo(file_in, file_out_compressed, quality=30)


def compress_photo(file_in, file_out, quality):
    """
    Compress the photo by reducing it's quality

    Parameters
    ----------
    file_in: str
        Source file to be compressed.
    file_out: str
        Destination for the compressed file.
    quality: int
        The quality of the result.
    """
    image = Image.open(file_in)
    image.save(file_out, quality=quality, optimize=True)


def action_generate(content_dir, templates_dir, static_dir, destination_dir, sass_dir):
    """
    Callback for the `generate` action.

    Parameters
    ----------
    content_dir: str
        Path to directory with input Markdown files.
    templates_dir: str
        Path to directory with Jinja templates.
    static_dir: str
        Path to directory with static files (CSS, images etc.).
    destinatation_dir: str
        Path to directory where to put the generated files.
    """
    # Compile css files
    sass.compile(dirname=(sass_dir, destination_dir))

    # Copy static files
    copy_static(static_dir, destination_dir)

    # Initialize Jinja2
    file_loader = FileSystemLoader(templates_dir)
    environment = Environment(loader=file_loader)
    environment.filters["markdownify"] = markdownify

    # Generate html files
    for file_in, file_in_rel, relative_dirname in files.relative_paths_walk(
        content_dir, "*.md"
    ):
        dir_out = os.path.join(destination_dir, relative_dirname)
        file_out = os.path.join(destination_dir, get_html_filename(file_in_rel))
        pathlib.Path(dir_out).mkdir(parents=True, exist_ok=True)
        generate_one_file(environment, content_dir, file_in, file_out)


def main():
    """
    Entry point of the whole program.

    Only parses command-line arguments and executes the right callback.
    """

    args = argparse.ArgumentParser(description="My SSG")
    args_sub = args.add_subparsers(help="Select what to do")
    args.set_defaults(action="help")
    args_help = args_sub.add_parser("help", help="Show this help.")
    args_help.set_defaults(action="help")

    args_version = args_sub.add_parser("version", help="Show version of this tool.")
    args_version.set_defaults(action="version")

    args_generate = args_sub.add_parser("generate", help="Generate the web.")
    args_generate.set_defaults(action="generate")
    args_generate.add_argument(
        "--content",
        dest="content_dir",
        default="content/",
        metavar="PATH",
        help="Directory with source (content) files.",
    )
    args_generate.add_argument(
        "--templates",
        dest="templates_dir",
        default="templates/",
        metavar="PATH",
        help="Directory with Jinja templates.",
    )
    args_generate.add_argument(
        "--static",
        dest="static_dir",
        default="static/",
        metavar="PATH",
        help="Directory with static files (images, styles, ...).",
    )
    args_generate.add_argument(
        "--destination",
        dest="destination_dir",
        default="out/",
        metavar="PATH",
        help="Directory where to store the result.",
    )
    args_generate.add_argument(
        "--sass",
        dest="sass_dir",
        default="sass/",
        metavar="PATH",
        help="Directory with sass stylesheet files.",
    )

    if len(sys.argv) < 2:

        class HelpConfig:
            """Fallback in case no argument is passed"""

            def __init__(self):
                self.action = "help"

        config = HelpConfig()
    else:
        config = args.parse_args()

    if config.action == "help":
        args.print_help()
    elif config.action == "version":
        print("Version 1.0")
    elif config.action == "generate":
        action_generate(
            config.content_dir,
            config.templates_dir,
            config.static_dir,
            config.destination_dir,
            config.sass_dir,
        )
    else:
        raise Exception("Internal error, unknown action")


if __name__ == "__main__":
    main()
