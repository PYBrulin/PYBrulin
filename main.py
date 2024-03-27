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
output = output.replace("fill: #006AFF;", "")
output = output.replace("fill: #417E87;", "")
output = output.replace("fill:#ffffff;", "")
output = output.replace("#006AFF", "")
output = output.replace("#ffffff", "")
output = output.replace('"#000000"', '""')
output = output.replace("#0579C3", "")
output = output.replace("#417E87", "")
output = output.replace('fill="currentColor"', "")
output = output.replace('stroke="currentColor"', '')
output = output.replace("stroke-width:2.04705", "stroke-width:1")
output = output.replace("stroke-width: 2px", "stroke-width: 1px")
output = output.replace('d="M0.5,6V0.5H380.5V6"', "")
output = output.replace('d="M6,110.5H0.5V0.5H6"', "")


with open("output.svg", "w") as f:
    f.write(output)
