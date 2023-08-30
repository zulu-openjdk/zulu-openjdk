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
    ver = directory.split('/')[-1]
    ver_path_dict[ver] = '{}/{}/Dockerfile'.format(github_base_path, directory[2:])

# Create a list with major versions like [6, 7]
versions = sorted([ver.removesuffix('-latest') for ver in ver_path_dict.keys() if "latest" in ver],
                  key=lambda version: '{0:0>90}'.format(version).lower())
versions.reverse()

# Created a sorted list of versions
versions_list = []
for ver in versions:
    versions_list += sorted([x for x in ver_path_dict.items()
                             if x[0][0] == ver or x[0][0:2] == ver],
                            key=lambda version: '{0:0>90}'.format(version[0]).lower())

# Enumerate items in the list with versions to use it in template as pointers to links
num_ver_dict = {}
for num, ver in enumerate(versions_list, start=11):  # links start from [11]
    num_ver_dict[num] = ver

# Split the dictionary by major versions
num_ver_dict_by_ver = {}
for version in versions:
    numbered_versions = {}
    for (num, ver) in num_ver_dict.items():
        if ver[0][0] == version.split('-')[0] \
                and version.split('-')[-1] == 'jre' \
                and (ver[0].split('-')[-1] == 'jre' or 'jre-latest' in ver[0]):
            numbered_versions[num] = ver
        elif ver[0][0:2] == version.split('-')[0] \
                and version.split('-')[-1] == 'jre' \
                and (ver[0].split('-')[-1] == 'jre' or 'jre-latest' in ver[0]):
            numbered_versions[num] = ver
        elif ver[0][0] == version.split('-')[0] \
                and version.split('-')[-1] == 'headless' \
                and (ver[0].split('-')[-1] == 'headless' or 'headless-latest' in ver[0]):
            numbered_versions[num] = ver
        elif ver[0][0:2] == version.split('-')[0] \
                and version.split('-')[-1] == 'headless' \
                and (ver[0].split('-')[-1] == 'headless' or 'headless-latest' in ver[0]):
            numbered_versions[num] = ver
        elif ver[0][0] == version.split('-')[0] \
                and version.split('-')[-1] == 'crac' \
                and (ver[0].split('-')[-1] == 'crac' or 'crac-latest' in ver[0]):
            numbered_versions[num] = ver
        elif ver[0][0:2] == version.split('-')[0] \
                and version.split('-')[-1] == 'crac' \
                and (ver[0].split('-')[-1] == 'crac' or 'crac-latest' in ver[0]):
            numbered_versions[num] = ver
        elif ver[0][0] == version.split('-')[0] \
                and version.isnumeric() \
                and 'jre' not in ver[0] and 'headless' not in ver[0]:
            numbered_versions[num] = ver
        elif ver[0][0:2] == version.split('-')[0] \
                and version.isnumeric() \
                and 'jre' not in ver[0] and 'headless' not in ver[0] and 'crac' not in ver[0]:
            numbered_versions[num] = ver

    num_ver_dict_by_ver[version] = numbered_versions

# Open a template
with open('README.j2') as temp_file:
    template = Template(temp_file.read(), autoescape=True)

# Render the template
rendered_temp = template.render(links=num_ver_dict_by_ver, versions=versions)

# Save a result to a file
with open('README.md', 'w') as f:
    f.write(rendered_temp)