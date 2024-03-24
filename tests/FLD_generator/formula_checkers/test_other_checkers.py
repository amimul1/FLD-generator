from typing import List, Set
from FLD_generator.formula import Formula, negate
from FLD_generator.formula_checkers.other_checkers import (
    _get_boolean_values,
    is_predicate_arity_consistent_set,
    is_nonsense,
)
from logger_setup import setup as setup_logger


def test_get_boolean_values():

    def _test(formul_rep: str, PAS_rep: str, gold: Set[str]):
        PAS = Formula(PAS_rep)

        formula = Formula(formul_rep)
        assert _get_boolean_values(formula, Formula(PAS_rep)) == set(gold)

        # negated_formula = negate(Formula(formul_rep))
        # negated_gold = set()
        # if 'T' in gold:
        #     negated_gold.add('F')
        # if 'F' in gold:
        #     negated_gold.add('T')
        # if 'Unknown' in gold:
        #     negated_gold.add('Unknown')
        # assert _get_boolean_values(negated_formula, PAS) == set(negated_gold)

    _test('{A}', '{A}', {'T'})
    _test('¬{A}', '{A}', {'F'})
    _test('{A}{a}', '{A}{a}', {'T'})
    _test('¬{A}{a}', '{A}{a}', {'F'})
    _test('{A}x', '{A}x', {'T'})
    _test('¬{A}x', '{A}x', {'F'})

    _test('({A} & {B})', '{A}', {'T'})
    _test('(¬{A} & {B})', '{A}', {'F'})
    _test('({A} & {B})', '{B}', {'T'})
    _test('({A} & ¬{B})', '{B}', {'F'})

    _test('({A} v {B})', '{A}', {'Unknown'})
    _test('(¬{A} v {B})', '{A}', {'Unknown'})
    _test('({A} v {B})', '{B}', {'Unknown'})
    _test('({A} v ¬{B})', '{B}', {'Unknown'})

    _test('({A} & ¬{A})', '{A}', {'T', 'F'})

    _test('¬({A} v {B})', '{A}', {'F'})
    _test('¬({A} & {B})', '{A}', {'Unknown'})

    _test('¬({A} & {B})', '{A}', {'Unknown'})

    _test('(x): {A}x', '{A}x', {'T'})
    _test('(x): ({A}x & {B}x)', '{A}x', {'T'})
    _test('¬((x): {A}x)', '{A}x', {'Unknown'})



def test_is_predicate_arity_consistent():
    assert is_predicate_arity_consistent_set(
        [Formula('{A}{a} v {B}{b}'), Formula('{C}')]
    )

    assert not is_predicate_arity_consistent_set(
        [Formula('{A}{a} v {B}{b}'), Formula('{A}')]
    )


def test_is_nonsense():
    assert is_nonsense(Formula('({A}{a} & {A}{a})'))
    assert is_nonsense(Formula('({A}{a} v {A}{a})'))


if __name__ == '__main__':
    setup_logger()

    # test_get_boolean_values()
    # test_is_predicate_arity_consistent()
    test_is_nonsense()
