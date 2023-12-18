using Microsoft.VisualStudio.TestTools.UnitTesting;
using NUnit.Framework;

[TestClass]
public class TestLevenshteinDistanceMSTest
{
    [TestMethod]
    public void TestDistanceEqualStrings()
    {
        LevenshteinDistance levenshtein = new LevenshteinDistance();
        Assert.AreEqual(0, levenshtein.Dist("kitten", "kitten"));
    }

    [TestMethod]
    public void TestDistanceDifferentStrings()
    {
        LevenshteinDistance levenshtein = new LevenshteinDistance();
        Assert.AreEqual(3, levenshtein.Dist("kitten", "sitting"));
    }

    [TestMethod]
    public void TestDistanceEmptyString()
    {
        LevenshteinDistance levenshtein = new LevenshteinDistance();
        Assert.AreEqual(3, levenshtein.Dist("", "abc"));
    }
}

[TestFixture]
public class TestLevenshteinDistanceNUnit
{
    [Test]
    public void TestDistanceEqualStrings()
    {
        LevenshteinDistance levenshtein = new LevenshteinDistance();
        NUnit.Framework.Assert.AreEqual(0, levenshtein.Dist("kitten", "kitten"));
    }

    [Test]
    public void TestDistanceDifferentStrings()
    {
        LevenshteinDistance levenshtein = new LevenshteinDistance();
        NUnit.Framework.Assert.AreEqual(3, levenshtein.Dist("kitten", "sitting"));
    }

    [Test]
    public void TestDistanceEmptyString()
    {
        LevenshteinDistance levenshtein = new LevenshteinDistance();
        NUnit.Framework.Assert.AreEqual(3, levenshtein.Dist("", "abc"));
    }
}
