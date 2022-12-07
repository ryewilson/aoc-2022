namespace Day1;

public class CalorieBag
{
    public long Calories {get; private set;} = 0;

    public bool HasCalories => Calories > 0;

    public void AddCalories(int calories)
    {
        Calories += calories;
    }
}