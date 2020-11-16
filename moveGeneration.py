"""Handles generation of all sorts of possible moves"""
from Utils import rank, col, crToPos, oppColor
from chesstables import*
from itertools import chain


class Move:
    def __init__(self, pos, dest, capture=False, flag=None):
        self.pos = pos
        self.dest = dest
        self.capture = capture
        self.flag = flag


def evalPiecePos(piece):
    p = piece.piecelower
    if piece.color == 'w':
        if p == 'p':
            return pawnEvalWhite[piece.pos]
        elif p == 'r':
            return rookEvalWhite[piece.pos]
        elif p == 'n':
            return knightEvalWhite[piece.pos]
        elif p == 'b':
            return bishopEvalWhite[piece.pos]
        elif p == 'q':
            return queenEvalWhite[piece.pos]
        elif p == 'k':
            return kingEvalWhite[piece.pos]
    if piece.color == 'b':
        if p == 'p':
            return pawnEvalBlack[piece.pos]
        elif p == 'r':
            return rookEvalBlack[piece.pos]
        elif p == 'n':
            return knightEvalBlack[piece.pos]
        elif p == 'b':
            return bishopEvalBlack[piece.pos]
        elif p == 'q':
            return queenEvalBlack[piece.pos]
        elif p == 'k':
            return kingEvalBlack[piece.pos]


def genAllMoves(board):
    moves = []
    ctm = board.ctm
    for p in board.pieces[ctm]:
        s = p.piecelower
        moves.extend(genMoves[s](board, p.pos, ctm))
    return moves


def genAllAttacked(board, ctm):
    moves = []
    for p in board.pieces[ctm]:
        s = p.piecelower
        moves.extend(genAttacked[s](board, p.pos, ctm))
    return moves


def genSlidingPieces(board, pos, table, ctm):
    moves = []
    for slide in table:
        for sq in slide:
            if board[sq].piece != '-':
                if board[sq].color != ctm:
                    move = Move(pos, sq, capture=True)
                    if not board.willBeCheck(move):
                        moves.append(move)
                        break
                else:
                    break
            else:
                move = Move(pos, sq)
                if not board.willBeCheck(move):
                    moves.append(move)
    return moves


def genKNMoves(board, pos, table, ctm):
    moves = []
    for sq in table:
        if board[sq].piece != '-':
            if board[sq].color != ctm:
                move = Move(pos, sq, capture=True)
                if not board.willBeCheck(move):
                    moves.append(move)
        else:
            move = Move(pos, sq)
            if not board.willBeCheck(move):
                moves.append(move)
    return moves


def genSlidingAttacked(board, pos, table, ctm):
    moves = []
    for slide in table:
        for sq in slide:
            if board[sq].piece != '-':
                if board[sq].color != ctm:
                    move = Move(pos, sq)
                    moves.append(move)
                    break
                else:
                    break
            else:
                move = Move(pos, sq)
                moves.append(move)
    return moves


def genKNAttacked(board, pos, table, ctm):
    moves = []
    for sq in table:
        if board[sq].piece != '-':
            if board[sq].color != ctm:
                move = Move(pos, sq)
                moves.append(move)
        else:
            move = Move(pos, sq)
            moves.append(move)
    return moves


def genBishopMoves(board, pos, ctm):
    return genSlidingPieces(board, pos, bishop_table[pos], ctm)


def genRookMoves(board, pos, ctm):
    return genSlidingPieces(board, pos, rook_table[pos], ctm)


def genKnightMoves(board, pos, ctm):
    return genKNMoves(board, pos, knight_table[pos], ctm)


def genQueenMoves(board, pos, ctm):
    return genSlidingPieces(board, pos,
                            chain(bishop_table[pos], rook_table[pos]), ctm)


def genKingMoves(board, pos, ctm):
    moves = []
    for m in genKNMoves(board, pos, king_table[pos], ctm):
        moves.append(m)
    if ctm == 'w':
        if board.castling['K'] == 1 and canCastleKingSide(board, pos):
            moves.append(Move(pos, pos + 2, flag="K"))
        if board.castling['Q'] == 1 and canCastleQueenSide(board, pos):
            moves.append(Move(pos, pos - 2, flag="Q"))
    elif ctm == 'b':
        if board.castling['k'] == 1 and canCastleKingSide(board, pos):
            moves.append(Move(pos, pos + 2, flag="k"))
        if board.castling['q'] == 1 and canCastleQueenSide(board, pos):
            moves.append(Move(pos, pos - 2, flag="q"))
    return moves


def canCastleKingSide(board, pos):
    if col(pos) == 4:
        if board[pos + 1].piece == '-' and board[pos + 2].piece == '-':

            moves = genAllAttacked(board, oppColor(board.ctm))
            for m in moves:
                if m.dest == pos + 1 or m.dest == pos + 2:
                    return False
            return True


def canCastleQueenSide(board, pos):
    if col(pos) == 4:
        if board[pos - 1].piece == '-' and board[pos - 2].piece == '-':
            moves = genAllAttacked(board, oppColor(board.ctm))
            for m in moves:
                if m.dest == pos - 1 or m.dest == pos - 2:
                    return False
            return True


def genPawnMoves(board, pos, ctm):
    moves = []
    r = rank(pos)
    c = col(pos)
    if ctm == 'w':
        if r == 1:
            if (board[crToPos(c, 3)].piece == '-' and
                    board[crToPos(c, 2)].piece == '-'):
                move = Move(pos, crToPos(c, 3))
                if not board.willBeCheck(move):
                    moves.append(Move(pos, crToPos(c, 3)))

        if board[crToPos(c, r + 1)].piece == '-':
            move = Move(pos, crToPos(c, r + 1))
            if not board.willBeCheck(move):
                moves.append(Move(pos, crToPos(c, r + 1)))
        if c != 7:
            sq = crToPos(c + 1, r + 1)
            if board[sq].piece != '-':
                if board[sq].color != ctm:
                    move = Move(pos, sq, capture=True)
                    if not board.willBeCheck(move):
                        moves.append(move)
        if c != 0:
            sq = crToPos(c - 1, r + 1)
            if board[sq].piece != '-':
                if board[sq].color != ctm:
                    move = Move(pos, sq, capture=True)
                    if not board.willBeCheck(move):
                        moves.append(move)
        if r == 6:
            for m in moves:
                m.flag = "P"
    if ctm == 'b':
        if r == 6:
            if (board[crToPos(c, 4)].piece == '-' and
                    board[crToPos(c, 5)].piece == '-'):
                move = Move(pos, crToPos(c, 4))
                if not board.willBeCheck(move):
                    moves.append(Move(pos, crToPos(c, 4)))
        if board[crToPos(c, r - 1)].piece == '-':
            move = Move(pos, crToPos(c, r - 1))
            if not board.willBeCheck(move):
                moves.append(Move(pos, crToPos(c, r - 1)))
        if c != 7:
            sq = crToPos(c + 1, r - 1)
            if board[sq].piece != '-':
                if board[sq].color != ctm:
                    move = Move(pos, sq, capture=True)
                    if not board.willBeCheck(move):
                        moves.append(move)
        if c != 0:
            sq = crToPos(c - 1, r - 1)
            if board[sq].piece != '-':
                if board[sq].color != ctm:
                    move = Move(pos, sq, capture=True)
                    if not board.willBeCheck(move):
                        moves.append(move)
        if r == 1:
            for m in moves:
                m.flag = "p"
    return moves


def genSlidingCaptures(board, pos, table, ctm):
    moves = []
    for slide in table:
        for sq in slide:
            if board[sq].piece != '-':
                if board[sq].color != ctm:
                    move = Move(pos, sq, capture=True)
                    if not board.willBeCheck(move):
                        moves.append(move)
                break
    return moves


def genBishopAttacked(board, pos, ctm):
    return genSlidingAttacked(board, pos, bishop_table[pos], ctm)


def genRookAttacked(board, pos, ctm):
    return genSlidingAttacked(board, pos, rook_table[pos], ctm)


def genKnightAttacked(board, pos, ctm):
    return genKNAttacked(board, pos, knight_table[pos], ctm)


def genKingAttacked(board, pos, ctm):
    return genKNAttacked(board, pos, king_table[pos], ctm)


def genQueenAttacked(board, pos, ctm):
    return genSlidingAttacked(board, pos,
                              chain(bishop_table[pos], rook_table[pos]), ctm)


def genPawnAttacked(board, pos, ctm):
    moves = []
    r = rank(pos)
    c = col(pos)
    if ctm == 'w':
        moves.append(Move(pos, crToPos(c + 1, r + 1)))
        moves.append(Move(pos, crToPos(c - 1, r + 1)))
    if ctm == 'b':
        moves.append(Move(pos, crToPos(c + 1, r - 1)))
        moves.append(Move(pos, crToPos(c - 1, r - 1)))
    return moves


genMoves = {}
genMoves['k'] = genKingMoves
genMoves['n'] = genKnightMoves
genMoves['q'] = genQueenMoves
genMoves['b'] = genBishopMoves
genMoves['r'] = genRookMoves
genMoves['p'] = genPawnMoves

genAttacked = {}
genAttacked['k'] = genKingAttacked
genAttacked['n'] = genKnightAttacked
genAttacked['q'] = genQueenAttacked
genAttacked['b'] = genBishopAttacked
genAttacked['r'] = genRookAttacked
genAttacked['p'] = genPawnAttacked
