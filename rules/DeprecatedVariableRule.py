from ansiblelint import AnsibleLintRule


class DeprecatedVariableRule(AnsibleLintRule):

    id = 'CUSTOM0001'
    shortdesc = 'Deprecated variable declarations'
    description = 'Check of lines that have old style$ ${var} declarations'
    tags = {'deprecated'}

    def match(self, file, line):
        return '${' in line
