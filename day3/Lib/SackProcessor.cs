namespace ElfLib;
public class SackProcessor
{
    private List<ElfSack> allSacks = new List<ElfSack>();
    private List<ElfGroup> allGroups = new List<ElfGroup>();

    public void LoadSack(string[] allLines)
    {
        // Every 3 sacks belong to a group
        var eGroup = new ElfGroup();
        allGroups.Add(eGroup);

        foreach(string line in allLines)
        {
            var sack = new ElfSack(line);
            allSacks.Add(sack);

            if(eGroup.NumberElves == 3)
            {
                eGroup = new ElfGroup();
                allGroups.Add(eGroup);
            }
            eGroup.AddSack(sack);
        }
    }


    public int GetTotalPriority()
    {
        return allSacks.Sum(sack => sack.PriorityValue);
    }

    public int GetBadgePriority()
    {
        return allGroups.Sum(g => g.GetPriorityOfBadge());
    }
}
