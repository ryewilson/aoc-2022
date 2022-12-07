using Day1;
// https://adventofcode.com/2022/day/1

// Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
// https://adventofcode.com/2022/day/1/input

/* Plan
    ** Open file
    ** line by line
    ** Parse each line as a number and store into new instance of CalorieBag
    ** continue adding to previous bag until line break
    ** After file processing finishes, find max CalorieBag

    ** Create unit tests
*/

if(args.Length == 0)
{
    Console.WriteLine("Invalid args - specify a single file to parse");
    Environment.ExitCode = 1;
    return;
}

string path = args[0];
if(!File.Exists(path))
{
    Console.WriteLine($"Error: unable to read input file ({path})");
    Environment.ExitCode = 1;
    return;
}

var inventory = await File.ReadAllLinesAsync(path);
if(inventory == null || inventory.Length == 0)
{
    Console.WriteLine("Error: file contains no inventory");
    Environment.ExitCode = 1;
    return;
}

var counter = new CalorieCounter();
counter.ProcessInventory(inventory);
Console.WriteLine($"Number of Elf bags processed: {counter.InventoryCount}");
Console.WriteLine($"Largest calorie count: {counter.GetLargestBag()}");

var topThree = counter.GetTopXBags(3);
Console.WriteLine($"Top three bags: {string.Join(", ", topThree)}");
Console.WriteLine($"Sum of the top three: {topThree.Sum()}");

Environment.ExitCode = 0;