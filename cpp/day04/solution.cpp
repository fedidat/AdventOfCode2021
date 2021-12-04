#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <numeric>

std::vector<std::string> get_input(std::string filename);
int part_1(std::vector<int> drawnNumbers, std::vector<std::vector<std::vector<int>>> boards);
int part_2(std::vector<int> drawnNumbers, std::vector<std::vector<std::vector<int>>> boards);
int solve(std::vector<int> drawnNumbers, std::vector<std::vector<std::vector<int>>> boards, bool firstBoard);

std::vector<int> splitInt(const std::string &s, char delim) {
    std::vector<int> elems;
    std::stringstream ss(s);
    std::string number;
    while (std::getline(ss, number, delim)) {
        if (number == "")
            continue;
        elems.push_back(std::stoi(number));
    }
    return elems;
}

int main() {
    // std::string filename = "day04/sample";
    std::string filename = "day04/input";
    std::vector<std::string> input = get_input(filename);
    std::vector<int> drawnNumbers = splitInt(input[0], ',');
    std::vector<std::vector<std::vector<int>>> boards(0);
    for (int i = 2; i < input.size() && !input.empty(); i++) {
        std::vector<std::vector<int>> board(0);
        for (int offset = 0; offset < 5; offset++, i++){
            board.push_back(splitInt(input[i], ' '));
        }
        boards.push_back(board);
    }
    std::cout << "Part 1: " << part_1(drawnNumbers, boards) << std::endl;
    std::cout << "Part 2: " << part_2(drawnNumbers, boards) << std::endl;
    return 0;
}

std::vector<std::string> get_input(std::string filename) {
    std::vector<std::string> input;
    std::string line;
    std::ifstream file (filename);
    if (!file.is_open()) throw std::invalid_argument("Unable to open file " + filename);
    while (getline(file, line))
        input.push_back(line);
    file.close();
    return input;
}

int part_1(std::vector<int> drawnNumbers, std::vector<std::vector<std::vector<int>>> boards) {
    return solve(drawnNumbers, boards, true);
}

int part_2(std::vector<int> drawnNumbers, std::vector<std::vector<std::vector<int>>> boards) {
    return solve(drawnNumbers, boards, false);
}

int solve(std::vector<int> drawnNumbers, std::vector<std::vector<std::vector<int>>> boards, bool firstBoard) {
    std::vector<std::set<int>> toDraw(boards.size(), std::set<int>());
    std::vector<std::map<int, int>> lines(boards.size(), std::map<int, int>()), columns(boards.size(), std::map<int, int>());
    for (int boardIdx = 0; boardIdx < boards.size(); boardIdx++) {
        for (int i=0; i<5; i++) {
            for (int j=0; j<5; j++) {
                lines[boardIdx].insert({boards[boardIdx][i][j], i});
                columns[boardIdx].insert({boards[boardIdx][i][j], j});
                toDraw[boardIdx].insert(boards[boardIdx][i][j]);
            }
        }
    }

    std::vector<std::vector<int>> lineScore(boards.size(), std::vector<int>(5, 0)), columnScore(boards.size(), std::vector<int>(5, 0));
    std::set<int> boardsLeft;
    for (int i = 0; i < boards.size(); ++i) 
        boardsLeft.insert(i);
    for (int drawnNumber : drawnNumbers) {
        for (int boardIdx = 0; boardIdx < boards.size(); boardIdx++) {
            if (boardsLeft.count(boardIdx)) {
                toDraw[boardIdx].erase(drawnNumber);
                if((lines[boardIdx].count(drawnNumber) && ++lineScore[boardIdx][lines[boardIdx][drawnNumber]] == 5)
                    || (columns[boardIdx].count(drawnNumber) && ++columnScore[boardIdx][columns[boardIdx][drawnNumber]] == 5)) {
                    if (firstBoard || boardsLeft.size() == 1)
                        return drawnNumber * std::accumulate(toDraw[boardIdx].begin(), toDraw[boardIdx].end(), 0);
                    else
                        boardsLeft.erase(boardIdx);
                }
            }
        }
    }
}
