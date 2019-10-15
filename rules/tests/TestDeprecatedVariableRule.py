import unittest
from ansiblelint import RulesCollection, Runner
from rules import DeprecatedVariableRule


class TestDeprecatedVariableRule(unittest.TestCase):
    collection = RulesCollection()
    collection.register(DeprecatedVariableRule())

    def test_positive(self):
        success = 'rules/tests/deprecated_var_success.yml'
        good_runner = Runner(self.collection, success, [], [], [])
        self.assertEqual([], good_runner.run())

    def test_negative(self):
        failure = 'rules/tests/deprecated_var_failure.yml'
        bad_runner = Runner(self.collection, failure, [], [], [])
        errs = bad_runner.run()
        self.assertEqual(1, len(errs))
