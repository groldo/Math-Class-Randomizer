from jinja2 import Environment, FileSystemLoader
import subprocess
import shlex
import datetime
import argparse
import yaml
from yaml.loader import SafeLoader
import area
import arithmetic


def create_file_from_jinja(template, markdown, context):
    environment = Environment(loader=FileSystemLoader("."))
    template = environment.get_template(template)
    with open(markdown, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))

# Open the file and load the file
with open('aufgaben/ex_config.yaml') as f:
    config = yaml.load(f, Loader=SafeLoader)

parser = argparse.ArgumentParser()
# parser.add_argument("outfile", type=str)
args = parser.parse_args()

area_ex = area.AreaEx(config).excersises
multiplication_ex = arithmetic.ArithmeticEx(config, config["division"]["count"]).excersises
division_ex = arithmetic.ArithmeticEx(config, config["division"]["count"]).excersises

context = {
    "today": datetime.date.today().strftime(format="%d.%m.%Y"),
    "area": area_ex,
    "multi": multiplication_ex,
    "division": division_ex,
}

markdown = ".".join(config["template"].split(".")[0:-1])
pdf = ".".join(config["template"].split(".")[0:-2]) + ".pdf"

create_file_from_jinja(config["template"], markdown, context)

cmd = "pandoc " + markdown + \
    " --data-dir /usr/share/pandoc/data "\
    "-F pandoc-crossref -s --dpi=300 "\
    "--toc --listings --template eisvogel -t pdf -o " + \
    pdf

args = shlex.split(cmd)
cmd = subprocess.Popen(args, stdout=subprocess.PIPE)
output = cmd.communicate()
