import string
import numpy as np
from nltk.stem import WordNetLemmatizer

class Generation():
    def __init__(self, command):
        self.command = command

        self.lemmatizer = WordNetLemmatizer()

        self.basic_movement = [
        "go", "come", "walk", "run", "bring", "take", "deliver", "send", "escort", "return", 
        "head", "travel", "drive", "fly", "sail", "ride", "cycle", "climb", "jump", "skip", 
        "crawl", "rush", "hurry", "advance", "retreat", "proceed", "follow", "leave", "arrive", 
        "depart", "exit", "enter", "approach", "circle", "cross", "navigate", "relocate", "mail", 
        "ship", "race", "sprint", "dash", "wander", "stroll", "meander", "march", "patrol", "tour", 
        "visit", "step", "trot", "gallop", "glide", "slide", "roll", "parade", "commute", "trek", 
        "hike", "descend", "ascend", "dive", "swim", "float", "paddle", "row", "accelerate", 
        "reverse", "back", "forward", "evacuate", "migrate", "emigrate", "immigrate", "stray", 
        "deviate", "veer", "meet", "chase", "flee", "escape", "pursue", "track", "traverse", 
        "circumnavigate", "orbit", "pass", "overtake", "weave", "zigzag", "shuffle", "tiptoe", 
        "strut", "saunter", "roam", "rove", "cruise", "sneak", "slither", "hop", "leap", "vault", 
        "scamper", "scurry", "scuttle", "bolt", "dart", "bustle", "hasten", "speed", "zoom", 
        "whisk", "ferry", "channel", "direct", "pilot", "transmit", "mobilize", "smuggle", 
        "scoot", "beeline", "disembark", "embark", "move", "maneuver", "carry", "drag", 
        "haul", "lug", "schlep", "transport", "guide", "lead", "steer", "convey", "deliver","rotate",

        ]
        self.arm_movement = [
        "wave", "shake", "fidget", "extend", "straighten", "gesture", "speak"
        ]

        self.vision_words = [
        "see", "look", "watch", "observe", "spot", "notice", "detect", "identify", "recognize", 
        "perceive", "scan", "survey", "inspect", "examine", "view", "witness", "gaze", "stare", 
        "peer", "glance", "peek", "glimpse", "sight", "discern", "distinguish", "locate", "find", 
        "discover", "reveal", "track", "monitor", "survey", "scrutinize", "analyze", "study", 
        "read", "interpret", "decode", "decipher", "focus", "zoom", "magnify", "spotlight", 
        "illuminate", "highlight", "contrast", "compare", "classify", "categorize", "label", 
        "mark", "pinpoint", "target", "aim", "align", "frame", "capture", "photograph", "record", 
        "document", "map", "chart", "plot", "trace", "outline", "sketch", "draw", "paint", 
        "visualize", "imagine", "envision", "anticipate", "predict", "forecast", "project", 
        "estimate", "measure", "calculate", "assess", "evaluate", "judge", "appraise", "review", 
        "verify", "confirm", "validate", "check", "audit", "test", "probe", "explore", "search", 
        "seek", "hunt", "scout", "patrol", "sweep", "comb", "filter", "sort", "organize", "arrange",
        "fetch","grab", "grasp", "clutch", "snatch", "seize", "hold", "catch", "pluck", "pick", "lift", 
        "tug", "tote", "hoist", "heave", "retrieve", "collect", "gather", "scoop", "clasp", 
        "clench", "grip", "snag", "yank", "wrench", "draw", "extract", "remove", "take", "bring", 
        "transfer", "reposition", "adjust", "handle", "pass", "hand", "throw", "toss", "fling", 
        "hurl", "press", "shove", "place", "set", "drop", "release", "unload", "load", "stack", 
        "arrange", "organize", "pack", "unpack", "reach", "stretch", "swing", 
        "wield", "brandish", "point",  "signal", "pat", "tap", "stroke", "rub", 
        "scratch", "poke", "prod", "nudge", "fumble", "juggle", "twist", "turn", 
        "spin", "flip", "fold", "unfold", "bend", "squeeze", "compress", "pinch", 
        "tweak", "align", "realign", "position", "rearrange", "manipulate", "operate", "control", 
        "pull", "push", "shift", "lower", "raise","toward"
        ]

        self.commandPreferencer = 'Following is an input statement via voice given to you SPOT the robotic dog, please interpret the command ' \
        'as you would think that a person talking to SPOT the robotic dog which has four legs, an arm with a gripper on the back, as well as ' \
        'cameras on the front, side, and back would. Return only the flawless created code and nothing else. Input: ' + self.command

        self.codeGenerationPrompter = 'Using the following working code as your reference create working code which expertly follows the command and when done' \
        'makes sure the robot is safely sitting down with its arm put away. Make sure each method exists and is correct according to uses in the ROS2 SPOT API Wrapper.' \
        'Remember for full functionality make sure you are using the wrapper and its services.'

        self.visionPromter = 'Given that this command requires vision please use openCV as well as this pretrained bounding box object detection model which is compatible with openCV ' \
        'located on the computer at ...'

        with open('visionCode.txt', 'r') as file:
            self.visionCode = file.read()

        with open('armCode.txt', 'r') as file:
            self.armCode = file.read()

        with open('basicCode.txt', 'r') as file:
            self.movementCode = file.read()

        with open('generalCode.txt','r') as file:
            self.generalCode = file.read()

        with open('topicsWiki.txt','r') as file:
            self.topicsList = file.read()

        with open('actionsWiki.txt','r') as file:
            self.actionsList = file.read()

        with open('servicesWiki.txt','r') as file:
            self.servicesList = file.read()

        self.wikiDump = self.actionsList + self.servicesList + self.topicsList

        self.categoryTuple = self.processCategory()

        self.prompt = self.promptBuilder()


    def processCategory(self):
        command = self.command
        visionCount, armCount, basicCount = 0, 0, 0
        table = str.maketrans('', '', string.punctuation)
        result = command.translate(table)
        words = command.lower().split()
        for word in words:
            self.lemmatizer.lemmatize(word)
            if word in self.arm_movement: armCount+=1
            if word in self.basic_movement: basicCount+=1
            if word in self.vision_words: visionCount+=1
        return (basicCount>0, armCount>0, visionCount>0)


    def promptBuilder(self):
        bNeed, aNeed, vNeed = self.categoryTuple[0], self.categoryTuple[1], self.categoryTuple[2]
        code = self.visionCode * vNeed + self.movementCode * bNeed + self.armCode * aNeed + self.generalCode * (1 if bNeed+aNeed+vNeed==0 else 0)
        if(vNeed == 1):
            prompt = self.codeGenerationPrompter + '\n' + code + '\n' +self.wikiDump + '\n' + self.visionPromter + '\n' + self.commandPreferencer
        else:
            prompt = self.codeGenerationPrompter + '\n' + code + '\n' + self.wikiDump + '\n' + self.commandPreferencer
        return prompt 
    
    def returnPrompt(self):
        return self.prompt
 
