import unittest
from main import generate_one_to_many, generate_many_to_many, filter_programs_by_name, Program, Computer, ProgramComputerLink

class TestProgramManagement(unittest.TestCase):
    def setUp(self):
        self.programs = [
            Program(1, 'Microsoft Word', 1, 2.0),
            Program(2, 'Microsoft Excel', 1, 1.5),
            Program(3, 'Google Docs', 3, 1.0),
            Program(4, 'LibreOffice Writer', 1, 1.8),
            Program(5, 'OpenOffice Calc', 4, 1.2)
        ]

        self.computers = [
            Computer(1, 'Model A-2000X', '8 GB DDR4', 'Иванов Иван Иванович'),
            Computer(2, 'UltraBook Pro 15S', '16 GB DDR4', 'Петрова Анна Сергеевна'),
            Computer(3, 'GamingBeast X9000', '32 GB DDR4', 'Смирнов Сергей Владимирович'),
            Computer(4, 'OfficeMaster 500', '64 GB DDR4', 'Козлова Екатерина Павловна'),
            Computer(5, 'PerformanceElite 3000', '128 GB DDR4', 'Михайлов Алексей Дмитриевич')
        ]

        self.program_computer_links = [
            ProgramComputerLink(1, 1),
            ProgramComputerLink(1, 2),
            ProgramComputerLink(2, 3),
            ProgramComputerLink(2, 1),
            ProgramComputerLink(3, 4),
            ProgramComputerLink(4, 5),
            ProgramComputerLink(3, 5)
        ]

    def test_generate_one_to_many(self):
        result = generate_one_to_many(self.programs, self.computers)
        # Add assertions based on the expected output

    def test_generate_many_to_many(self):
        result = generate_many_to_many(self.programs, self.program_computer_links, self.computers)
        # Add assertions based on the expected output

    def test_filter_programs_by_name(self):
        result = filter_programs_by_name(self.programs, 'Microsoft')
        # Add assertions based on the expected output

if __name__ == '__main__':
    unittest.main()
