
use std::fs;
use std::collections::HashSet;

fn get_input(filename: &str) -> Vec<Vec<u32>> {
    let input: String = fs::read_to_string(filename).expect("Could not read file");
    let trim: &str = input.trim();
    let grid: Vec<Vec<u32>> = trim.split("\n")
        .map(|l| l.chars()
            .map(|n| n.to_digit(10).unwrap())
            .collect())
        .collect();
    grid
}

fn part1(filename: &str) -> u32 {
    let grid: Vec<Vec<u32>> = get_input(filename);
    let mut count: u32 = 0;
    (0..grid.len()).for_each(|y|
        (0..grid[0].len()).for_each(|x|
            if [(y as i32, x as i32-1), (y as i32, x as i32+1), (y as i32-1, x as i32), (y as i32+1, x as i32)].iter()
                .all(|(dy, dx)| &grid[y][x] < grid.get(*dy as usize).and_then(|l| l.get(*dx as usize)).unwrap_or(&10)) {
                count += 1 + grid[y][x];
            }
        )
    );

    count
}

fn remove_basin((x,y): (i32,i32), coords: &mut HashSet<(i32,i32)>) -> usize {
    if !coords.remove(&(x,y)) {
      return 0;
    }
    let mut res: usize = 1;
    for (dx,dy) in vec![(x-1,y),(x+1,y),(x,y-1),(x,y+1)] {
        res += remove_basin((dx, dy), coords);
    }
    res
}

fn part2(filename: &str) -> usize {
    let grid: Vec<Vec<u32>> = get_input(filename);
    let mut points: HashSet<(i32, i32)> = (0..grid[0].len()).map(|y| //only keep coords != 9
        (0..grid.len()).map(move |x| (x, y)))
        .flatten()
        .filter(|(x, y)| grid[*x][*y] != 9)
        .map(|(x, y)| (x as i32, y as i32))
        .collect();

    let mut basin_sizes = vec![];
    while let Some(&p) = points.iter().next() { //remove basins while grid not empty (DFS)
        basin_sizes.push(remove_basin(p, &mut points));
    }

    basin_sizes.sort_by(|a, b| a.cmp(b).reverse()); //sort
    basin_sizes.truncate(3); //top 3
    basin_sizes.iter().product() //return product
}

fn main() {
    println!("{}", part1("input"));
    println!("{}", part2("input"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn samples() {
        assert_eq!(part1("sample"), 15);
        assert_eq!(part2("sample"), 1134);
    }

    #[test]
    fn part1_expected() {
        assert_eq!(part1("input"), 560);
    }

    #[test]
    fn part2_expected() {
        assert_eq!(part2("input"), 959136);
    }
}
