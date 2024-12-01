from typing import List, Optional, Dict, Tuple, List

from .formula import Formula, DERIVE


class Argument:

    def __init__(self,
                 premises: List[Formula],
                 conclusion: Formula,
                 assumptions: Dict[Formula, Formula],
                 intermediate_constants: Optional[List[Formula]] = None,
                 id: Optional[str] = None):
        self.premises = premises
        self.conclusion = conclusion
        self.assumptions = assumptions

        if intermediate_constants is not None:
            for constant in intermediate_constants:
                if constant.rep != constant.constants[0].rep:
                    raise ValueError(f'The intermediate formula {constant.rep} must be a single constant')
            self.intermediate_constants = intermediate_constants
        else:
            self.intermediate_constants = []

        self.id = id

    def __str__(self) -> str:
        return f'Argument(id="{self.id}", assumptions={str(self.assumptions)}, premises={str(self.premises)}, conclusion={str(self.conclusion)}, intermediate_constants={str(self.intermediate_constants)})'

    def __repr__(self) -> str:
        return str(self)

    @property
    def all_formulas(self) -> List[Formula]:
        # intermediate_constants is not formulas.
        return self.premises\
            + [self.assumptions[premise] for premise in self.premises
               if premise in self.assumptions]\
            + [self.conclusion]

    @classmethod
    def from_json(cls, json_dict: Dict) -> 'Argument':
        assumption_reps = [cls._parse_premise(rep)[0] for rep in json_dict['premises']]
        premise_reps = [cls._parse_premise(rep)[1] for rep in json_dict['premises']]

        assumptions = [(Formula(rep) if rep is not None else None) for rep in assumption_reps]
        premises = [Formula(rep) for rep in premise_reps]
        intermediate_constants = [Formula(rep) for rep in json_dict.get('intermediate', [])]
        return Argument(
            premises,
            Formula(json_dict['conclusion']),
            {premise: assumption for premise, assumption in zip(premises, assumptions)
             if assumption is not None},
            intermediate_constants=intermediate_constants,
            id=json_dict['id'],
        )

    @classmethod
    def _parse_premise(self, rep: str) -> Tuple[Optional[str], str]:
        if rep.find(f' {DERIVE} ') >= 0:
            assumption, premise = rep.split(f' {DERIVE} ')
            return (assumption, premise)
        else:
            return None, rep

    def to_json(self) -> Dict:
        return {
            'id': self.id,
            'intermediate': [constant.rep for constant in self.intermediate_constants],
            'premises': [
                (premise.rep if premise not in self.assumptions else f'{self.assumptions[premise].rep} {DERIVE} {premise.rep}')
                for premise in self.premises
            ],
            'conclusion': self.conclusion.rep,
        }


def is_reference_argument(arg: Argument) -> bool:
    return arg.id.find('reference') >= 0


def is_negation_elim_argument(arg: Argument) -> bool:
    return arg.id.find('negation_elim') >= 0


def is_negation_intro_argument(arg: Argument) -> bool:
    return arg.id.find('negation_intro') >= 0


def is_negation_argument(arg: Argument) -> bool:
    return is_negation_elim_argument(arg) or is_negation_intro_argument(arg)


def is_existential_argument(argument: Argument) -> bool:
    return argument.id.find('existential') >= 0


def is_universal_argument(argument: Argument) -> bool:
    return argument.id.find('universal') >= 0


def is_universal_intro_argument(argument: Argument) -> bool:
    return argument.id.find('universal_intro') >= 0


def is_propositional_argument(argument: Argument) -> bool:
    return argument.id.find('propositional') >= 0


def is_theorem_argument(argument: Argument) -> bool:
    return argument.id.find('theorem') >= 0


def get_theorem_adjust_weight(argument: Argument,
                              subset: Optional[str] = None,
                              suppress_others=False) -> float:
    """
    Considered ./outputs/G02.compute_rule_stats.sh/2024-08-08/
    """
    if argument.id.find('theorem') < 0:
        return None
    if subset is None:
        return 1.0

    if subset == 'G_MP':
        if argument.id.find('predicate.universal_theorem.implication_elim') >= 0:
            return 50
        else:
            if suppress_others:
                return 0.0
            else:
                return 1.0

    elif subset == 'G_MP.syllogism':
        if argument.id.find('predicate.universal_theorem.implication_elim') >= 0:
            return 50
        elif argument.id.find('syllogism') >= 0:
            return 0.1
        else:
            if suppress_others:
                return 0.0
            else:
                return 1.0

    elif subset == 'G_MP.syllogism.contraposition':
        if argument.id.find('predicate.universal_theorem.implication_elim') >= 0:
            return 50
        elif argument.id.find('syllogism') >= 0:
            return 0.1
        elif argument.id.find('contraposition') >= 0:
            return 1.0
        else:
            if suppress_others:
                return 0.0
            else:
                return 1.0

    elif subset == 'G_MP.syllogism.contraposition.interchangeability':
        if argument.id.find('predicate.universal_theorem.implication_elim') >= 0:
            return 50
        elif argument.id.find('syllogism') >= 0:
            return 0.1
        elif argument.id.find('contraposition') >= 0:
            return 1.0
        elif argument.id.find('interchangeability') >= 0:
            return 0.25
        else:
            if suppress_others:
                return 0.0
            else:
                return 1.0

    elif subset == 'all':
        if argument.id.find('predicate.universal_theorem.implication_elim') >= 0:
            return 50
        elif argument.id.find('syllogism') >= 0:
            return 0.1
        elif argument.id.find('contraposition') >= 0:
            return 1.0
        elif argument.id.find('interchangeability') >= 0:
            return 0.25
        else:
            return 1.0

    else:
        raise ValueError(f'Unknown subset: {subset}')
