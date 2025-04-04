import numpy as np
import random
from DiagnosisSystemClass import DiagnosisSystemClass

class ExampleDiagnosisSystem(DiagnosisSystemClass):

    def __init__(self):
        
        super().__init__()
        # your initialization code here
        # if the models or parameters does not exist in the data/resources directory run training on the 
        # training data and save the models and parameters in the data/resources directory
        # you can load models and precomputed parameters here
        # training and loading does not count towards the computation time

    def diagnose_sample(self, sample):

        sample = sample[self.signal_names]
        
        # process faults
        fault_detection = random.randint(0, 1)
        
        if fault_detection == 1:
            fault_isolation = np.random.uniform(0, 1, self.n_faults)
            fault_isolation = fault_isolation / np.sum(fault_isolation)
        else:
            fault_isolation = np.zeros(self.n_faults)

        # cyber attacks
        cyber_detection = random.randint(0, 1)
        
        if cyber_detection == 1:
            cyber_isolation = np.random.uniform(0, 1, self.n_loops)
        else:
            cyber_isolation = np.zeros(self.n_loops)

        return fault_detection, fault_isolation, cyber_detection, cyber_isolation
        
