# Math-Class-Randomizer

random math excersise sheets

## usage

1. Use devcontainer setup with vs code. It installs all necessary pip requirements.
2. Run `python3 math_class_randomizer`
3. With default config template is used from `templates/math_class.md.j2`
4. Creates a markdown and a pdf file
5. You can also make any adjustments to the output markdown file
6. And then recompile it with:
    `pandoc out/example.md -s --data /usr/share/pandoc/data --template eisvogel --listings -o out/example.pdf`
    or use the vs code task `generate pdf` it will create a file `input.md.pdf`

Also see [out/example.pdf](out/example.pdf) for an example.
Template is written in german.

## OpenAI

The app uses the ChatGPT API to create excercises.
To opt out of it use:

```python
openai:
    enable: false
```

in the `config.yaml`

Otherwise create an api token and write it into `math_class_randomizer/secret.yaml`:

```yaml
openaiapi: "your api key goes here ..."
```
