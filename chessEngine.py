"""Calculates moves of AI"""
from moveGeneration import *
import Utils
import time



def minimax(depth, board, alpha, beta, isMaximisingPlayer):
        if (depth == 0):
            return -board.evalPos()
        moves = genAllMoves(board)
        if isMaximisingPlayer:
            bestMove = -99999
            for m in moves:
                board.makeMove(m)
                a = minimax(depth - 1, board, alpha, beta, False)
                bestMove = max(bestMove, a)
                board.undoMove(m)
                alpha = max(alpha, bestMove)
                if beta <= alpha:
                    return beta
            if len(moves) == 0:
                if board.isInCheck('b'):
                    return -100000
                else:
                    return 0
            return bestMove
        else:
            bestMove = 99999
            for m in moves:
                board.makeMove(m)
                b = minimax(depth - 1, board, alpha, beta, True)

                bestMove = min(bestMove, b)
                board.undoMove(m)
                beta = min(beta, bestMove)
                if beta <= alpha:
                        return alpha
            if len(moves) == 0:
                if board.isInCheck('w'):
                    return 100000
                else:
                    return 0
            return bestMove
def findBestMove(depth,board,alpha,beta,isMaximisingPlayer):
    "hereeee"
    moves = genAllMoves(board)
    if len(moves) == 0:
        return "wCheckMate"
    if isMaximisingPlayer:
            best= -99999
            prevBest = -99999
            bestMove = -99999
            alpha = -99999
            beta = 99999
            movehist2 = 0
            for m in moves:
                board.makeMove(m)
                c = minimax(depth-1, board, alpha, beta, False)
                best = max(best, c)
                if best > prevBest:
                    bestMove = m
                    prevBest = best
                board.undoMove(m)
                alpha = max(alpha, best)
                if beta <= alpha:
                    return bestMove
            if bestMove == -99999:
                if len(moves) >0:
                    return moves[0]
                else:
                    return "checkMate"
            Utils.EngineDoneThinking = 1
            return bestMove