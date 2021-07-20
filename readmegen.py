import os
import sys

from jinja2 import Template

github_base_path = 'https://github.com/zulu-openjdk/zulu-openjdk/blob/master'

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])
    github_base_path += '/{}'.format(sys.argv[1])

# Create a list of directories that names start with a digit
ubuntu_dirs = [x[0] for x in os.walk('.') if len(x[0]) > 2 and x[0][2].isdigit()]

ver_path_dict = {}

# Create a dictionary with OpenJDK versions and paths to Dockerfiles
for directory in ubuntu_dirs:
    ver = directory.split('-')[0][2:]
    ver_path_dict[ver] = '{}/{}/Dockerfile'.format(github_base_path, directory[2:])

# Create a list with major versions like [6, 7]
versions = sorted([ver for ver in ver_path_dict.keys() if 1 <= len(ver) <= 3],
                  key=lambda version: '{0:0>9}'.format(version).lower())

# Created a sorted list of versions
versions_list = []
for ver in versions:
    versions_list += sorted([x for x in ver_path_dict.items()
                             if x[0][0] == ver or x[0][0:2] == ver],
                            key=lambda version: '{0:0>9}'.format(version[0]).lower())

# Enumerate items in the list with versions to use it in template as pointers to links
num_ver_dict = {}
for num, ver in enumerate(versions_list, start=10):
    num_ver_dict[num] = ver

# Split the dictionary by major versions
num_ver_dict_by_ver = {}
for version in versions:
    num_ver_dict_by_ver[version] = {num: ver for (num, ver) in num_ver_dict.items() if
                                    ver[0][0] == version or ver[0][0:2] == version}

# Open a template
with open('README.j2') as temp_file:
    template = Template(temp_file.read(), autoescape=True)

# Render the template
rendered_temp = template.render(links=num_ver_dict_by_ver, versions=versions)

# Save a result to a file
with open('README.md', 'w') as f:
    f.write(rendered_temp)
