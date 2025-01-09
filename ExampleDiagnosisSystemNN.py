import numpy as np
import random
from DiagnosisSystemClass import DiagnosisSystemClass
from tensorflow import keras
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

'''
This is an example implementation of the DiagnosisSystemClass.py using a neural network for residual generator.

Please note that this is not a good implementation of the DiagnosisSystemClass.py. It is only an example implementation. Don't expect any good performance from this implementation.
'''

class ExampleDiagnosisSystemNN(DiagnosisSystemClass):

    def __init__(self):
        super().__init__()
        # Try to load existing model and scalers
        try:
            self.model = keras.models.load_model('data/resources/diagnosis_model.h5')
            self.scaler_X = joblib.load('data/resources/scaler_X.pkl')
            self.scaler_y = joblib.load('data/resources/scaler_y.pkl')
        except (OSError, IOError):
            # If loading fails, build and train new model
            self.scaler_X = StandardScaler()
            self.scaler_y = StandardScaler()
            self.model = self._build_and_train_model()
        
    def _build_and_train_model(self):
        # Load and prepare data
        df = pd.read_csv('data/training_data/example_data.csv', sep=';')
        X = df[['TS42P', 'B', 'FP4P']].values
        y = df['TP42P'].values.reshape(-1, 1)
        
        # Scale the data
        X_scaled = self.scaler_X.fit_transform(X)
        y_scaled = self.scaler_y.fit_transform(y)
        
        # Build model
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(3,)),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(1)
        ])
        
        # Compile model
        model.compile(
            optimizer='adam',
            loss=keras.losses.MeanSquaredError(),
            metrics=['mae']
        )
        
        # Train model
        model.fit(
            X_scaled, y_scaled,
            epochs=10,
            batch_size=128,
            validation_split=0.2,
            verbose=1
        )
        
        # Save model
        model.save('data/resources/diagnosis_model.h5')
        joblib.dump(self.scaler_X, 'data/resources/scaler_X.pkl')
        joblib.dump(self.scaler_y, 'data/resources/scaler_y.pkl')   
        return model

    def diagnose_sample(self, sample):
        # Get prediction for the sample
        input_data = sample[['TS42P', 'B', 'FP4P']].values.reshape(1, -1)
        scaled_input = self.scaler_X.transform(input_data)
        prediction = self.model(scaled_input)
        prediction = self.scaler_y.inverse_transform(prediction)
        residual = sample['TP42P'].values[0] - prediction[0, 0]
        # process faults
        fault_detection = residual > 0.2
        
        if fault_detection == 1:
            fault_isolation = np.random.uniform(0, 1, self.n_faults)
            fault_isolation = fault_isolation / np.sum(fault_isolation)
        else:
            fault_isolation = np.zeros(self.n_faults)

        # cyber attacks
        cyber_detection = random.randint(0, 1)
        
        if cyber_detection == 1:
            cyber_isolation = np.random.uniform(0, 1, self.n_loops)
            cyber_isolation = cyber_isolation / np.sum(cyber_isolation)
        else:
            cyber_isolation = np.zeros(self.n_loops)

        return fault_detection, fault_isolation, cyber_detection, cyber_isolation
        
