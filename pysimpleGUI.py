import pygame as pg

pg.init()

largeFont = pg.font.SysFont('calibri', 42)
smallFont = pg.font.SysFont('calibri', 32)
tinyFont = pg.font.SysFont('calibri', 18)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHTRED = (255, 128, 128)
GREEN = (0, 255, 0)
LIGHTGREEN = (128, 255, 128)
BGCOLOR = (0, 0, 128)
LIGHTGREY = (200, 200, 200)
DARKGREEN = (0, 128, 0)
DARKRED = (128, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

def euclidDis(p1, p2):
    #Finner avstanden mellom to punkt i 2d rom ved hjelp av pytagoras
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)

class Button():
    def __init__(self, shape, func, textBox = None, params=[]):
        self.func, self.params = func, params
        self.textBox = textBox
        self.shape = shape
        self.isactive = True
        try:
            if not self.shape.isshape:
                raise Exception('Not a valid shape object')
        except:
            raise Exception('Not a valid shape object')

    def collide(self, point, GM):
        if self.isactive:
            if self.shape.collide(point):
                self.func(GM, self.params)

    def draw(self):
        if self.isactive:
            self.shape.draw()
            if self.textBox != None:
                self.textBox.draw()

class Selector():
    def __init__(self, buttons, selectorColor=WHITE, startSelected=0):
        self.buttons = buttons
        self.selectorColor = selectorColor
        self.selected = startSelected
        self.isactive = True

    def getOutput(self):
        return self.selected

    def draw(self):
        if self.isactive:
            #Draw the outline (a bit convoluted)
            self.buttons[self.selected].shape.centerx -= 2
            self.buttons[self.selected].shape.centery -= 2
            self.buttons[self.selected].shape.update()
            orgColor = self.buttons[self.selected].shape.color
            self.buttons[self.selected].shape.color = self.selectorColor
            self.buttons[self.selected].shape.color = orgColor
            self.buttons[self.selected].shape.draw()
            self.buttons[self.selected].shape.centerx += 2
            self.buttons[self.selected].shape.centery += 2
            self.buttons[self.selected].shape.update()

            #Draw the buttons
            [button.draw() for button in self.buttons]

    def collide(self, point):
        if self.isactive:
            for i, button in enumerate(self.buttons):
                if button.shape.collide(point):
                    self.selected = i

class GUICircle():
    def __init__(self, center, radius, color, surface=None):
        self.center, self.radius, self.color, self.surface = center, radius, color ,surface
        self.isshape = True
        self.isactive = True

    def collide(self, point):
        if self.isactive:
            return euclidDis(point, self.center) <= self.radius
        return False

    def draw(self):
        if self.isactive:
            pg.draw.circle(self.surface, self.color, self.center, self.radius)

    def update(self):
        pass

class GUIRect():
    def __init__(self, center, size, color, surface=None, topleft=False):
        self.center, self.size, self.color, self.surface = center, size, color, surface
        self.topleft = topleft
        self.rect = pg.Rect(0, 0, self.size[0], self.size[1])
        if not topleft:
            self.rect.center = center[0], center[1]
        else:
            self.rect.topleft = center[0], center[1]

        self.isshape = True
        self.isactive = True

    def collide(self, point):
        if self.isactive:
            newRect = pg.Rect(point[0], point[1], 1, 1)
            return bool(newRect.colliderect(self.rect))
        return False

    def draw(self):
        if self.isactive:
            pg.draw.rect(self.surface, self.color, self.rect)

    def update(self):
        self.rect = pg.Rect(0, 0, self.size[0], self.size[1])
        if not self.topleft:
            self.rect.center = self.center[0], self.center[1]
        else:
            self.rect.topleft = self.center[0], self.center[1]

class Bar():
    def __init__(self, center, size, color, surface=None, topleft=False, borderColor=BLACK):
        ##Automatically change direction of bar based on longest dimension
        self.center, self.size, self.color, self.surface, self.borderColor = center, size, color, surface, borderColor
        self.topleft = topleft
        self.rect = pg.Rect(0, 0, self.size[0], self.size[1])
        if not topleft:
            self.rect.center = center[0], center[1]
        else:
            self.rect.topleft = center[0], center[1]

        self.isactive = True
        self.fill = 1

    def collide(self, point):
        pass

    def draw(self):
        if self.isactive:
            pg.draw.rect(self.surface, self.color, self.rect)

            # Horisontal lines
            self.rect.width = self.size[0]
            self.rect.height = 2
            pg.draw.rect(self.surface, self.borderColor, self.rect)
            self.rect.top += self.size[1]
            pg.draw.rect(self.surface, self.borderColor, self.rect)
            self.update()  # Reset the rect for more mutilation

            # Vertical lines
            self.rect.width = 2
            pg.draw.rect(self.surface, self.borderColor, self.rect)
            self.rect.left += self.size[0]
            self.rect.height += 2
            pg.draw.rect(self.surface, self.borderColor, self.rect)

            self.update() #Make sure the rect is in good condition after we are done

    def setFill(self, fill):
        self.fill = fill
        self.update()

    def update(self):
        self.rect = pg.Rect(0, 0, self.size[0], self.size[1])
        if not self.topleft:
            self.rect.center = self.center[0], self.center[1]
        else:
            self.rect.topleft = self.center[0], self.center[1]

        self.rect.width *= self.fill

class Slider():
    def __init__(self, center, size, color, surface=None, topleft=False, borderColor=BLACK, sliderColor=BLACK):
        ##Automatically change direction of bar based on longest dimension
        self.center, self.size, self.color, self.surface, self.borderColor = center, size, color, surface, borderColor
        self.sliderColor = sliderColor
        self.topleft = topleft
        self.rect = pg.Rect(0, 0, self.size[0], self.size[1])
        if not topleft:
            self.rect.center = center[0], center[1]
        else:
            self.rect.topleft = center[0], center[1]

        self.isactive = True
        self.fill = 1

    def collide(self, point):
        if not self.isactive:
            return False

        rect = pg.Rect(0, 0, self.size[0], self.size[1])
        if not self.topleft:
            rect.center = self.center[0], self.center[1]
        else:
            rect.topleft = self.center[0], self.center[1]

        newRect = pg.Rect(point[0], point[1], 1, 1)
        if rect.colliderect(newRect):
            self.setFill((point[0]-rect.top-12)/self.size[0])

    def draw(self):
        if self.isactive:
            pg.draw.rect(self.surface, self.color, self.rect)

            #Horisontal lines
            self.rect.width = self.size[0]
            self.rect.height = 2
            pg.draw.rect(self.surface, self.borderColor, self.rect)
            self.rect.top += self.size[1]
            pg.draw.rect(self.surface, self.borderColor, self.rect)
            self.update() #Reset the rect for more mutilation


            #Vertical lines
            self.rect.width = 2
            pg.draw.rect(self.surface, self.borderColor, self.rect)
            self.rect.left += self.size[0]
            self.rect.height += 2
            pg.draw.rect(self.surface, self.borderColor, self.rect)
            self.rect.left += (self.size[0]*self.fill) - (self.size[0])

            #Making the slider
            self.rect.width = 6
            self.rect.height += 6
            self.rect.top -= 3
            pg.draw.rect(self.surface, self.borderColor, self.rect)

            self.update() #Make sure the rect is in good condition after we are done

    def setFill(self, fill):
        self.fill = fill
        self.update()

    def update(self):
        self.rect = pg.Rect(0, 0, self.size[0], self.size[1])
        if not self.topleft:
            self.rect.center = self.center[0], self.center[1]
        else:
            self.rect.topleft = self.center[0], self.center[1]

        self.rect.width *= self.fill

class TextBox():
    def __init__(self, center, color, text, surface=None, font=largeFont, maxWidth=float('inf'), lineDis=1):
        self.center, self.color, self.text, self.font = center, color, text, font
        self.maxWidth = maxWidth
        self.surface = surface
        self.lineDis = lineDis*self.font.size(self.text)[1]
        self.getDescs()
        self.isactive = True

    def draw(self):
        if self.isactive:
            for i, desc in enumerate(self.descs):
                rect = desc.get_rect()
                rect.center = self.center[0], self.center[1]+i*self.lineDis
                self.surface.blit(desc, rect)

    def newText(self, text, color=None):
        self.text = text
        if color == None:
            color = self.color
        self.color = color
        self.getDescs()

    def getWordLen(self, word):
        return self.font.size(word)[0]

    def getDescs(self):
        words = [word for word in self.text.split(' ') if word != '']
        wordLens = [self.getWordLen(word) for word in words]
        self.descs = []
        newLine = 0
        for i, word in enumerate(words):
            if sum(wordLens[newLine:i+1]) >= self.maxWidth:
                self.descs += [self.font.render(' '.join(words[newLine:i]), True, self.color)]
                newLine = i
            elif word == '\\n':
                self.descs += [self.font.render(' '.join(words[newLine:i]), True, self.color)]
                newLine = i+1

        remaining = [word for word in words[newLine:i+1] if word != '\\n']
        self.descs += [self.font.render(' '.join(remaining), True, self.color)]

class Layout():
    def __init__(self):
        self.buttons = []
        self.textBoxes = []
        self.shapes = []
        self.selectors = []
        self.bars = []

    def draw(self):
        if self.checkSurface():
            [button.draw() for button in self.buttons]
            [text.draw() for text in self.textBoxes]
            [shape.draw() for shape in self.shapes]
            [selector.draw() for selector in self.selectors]
            [bar.draw() for bar in self.bars]
        else:
            raise Exception('Some elements have undeffined surfaces. Set a surface for all elements in this layout by using the setSurface(surface) method of the layout object')

    def collide(self, pos, GM):
        [button.collide(pos, GM) for button in self.buttons]
        [selector.collide(pos) for selector in self.selectors]
        [bar.collide(pos) for bar in self.bars]

    def addBar(self, bar):
        self.bars += [bar]

    def addButton(self, button):
        self.buttons += [button]

    def addTextBox(self, textBox):
        self.textBoxes += [textBox]

    def addShape(self, shape):
        self.textBoxes += [shape]

    def addSelector(self, selector):
        self.selectors += [selector]

    def setSurface(self, surface):
        for textBox in self.textBoxes:
            textBox.surface = surface

        for button in self.buttons:
            button.shape.surface = surface
            if button.textBox != None:
                button.textBox.surface = surface

        for shape in self.shapes:
            shape.surface = surface

        for selector in self.selectors:
            for button in selector.buttons:
                button.shape.surface = surface

        for bar in self.bars:
            bar.surface = surface

    def checkSurface(self):
        #Checks if all contents have a defined surface
        for textBox in self.textBoxes:
            if textBox.surface == None:
                return False

        for button in self.buttons:
            if button.shape.surface == None:
                return False
            if button.textBox != None:
                if button.textBox.surface == None:
                    return False

        for shape in self.shapes:
            if shape.surface == None:
                return False

        for selector in self.selectors:
            for button in selector.buttons:
                if button.shape.surface == None:
                    return False

        for bar in self.bars:
            if bar.surface == None:
                return False

        return True
