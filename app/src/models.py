from typing import Any, Iterable


def rec_to_model(model: any, rec: Iterable):
    return model.parse_obj(rec)
