import numpy as np


import numpy as np

def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return (((93.65140858898903 - (x[0] + x[2]) ** 2) ** 2) * (((x[1] + x[0]) * (60.47785699965641 + 53.47835550884468)) - ((x[2] + x[0]) * (-71.74007332603995 - 96.15173552509577)))) + (x[0] * (((22.052833372136263 ** 2) ** 2) * ((x[1] * x[0]) / -11.39694535089464))) + ((x[2] - np.sin(30.54037427125394)) ** 2)

def f3(x: np.ndarray) -> np.ndarray: 
    return (((np.cos(x[1]) * x[1]) + ((x[0] * x[0]) - x[2])) + (((np.cos(x[1]) * x[1]) + ((x[0] * x[0]) - x[2])) + ((-4.44 - (x[2] - 4.72)) + ((x[0] - np.exp(x[1])) + ((np.cos(6.311312200338675) / np.exp(x[1])) + 3.88)))))

def f4(x: np.ndarray) -> np.ndarray: 
    return (((np.sin(3.39) + (np.cos(x[1]) + (3.5 + (np.cos(x[1]) * 6.03)))) - (x[0] / 9.94)) + ((((4.039379772219219 + x[0]) / 2.9322925775842803) / (np.log(5.831417165992318) + np.cos(x[1]))) / np.exp(3.39)))

def f5(x: np.ndarray) -> np.ndarray: 
    return (x[0] / 5.32) * (x[0] * ((x[1] * x[1]) * ((x[0] / 5.44) * (((np.exp((x[0] - 4.622597263842002)) / np.log((x[1] / 5.660723354439844))) / ((x[0] + 9.149700402020141) ** 7.473502402718542)) / ((x[0] + 9.149700402020141) * 7.473502402718542)))))

def f6(x: np.ndarray) -> np.ndarray: 
    return ((((((x[1] / 1.89) + ((x[1] / 3.651384745600388) + (x[1] - x[0]))) - (x[0] / -5.89)) - (x[0] / -6.72)) - (x[1] / 9.24)) - (np.sin((x[0] / 9.71)) / (3.99 + 3.65)))

def f7(x: np.ndarray) -> np.ndarray: 
    return (((((((4.16209945259306 ** (x[0] * x[1])) + ((8.050256961346829 * 9.495403289272176) / 6.8136662010600375)) + 6.122674953917595) ** np.cos((x[1] - x[0]))) * 1.73) ** np.cos((x[1] - x[0]))) ** np.cos((x[1] - x[0]))) ** np.cos((x[1] - x[0]))

def f8(x: np.ndarray) -> np.ndarray:
    return (((np.tan(-7.77) / np.exp(x[5])) * 7.84) + ((x[5] * 9.348939228632076) * ((np.cos((x[5] * 7.411006314670986)) + np.exp(x[5])) * ((x[5] + 5.376030842358552) / 4.390448716336096)))) + (np.tan(-7.77) / np.exp(x[5]))
