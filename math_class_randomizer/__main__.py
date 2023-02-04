from jinja2 import Environment, FileSystemLoader
import subprocess
import shlex
import area
import arithmetic
import textex
import config
import context


def create_file_from_jinja(template, markdown, context):
    environment = Environment(loader=FileSystemLoader("."))
    #environment.trim_blocks = True
    environment.lstrip_blocks = True
    template = environment.get_template(template)
    with open(markdown, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))

#parser = argparse.ArgumentParser()
#parser.add_argument("--config", type=str, default="./config.yaml")
#args = parser.parse_args()
#print(args.config)

config = config.Config().config
context = context.Context()

context.add_to_context(
    "area", 
    area.AreaEx(config).excersises
    )
context.add_to_context(
    "multi", arithmetic.ArithmeticEx(config["multiplication"]).excersises
    )
context.add_to_context(
    "division", 
    arithmetic.ArithmeticEx(config["division"]).excersises
    )

if config["openai"]["enable"]:
    context.add_to_context(
        "crossmultiplytext", 
        textex.TextEx(
            config["cross_multiplication_text"],
            config["secret"]["openaiapi"]).excersises
        )
    context.add_to_context(
        "procenttext", 
        textex.TextEx(
            config["procent_text"],
            config["secret"]["openaiapi"]).excersises
        )

markdown = config["markdown"]
pdf = config["pdf"]

create_file_from_jinja(config["template"], markdown, context.context)

cmd = "pandoc " + markdown + \
    " --data-dir /usr/share/pandoc/data "\
    "-F pandoc-crossref -s --dpi=300 "\
    "--toc --listings --template eisvogel -t pdf -o " + \
    pdf

args = shlex.split(cmd)
cmd = subprocess.Popen(args, stdout=subprocess.PIPE)
output = cmd.communicate()
