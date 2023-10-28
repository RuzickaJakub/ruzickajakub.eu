# NOPEA STATIC SITE GENERATOR

The purpose of the Nopea static site generator is - obviously - to generate a static website.

This comprise of the following:
- translate the markdown files with yaml metadata to html files using the templates based on the jinja2 engine [1]
- copy all the stylesheets, media and other static content
- create a smaller (and lower in quality) version of each .jpg image for faster loading.

That's is. Simple isn't it?

## Documentation

### Website generation
Generate a website with a command
```
./nopea_ssg/nopea_ssg.py generate
```
or run
```
./nopea_ssg/nopea_ssg.py generate -h
```
to get a detailed help about the arguments.

### Content metadata
The metadata can be arbitrary as far as they conform the yaml syntax. The parsed metadata are passed directly to the templating engine.

The only **important key** used inside the code is the `layout`, which defines which template should be used. The name of the template is the value of the `layout` concatenated with `.html`

Apart from `layout` following keys are currently used:
- `title`: title showed on the tab
- `lang`: language in which the page is written
- `introimage`: the path to the section image
- `photos`: containing the directory name, where photos are located and then list of image filenames and their caption to be used.

### Content
Everything after metadata is considered to be a content. The content is simply translated using the markdown.markdown function [2].

### Templates
When using `href` in the templates, prepend them with {{ SITE.path_to_root }}. This allows site to be viewed offline as a collection of html files.

For the template reference check [1].

### Python
The Black code formatter [3] and Pylint [4] are used so that the code has some quality.

## Links
- [1] [https://jinja.palletsprojects.com/en/3.1.x/](https://jinja.palletsprojects.com/en/3.1.x/)
- [2] [https://python-markdown.github.io/reference/](https://python-markdown.github.io/reference/)
- [3] [https://pypi.org/project/black/](https://pypi.org/project/black/)
- [4] [https://pypi.org/project/pylint/](https://pypi.org/project/pylint/)
