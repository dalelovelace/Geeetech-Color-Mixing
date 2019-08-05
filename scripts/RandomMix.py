# Created by Dale Lovelace

from ..Script import Script
#import random
from random import seed
from random import random
from random import randint

class RandomMix(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Randomly change extruder mix",
            "key": "RandomMix",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "minimum":
                {
                    "label": "Minimum",
                    "description": "Minimum extrusion percentage for extruder 0",
                    "type": "int",
                    "default_value": 80,
                    "minimum_value": "0",
                    "maximum_value": "100"
                },
                "maximum":
                {
                    "label": "Maximum",
                    "description": "Maximum extrusion percentage for extruder 0",
                    "type": "int",
                    "default_value": 100,
                    "minimum_value": "0",
                    "maximum_value": "100"
                }
            }
        }"""

    def execute(self, data):
        min = self.getSettingValueByKey("minimum")
        max = self.getSettingValueByKey("maximum")
        for layer in data:
            layer_index = data.index(layer)
            lines = layer.split("\n")
            for line in lines:
                if line.startswith("G1"):
                    S0 = randint(min, max)
                    S1 = 100 - S0
                    text = "M163 S0 P" + str(S0 / 100) + "\n"
                    text = text + "M163 S1 P" + str(S1 / 100) + "\n"
                    text = text + "M164 S2\n"
                    line_index = lines.index(line)
                    lines[line_index] = text + line
                final_lines = "\n".join(lines)
                data[layer_index] = final_lines
        return data

