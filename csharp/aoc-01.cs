// AOC 2024 1.1

int AOC1_1(string filePath)
{
    List<string> inputData = File.ReadAllText(filePath).Split("\n").SkipLast(1).ToList();

    List<int> arr1 = inputData.Select(x => int.Parse(x.Split(' ', StringSplitOptions.RemoveEmptyEntries)[0])).ToList();
    List<int> arr2 = inputData.Select(x => int.Parse(x.Split(' ', StringSplitOptions.RemoveEmptyEntries)[1])).ToList();

    arr1.Sort();
    arr2.Sort();

    int result = arr1.Zip(arr2, (a, b) => Math.Abs(a - b)).Sum();

    return result;
}


int AOC1_2(string filePath)
{
    string inputFilePath = "../01/1.input.txt";
    List<string> inputData = File.ReadAllText(inputFilePath).Split("\n").SkipLast(1).ToList();

    List<int> arr1 = inputData.Select(x => int.Parse(x.Split(' ', StringSplitOptions.RemoveEmptyEntries)[0])).ToList();
    List<int> arr2 = inputData.Select(x => int.Parse(x.Split(' ', StringSplitOptions.RemoveEmptyEntries)[1])).ToList();

    Dictionary<int, int> elementCount = arr1.Distinct().ToDictionary(x => x, x => arr2.Count(y => y == x));
    int result = arr1.Select(x => x * elementCount[x]).Sum();
    return result;
}

// Console.WriteLine(AOC1_1("../01/1.input.txt"));
Console.WriteLine(AOC1_2("../01/1.input.txt"));
