# Spot-Prompt-Algorithm

## Key words by category

### Basic Movement Words
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
"haul", "lug", "schlep", "transport", "guide", "lead", "steer", "convey", "deliver","rotate"

### Arm Movement Words
"wave", "shake", "fidget", "extend", "straighten", "gesture"

### Vision Words
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

## Initial Prompts (Not Code / Wiki)
self.commandPreferencer = 'Following is an input statement via voice given to you SPOT the robotic dog, please interpret the command ' \
'as you would think that a person talking to SPOT the robotic dog which has four legs, an arm with a gripper on the back, as well as ' \
'cameras on the front, side, and back would. Return only the flawless created code and nothing else. Input: ' + self.command

self.codeGenerationPrompter = 'Using the following working code as your reference create working code which expertly follows the command and when done' \
'makes sure the robot is safely sitting down with its arm put away. Make sure each method exists and is correct according to uses in the ROS2 SPOT API Wrapper.' \
'Remember for full functionality make sure you are using the wrapper and its services.'

self.visionPromter = 'Given that this command requires vision please use openCV as well as this pretrained bounding box object detection model which is compatible with openCV ' \
'located on the computer at ...'
