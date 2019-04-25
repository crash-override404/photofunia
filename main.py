from .config import Config
from .utils import Utils
from .exceptions import PhotofuniaException

class Photofunia:
    """docstring for Photofunia"""
    def __init__(self):
        self.config = Config()
        self.utils = Utils()

    def info(self, name):
        name = name.replace(' ', '-')
        name = name.replace('_', '-')
        url = self.utils.urlEncode(self.config.host, '/2.0/effects/' + name, self.config.params)
        response = self.utils.getContent(url)
        return response.json()

    def sketch(self, path, fade=True):
        url = self.utils.urlEncode(self.config.host, self.config.path['sketch'], self.config.params)
        data = {'fade': self.config.bool_dict[fade][0], 'name': 'image'}
        files = {'image': open(path, 'rb')}
        response = self.utils.postContent(url, data=data, files=files)
        return response.json()

    def neon(self, text1, text2):
        url = self.utils.urlEncode(self.config.host, self.config.path['neon'], self.config.params)
        data = {'text1': text1, 'text2': text2}
        response = self.utils.postContent(url, data=data)
        return response.json()

    def neon_writing(self, text, text2=None):
        url = self.utils.urlEncode(self.config.host, self.config.path['neon-writing'], self.config.params)
        data = {'text': text, 'text2': text2}
        response = self.utils.postContent(url, data=data)
        return response.json()

    def passage(self, path):
        url = self.utils.urlEncode(self.config.host, self.config.path['passage'], self.config.params)
        data = {'name': 'image'}
        files = {'image': open(path, 'rb')}
        response = self.utils.postContent(url, data=data, files=files)
        return response.json()

    def explorer_drawing(self, path):
        url = self.utils.urlEncode(self.config.host, self.config.path['explorer-drawing'], self.config.params)
        data = {'name': 'image'}
        files = {'image': open(path, 'rb')}
        response = self.utils.postContent(url, data=data, files=files)
        return response.json()

    def light_writing(self, text, base='e1'):
        if base not in ['e', 'e1', 'e2', 'e3', 'e4']:
            raise PhotofuniaException('Invalid image base')
        url = self.utils.urlEncode(self.config.host, self.config.path['light-writing'], self.config.params)
        data = {'text': text, 'base': base}
        response = self.utils.postContent(url, data=data)
        return response.json()

    def watercolour_text(self, text, text2=None, color=1, font='segoeprb', splashes=True):
        if color not in [1, 2, 3, 4]:
            raise PhotofuniaException('Invalid color value')
        if font not in ['segoeprb', 'lobster']:
            raise PhotofuniaException('Invalid font value')
        url = self.utils.urlEncode(self.config.host, self.config.path['watercolour-text'], self.config.params)
        data = {'text': text, 'text2': text2, 'color': color, 'font': font, 'splashes': self.bool_dict[splashes][0]}
        response = self.utils.postContent(url, data=data)
        return response.json()

    def number_plate(self, text, colour='orange'):
        if colour not in ['orange', 'green', 'gray', 'blue', 'purple']:
            raise PhotofuniaException('Invalid colour value')
        url = self.utils.urlEncode(self.config.host, self.config.path['number-plate'], self.config.params)
        data = {'text': text, 'colour': colour}
        response = self.utils.postContent(url, data=data)
        return response.json()

    def two_valentines(self, text, image, text2, image2):
        url = self.utils.urlEncode(self.config.host, self.config.path['two-valentines'], self.config.params)
        data = {'text': text, 'text2': text2}
        files = {'image': open(image, 'rb'), 'image2': open(image2, 'rb')}
        response = self.utils.postContent(url, data=data, files=files)
        return response.json()

    def calendar(self, path, type='Year', year='2019'):
        url = self.utils.urlEncode(self.config.host, self.config.path['calendar'], self.config.params)
        data = {'type': type, 'year': year}
        files = {'image': open(path, 'rb')}
        response = self.utils.postContent(url, data=data, files=files)
        return response.json()