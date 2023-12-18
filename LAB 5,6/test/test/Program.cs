using System;

class LevenshteinDistance
{
    public int Dist(string a, string b)
    {
        int Rec(int i, int j)
        {
            if (i == 0 || j == 0)
            {
                return Math.Max(i, j);
            }
            else if (a[i - 1] == b[j - 1])
            {
                return Rec(i - 1, j - 1);
            }
            else
            {
                return 1 + Math.Min(Rec(i, j - 1), Math.Min(Rec(i - 1, j), Rec(i - 1, j - 1)));
            }
        }

        return Rec(a.Length, b.Length);
    }

    static void Main()
    {
        Console.Write("Введите первое слово: ");
        string str1 = Console.ReadLine();

        Console.Write("Введите второе слово: ");
        string str2 = Console.ReadLine();

        LevenshteinDistance levenshtein = new LevenshteinDistance();
        int lev = levenshtein.Dist(str1, str2);
        Console.WriteLine("Расстояние Левенштейна: " + lev);
    }
}
