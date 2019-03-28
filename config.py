#!/usr/local/bin/python
# -*- coding: utf-8 -*-
class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Dev config class."""
    #Open Debug
    DEBUG=True
