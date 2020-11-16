def rev(l):
	temp = []
	for a in l:
		for b in a:
			temp.append(b)
	temp.reverse()
	print(temp)
l = [

    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]
rev(l)

if self.squares[pos].piecelower == 'r':
            if Utils.col(pos) == 0:
                if self.ctm == 'w':
                    self.castling['Q'] = 0
                else:
                    self.castling['q'] = 0
            elif Utils.col(pos) == 7:
                if self.ctm == 'w':
                    self.castling['K'] = 0
                else:
                    self.castling['k'] = 0
        if self.squares[pos].piecelower == 'k':
            if self.ctm == 'w':
                self.castling["K"] = 0
                self.castling["Q"] = 0
            else:
                self.castling['k'] = 0
                self.castling['q'] = 0