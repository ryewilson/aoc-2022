using ElfLib;

string[] allLines = File.ReadAllLines(args[0]);

var processor = new SackProcessor();
processor.LoadSack(allLines);

Console.WriteLine($"Part 1 Priority: {processor.GetTotalPriority()}");

Console.WriteLine($"Part 2 priority: {processor.GetBadgePriority()}");