
import json


class InvalidStudentError(Exception):
    """Raised when a student record is invalid."""


class StudentManager:
    """Load and validate student records from a JSON file."""

    def load_students(self, filename):
        """
        Load student records and validate their data.

        Args:
            filename (str): Path to the JSON file.

        Returns:
            list: A list of valid student records.

        Raises:
            InvalidStudentError: If a student record is invalid.
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the JSON is malformed.
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                students = json.load(file)

        except FileNotFoundError:
            print(f"Error: File '{filename}' was not found.")
            return []

        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON.")
            return []

        else:
            if not isinstance(students, list):
                print("Error: JSON must contain a list of students.")
                return []

            valid_students = []

            for index, student in enumerate(students, start=1):
                try:
                    if not isinstance(student, dict):
                        raise InvalidStudentError(
                            "Record must be a dictionary."
                        )

                    name = student.get("name")
                    age = student.get("age")

                    if not isinstance(name, str) or not name.strip():
                        raise InvalidStudentError(
                            "Name must be a non-empty string."
                        )

                    if (
                        not isinstance(age, int)
                        or isinstance(age, bool)
                        or not 18 <= age <= 100
                    ):
                        raise InvalidStudentError(
                            "Age must be an integer between 18 and 100."
                        )

                except InvalidStudentError as error:
                    print(f"Record {index} rejected: {error}")

                else:
                    valid_students.append(student)
                    print(f"Valid student: {name}, Age: {age}")

            return valid_students

        finally:
            print("Student loading operation finished.")


# Create an object and load records
manager = StudentManager()

valid_students = manager.load_students("students.json")

print("\nFinal valid student list:")
print(valid_students)