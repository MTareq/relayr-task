class Finder:

    def __init__(self, str_list):
        self.str_list = str_list

    def is_anagram(self, substring, string, ignore_case):
        """
            Checks if string is anagram to another

            Args:
                substring(str): input substring.
                string(str): sting from Finder str_list.
                ignore_case(bool): optional Boolean to ignore case.
            Returns:
                Boolean
        """
        if ignore_case:
            sorted_str = ''.join(sorted(string.lower()))
            sorted_substr = ''.join(sorted(substring.lower()))
        else:
            sorted_str = ''.join(sorted(string))
            sorted_substr = ''.join(sorted(substring))
        if sorted_str == sorted_substr:
            return True
        return False

    def find(self, substring, ignore_case=False):
        """
            Find if substring exists in the intial str_list regardless of charectar order
            Args:
                substring(str): input substring.
                ignore_case(bool): optional Boolean to ignore case.
            Returns:
                Boolean
        """
        results = []
        if type(substring) is not str:
            print('Error: Invalid Type passed to finder {}'.format(substring))
            return
        for string in self.str_list:
            if type(string) is not str:
                print('Warning: Invalid Type passed to the initial list: {}'.format(string))
                continue
            if self.is_anagram(substring, string, ignore_case):
                results.append(string)
        return results
