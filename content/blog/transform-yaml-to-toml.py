import yaml
import sys 

def output_toml(obj):
    result = f"""+++
title = \"{obj['title'].strip()}\"
date = {obj['date']}
"""
    
    if 'draft' in obj:
        result += "draft = true\n"
    if 'photos' in obj:
        for photo in obj['photos']['items']:
            for key in photo.keys():
                file = key
                caption = photo[key]
                result += f"""[[extra.photos]]
file = \"{file.strip()}\"
caption = \"{caption.strip()}\"
"""
    result += "+++"
    return result

def parse_yaml(lines):
    """
    Splits lines into YAML header and actual contents.

    YAML header is surrounded by triple dash (---) and must be at
    the beginning of the file.

    Returns
    -------
    Tuple of dictionary (parsed YAML header) and contents.
    """

    header = []
    content = []
    header_found = False

    inside_content = False
    for line in lines:
        line = line.rstrip()
        if line == "---":
            if header_found:
                inside_content = True
            header_found = True
            continue
        if inside_content:
            content.append(line)
        else:
            header.append(line)

    if not header_found:
        content = header
        header = []
    header_dict = yaml.load("\n".join(header), Loader=yaml.FullLoader)
    if not header_dict:
        header_dict = {}
    return (header_dict, "\n".join(content))


if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'r') as fil:
       lines = fil.readlines()
       if lines[0].strip() == '+++':
           print(fil.read())
        
    (yaml, content) = parse_yaml(lines)

    toml = output_toml(yaml)
    result = toml + content
    print(result)
