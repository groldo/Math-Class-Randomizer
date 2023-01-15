import yaml
from yaml.loader import SafeLoader

class Config():
    def __init__(self):
        self.config = self.load_yaml('./config.yaml')
        if self.config["openai"]["enable"]:
            self.secret = self.load_yaml('./secret.yaml')
            self.config["secret"]= self.secret

    @staticmethod
    def load_yaml(infile):
        with open(infile) as f:
            config = yaml.load(f, Loader=SafeLoader)
        return config
