namespace Day1;

public class CalorieCounter
{
    private IList<CalorieBag> allCalorieBags = new List<CalorieBag>();

    public int InventoryCount => allCalorieBags.Count;

    public long GetLargestBag()
    {
        return allCalorieBags.Max( bag => bag.Calories);
    }

    public IEnumerable<long> GetTopXBags(int numBags)
    {
        return allCalorieBags.OrderByDescending(bag => bag.Calories).Take(numBags).Select(bag => bag.Calories);
    }

    public void ProcessInventory(IList<string> allInventory)
    {
        var currentBag = new CalorieBag();

        foreach(string line in allInventory)
        {
            // Blank line means the start of a new elf inventory
            if(string.IsNullOrEmpty(line))
            {
                // Finish the previous bag
                if(currentBag.HasCalories)
                {
                    allCalorieBags.Add(currentBag);
                }
                currentBag = new CalorieBag();
            }
            else
            {
                int calories = int.Parse(line);
                currentBag.AddCalories(calories);
            }
        }

        allCalorieBags.Add(currentBag);
    }

}