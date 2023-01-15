# Math-Class-Randomizer

random math excersise sheets

## usage

1. Use devcontainer setup with vs code. It installs all necessary pip requirements.
2. Run `python3 math_class_randomizer`
3. With default config template is used from `templates/math_class.md.j2`
4. Create a markdown and a pdf file

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

Otherwise create a api token and write it into `math_class_randomizer/secret.yaml`:

```yaml
openaiapi: "your api key goes here ..."
```
