from h2oaicore.transformer_utils import CustomTransformer
import datatable as dt
import numpy as np


class MyTimeColTransformer(CustomTransformer):
    @staticmethod
    def get_default_properties():
        return dict(col_type="time_column", min_cols=1, max_cols=1, relative_importance=1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        assert 'tgc' in kwargs
        self.encoder = kwargs['encoder']

    def fit_transform(self, X: dt.Frame, y: np.array = None):
        self.encoder.fit(X.to_pandas())
        return self.transform(X)

    def transform(self, X: dt.Frame):
        return self.encoder.transform(X.to_pandas())
