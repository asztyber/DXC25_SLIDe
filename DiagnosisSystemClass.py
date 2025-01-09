import numpy as np
import random

class DiagnosisSystemClass:

    def __init__(self):
        self.signal_names = [
            'B', 'FS2', 'TS21', 'GV3', 'FS3', 'TS31', 'SP31', 'CV31',  'TS32', 'SP32', 'CV32', 'GV4', 'FS4',
            'TS41', 'SP41', 'CV41',  'TS42', 'SP42', 'CV42'
        ]
        self.n_faults = 16
        self.n_loops = 4
   

    def diagnose_sample(self, sample):
        """
        This function should return the diagnosis of a sample.
        The diagnosis should be a tuple with the following elements:
        - fault_detection: 0 or 1
        - fault_isolation: a numpy array with the probabilities of each fault of length n_faults
        - cyber_detection: 0 or 1
        - cyber_isolation: a numpy array with the probabilities of each loop of length n_loops
        """
        pass
