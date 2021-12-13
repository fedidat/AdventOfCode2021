package fedidat.com.aoc21;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Day13 {
    record Input(Set<Point> points, List<Fold> folds) { }
    record Point(int x, int y) { }
    record Fold(char axis, int along) { }

    public static void main(String[] args) throws IOException {
        // String filename = "input/sample";
        String filename = "input/input";
        Input input = getInput(filename);
        System.out.println("Part 1: " + part1(input));
        System.out.println("Part 2: " + "\n" + part2(input));
    }

    public static Input getInput(String filename) throws IOException {
        String[] input = Files.readString(Paths.get(filename), StandardCharsets.UTF_8)
            .trim()
            .split("\n\n");
        Set<Point> points = Arrays.stream(input[0].split("\n"))
            .map(s -> s.split(","))
            .map(s -> new Point(Integer.parseInt(s[0]), Integer.parseInt((s[1]))))
            .collect(Collectors.toSet());
        List<Fold> folds = Arrays.stream(input[1].split("\n"))
            .map(s -> s.replace("fold along ", "").split("="))
            .map(m -> new Fold(m[0].charAt(0), Integer.parseInt(m[1])))
            .collect(Collectors.toList());
        return new Input(points, folds);
    }

    public static int part1(Input input) {
        doFolds(input.points, input.folds.subList(0, 1));
        return input.points.size();
    }

    public static String part2(Input input) {
        doFolds(input.points, input.folds);
        return printGrid(input.points);
    }

    public static String printGrid(Set<Point> points) {
        StringBuilder sb = new StringBuilder();
        for (int y = 0; y <= points.stream().map(p -> p.y).max(Integer::compare).get(); y++) {
            for (int x = 0; x <= points.stream().map(p -> p.x).max(Integer::compare).get(); x++)
                sb.append(points.contains(new Point(x, y)) ? '#' : '.');
            sb.append('\n');
        }
        return sb.toString();
    }

    public static void doFolds(Set<Point> points, List<Fold> folds) {
        folds.forEach(f -> new HashSet<>(points).forEach(p -> {
            if (f.axis == 'x' && p.x >= f.along) {
                points.remove(p);
                points.add(new Point(f.along - (p.x - f.along), p.y));
            }
            if (f.axis == 'y' && p.y >= f.along) {
                points.remove(p);
                points.add(new Point(p.x, f.along - (p.y - f.along)));
            }
        }));
    }
}
