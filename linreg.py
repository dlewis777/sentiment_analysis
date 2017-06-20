import numpy as np
from scipy.stats import pearsonr
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.metrics import mean_squared_error as MSE
import util


def train_model(features, labels):
    model = Ridge()
    model.fit(features, labels)
    return model


if __name__ == "__main__":
    import sys
    TRAIN_FILE = sys.argv[1]
    DEV_FILE = sys.argv[2]
    train_data = util.read_data(TRAIN_FILE)
    vocab = util.get_vocab(train_data)
    train_feats = util.get_features(train_data, vocab)
    train_labels = util.get_labels(train_data)
    model = train_model(train_feats, train_labels)

    dev_data = util.read_data(DEV_FILE)
    dev_feats = util.get_features(dev_data, vocab)
    dev_labels = util.get_labels(dev_data)
    train_preds = model.predict(train_feats)
    print("TRAIN MSE: %.2f" % np.sqrt(MSE(train_preds, train_labels)))
    print("TRAIN r: %.2f" % pearsonr(train_preds, train_labels)[0])
    dev_preds = model.predict(dev_feats)
    print("DEV MSE: %.2f" % np.sqrt(MSE(dev_preds, dev_labels)))
    print("DEV r: %.2f" % pearsonr(dev_preds, dev_labels)[0])

    
