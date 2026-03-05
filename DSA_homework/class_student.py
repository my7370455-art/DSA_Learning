class Student():
    def input(self):
        self.information = list(map(str, input().split()))
        self.name = self.information.pop(0)
        self.age = int(self.information.pop(0))
        self.scores = list(map(float, self.information))

    def calculate(self):
        self.average = sum(self.scores) / len(self.scores)

    def output(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"avg score: {self.average:.2f}")

def main():
    student = Student()
    student.input()
    student.calculate()
    student.output()

if __name__ == "__main__":
    main()