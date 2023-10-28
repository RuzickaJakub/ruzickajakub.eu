#!/usr/bin/env python3
"""
Preprocessing for the overview template
"""
import os
import mdyml


def preprocess_overview(meta):
    """
    Add a `files` key to meta information. `files` is a list of tuples,
    where each tuple contains the html_path to the file, the title and date.
    These are used in the overview template to generate the topic dispatcher.

    Parameters
    ----------
    meta: list
        The page meta information loaded from the file. Must include
        input_filename, which is added by the generator.
    """
    directory = os.path.normpath(
        os.path.join(
            meta["input_filename"], meta["SITE"].path_to_root, meta["directory"]
        )
    )

    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        (file_meta, _) = mdyml.load_markdown_with_yaml_header_from_file(path)
        html_path = os.path.join(meta["directory"], filename.replace(".md", ".html"))
        files.append((html_path, file_meta["title"], file_meta["date"]))
    files.sort(key=lambda a: a[2])
    meta["files"] = files
    return meta
