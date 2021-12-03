#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

std::vector<std::string> get_input(std::string filename);
int part_1(std::vector<std::string> input);
int part_2(std::vector<std::string> input);
int metric(std::vector<std::string> source, char mainDigit, char otherDigit);

int main() {
    // std::string filename = "day03/sample";
    std::string filename = "day03/input";
    std::vector<std::string> input = get_input(filename);
    std::cout << "Part 1: " << part_1(input) << std::endl;
    std::cout << "Part 2: " << part_2(input) << std::endl;
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

int part_1(std::vector<std::string> input) {
    const size_t SIZE = input[0].size();
    std::vector<int> ones(SIZE, 0);
    for (int i = 0; i < SIZE; ++i)
        ones[i] = std::count_if(input.begin(), input.end(), [i](std::string line){ return line[i] == '1'; });

    int gamma = 0;
    for (int i = 0; i < SIZE; ++i)
        gamma = (gamma << 1) + (ones[i] > input.size() / 2);

    int epsilon = gamma ^ ((1 << SIZE) - 1);
    return gamma * epsilon;
}

int part_2(std::vector<std::string> input) {
    int oxygen = metric(input, '1', '0');
    int co2 = metric(input, '0', '1');
    return oxygen * co2;
}

int metric(std::vector<std::string> source, char mainDigit, char otherDigit) {
    std::vector<std::string> input = source;
    for (int i = 0; i < input[0].size() && input.size() > 1; ++i) {
        int onesCount = std::count_if(input.begin(), input.end(), [i](std::string line){ return line[i] == '1'; });
        char chosenDigit = (onesCount * 2 >= input.size()) ? mainDigit : otherDigit;
        input.erase(std::remove_if(input.begin(), input.end(), [i, chosenDigit](std::string line){ return line[i] != chosenDigit; }), input.end());
    }
    return std::stoi(input[0], nullptr, 2);
}
