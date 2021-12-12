module day11;

import std.stdio : writeln, File;
import std.algorithm : map;
import std.array : array;

void main()
{
	ubyte[][] input = File("input", "r")
		.byLine
		.map!(line =>line
			.map!(c => cast(ubyte) (c - '0'))
			.array)
		.array;
	ulong[2] r = solve(input);
	writeln("Part 1: ", r[0]);
	writeln("Part 2: ", r[1]);
}

ulong[2] solve(scope ubyte[][] field) {
	ulong flashesAt100;
	ulong flashesTotal = 0;
	ulong step;
	for (step = 1; step; step++) {
		foreach (row; field)
			++row[];
		foreach (const x, row; field)
			foreach (const y, ref cell; row)
				flashesTotal += tryFlash(field, x, y, cell);
		long flashesInStep = 0;
		foreach (row; field)
			foreach (ref cell; row)
				if (cell >= 10) {
					cell = 0;
					flashesInStep++;
				}
		if (step == 100)
			flashesAt100 = flashesTotal;
		if (flashesInStep == (field.length * field[0].length))
			break;
	}
	return [flashesAt100, step];
}

ulong tryFlash(scope ubyte[][] field, const size_t x, const size_t y, ref ubyte cell) {
	if (cell != 10)
		return 0;
	cell++;
	ulong flashes = 0;
	foreach (const dx; [-1, 0, 1])
		foreach (const dy; [-1, 0, 1])
			if ((dx || dy)
			&& x + dx >= 0 && x + dx < field.length
			&& y + dy >= 0 && y + dy < field[0].length
			&& field[x + dx][y + dy] < 10) {
				field[x + dx][y + dy]++;
				flashes += tryFlash(field, x + dx, y + dy, field[x + dx][y + dy]);
			}
	return flashes + 1;
}
