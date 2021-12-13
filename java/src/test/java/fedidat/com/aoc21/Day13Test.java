package fedidat.com.aoc21;

import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class Day13Test {

    @Test
    void part1_sample() throws IOException {
        assertEquals(17, Day13.part1(Day13.getInput("input/sample")));
    }

    @Test
    void part2_sample() throws IOException {
        assertEquals("""
                #####
                #...#
                #...#
                #...#
                #####
                """, Day13.part2(Day13.getInput("input/sample")));
    }

    @Test
    void part1_input() throws IOException {
        assertEquals(621, Day13.part1(Day13.getInput("input/input")));
    }

    @Test
    void part2_input() throws IOException {
        assertEquals("""
                #..#.#..#.#..#...##..##...##....##.####
                #..#.#.#..#..#....#.#..#.#..#....#....#
                ####.##...#..#....#.#....#..#....#...#.
                #..#.#.#..#..#....#.#.##.####....#..#..
                #..#.#.#..#..#.#..#.#..#.#..#.#..#.#...
                #..#.#..#..##...##...###.#..#..##..####
                """, Day13.part2(Day13.getInput("input/input")));
    }
}