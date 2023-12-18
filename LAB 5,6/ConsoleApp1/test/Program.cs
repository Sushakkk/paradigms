using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class TestLevenshteinDistance
{
    [TestMethod]
    public void TestDistanceEqualStrings()
    {
        // Arrange
        LevenshteinDistance levenshtein = new LevenshteinDistance();

        // Act
        int result = levenshtein.Dist("kitten", "kitten");

        // Assert
        Assert.AreEqual(0, result);
    }

    [TestMethod]
    public void TestDistanceDifferentStrings()
    {
        // Arrange
        LevenshteinDistance levenshtein = new LevenshteinDistance();

        // Act
        int result = levenshtein.Dist("kitten", "sitting");

        // Assert
        Assert.AreEqual(3, result);
    }

    [TestMethod]
    public void TestDistanceEmptyString()
    {
        // Arrange
        LevenshteinDistance levenshtein = new LevenshteinDistance();

        // Act
        int result = levenshtein.Dist("", "abc");

        // Assert
        Assert.AreEqual(3, result);
    }
}
