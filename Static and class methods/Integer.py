from math import floor
import string


class Integer:
    def __init__(self, value):
        self.value = value

    # Can access class variables? - Yes
    # Can modify class variables? - Yes
    # Creates new instances? - Yes (often used as alternative constructors)
    # Used for - Working with the class

    # class method is a method that belongs to the class itself , not to an individual object (instance).
    @classmethod
    def from_float(cls, float_value):

        if not isinstance(float_value, float):
            return "value is not a float"

        # cls → refers to the class itself (Integer), allowing us to create a new instance using cls(...).
        return cls(floor(float_value))

    @staticmethod
    def getValue(value):
        if value == "I":
            return 1
        elif value == "V":
            return 5
        elif value == "X":
            return 10
        elif value == "L":
            return 50
        elif value == "C":
            return 100
        elif value == "D":
            return 500
        elif value == "M":
            return 1000
        return -1

        # mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # return mapping.get(ch, -1)

    @classmethod
    def romanToDecimal(cls, value):
        result = 0
        i = 0
        while i < len(value):
            curr_value = cls.getValue(value[i])

            if i + 1 < len(value):
                next_curr_value = cls.getValue(value[i + 1])

                if curr_value >= next_curr_value:
                    result += curr_value
                else:
                    result += next_curr_value - curr_value
                    i += 1  # extra increment here for subtractive pairs

            else:
                result += curr_value
            i += 1  # regular increment

        return result

    @classmethod
    def from_roman(cls, value):
        return cls(cls.romanToDecimal(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
