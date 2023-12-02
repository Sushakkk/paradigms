import unittest
from main import *
class Test_Program(unittest.TestCase):
    # Глобальные переменные
    programs = [
        Program(1, 'Microsoft Word', 1, 2.0),
        Program(2, 'Microsoft Excel', 1, 1.5),
        Program(3, 'Google Docs', 3, 1.0),
        Program(4, 'LibreOffice Writer', 1, 1.8),
        Program(5, 'OpenOffice Calc', 4, 1.2)
    ]

    computers = [
        Computer(1, 'Model A-2000X', '8 GB DDR4', 'Иванов Иван Иванович'),
        Computer(2, 'UltraBook Pro 15S', '16 GB DDR4', 'Петрова Анна Сергеевна'),
        Computer(3, 'GamingBeast X9000', '32 GB DDR4', 'Смирнов Сергей Владимирович'),
        Computer(4, 'OfficeMaster 500', '64 GB DDR4', 'Козлова Екатерина Павловна'),
        Computer(5, 'PerformanceElite 3000', '128 GB DDR4', 'Михайлов Алексей Дмитриевич')
    ]

    pr_comp = [
        ProgramComputer(1, 1), ProgramComputer(1, 2), ProgramComputer(1, 4),
        ProgramComputer(2, 3), ProgramComputer(2, 1),
        ProgramComputer(3, 4), ProgramComputer(4, 5),
        ProgramComputer(3, 5)
    ]

    def test_A1(self):
        one_to_many = [(p.name, p.size_in_gb, c.owner, c.model)
                       for p in self.programs
                       for c in self.computers
                       if p.comp_id == c.id]

        self.assertEqual(a1_solution(one_to_many),
                         [('Microsoft Word', 2.0, 'Иванов Иван Иванович', 'Model A-2000X'),
                          ('Microsoft Excel', 1.5, 'Иванов Иван Иванович', 'Model A-2000X'),
                          ('LibreOffice Writer', 1.8, 'Иванов Иван Иванович', 'Model A-2000X'),
                          ('OpenOffice Calc', 1.2, 'Козлова Екатерина Павловна', 'OfficeMaster 500'),
                          ('Google Docs', 1.0, 'Смирнов Сергей Владимирович', 'GamingBeast X9000')])

    def test_A2(self):
        one_to_many = [(p.name, p.size_in_gb, c.owner, c.model)
                       for p in self.programs
                       for c in self.computers
                       if p.comp_id == c.id]

        self.assertEqual(a2_solution(one_to_many),
                         [('Иванов Иван Иванович', 5.3),
                          ('Козлова Екатерина Павловна', 1.2),
                          ('Смирнов Сергей Владимирович', 1.0)])

    def test_A3(self):
        many_to_many_temp = [(p.name, p_c.pr_id, p_c.comp_id)
                             for p_c in self.pr_comp
                             for p in self.programs
                             if p.id == p_c.pr_id]

        many_to_many = [(pr_name, c.model, c.owner)
                        for pr_name, dep_id, p_c_id in many_to_many_temp
                        for c in self.computers if c.id == p_c_id]

        self.assertDictEqual(a3_solution(many_to_many),{'Microsoft Excel': ['Карпов Сергей Владимирович', 'Иванов Иван Иванович']})


if __name__ == '__main__':
    unittest.main()
