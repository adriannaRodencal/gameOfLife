

class Rules(object):

    ruleSets = {'original': {'bornNum': '3', 'surviveNum': '2, 3'},
                   'lava': {'bornNum': '4, 5, 6, 7, 8', 'surviveNum': '1, 2, 3, 4, 5'},
                   'random': {'bornNum': '2, 4, 6, 8', 'surviveNum': '1, 3, 5, 7'}}
                   # 'original': {'bornNum': 'O', 'surviveNum': '.'},
                   # 'original': {'bornNum': 'O', 'surviveNum': '.'}

    ruleSet = 'original'

    bornNum = ruleSets[ruleSet]['bornNum']
    surviveNum = ruleSets[ruleSet]['surviveNum']

    @classmethod
    def set_rules(cls, ruleSet):
        """
        Using classmethod set the current display set
        Using classmethod set the current display set
        and be able to change it
        :param ruleSet: chosen set of rules that
        are printed during simulation
        :return: none
        """
        legalValues = cls.ruleSets.keys()
        if ruleSet in legalValues:
            cls.ruleSet = ruleSet
            cls.bornNum = cls.ruleSets[ruleSet]['bornNum']
            cls.surviveNum = cls.ruleSets[ruleSet]['surviveNum']
        elif ruleSet == 'choice':
            cls.surviveNum = input('How many neighbors do you want your cell to have to survive? ')
            cls.bornNum = input('How many neighbors do you want your cell to have to be born? ')
        else:
            raise ValueError(f'RuleSet must be in {legalValues}.')