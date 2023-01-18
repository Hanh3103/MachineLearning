import numpy as np
from scipy.optimize import minimize


class SVM:
    def __init__(self, C=1.0, tol=1e-4, max_iter=1000):
        self.C = C
        self.tol = tol
        self.max_iter = max_iter
        self.w = None
        self.b = None
        self.support_vectors_ = None
        self.support_vector_labels_ = None

    def fit(self, X, y):
        def objective(w, X, y, C):
            n_samples, n_features = X.shape
            w = w.reshape(n_features, 1)
            margin = y * (X @ w + self.b)
            hinge_loss = np.maximum(0, 1 - margin)
            objective = 0.5 * (w.T @ w) + C * np.sum(hinge_loss)
            return objective

        def gradient(w, X, y, C):
            n_samples, n_features = X.shape
            w = w.reshape(n_features, 1)
            margin = y * (X @ w + self.b)
            gradient = w
            hinge_loss = 1 - margin
            hinge_loss[hinge_loss <= 0] = 0
            gradient -= C * (X.T @ (hinge_loss * y))
            return gradient.flatten()

        def zerofun(w, X, y):
            n_samples, n_features = X.shape
            w = w.reshape(n_features, 1)
            return np.sum(w * y)

        n_samples, n_features = X.shape
        initial_w = np.zeros(n_features)

        constraints = {'type': 'eq', 'fun': zerofun, 'args': (X, y)}
        result = minimize(fun=objective, x0=initial_w, args=(X, y, self.C),
                          jac=gradient, constraints=constraints, method='SLSQP',
                          options={'disp': True, 'maxiter': self.max_iter, 'tol': self.tol})
        self.w = result.x.reshape(n_features, 1)
        support_vectors_idx = (X @ self.w + self.b) * y < 1
        self.support_vectors_ = X[support_vectors_idx]
        self.support_vector_labels_ = y[support_vectors_idx]
        self.b = np.mean(self.support_vector_labels_ - (self.support_vectors_ @ self.w))