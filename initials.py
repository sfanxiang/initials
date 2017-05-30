#!/usr/bin/env python3
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

def main(file_in, file_out):
	words_initial = {}

	with open(file_in, 'r') as f:
		for x in f:
			x = x.strip('\r').strip('\n')
			if x == '': continue
			if x[0].upper() not in words_initial:
				words_initial[x[0].upper()] = []
			words_initial[x[0].upper()].append(x)

	with open(file_out, 'w') as f:
		first = True
		for initial, word_list in sorted(words_initial.items()):
			if first:
				first = False
			else:
				f.write('\n')
			f.write(initial + '\n')
			for word in sorted(word_list):
				f.write(word + '\n')

if len(sys.argv) < 3:
	print('usage: <input file> <output file>')
	sys.exit(1)
else:
	main(sys.argv[1], sys.argv[2])
