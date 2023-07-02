# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline

from deep_translator import MyMemoryTranslator
def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source="en-US", target="fr-FR").translate(englishText)
    return frenchText
def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source="fr-FR", target="en-US").translate(frenchText)
    return englishText

