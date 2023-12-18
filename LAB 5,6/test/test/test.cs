using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class TestLevenshteinDistance
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
