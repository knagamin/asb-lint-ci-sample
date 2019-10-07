ANSIBLE_LINT="ansible-lint -r rules"

@test "Can read DeprecateVariableRule" {
    run bash -c "${ANSIBLE_LINT} -L | grep Deprecated"
    [ "${status}" -eq 0 ]
}

@test "DeprecateVariableRule shows success" {
    run ${ANSIBLE_LINT} tests/deprecated_var_*success.yml
    [ "${status}" -eq 0 ]
}

@test "DeprecateVariableRule shows failure" {
    run ${ANSIBLE_LINT} tests/deprecated_var_*failure.yml
    [ "${status}" -ne 0 ]
}
