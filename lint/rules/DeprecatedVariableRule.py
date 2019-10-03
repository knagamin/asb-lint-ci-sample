from ansiblelint import AnsibleLintRule


class DeprecatedVariableRule(AnsibleLintRule):

    id = 'ANSIBLE0001'
    shortdesc = 'Deprecated variable declarations'
    description = 'Check of lines that have old style$ ${var} ' + \
                  'declarations'
    tags = {'deprecated', 'myown'}

    def match(self, file, line):
        return '${' in line
