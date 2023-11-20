from operator import itemgetter
class Program:
    def __init__(self, id, name, comp_id, size_in_gb):
        self.id = id
        self.name = name
        self.comp_id = comp_id
        self.size_in_gb = size_in_gb

class Computer:
    def __init__(self, id, model, RAM, owner):
        self.id = id
        self.model = model
        self.RAM = RAM
        self.owner = owner

class ProgramComputerLink:
    def __init__(self, pr_id, comp_id):
        self.pr_id = pr_id
        self.comp_id = comp_id

def generate_one_to_many(programs, computers):
    return [(p.name, p.size_in_gb, c.owner, c.model) for p in programs for c in computers if p.comp_id == c.id]

def generate_many_to_many(programs, program_computer_links, computers):
    many_to_many_temp = [(p.name, p_c.pr_id, p_c.comp_id) for p_c in program_computer_links for p in programs if p.id == p_c.pr_id]
    return [(pr_name, c.model, c.owner) for pr_name, _, p_c_id in many_to_many_temp for c in computers if c.id == p_c_id]

def filter_programs_by_name(programs, name_substring):
    return [p for p in programs if name_substring in p.name]

def main():
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

    pr_comp = [ProgramComputerLink(1, 1), ProgramComputerLink(1, 2), ProgramComputerLink(1, 4),
               ProgramComputerLink(2, 3), ProgramComputerLink(2, 1),
               ProgramComputerLink(3, 4), ProgramComputerLink(4, 5),
               ProgramComputerLink(3, 5)]

    one_to_many_sorted = sorted(generate_one_to_many(programs, computers), key=itemgetter(0))
    many_to_many = generate_many_to_many(programs, pr_comp, computers)

    one_to_many = [(p.name, p.size_in_gb, c.owner, c.model)
                   for p in programs
                   for c in computers
                   if p.comp_id == c.id]

    many_to_many_temp = [(p.name, p_c.pr_id, p_c.comp_id)
                         for p_c in pr_comp
                         for p in programs
                         if p.id == p_c.pr_id]

    return one_to_many_sorted, many_to_many, many_to_many_temp


if __name__ == '__main__':
    main()
