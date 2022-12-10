
/*
For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

ASCII A-Z = 65->90
a-z = 97->122

1) Find item type that appears in each compartment
2) find #value for that item
3) sum across all sacks (not this class)
*/
namespace ElfLib;

public class ElfGroup
{
    public int NumberElves => elves.Count;

    private List<ElfSack> elves = new List<ElfSack>();

    public void AddSack(ElfSack sack)
    {
        elves.Add(sack);
    }

    public int GetPriorityOfBadge()
    {
        // Search through all elves sacks and find the only common letter
        // Intersect 1/2 then result/3
        char common = elves[0].SackContents.Intersect(elves[1].SackContents)
            .Intersect(elves[2].SackContents).First();

        // Find value
        return ElfSack.GetCharValue(common);
    }
}

public class ElfSack
{
    private const int UppercaseOffset = 38;
    private const int LowercaseOffset = 96;

    public int PriorityValue {get; private set;}

    public string SackContents {get; private set;}

    public ElfSack(string contents)
    {
        SackContents = contents;
        // Split string into two compartments
        int len = contents.Length / 2;
        string firstCompartment = contents.Substring(0, len);
        string secondCompartment = contents.Substring(len, len);
        if(firstCompartment.Length != secondCompartment.Length)
        {
            throw new InvalidDataException("Substrings should be same length!");
        }

        var matchingChar = firstCompartment.Intersect(secondCompartment);
        if(matchingChar.Count() > 1)
        {
            throw new InvalidOperationException("More than one duplicated char?");
        }

        char match = matchingChar.First();
        PriorityValue = GetCharValue(match);
    }

    public static int GetCharValue(char match)
    {
        if(char.IsUpper(match))
        {
            return (int)match - UppercaseOffset;
        }
        else
        {
            return (int)match - LowercaseOffset;
        }    
    }
}