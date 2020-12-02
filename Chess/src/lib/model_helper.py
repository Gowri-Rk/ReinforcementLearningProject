"""
Helper methods for working with trained models.
"""

from logging import getLogger
from lib.config import ResourceConfig

logger = getLogger(__name__)


def load_newest_model_weight(rc: ResourceConfig, model):
    """
    :param chess_zero.agent.model.ChessModel model:
    :return:
    """
    dirs = get_newest_model_dirs(rc)
    if not dirs:
        return False
    model_dir = dirs[-1]
    config_path = os.path.join(model_dir, rc.model_config_filename)
    weight_path = os.path.join(model_dir, rc.model_weight_filename)
    return model.load(config_path, weight_path)

def load_best_model_weight(model):
    """
    :param ..agent.model.ChessModel model:
    :return:
    """
    return model.load(model.config.resource.model_best_config_path, model.config.resource.model_best_weight_path)


def save_as_best_model(model):
    """

    :param ..agent.model.ChessModel model:
    :return:
    """
    return model.save(model.config.resource.model_best_config_path, model.config.resource.model_best_weight_path)


def reload_best_model_weight_if_changed(model):
    """

    :param ..agent.model.ChessModel model:
    :return:
    """
    if model.config.model.distributed:
        return load_best_model_weight(model)
    else:
        logger.debug("start reload the best model if changed")
        digest = model.fetch_digest(model.config.resource.model_best_weight_path)
        if digest != model.digest:
            return load_best_model_weight(model)

        logger.debug("the best model is not changed")
        return False
