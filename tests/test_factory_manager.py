import pytest

from factory_manager import FactoryManager

class TestFactoryManager:

    def test_create_object_unkown_name(self):

        with pytest.raises(ValueError):
            FactoryManager().create_from_name("unknown_name", None)

    def test_create_object_unkown_class(self):

        with pytest.raises(ValueError):
            FactoryManager().create_from_cls(str, None)

    def test_register_name_twice(self):

        factory = FactoryManager()
        factory.add_object_hierarchy('string', str)
        with pytest.raises(ValueError):
            factory.add_object_hierarchy('string', str)

    def test_register_class_twice(self):

        factory = FactoryManager()
        factory.add_object_hierarchy('string', str)
        with pytest.raises(ValueError):
            factory.add_object_hierarchy('another string', str)

    def test_register_class_factory_twice(self):

        factory = FactoryManager()
        factory.add_factory_method(str, None)
        with pytest.raises(ValueError):
            factory.add_factory_method(str, None)
