// Day 2 - Rock, Paper, Scissors

using Day2Lib;

var input = File.ReadAllLines(args[0]);

GameScore score = RPSGame.PlayGame(input);

Console.WriteLine($"Score: {score}");