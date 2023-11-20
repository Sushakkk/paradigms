using System;

class QuadraticEquationSolver
{
    static double InputCoefficient(string prompt)
    {
        while (true)
        {
            try
            {
                Console.Write(prompt);
                double coefficient = Convert.ToDouble(Console.ReadLine());
                return coefficient;
            }
            catch (FormatException)
            {
                Console.WriteLine("Некорректный ввод. Пожалуйста, введите действительное число.");
            }
        }
    }

    static double CalculateDiscriminant(double a, double b, double c)
    {
        return b * b - 4 * a * c;
    }

    static double[] CalculateRoots(double a, double b, double discriminant)
    {
        if (a == 0)
        {
            throw new ArgumentException("Коэффициент 'a' не может быть равен нулю для квадратного уравнения.");
        }

        if (discriminant > 0)
        {
            double x1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
            double x2 = (-b - Math.Sqrt(discriminant)) / (2 * a);
            return new double[] { x1, x2 };
        }
        else if (discriminant == 0)
        {
            double x = -b / (2 * a);
            return new double[] { x };
        }
        else
        {
            return null;
        }
    }

    static void Main(string[] args)
    {
        double a, b, c;

        // Проверка наличия параметров командной строки
        if (args.Length == 3)
        {
            try
            {
                a = Convert.ToDouble(args[0]);
                b = Convert.ToDouble(args[1]);
                c = Convert.ToDouble(args[2]);
            }
            catch (FormatException)
            {
                Console.WriteLine("Некорректные коэффициенты. Пожалуйста, введите действительные числа.");
                return;
            }
        }
        else
        {
            Console.WriteLine("Введите коэффициенты уравнения:");
            a = InputCoefficient("Коэффициент A: ");

            while (a == 0)
            {
                Console.WriteLine("Коэффициент 'a' не может быть равен нулю для квадратного уравнения.");
                a = InputCoefficient("Коэффициент A: ");
            }

            b = InputCoefficient("Коэффициент B: ");
            c = InputCoefficient("Коэффициент C: ");
        }

        double discriminant = CalculateDiscriminant(a, b, c);

        if (discriminant >= 0)
        {
            double[] roots = CalculateRoots(a, b, discriminant);
            Console.WriteLine("Дискриминант: " + discriminant);
            Console.WriteLine("Корни уравнения: " + string.Join(", ", roots));
        }
        else
        {
            Console.WriteLine("Уравнение не имеет действительных корней.");
        }
    }
}
