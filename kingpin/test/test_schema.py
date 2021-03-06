import demjson
import os

import unittest

from kingpin import exceptions
from kingpin import schema


class TestSchema(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        super(TestSchema, self).setUp(*args, **kwargs)

        dirname, filename = os.path.split(os.path.abspath(__file__))
        self.examples = '%s/../../examples' % dirname

    def test_validate_with_simple_json(self):
        json = demjson.decode(open('%s/simple.json' % self.examples).read())
        ret = schema.validate(json)
        self.assertEqual(None, ret)

    def test_validate_with_complex_json(self):
        json = demjson.decode(open('%s/complex.json' % self.examples).read())
        ret = schema.validate(json)
        self.assertEqual(None, ret)

    def test_validate_with_invalid_json(self):
        json = {'this': 'is', 'invalid': 'ok'}
        with self.assertRaises(exceptions.InvalidScript):
            schema.validate(json)

    def test_validate_with_array_syntax(self):
        json = [{'actor': 'some actor'}]
        schema.validate(json)

    def test_validate_with_invalid_array(self):
        json = [{'garbage': 'json'}]
        with self.assertRaises(exceptions.InvalidScript):
            schema.validate(json)
