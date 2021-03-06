"""Provides tables with all possible squares that piece can go to"""
knight_table = \
    [   [17, 10],
        [16, 18, 11],
        [17, 19, 12, 8],
        [18, 20, 13, 9],
        [19, 21, 14, 10],
        [20, 22, 15, 11],
        [21, 23, 12],
        [22, 13],
        [25, 18, 2],
        [24, 26, 19, 3],
        [25, 27, 20, 4, 0, 16],
        [26, 28, 21, 5, 1, 17],
        [27, 29, 22, 6, 2, 18],
        [28, 30, 23, 7, 3, 19],
        [29, 31, 4, 20],
        [30, 5, 21],
        [33, 26, 10, 1],
        [32, 34, 27, 11, 2, 0],
        [33, 35, 28, 12, 3, 1, 8, 24],
        [34, 36, 29, 13, 4, 2, 9, 25],
        [35, 37, 30, 14, 5, 3, 10, 26],
        [36, 38, 31, 15, 6, 4, 11, 27],
        [37, 39, 7, 5, 12, 28],
        [38, 6, 13, 29],
        [41, 34, 18, 9],
        [40, 42, 35, 19, 10, 8],
        [41, 43, 36, 20, 11, 9, 16, 32],
        [42, 44, 37, 21, 12, 10, 17, 33],
        [43, 45, 38, 22, 13, 11, 18, 34],
        [44, 46, 39, 23, 14, 12, 19, 35],
        [45, 47, 15, 13, 20, 36],
        [46, 14, 21, 37],
        [49, 42, 26, 17],
        [48, 50, 43, 27, 18, 16],
        [49, 51, 44, 28, 19, 17, 24, 40],
        [50, 52, 45, 29, 20, 18, 25, 41],
        [51, 53, 46, 30, 21, 19, 26, 42],
        [52, 54, 47, 31, 22, 20, 27, 43],
        [53, 55, 23, 21, 28, 44],
        [54, 22, 29, 45],
        [57, 50, 34, 25],
        [56, 58, 51, 35, 26, 24],
        [57, 59, 52, 36, 27, 25, 32, 48],
        [58, 60, 53, 37, 28, 26, 33, 49],
        [59, 61, 54, 38, 29, 27, 34, 50],
        [60, 62, 55, 39, 30, 28, 35, 51],
        [61, 63, 31, 29, 36, 52],
        [62, 30, 37, 53],
        [58, 42, 33],
        [59, 43, 34, 32],
        [60, 44, 35, 33, 40, 56],
        [61, 45, 36, 34, 41, 57],
        [62, 46, 37, 35, 42, 58],
        [63, 47, 38, 36, 43, 59],
        [39, 37, 44, 60],
        [38, 45, 61],
        [50, 41],
        [51, 42, 40],
        [52, 43, 41, 48],
        [53, 44, 42, 49],
        [54, 45, 43, 50],
        [55, 46, 44, 51],
        [47, 45, 52],
        [46, 53]]

rook_table = \
    [   [[8, 16, 24, 32, 40, 48, 56], [1, 2, 3, 4, 5, 6, 7]],
        [[9, 17, 25, 33, 41, 49, 57], [2, 3, 4, 5, 6, 7], [0]],
        [[10, 18, 26, 34, 42, 50, 58], [3, 4, 5, 6, 7], [1, 0]],
        [[11, 19, 27, 35, 43, 51, 59], [4, 5, 6, 7], [2, 1, 0]],
        [[12, 20, 28, 36, 44, 52, 60], [5, 6, 7], [3, 2, 1, 0]],
        [[13, 21, 29, 37, 45, 53, 61], [6, 7], [4, 3, 2, 1, 0]],
        [[14, 22, 30, 38, 46, 54, 62], [7], [5, 4, 3, 2, 1, 0]],
        [[15, 23, 31, 39, 47, 55, 63], [6, 5, 4, 3, 2, 1, 0]],
        [[16, 24, 32, 40, 48, 56], [9, 10, 11, 12, 13, 14, 15], [0]],
        [[17, 25, 33, 41, 49, 57], [10, 11, 12, 13, 14, 15], [1], [8]],
        [[18, 26, 34, 42, 50, 58], [11, 12, 13, 14, 15], [2], [9, 8]],
        [[19, 27, 35, 43, 51, 59], [12, 13, 14, 15], [3], [10, 9, 8]],
        [[20, 28, 36, 44, 52, 60], [13, 14, 15], [4], [11, 10, 9, 8]],
        [[21, 29, 37, 45, 53, 61], [14, 15], [5], [12, 11, 10, 9, 8]],
        [[22, 30, 38, 46, 54, 62], [15], [6], [13, 12, 11, 10, 9, 8]],
        [[23, 31, 39, 47, 55, 63], [7], [14, 13, 12, 11, 10, 9, 8]],
        [[24, 32, 40, 48, 56], [17, 18, 19, 20, 21, 22, 23], [8, 0]],
        [[25, 33, 41, 49, 57], [18, 19, 20, 21, 22, 23], [9, 1], [16]],
        [[26, 34, 42, 50, 58], [19, 20, 21, 22, 23], [10, 2], [17, 16]],
        [[27, 35, 43, 51, 59], [20, 21, 22, 23], [11, 3], [18, 17, 16]],
        [[28, 36, 44, 52, 60], [21, 22, 23], [12, 4], [19, 18, 17, 16]],
        [[29, 37, 45, 53, 61], [22, 23], [13, 5], [20, 19, 18, 17, 16]],
        [[30, 38, 46, 54, 62], [23], [14, 6], [21, 20, 19, 18, 17, 16]],
        [[31, 39, 47, 55, 63], [15, 7], [22, 21, 20, 19, 18, 17, 16]],
        [[32, 40, 48, 56], [25, 26, 27, 28, 29, 30, 31], [16, 8, 0]],
        [[33, 41, 49, 57], [26, 27, 28, 29, 30, 31], [17, 9, 1], [24]],
        [[34, 42, 50, 58], [27, 28, 29, 30, 31], [18, 10, 2], [25, 24]],
        [[35, 43, 51, 59], [28, 29, 30, 31], [19, 11, 3], [26, 25, 24]],
        [[36, 44, 52, 60], [29, 30, 31], [20, 12, 4], [27, 26, 25, 24]],
        [[37, 45, 53, 61], [30, 31], [21, 13, 5], [28, 27, 26, 25, 24]],
        [[38, 46, 54, 62], [31], [22, 14, 6], [29, 28, 27, 26, 25, 24]],
        [[39, 47, 55, 63], [23, 15, 7], [30, 29, 28, 27, 26, 25, 24]],
        [[40, 48, 56], [33, 34, 35, 36, 37, 38, 39], [24, 16, 8, 0]],
        [[41, 49, 57], [34, 35, 36, 37, 38, 39], [25, 17, 9, 1], [32]],
        [[42, 50, 58], [35, 36, 37, 38, 39], [26, 18, 10, 2], [33, 32]],
        [[43, 51, 59], [36, 37, 38, 39], [27, 19, 11, 3], [34, 33, 32]],
        [[44, 52, 60], [37, 38, 39], [28, 20, 12, 4], [35, 34, 33, 32]],
        [[45, 53, 61], [38, 39], [29, 21, 13, 5], [36, 35, 34, 33, 32]],
        [[46, 54, 62], [39], [30, 22, 14, 6], [37, 36, 35, 34, 33, 32]],
        [[47, 55, 63], [31, 23, 15, 7], [38, 37, 36, 35, 34, 33, 32]],
        [[48, 56], [41, 42, 43, 44, 45, 46, 47], [32, 24, 16, 8, 0]],
        [[49, 57], [42, 43, 44, 45, 46, 47], [33, 25, 17, 9, 1], [40]],
        [[50, 58], [43, 44, 45, 46, 47], [34, 26, 18, 10, 2], [41, 40]],
        [[51, 59], [44, 45, 46, 47], [35, 27, 19, 11, 3], [42, 41, 40]],
        [[52, 60], [45, 46, 47], [36, 28, 20, 12, 4], [43, 42, 41, 40]],
        [[53, 61], [46, 47], [37, 29, 21, 13, 5], [44, 43, 42, 41, 40]],
        [[54, 62], [47], [38, 30, 22, 14, 6], [45, 44, 43, 42, 41, 40]],
        [[55, 63], [39, 31, 23, 15, 7], [46, 45, 44, 43, 42, 41, 40]],
        [[56], [49, 50, 51, 52, 53, 54, 55], [40, 32, 24, 16, 8, 0]],
        [[57], [50, 51, 52, 53, 54, 55], [41, 33, 25, 17, 9, 1], [48]],
        [[58], [51, 52, 53, 54, 55], [42, 34, 26, 18, 10, 2], [49, 48]],
        [[59], [52, 53, 54, 55], [43, 35, 27, 19, 11, 3], [50, 49, 48]],
        [[60], [53, 54, 55], [44, 36, 28, 20, 12, 4], [51, 50, 49, 48]],
        [[61], [54, 55], [45, 37, 29, 21, 13, 5], [52, 51, 50, 49, 48]],
        [[62], [55], [46, 38, 30, 22, 14, 6], [53, 52, 51, 50, 49, 48]],
        [[63], [47, 39, 31, 23, 15, 7], [54, 53, 52, 51, 50, 49, 48]],
        [[57, 58, 59, 60, 61, 62, 63], [48, 40, 32, 24, 16, 8, 0]],
        [[58, 59, 60, 61, 62, 63], [49, 41, 33, 25, 17, 9, 1], [56]],
        [[59, 60, 61, 62, 63], [50, 42, 34, 26, 18, 10, 2], [57, 56]],
        [[60, 61, 62, 63], [51, 43, 35, 27, 19, 11, 3], [58, 57, 56]],
        [[61, 62, 63], [52, 44, 36, 28, 20, 12, 4], [59, 58, 57, 56]],
        [[62, 63], [53, 45, 37, 29, 21, 13, 5], [60, 59, 58, 57, 56]],
        [[63], [54, 46, 38, 30, 22, 14, 6], [61, 60, 59, 58, 57, 56]],
        [[55, 47, 39, 31, 23, 15, 7], [62, 61, 60, 59, 58, 57, 56]]]

king_table = \
    [   [8, 1, 9],
        [9, 2, 0, 10, 8],
        [10, 3, 1, 11, 9],
        [11, 4, 2, 12, 10],
        [12, 5, 3, 13, 11],
        [13, 6, 4, 14, 12],
        [14, 7, 5, 15, 13],
        [15, 6, 14],
        [16, 9, 0, 17, 1],
        [17, 10, 1, 8, 18, 16, 0, 2],
        [18, 11, 2, 9, 19, 17, 1, 3],
        [19, 12, 3, 10, 20, 18, 2, 4],
        [20, 13, 4, 11, 21, 19, 3, 5],
        [21, 14, 5, 12, 22, 20, 4, 6],
        [22, 15, 6, 13, 23, 21, 5, 7],
        [23, 7, 14, 22, 6],
        [24, 17, 8, 25, 9],
        [25, 18, 9, 16, 26, 24, 8, 10],
        [26, 19, 10, 17, 27, 25, 9, 11],
        [27, 20, 11, 18, 28, 26, 10, 12],
        [28, 21, 12, 19, 29, 27, 11, 13],
        [29, 22, 13, 20, 30, 28, 12, 14],
        [30, 23, 14, 21, 31, 29, 13, 15],
        [31, 15, 22, 30, 14],
        [32, 25, 16, 33, 17],
        [33, 26, 17, 24, 34, 32, 16, 18],
        [34, 27, 18, 25, 35, 33, 17, 19],
        [35, 28, 19, 26, 36, 34, 18, 20],
        [36, 29, 20, 27, 37, 35, 19, 21],
        [37, 30, 21, 28, 38, 36, 20, 22],
        [38, 31, 22, 29, 39, 37, 21, 23],
        [39, 23, 30, 38, 22],
        [40, 33, 24, 41, 25],
        [41, 34, 25, 32, 42, 40, 24, 26],
        [42, 35, 26, 33, 43, 41, 25, 27],
        [43, 36, 27, 34, 44, 42, 26, 28],
        [44, 37, 28, 35, 45, 43, 27, 29],
        [45, 38, 29, 36, 46, 44, 28, 30],
        [46, 39, 30, 37, 47, 45, 29, 31],
        [47, 31, 38, 46, 30],
        [48, 41, 32, 49, 33],
        [49, 42, 33, 40, 50, 48, 32, 34],
        [50, 43, 34, 41, 51, 49, 33, 35],
        [51, 44, 35, 42, 52, 50, 34, 36],
        [52, 45, 36, 43, 53, 51, 35, 37],
        [53, 46, 37, 44, 54, 52, 36, 38],
        [54, 47, 38, 45, 55, 53, 37, 39],
        [55, 39, 46, 54, 38],
        [56, 49, 40, 57, 41],
        [57, 50, 41, 48, 58, 56, 40, 42],
        [58, 51, 42, 49, 59, 57, 41, 43],
        [59, 52, 43, 50, 60, 58, 42, 44],
        [60, 53, 44, 51, 61, 59, 43, 45],
        [61, 54, 45, 52, 62, 60, 44, 46],
        [62, 55, 46, 53, 63, 61, 45, 47],
        [63, 47, 54, 62, 46],
        [57, 48, 49],
        [58, 49, 56, 48, 50],
        [59, 50, 57, 49, 51],
        [60, 51, 58, 50, 52],
        [61, 52, 59, 51, 53],
        [62, 53, 60, 52, 54],
        [63, 54, 61, 53, 55],
        [55, 62, 54]]

bishop_table = \
    [   [[9, 18, 27, 36, 45, 54, 63]],
        [[10, 19, 28, 37, 46, 55], [8]],
        [[11, 20, 29, 38, 47], [9, 16]],
        [[12, 21, 30, 39], [10, 17, 24]],
        [[13, 22, 31], [11, 18, 25, 32]],
        [[14, 23], [12, 19, 26, 33, 40]],
        [[15], [13, 20, 27, 34, 41, 48]],
        [[14, 21, 28, 35, 42, 49, 56]],
        [[17, 26, 35, 44, 53, 62], [1]],
        [[18, 27, 36, 45, 54, 63], [16], [0], [2]],
        [[19, 28, 37, 46, 55], [17, 24], [1], [3]],
        [[20, 29, 38, 47], [18, 25, 32], [2], [4]],
        [[21, 30, 39], [19, 26, 33, 40], [3], [5]],
        [[22, 31], [20, 27, 34, 41, 48], [4], [6]],
        [[23], [21, 28, 35, 42, 49, 56], [5], [7]],
        [[22, 29, 36, 43, 50, 57], [6]],
        [[25, 34, 43, 52, 61], [9, 2]],
        [[26, 35, 44, 53, 62], [24], [8], [10, 3]],
        [[27, 36, 45, 54, 63], [25, 32], [9, 0], [11, 4]],
        [[28, 37, 46, 55], [26, 33, 40], [10, 1], [12, 5]],
        [[29, 38, 47], [27, 34, 41, 48], [11, 2], [13, 6]],
        [[30, 39], [28, 35, 42, 49, 56], [12, 3], [14, 7]],
        [[31], [29, 36, 43, 50, 57], [13, 4], [15]],
        [[30, 37, 44, 51, 58], [14, 5]],
        [[33, 42, 51, 60], [17, 10, 3]],
        [[34, 43, 52, 61], [32], [16], [18, 11, 4]],
        [[35, 44, 53, 62], [33, 40], [17, 8], [19, 12, 5]],
        [[36, 45, 54, 63], [34, 41, 48], [18, 9, 0], [20, 13, 6]],
        [[37, 46, 55], [35, 42, 49, 56], [19, 10, 1], [21, 14, 7]],
        [[38, 47], [36, 43, 50, 57], [20, 11, 2], [22, 15]],
        [[39], [37, 44, 51, 58], [21, 12, 3], [23]],
        [[38, 45, 52, 59], [22, 13, 4]],
        [[41, 50, 59], [25, 18, 11, 4]],
        [[42, 51, 60], [40], [24], [26, 19, 12, 5]],
        [[43, 52, 61], [41, 48], [25, 16], [27, 20, 13, 6]],
        [[44, 53, 62], [42, 49, 56], [26, 17, 8], [28, 21, 14, 7]],
        [[45, 54, 63], [43, 50, 57], [27, 18, 9, 0], [29, 22, 15]],
        [[46, 55], [44, 51, 58], [28, 19, 10, 1], [30, 23]],
        [[47], [45, 52, 59], [29, 20, 11, 2], [31]],
        [[46, 53, 60], [30, 21, 12, 3]],
        [[49, 58], [33, 26, 19, 12, 5]],
        [[50, 59], [48], [32], [34, 27, 20, 13, 6]],
        [[51, 60], [49, 56], [33, 24], [35, 28, 21, 14, 7]],
        [[52, 61], [50, 57], [34, 25, 16], [36, 29, 22, 15]],
        [[53, 62], [51, 58], [35, 26, 17, 8], [37, 30, 23]],
        [[54, 63], [52, 59], [36, 27, 18, 9, 0], [38, 31]],
        [[55], [53, 60], [37, 28, 19, 10, 1], [39]],
        [[54, 61], [38, 29, 20, 11, 2]],
        [[57], [41, 34, 27, 20, 13, 6]],
        [[58], [56], [40], [42, 35, 28, 21, 14, 7]],
        [[59], [57], [41, 32], [43, 36, 29, 22, 15]],
        [[60], [58], [42, 33, 24], [44, 37, 30, 23]],
        [[61], [59], [43, 34, 25, 16], [45, 38, 31]],
        [[62], [60], [44, 35, 26, 17, 8], [46, 39]],
        [[63], [61], [45, 36, 27, 18, 9, 0], [47]],
        [[62], [46, 37, 28, 19, 10, 1]],
        [[49, 42, 35, 28, 21, 14, 7]],
        [[48], [50, 43, 36, 29, 22, 15]],
        [[49, 40], [51, 44, 37, 30, 23]],
        [[50, 41, 32], [52, 45, 38, 31]],
        [[51, 42, 33, 24], [53, 46, 39]],
        [[52, 43, 34, 25, 16], [54, 47]],
        [[53, 44, 35, 26, 17, 8], [55]],
        [[54, 45, 36, 27, 18, 9, 0]]]


pawnEvalWhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0, 5,
    5, 10, 2.5, 2.5, 10, 5, 5, 10, 10,
    20, 30, 30, 20, 10, 10, 50, 50, 50,
    50, 50, 50, 50, 50, 0, 0, 0, 0,
    0, 0, 0, 0
    ]
pawnEvalBlack = [-pawnEvalWhite[i] for i in range(63,-1,-1)]


knightEvalWhite = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40, -30,
    5, 10, 1.5, 1.5, 10, 5, -30, -30, 0, 1.5,
    20, 20, 1.5, 0, -30, -30, 5, 1.5, 20, 20,
    1.5, 5, -30, -30, 0, 10, 1.5, 1.5, 10, 0,
    -30, -40, -20, 0, 0, 0, 0, -20, -40, -50,
    -40, -30, -30, -30, -30, -40, -50
    ]

knightEvalBlack = [-knightEvalWhite[i] for i in range(63,-1,-1)]

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10,
    -20, -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10, -10,
    0, 10, 10, 10, 10, 0, -10, -10, 5,
    5, 10, 10, 5, 5, -10, -10, 0, 5,
    10, 10, 5, 0, -10, -10, 0, 0, 0,
    0, 0, 0, -10, -20, -10, -10, -10,
    -10, -10, -10, -20
    ]

bishopEvalBlack = [-bishopEvalWhite[i] for i in range(63,-1,-1)]

rookEvalWhite = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
    ]

rookEvalBlack = [-rookEvalWhite[i] for i in range(63,-1,-1)]

queenEvalWhite = [
    -20, -10, -10, -5, -5, -10, -10,
    -20, -10, 0, 0, 0, 0, 5, 0,
    -10, -10, 0, 5, 5, 5, 5, 5,
    -10, -5, 0, 5, 5, 5, 5, 0,
    0, -5, 0, 5, 5, 5, 5, 0,
    -5, -10, 0, 5, 5, 5, 5, 0,
    -10, -10, 0, 0, 0, 0, 0, 0,
    -10, -20, -10, -10, -5, -5, -10, -10, -20
    ]

queenEvalBlack = [-queenEvalWhite[i] for i in range(63,-1,-1)]

kingEvalWhite = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20,
    -10, -20, -30, -30, -40, -40, -30,
    -30, -20, -30, -40, -40, -50, -50,
    -40, -40, -30, -30, -40, -40, -50,
    -50, -40, -40, -30, -30, -40, -40,
    -50, -50, -40, -40, -30, -30, -40,
    -40, -50, -50, -40, -40, -30
    ]

kingEvalBlack = [-kingEvalWhite[i] for i in range(63,-1,-1)]