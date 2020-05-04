from sklearn.decomposition import PCA,KernelPCA
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier, MLPRegressor


class NNR:
    usepca = False
    pca = None

    xscaler = StandardScaler()
    yscaler = StandardScaler()

    xtrain = 0
    ytrain = 0
    xtest = 0
    ytest = 0
    
    regressor = None
    regression = True

    def __init__(self,
                 xtrain, ytrain, regression=True,
                 usepca=False, n_components=0.99,
                 hidden_layer_sizes=(150, 30),
                 activation="relu", **kwargs):
        
        # if PCA
        self.usepca = usepca
        self.regression = regression
        if usepca:
            self.pca = KernelPCA(n_components=n_components, kernel="rbf")
            xtrain_pca = self.pca.fit_transform(xtrain)
            print("@nnr: explained variance ratio = ", self.pca.explained_variance_ratio_)
            # scale
            xtrain_scaled = self.xscaler.fit_transform(xtrain_pca)
        else:
            # scale
            xtrain_scaled = self.xscaler.fit_transform(xtrain)
        
        if regression:
            ytrain_scaled = self.yscaler.fit_transform(ytrain)
        else:
            ytrain_scaled = ytrain
        print("xtrain.shape=", xtrain_scaled.shape, "ytrain.shape=", ytrain_scaled.shape)
        
        # NN
        if regression:
            self.regressor = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, activation=activation,
                                          solver="adam", learning_rate="invscaling", learning_rate_init=0.001,
                                          verbose=True, **kwargs)
        else:
            self.regressor = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, activation=activation,
                                           solver="adam", learning_rate="invscaling", learning_rate_init=0.001,
                                           verbose=True, **kwargs)
                
        print("@nnr: fitting NN ...")
        self.regressor.fit(xtrain_scaled, ytrain_scaled)

    def transform(self, x):
        if self.usepca:
            return self.xscaler.transform(self.pca.transform(x))
        else:
            return self.xscaler.transform(x)
    
    def predict(self, xtest):
        if not self.regression:
            return self.regressor.predict(self.transform(xtest))
        else:
            return self.yscaler.inverse_transform(
                self.regressor.predict(self.transform(xtest)))
        
    def predict_proba(self, xtest):
        if self.regression:
            return self.regressor.predict_proba(self.transform(xtest))
