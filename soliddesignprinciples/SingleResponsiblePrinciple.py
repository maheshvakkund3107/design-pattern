class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}:{text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # Adding the below three methods disturbs the Single Responsible principle pattern.
    def save(self, filename):
        file1 = open(filename, "w")
        file1.write(str(self))
        file1.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


# Alternative approach to avoid breaking single responsible principle pattern.
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file2 = open(filename, "w")
        file2.write(str(journal))
        file2.close()


if __name__ == '__main__':
    j = Journal()
    j.add_entry("First Entry")
    j.add_entry("Second Entry")
    print(f"Journal Entries: \n {j}")
    p = PersistenceManager()
    file = r'/Users/maheshvakkund/PycharmProjects/pythonProject/design-pattern/journal.txt'
    p.save_to_file(j, file)

    with open(file) as fh:
        print(fh.read())
