#!/usr/bin/env python3
#coding:utf-8


from loginsan.textSanitizer import textSanitizer
from loginsan.emailChecker import emailChecker

def main():
    print('Testing text sanitizer for [ $£%£.?/,dededede;,;:73489é"_" ] ')
    print(textSanitizer.text_only("$£%£.?/,dededede;,;:73489é\"_\"é'"))

    print('Testing email checker for [ arthur@arthurpons.fr ]')
    print(emailChecker.checkEmail('arthur@arthurpons.fr'))

    print('Testing email checker for [ thisemaildoesnotexists@arthurpons.fr ]')
    print(emailChecker.checkEmail('thisemaildoesnotexists@arthurpons.fr'))

if __name__ == "__main__":
    main()