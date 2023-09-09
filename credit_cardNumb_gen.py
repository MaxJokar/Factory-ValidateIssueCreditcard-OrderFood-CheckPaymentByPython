"""
Title: Simple Credit Card Number Generator
Author: d3adc0de
Description: A simple script to generate random credit card numbers, using the same (or similar)
             approach used by major Credit Card Issuers.
             To do that, the script uses the expected prefix and length used by a specific
             issuer, and further validates the generated number against the Luhn Formula. 
"""
import string
import random
import argparse
import sys
from pprint import pprint
   

class CardNumberGenerator:
    def __init__(self, issuer = None, validate = True):
        self.issuer = None
        if issuer:
            self.issuer = CardNumberGenerator.pick_issuer(issuer)
        self.validate = validate
     
    @staticmethod
    def pick_issuer(index):
        return CardNumberGenerator.issuers()[index]
        
    def generate(self, number=1):
        cards = []
        params = CardNumberGenerator.card_parameters()
        while len(cards) < number:
            if not self.issuer:
                issuer = random.choice(CardNumberGenerator.issuers())
            else:
                issuer = self.issuer
            card_number = str(random.choice(params[issuer]["start"]))
            card_number += str(CardNumberGenerator.random_number(n=random.choice(params[issuer]["length"])-len(card_number)))
            
            valid = CardNumberGenerator.validate_card(card_number) if self.validate else True
            if valid:
                cards.append((issuer, card_number))
        return cards
    
    @staticmethod
    def issuers():
        return list(CardNumberGenerator.card_parameters().keys())
    
    @staticmethod
    def card_parameters():
        d = {
            "American Express" : { "start" : [34, 37], "length": [15] },
            "Bankcard": { "start" : [5610] + list(range(560221,560225+1)), "length": [16] },
            "China T-Union": { "start" : [31], "length": [19] },
            "China UnionPay": { "start" : [62, 81], "length": [16, 19] },
            "Dankort": { "start" : [5019, 4571], "length": [16] },
            "Diners Club - Carte Blanche": {"start": [300, 301, 302, 303, 304, 305, 38, 39, 3095], "length": [16, 19] },
            "Diners Club - enRoute": {"start": [2014, 2149], "length": [15] },
            "Diners Club - International": {"start": [36], "length": [14, 19] },
            "Diners Club - USA & Canada": {"start": [54], "length": [16] },
            "Discover": {"start" : list(range(622126,622925+1)) + [6011, 644, 645, 646, 647, 648, 649, 65], "length": [16, 17, 18, 19]},
            "InterPayment": {"start": [636], "length": [16, 19]},
            "InstaPayment": {"start": [637, 638, 639], "length": [16]},
            "JCB": {"start": list(range(3528,3589+1)), "length": [16, 19]},
            "LankaPay": {"start": [357111], "length": [16]},
            "Laser": {"start": [6304, 6706, 6771, 6709], "length": [16, 19]},
            "Maestro": {"start": [6759, 676770, 676774], "length": [12, 19]},
            "Maestro (OLD)": {"start": [5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763], "length": [16, 19]},
            "Maestro UK": {"start": [50, 56, 57, 58, 59], "length": [12,19]},
            "MasterCard": {"start": [51, 52, 53, 54, 55] + list(range(222100,272099+1)), "length": [16]},
            "MIR": {"start": list(range(2200,2204+1)), "length": [16]},
            "NPS Pridnestrovie": {"start": list(range(6054740, 6054744+1)), "length": [16]},
            "Solo": {"start": [6334, 6767], "length": [16, 18, 19]},
            "Solo": {"start": [4903, 4905, 4911, 4936, 564182, 633110, 6333, 6759], "length": [16, 18, 19]},
            "Troy": {"start": list(range(979200, 979289+1)), "length": [16]},
            "RuPay": {"start": [60, 6521, 6522], "length": [16]},
            "UATP": {"start": [1], "length": [15]},
            "UkrCard": {"start": [6040, 6041], "length": [16]},
            "Verve": {"start": list(range(506099, 506198+1)) + list(range(650002, 650027+1)), "length": [16, 19]},
            "Visa": {"start": [4], "length": [13, 16, 19]},
            "Visa Electron": {"start": [4026, 417500, 4508, 4844, 4913, 4917], "length": [16]}
            }
        return d
     
    # Luhn Formula
    # Not sure if it's respected by all issuers, though 
    # I believe that virtual cards (and sort of) don't 
    @staticmethod
    def validate_card(card_number):
        sum = 0
        reversed = list(card_number)[:-1][::-1]
        p = []
        for i in range(len(reversed)):
            if (i+1) % 2 == 1:
                p.append(int(reversed[i]) * 2)
            else: 
                p.append(int(reversed[i]))
        numbers = [(x-9) if x>9 else x for x in p]
        for number in numbers:
            sum += number
        return (sum % 10) == int(card_number[-1:])
    
    @staticmethod
    def random_number(n=20):
        num = ''.join(random.choices(string.digits, k=n))
        return str(num)


def main():
    parser = argparse.ArgumentParser(description='Credit Card Number Generator - A simple PoC', add_help=True)

    parser.add_argument(
        '-i', '--issuer', required=False, type=int, choices=list(range(len(CardNumberGenerator.issuers()))), default=None, help='Index of issuer')
    parser.add_argument(
        '-s', '--skip-validation', required=False, default=False, action='store_true', help='Skip Luhn Formula validation')
    parser.add_argument(
        '-n', '--number', required=False, type=int, default=1, help='Number of credit cards to generate')
    parser.add_argument(
        '-H', '--extended-help', required=False, default=False, action='store_true', help='Extended Help, show issuer list')

    args = parser.parse_args()

    if args.extended_help:
        parser.print_help()
        print("[*] List of issuers:")
        i = 0
        for k in CardNumberGenerator.issuers():
            print(f"  -{i}: {k}")
            i += 1
        sys.exit(0)
    
    cc_to_generate = 1
    if int(args.number) > 1:
        cc_to_generate = int(args.number)
    
    generator = CardNumberGenerator(issuer = args.issuer, validate=(not args.skip_validation))
    cards = generator.generate(cc_to_generate)
    pprint(cards)
    
    
if __name__ == '__main__':
    main()
    
# [('Maestro', '6759807023271357887')]