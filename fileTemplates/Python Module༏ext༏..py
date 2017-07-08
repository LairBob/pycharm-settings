# -*- coding: utf-8 -*-
"""
Created on ${DATE} ${TIME}

@author: ${USER}
"""

from py_log.logger import logMain


if __name__ == "__main__":
    logMain.open(fileName=${NAME})
    logMain.loggingLevel = "INFO"
    logMain.consoleMirror = True

    testUnits = {}
    testUnits[${NAME}] = True

    if testUnits[${NAME}]:
        logMain.INFO('Testing')
        
    logMain.INFO(${NAME} + ' Completed')