import copy
import os

from bs4 import BeautifulSoup

source_path = "profile-summary-card-output/transparent"
images_references = ["E.svg"] + [
    os.path.join(source_path, file).replace("/", os.sep)
    for file in os.listdir(source_path)
]
source_content = {}

for file in images_references:
    if not file.endswith(".svg"):
        continue

    # with open("_compound.svg", "r") as f:
    with open(file) as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    # Find the first <svg> tag in the document
    svg = soup.find("svg")

    source_content[file] = svg


print(source_content["E.svg"].prettify())

with open("compound_source.svg") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

images = soup.find_all("image")

# Replace the <image> tag with the content of the source SVG files
for image in images:
    image_href = image["href"].replace("/", os.sep)

    if image_href in source_content:
        print(f"Replacing {image_href} image with source content...")
        source_svg = source_content[image_href]

        # Replace the <image> tag
        image.replace_with(copy.deepcopy(source_svg))

output = soup.prettify()

# Replace colors while we are at it
output = output.replace("#006AFF", "#408beb")

with open("output.svg", "w") as f:
    f.write(output)
