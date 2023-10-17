using System;

public class LevenshteinDistance
{
    private static int CalculateDistance(string a, string b)
    {
        int[,] dp = new int[a.Length + 1, b.Length + 1];

        for (int i = 0; i <= a.Length; i++)
        {
            dp[i, 0] = i;
        }

        for (int j = 0; j <= b.Length; j++)
        {
            dp[0, j] = j;
        }

        for (int i = 1; i <= a.Length; i++)
        {
            for (int j = 1; j <= b.Length; j++)
            {
                if (a[i - 1] == b[j - 1])
                    dp[i, j] = dp[i - 1, j - 1];
                else
                    dp[i, j] = 1 + Math.Min(Math.Min(dp[i, j - 1], dp[i - 1, j]), dp[i - 1, j - 1]);
            }
        }

        return dp[a.Length, b.Length];
    }

    public static void Main(string[] args)
    {
        Console.Write("Введите первую строку: ");
        string str1 = Console.ReadLine();

        Console.Write("Введите вторую строку: ");
        string str2 = Console.ReadLine();

        int lev = CalculateDistance(str1, str2);

        Console.WriteLine("Расстояние Левенштейна: " + lev);
    }
}
