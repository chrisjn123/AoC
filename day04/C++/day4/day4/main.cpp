#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>

int main()
{
	std::string filename{ "C:\\Users\\Nickellbut\\Desktop\\AoC\\day4\\input.txt" };
	std::vector<std::string> lines;
	std::fstream iFile{ filename };

	while (!iFile.eof())
	{
		std::string tmp;
		std::getline(iFile, tmp);
		lines.emplace_back(tmp);
	}
}