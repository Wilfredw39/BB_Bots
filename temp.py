from main import BlackBoard


def start():
    className_xpath = ''
    className_ultra_xpath = ''

    className = BlackBoard(course_xpath=className_xpath,
                           bb_ultra_xpath=className_ultra_xpath)

    className.enterClass()
