class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        if not lname: raise ValueError("Last name cannot be empty.")
        if not fname: raise ValueError("First name cannot be empty.")
        if not major: raise ValueError("Major cannot be empty.")
        if not isinstance(gpa, float) or gpa < 0.0 or gpa > 4.0: raise ValueError("GPA must be a float between 0.0 and 4.0.")

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)