# -*- coding: utf-8 -*-
class Config:
    """docstring for Config"""
    def __init__(self):
        self.host = 'https://api.photofunia.com'
        self.path = {
            'sketch': '/2.0/effects/sketch',
            'neon': '/2.0/effects/neon',
            'neon-writing': '/2.0/effects/',
            'passage': '/2.0/effects/passage',
            'explorer-drawing': '/2.0/effects/explorer-drawing',
            'light-writing': '/2.0/effects/light-writing',
            'watercolour-text': '/2.0/effects/watercolour-text',
            'number-plate': '/2.0/effects/number-plate',
            'two-valentines': '/2.0/effects/two-valentines',
            'calendar': '/2.0/effects/calendar'
        }
        self.params = {
        	'access_key': 'e3084acf282e8323181caa61fa305b2a',
        	'lang': 'en'
        }
        self.bool_dict = {
        	True: ['yes', 'active'],
        	False: ['no', 'deactive']
        }