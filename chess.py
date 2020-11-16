import pygame
import sys
import Utils
import time
import chessBoard
from moveGeneration import*
from chessEngine import *
import random


class Colors:
    """Colors namespace"""
    WHITE = (255, 255, 255)
    GREEN = (0, 120, 0)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    LIGHTBLUE = (100, 100, 255)
    DARKRED = (70, 0, 0)
    YELLOW = (255, 255, 0)
    WEIRD = (0, 255, 255)
    GREY = (70, 70, 70)


class Field:
    """Class handling user interface objects"""

    def __init__(self, center, dims, z=5, color=Colors.GREY):
        self.z = z
        self.color = color
        self.center = center
        self.box = pygame.Surface(dims)
        self.box.fill(color)
        self.rect = self.box.get_rect()
        self.rect.center = center

    def draw(self, scr):
        scr.blit(self.box, self.rect)


class ButtonActions:
    def startGame():
        Game.State = 'w'
        Game.Player = 'w'
        Game.Ui.createChessUI()

    def doNothing():
        pass

    def drawAbout():
        pass


class Button(Field):
    """Button consist of a field and a text field"""

    def __init__(self, field, field2, textField, action=ButtonActions.doNothing):
        self.field = field
        self.field2 = field2
        self.z = field.z
        self.state = 1
        self.rect = self.field.rect
        self.rect = field.rect
        self.center = field.rect.center
        self.textField = textField
        self.textRect = textField.box.get_rect()
        self.textRect.center = self.center
        self.action = action

    def draw(self, scr):
        if self.state == 1:
            scr.blit(self.field.box, self.rect)
        elif self.state == 2:
            scr.blit(self.field2.box, self.rect)
        self.textRect.center = self.rect.center
        scr.blit(self.textField.box, self.textRect)

    def onClick(self):
        self.state = 2

    def onRelease(self):
        self.action()

    def unClick(self):
        self.state = 1


class ImgField(Field):
    """Field consisting of image"""
    def __init__(self, imgPath, center, size=None, z=6):
        self.z = z
        self.box = pygame.image.load('images/' + imgPath)
        if size != None:
            self.box = pygame.transform.scale(self.box, size)
        self.box = self.box.convert_alpha()
        self.center = center
        self.rect = self.box.get_rect()
        self.rect.center = center

    def draw(self, scr):
        scr.blit(self.box, self.rect)


class TextField(Field):
    """Field consisting of text"""
    def __init__(self, text, center, font, z=7, color=Colors.WHITE):
        self.z = z
        self.center = center
        self.text = text
        self.box = font.render(text, True, color)
        self.rect = self.box.get_rect()
        self.rect.center = center

    def updateText(self, text):
        font.render(text, True, Colors.WHITE)
        self.rect = self.box.get_rect()
        self.rect.center = self.center

    def draw(self, scr):
        scr.blit(self.box, self.rect)


class MouseClass:
    """class handling clicks and hovers"""
    @staticmethod
    def GetObjClicked(mousePos, bRepr):
        if Game.State == Game.Player and len(Game.asyncTasks) == 0:
            for k, v in bRepr.tiles.items():
                if v.rect.collidepoint(mousePos):
                    s = BoardRepr.Selected
                    if (s == None and not bRepr.isTileEmpty(k) and
                            bRepr.getColor(v.pos) == bRepr.board.ctm):
                        v.onClick()
                        bRepr.HighlightTiles(v.pos)
                        BoardRepr.Selected = v
                        break
                    elif s is not None:
                        for m in bRepr.board.availableMoves(s.pos):
                            if s.pos == m.pos and v.pos == m.dest:
                                bRepr.board.makeMove(m)
                                bRepr.updatePieces(m)
                                break
                        BoardRepr.Selected = None
                        bRepr.unHighlightTiles()
        for b in Game.Ui.buttons:
            if b.field.rect.collidepoint(mousePos):
                b.onClick()

    @staticmethod
    def ReleaseButton(mousePos):
        for b in Game.Ui.buttons:
            b.unClick()
            if b.field.rect.collidepoint(mousePos):
                b.onRelease()


class TileSprite(Field):
    """Represents and draws the tile object"""
    Size = 90

    def __init__(self, pos, color):
        self.z = 5
        self.color = color
        self.pos = pos
        self.rank = Utils.rank(pos)
        self.col = Utils.col(pos)
        s = TileSprite.Size
        i = self.rank
        j = self.col
        self.center = (s / 2 + s * j, s / 2 + s * (7 - i))
        self.box = pygame.Surface((TileSprite.Size, TileSprite.Size))
        self.box.fill(color)
        self.rect = self.box.get_rect()
        self.rect.center = self.center

    def onClick(self):
        self.box.fill(Colors.WEIRD)

    def unClick(self, board):
        # self.box.fill(self.color)
        board.unHighlightTiles()

    def setColor(self, color):
        self.box.fill(color)


class BoardRepr:
    """Represents and draws virtual board"""
    def __init__(self, scr, board):
        self.scr = scr
        self.tiles = {}
        self.board = board
        BoardRepr.PieceSprites = []
        BoardRepr.Selected = None

    def createBRepr(self):
        s = TileSprite.Size
        for pos in range(64):
            if (Utils.rank(pos) + Utils.col(pos)) % 2 == 1:
                self.tiles[pos] = TileSprite(
                    pos, Colors.WHITE)
            else:
                self.tiles[pos] = TileSprite(
                    pos, Colors.GREY)

    def draw(self):
        for tile in self.tiles.values():
            tile.draw(self.scr)
        self.drawBoard()

    def isTileEmpty(self, pos):
        return self.board.isTileEmpty(pos)

    def getColor(self, pos):
        return self.board.squares[pos].color

    def HighlightTiles(self, pos):
        moves = self.board.availableMoves(pos)
        for m in moves:
            self.tiles[m.dest].setColor(Colors.DARKRED)

    def unHighlightTiles(self):
        for p in self.tiles.values():
            p.setColor(p.color)

    def drawBoard(self):
        for ps in BoardRepr.PieceSprites:
            self.drawPiece(ps)

    def createPieceSprites(self):
        for p in self.board.pieces['b']:
            ps = PieceSprite(p)
            BoardRepr.PieceSprites.append(ps)
            time = random.random() + 1
            delay = random.randint(1500, 3500)
            ps.TweenToY(ps, time, delay)
        for p in self.board.pieces['w']:
            ps = PieceSprite(p)
            BoardRepr.PieceSprites.append(ps)
            time = random.random() + 1
            delay = random.randint(500, 2500)
            ps.TweenToY(ps, time, delay)

    def drawPiece(self, ps):
        self.scr.blit(ps.box, ps.rect)

    @staticmethod
    def updatePieces(move):
        """Updates position of pieceSprites"""
        if move.flag != None:
            if move.flag == 'K' or move.flag == 'k':
                for ps in BoardRepr.PieceSprites:
                    if ps.pos == move.pos:
                        ps.updatePos(move.dest)
                    elif ps.pos == (move.dest + 1):
                        ps.updatePos((move.pos + 1))
            if move.flag == 'q' or move.flag == 'Q':
                for ps in BoardRepr.PieceSprites:
                    if ps.pos == move.pos:
                        ps.updatePos(move.dest)
                    elif ps.pos == move.dest - 2:
                        ps.updatePos(move.pos - 1)
            if move.flag == 'p' or move.flag == 'P':
                for ps in BoardRepr.PieceSprites:
                    if ps.pos == move.dest:
                        BoardRepr.PieceSprites.remove(ps)
                for ps in BoardRepr.PieceSprites:
                    if ps.pos == move.pos:
                        ps.promoteToQueen()
                        ps.updatePos(move.dest)

        else:
            for ps in BoardRepr.PieceSprites:
                if ps.pos == move.dest:
                    BoardRepr.PieceSprites.remove(ps)
            for ps in BoardRepr.PieceSprites:
                if ps.pos == move.pos:
                    ps.updatePos(move.dest)


class PieceSprite(ImgField):
    """Graphical represantiation of piece object"""
    def __init__(self, piece):
        self.piecestr = piece.piece
        self.col = piece.color
        self.box = pygame.image.load('images/' + self.col + self.piecestr[0] + ".png")
        self.box = pygame.transform.scale(self.box, (64, 64))
        self.box = self.box.convert_alpha()
        self.pos = piece.pos
        self.rect = self.box.get_rect()
        self.rect.center = Utils.posToTileCenter(self.pos)

    def updatePos(self, pos):
        self.pos = pos
        self.rect.center = Utils.posToTileCenter(self.pos)

    def promoteToQueen(self):
        self.box = pygame.image.load('images/' + self.col + 'q' + ".png")
        self.box = pygame.transform.scale(self.box, (64, 64))

    def easeOutY(self, args):
        """Animate in y axis"""
        """gets called multiple of times asynchronously"""
        # args = (startPos,endPos,startTime,time)
        ps = args["pieceSprite"]
        startY = args["startY"]
        endY = args["endY"]
        delay = args["delay"]
        func = args["func"]
        startTime = args["startTime"]
        time = args["duration"]
        diff = endY - startY
        if pygame.time.get_ticks() - startTime < delay:
            return startY
        curTime = (pygame.time.get_ticks() - startTime - delay) / (1000 * time)
        ps.rect.centery = getattr(Utils, func)(curTime, startY, diff, 1)
        # when its finished
        if(curTime >= 1):
            for task in Game.asyncTasks:
                if task["args"] is args:
                    Game.asyncTasks.remove(task)

    def TweenToY(self, ps, time, delay=0, func="easeOutBounce"):
        """starts asynchornous call"""
        startPos = ps.rect.centery
        ps.rect.bottom = 0
        Game.asyncTasks.append(
            {"obj": self, "func": "easeOutY",
             "args": {"pieceSprite": ps,
                      "startY": ps.rect.centery,
                      "endY": startPos,
                      "startTime": pygame.time.get_ticks(),
                      "duration": time,
                      "delay": delay,
                      "func": func}})


class UI:
    def __init__(self, scr):
        self.fields = []
        self.font = pygame.font.Font('font.ttf', 20)
        self.font1 = pygame.font.Font('font.ttf', 80)
        self.buttons = []
        self.scr = scr
        self.scrRect = self.scr.get_rect()
        self.center = self.scr.get_rect().center

    def addField(self, f):
        if isinstance(f, Button):
            self.buttons.append(f)
        self.fields.append(f)

    def wCheckMate(self):
        """Create menu suited for end of game"""
        x = self.center[0]
        y = self.center[1]
        self.fields = []
        txt1 = TextField("CheckMate :)", (x + 2, y - 62),
                         self.font1, color=Colors.GREEN)
        self.addField(txt1)
        txt2 = TextField("CheckMate :)", (x, y - 60),
                         self.font1, color=Colors.LIGHTBLUE)

    def bCheckMate(self):
        """Create menu suited for end of game"""
        x = self.center[0]
        y = self.center[1]
        self.fields = []
        txt1 = TextField("CheckMate :(", (x + 2, y - 62),
                         self.font1, color=Colors.GREEN)
        self.addField(txt1)
        txt2 = TextField("CheckMate :(", (x, y - 60),
                         self.font1, color=Colors.LIGHTBLUE)

        self.addField(txt2)

    def createMenu(self):
        "Creates welcome screen"
        x = self.center[0]
        y = self.center[1]
        self.fields = []

        self.buttons = []
        img1 = ImgField("backgroundStart.jpg", (x, y), z=2)

        self.addField(img1)
        img3 = ImgField("logo.png", (x, y - 230), (256, 256))
        self.addField(img3)

        startPos = img3.rect.centery
        img3.rect.top = self.scrRect.bottom
        self.TweenToY(img3, startPos, 2, 2000, "easeOutExpo")

        txt1 = TextField("CHESS", (x + 2, y - 62),
                         self.font1, color=Colors.GREEN)
        self.addField(txt1)
        txt2 = TextField("CHESS", (x, y - 60), self.font1,
                         color=Colors.LIGHTBLUE)
        self.addField(txt2)

        startPos = txt1.rect.centery
        txt1.rect.bottom = self.scrRect.top
        self.TweenToY(txt1, startPos, 2)

        startPos = txt2.rect.centery
        txt2.rect.bottom = self.scrRect.top
        self.TweenToY(txt2, startPos, 2)

        f11 = ImgField("green_button04.png", (x, y + 100))
        f12 = ImgField("green_button05.png", (x, y + 100))
        tf1 = TextField("Start Game", (x, y + 100), self.font)
        b1 = Button(f11, f12, tf1, action=ButtonActions.startGame)
        self.addField(b1)
        startPos = b1.rect.centerx
        b1.rect.right = self.scrRect.left
        self.TweenToX(b1, startPos, 2, func="easeOutBack")

        f21 = ImgField("yellow_button04.png", (x, y + 175))
        f22 = ImgField("yellow_button05.png", (x, y + 175))
        tf2 = TextField("About", (x, y + 175), self.font)
        b2 = Button(f21, f22, tf2, action=ButtonActions.drawAbout)
        self.addField(b2)

        startPos = b2.rect.centerx
        b2.rect.left = self.scrRect.right
        self.TweenToX(b2, startPos, 2, func="easeOutBack")

    def createChessUI(self):
        """clears the ui screen"""
        x = self.center[0]
        y = self.center[1]
        self.fields = []
        self.buttons = []

    def drawUI(self):
        """draws currently selected ui screen"""
        self.fields.sort(key=Utils.sortFields)
        for f in self.fields:
            f.draw(self.scr)

    def easeOutX(self, args):
        """gets called multiple of times asynchronously"""
        # args = (startPos,endPos,startTime,time)
        field = args["field"]
        startX = args["startX"]
        endX = args["endX"]
        delay = args["delay"]
        func = args["func"]
        startTime = args["startTime"]
        time = args["duration"]
        if pygame.time.get_ticks() - startTime < delay:
            return startX
        curTime = (pygame.time.get_ticks() - startTime - delay) / (1000 * time)
        diff = endX - startX
        field.rect.centerx = getattr(Utils, func)(curTime, startX, diff, 1)
        # when its finished
        if(curTime >= 1):
            for task in Game.asyncTasks:
                if task["args"] is args:
                    Game.asyncTasks.remove(task)

    def easeOutY(self, args):
        """gets called multiple of times asynchronously"""
        # args = (startPos,endPos,startTime,time)
        field = args["field"]
        startY = args["startY"]
        endY = args["endY"]
        delay = args["delay"]
        func = args["func"]
        startTime = args["startTime"]
        time = args["duration"]
        diff = endY - startY
        if pygame.time.get_ticks() - startTime < delay:
            return startY
        curTime = (pygame.time.get_ticks() - startTime - delay) / (1000 * time)
        field.rect.centery = getattr(Utils, func)(curTime, startY, diff, 1)
        # when its finished
        if(curTime >= 1):
            for task in Game.asyncTasks:
                if task["args"] is args:
                    Game.asyncTasks.remove(task)

    def TweenToX(self, field, dest, time, delay=0, func="easeOutBounce"):
        """starts asynchornous call"""
        Game.asyncTasks.append(
            {"obj": self, "func": "easeOutX",
             "args": {"field": field,
                      "startX": field.rect.centerx,
                      "endX": dest,
                      "startTime": pygame.time.get_ticks(),
                      "duration": time,
                      "delay": delay,
                      "func": func}})

    def TweenToY(self, field, dest, time, delay=0, func="easeOutBounce"):
        """starts asynchornous call"""
        Game.asyncTasks.append(
            {"obj": self, "func": "easeOutY",
             "args": {"field": field,
                      "startY": field.rect.centery,
                      "endY": dest,
                      "startTime": pygame.time.get_ticks(),
                      "duration": time,
                      "delay": delay,
                      "func": func}})


class Game:
    """Class for handling main loop and global events"""
    State = 's'
    Player = 'n'
    asyncTasks = []

    def __init__(self, res):
        pygame.init()
        self.scr = pygame.display.set_mode(res)
        Game.Ui = UI(self.scr)
        Game.Ui.createMenu()
        self.board = chessBoard.Board()
        self.board.setStartingPos()
        self.bRepr = BoardRepr(self.scr, self.board)
        self.bRepr.createBRepr()
        self.firstTime = True

    def update(self):
        self.scr.fill(Colors.GREY)
        if Game.State != 's':
            if self.firstTime:
                self.firstTime = False
                self.bRepr.createPieceSprites()
            self.bRepr.draw()
        Game.Ui.drawUI()
        pygame.display.flip()


def handleAsync():
    """iterates over ongoing asynchronous calls"""

    for task in Game.asyncTasks:
        func = getattr(task["obj"], task["func"])
        func(task["args"])


def main():
    game = Game((720, 720))
    #main loop
    while True:
        handleAsync()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mPos = pygame.mouse.get_pos()
                MouseClass.GetObjClicked(mPos, game.bRepr)
            if event.type == pygame.MOUSEBUTTONUP:
                mPos = pygame.mouse.get_pos()
                MouseClass.ReleaseButton(mPos)

        game.update()
        if game.board.ctm == 'b':
            move = findBestMove(3, game.board, 1, 1, True)
            if move == "wCheckMate":
                game.Ui.wCheckMate()
                game.board.ctm = 'e'
                continue
            game.board.makeMove(move)
            game.bRepr.updatePieces(move)
            game.board.ctm = 'w'
            if len(game.board.allAvailableMoves()) == 0:
                game.Ui.bCheckMate()
                game.board.ctm = 'e'
                continue


# makes sure that module won't run when imported by another module
if __name__ == "__main__":
    main()
