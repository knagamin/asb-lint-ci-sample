import unittest
from ansiblelint import RulesCollection, Runner
from rules import DeprecatedVariableRule


class TestDeprecatedVariableRule(unittest.TestCase):
    collection = RulesCollection()

    def setup(self):
        self.collection.register(DeprecatedVariableRule())

    def test_positive(self):
        success = 'tests/deprecated_var_success.yml'
        good_runner = Runner(self.collection, success, [], [], [], 1)
        self.assertEqual([], good_runner.run())

    def test_negative(self):
#        failure = 'tests/deprecated_var_failure.yml'
        failure = 'tests/site.yml'
        bad_runner = Runner(self.collection, failure, [], [], [], 1)
        errs = bad_runner.run()
        self.assertEqual(2, len(errs))
