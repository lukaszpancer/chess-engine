"""Board in text format - virtual"""
import Utils
from moveGeneration import*


class Piece:
    def __init__(self, p, pos):
        if p == '-':
            self.color = '-'
        elif p.isupper():
            self.color = 'w'
        else:
            self.color = 'b'
        self.piece = p
        self.piecelower = self.piece.lower()
        if self.piecelower == 'p':
            self.value = 100
        elif self.piecelower == 'n':
            self.value = 300
        elif self.piecelower == 'b':
            self.value = 300
        elif self.piecelower == 'r':
            self.value = 500
        elif self.piecelower == 'q':
            self.value = 900
        elif self.piecelower == 'k':
            self.value = 10000
        self.pos = pos

    def __repr__(self):
        return self.piece

    def promoteToQueen(self):
        if self.color == 'w':
            self.piece = 'Q'
            self.piecelower = 'q'
            self.value = 900
        elif self.color == 'b':
            self.piece = 'q'
            self.piecelower = 'q'
            self.value = 900

    def dethrone(self):
        if self.color == 'w':
            self.piece = 'P'
            self.piecelower = 'p'
            self.value = 100
        elif self.color == 'b':
            self.piece = 'p'
            self.piecelower = 'p'
            self.value = 100


class Board:
    def __init__(self):
        self.pieces = {"b": [], "w": []}
        self.squares = [Piece("-", i) for i in range(64)]
        self.kings = {'w': None, 'b': None}

    def __getitem__(self, index):
        return self.squares[index]

    def isTileEmpty(self, pos):
        return True if self.squares[pos] == '-' else False

    def __repr__(self):
        rows = []
        rows.append("  ABCDEFGH")
        rows.append("  ________")
        for row in range(7, -1, -1):
            rows.append(str(row + 1) + "|" + "".join(
                s.piece for s in self.squares[row * 8:(row + 1) * 8]) + "|" + str(row + 1))

        rows.append("  ‾‾‾‾‾‾‾‾")
        rows.append("  ABCDEFGH")
        return "\n".join(rows)

    def setSqr(self, pos, piece):
        self.squares[pos] = piece

    def addPiece(self, piece):
        self.pieces[piece.color].append(piece)
        if piece.piecelower == 'k':
            self.kings[piece.color] = piece

    def allAvailableMoves(self):
        return genAllMoves(self)

    def allAttacked(self, color):
        return genAllAttacked(self, color)

    def availableMoves(self, pos):
        p = self.squares[pos].piecelower
        return genMoves[p](self, pos, self.ctm)

    def willBeCheck(self, move):
        answer = False
        self.makeMove(move)
        if self.isInCheck(move.color):
            answer = True
        self.undoMove(move)
        return answer

    def isInCheck(self, color):
        king = self.kings[color]
        for m in self.allAttacked(Utils.oppColor(color)):

            if king.pos == m.dest:
                return True
        return False

    def setStartingPos(self):
        fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        #fen = '8/6k1/8/K1b5/8/8/1q6/8 w - - 0 1'
        self.setByFEN(fen)

    def setByFEN(self, fen):
        pieces, ctm, castling, en_passant, rule50, movecnt = fen.split()
        pos = 0
        for p in pieces:
            if p.isdigit():
                pos += int(p)
                continue
            elif p == '/':
                continue
            r = Utils.rank(pos)
            c = Utils.col(pos)
            sqr = Utils.crToPos(c, 7 - r)
            piece = Piece(p, sqr)
            self.setSqr(sqr, piece)
            self.addPiece(piece)
            pos += 1
        self.ctm = ctm
        self.castling = {'K': 0, 'Q': 0, 'k': 0, 'q': 0}
        for c in castling:
            if castling != '-':
                for c in castling:
                    assert c in 'KQkq'
                    self.castling[c] = 1
        #self.en_passant = squares.get(en_passant, None)
        self.movecnt = int(movecnt)
        #self.checked = self._is_checked()

    def makeMove(self, move):
        pos = move.pos
        dest = move.dest
        col = self.squares[pos].color
        move.color = col
        if move.flag != None:
            if move.flag == "K" or move.flag == 'k':
                self.squares[dest] = self.squares[pos]
                self.squares[dest].pos = dest
                self.squares[pos + 1] = self.squares[dest + 1]
                self.squares[pos + 1].pos = pos + 1
                self.squares[pos] = Piece('-', pos)
                self.squares[dest + 1] = Piece('-', dest + 1)
            elif move.flag == "Q" or move.flag == 'q':
                self.squares[dest] = self.squares[pos]
                self.squares[dest].pos = dest
                self.squares[pos - 1] = self.squares[dest - 2]
                self.squares[pos - 1].pos = pos - 1
                self.squares[pos] = Piece('-', pos)
                self.squares[dest - 2] = Piece('-', dest - 2)
            elif move.flag == 'p' or move.flag == 'P':
                if self.squares[dest].color != '-':
                    move.capture = True
                if move.capture:
                    move.captured = self.squares[dest]
                    self.pieces[Utils.oppColor(col)].remove(move.captured)

                self.squares[dest] = self.squares[pos]
                self.squares[pos] = Piece('-', pos)
                self.squares[dest].pos = dest
                self.squares[dest].promoteToQueen()
            self.ctm = Utils.oppColor(self.ctm)
            return
        if self.squares[dest].color != '-':
            move.capture = True
        if move.capture:
            move.captured = self.squares[dest]
            self.pieces[Utils.oppColor(col)].remove(move.captured)

        self.squares[dest] = self.squares[pos]
        self.squares[pos] = Piece('-', pos)
        self.squares[dest].pos = dest

        self.ctm = Utils.oppColor(self.ctm)

    def undoMove(self, move):
        pos = move.pos
        dest = move.dest
        col = move.color

        if move.flag != None:
            if move.flag == "K" or move.flag == 'k':
                self.squares[pos] = self.squares[dest]
                self.squares[pos].pos = pos
                self.squares[dest + 1] = self.squares[pos + 1]
                self.squares[dest + 1].pos = dest + 1
                self.squares[pos + 1] = Piece('-', pos + 1)
                self.squares[pos + 2] = Piece('-', pos + 2)
            elif move.flag == "Q" or move.flag == 'q':
                self.squares[pos] = self.squares[dest]
                self.squares[pos].pos = pos
                self.squares[dest - 2] = self.squares[pos - 1]
                self.squares[dest - 2].pos = dest - 2
                self.squares[pos - 1] = Piece('-', pos - 1)
                self.squares[pos - 2] = Piece('-', pos - 2)
            elif move.flag == 'p' or move.flag == 'P':
                self.squares[pos] = self.squares[dest]
                self.squares[pos].pos = pos
                self.squares[pos].dethrone()
                if move.capture:
                    self.squares[dest] = move.captured
                    self.pieces[Utils.oppColor(col)].append(move.captured)
                else:
                    self.squares[dest] = Piece("-", dest)
                    self.ctm = Utils.oppColor(self.ctm)
            return
        self.squares[pos] = self.squares[dest]
        self.squares[pos].pos = pos
        if move.capture:
            self.squares[dest] = move.captured
            self.pieces[Utils.oppColor(col)].append(move.captured)
        else:
            self.squares[dest] = Piece("-", dest)
        self.ctm = Utils.oppColor(self.ctm)

    def evalPos(self):
        wScore = 0
        for p in self.pieces['w']:
            wScore += p.value + evalPiecePos(p)
        bScore = 0
        for p in self.pieces['b']:
            bScore += p.value - evalPiecePos(p)
        return wScore - bScore
