#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
	fstream iFile{ "C:\\Users\\Haleigh Hurlbut\\Desktop\\AdventOfCode\\AoC\\day5cpp\\input.txt" };
	string line{};
	vector<string> lines{};
	vector<string> moves{};

	while (!iFile.eof())
	{
		getline(iFile, line);
		if (line.find("move"))
			lines.emplace_back(line);
		else
			moves.emplace_back(line);
	}
	iFile.close();

	map<int, vector<string>> stacks{};

	lines.pop_back();
	lines.pop_back();

	for (string str : lines)
	{
		int stackNum = 1;
		int countWhiteSpace = 0;

		for (int i = 0; i < str.size(); i++)
		{
			if (str.substr(i, 1) == " ")
			{
				countWhiteSpace++;
				if (countWhiteSpace == 4)
				{
					stackNum++;
					countWhiteSpace = 0;
				}
			}
			else
			{
				if (str.substr(i, 1) != "[" && str.substr(i, 1) != "]")
				{
					countWhiteSpace = 0;
					stacks[stackNum].emplace_back(str.substr(i, 1));
					stackNum++;
				}
			}
		}
	}

	for (int i = 1; i < 10; i++)
	{
		reverse(stacks[i].begin(), stacks[i].end());
	}

	//move 3 from 2 to 9
	for (auto move : moves)
	{
		size_t pos = 0;
		pos = move.find("move") ;
		int count = stoi(move.substr(pos + 4, 3));
		pos = move.find("from");
		int src = stoi(move.substr(pos + 4, 3));
		pos = move.find("to");
		int dest = stoi(move.substr(pos + 2));

		// Part 1
		//for (int i = 0; i < count; i++)
		//{
		//	string tmp = stacks[src].back();
		//	stacks[src].pop_back();
		//	stacks[dest].push_back(tmp);
		//}

		// Part 2
		vector<string> tmp;
		for (int i = 0; i < count; i++)
		{
			tmp.push_back(stacks[src].back());
			stacks[src].pop_back();
		}
		reverse(tmp.begin(), tmp.end());
		for (auto s : tmp)
		{
			stacks[dest].push_back(s);
		}

	}

	for (int i = 1; i < 10; i++)
	{
		cout << stacks[i].back();
	}
	cout << endl;
	cout << "QRQFHFWCL" << endl;

	return (0);
}