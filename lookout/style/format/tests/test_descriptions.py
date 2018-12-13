import lzma
from math import ceil
from pathlib import Path
from random import randint
import unittest

import bblfsh
from lookout.core.api.service_data_pb2 import File

from lookout.style.format.analyzer import FormatAnalyzer
from lookout.style.format.descriptions import describe_rule
from lookout.style.format.feature_extractor import FeatureExtractor, FeatureGroup
from lookout.style.format.features import FeatureId
from lookout.style.format.rules import Rule, RuleStats
from lookout.style.format.tests.test_analyzer import get_train_config
from lookout.style.format.utils import merge_dicts


class DescriptionsTests(unittest.TestCase):

    @classmethod
    def return_node_feature(cls, feature_id):
        return ("•••%s" % feature_id.name,
                cls.fe.feature_to_indices[FeatureGroup.node][0][feature_id],
                cls.fe.features[FeatureGroup.node][0][feature_id])

    @classmethod
    def setUpClass(cls):
        config = FormatAnalyzer._load_train_config(merge_dicts(
            get_train_config(), {
                "javascript": {
                    "feature_extractor": {
                        "left_siblings_window": 1,
                        "right_siblings_window": 1,
                        "parents_depth": 1,
                        "node_features": ["start_line", "reserved", "roles"],
                    },
                },
            }))
        base = Path(__file__).parent
        with lzma.open(str(base / "benchmark.js.xz"), mode="rt") as fin:
            contents = fin.read()
        with lzma.open(str(base / "benchmark.uast.xz")) as fin:
            uast = bblfsh.Node.FromString(fin.read())
        file = File(content=bytes(contents, "utf-8"), uast=uast)
        files = [file, file]
        cls.fe = FeatureExtractor(language="javascript",
                                  **config["javascript"]["feature_extractor"])
        cls.fe.extract_features(files)
        cls.class_representations = cls.fe.composite_class_representations
        cls.n_classes = len(cls.fe.labels_to_class_sequences)
        cls.ordinal = cls.return_node_feature(FeatureId.start_line)
        cls.categorical = cls.return_node_feature(FeatureId.reserved)
        cls.bag = cls.return_node_feature(FeatureId.roles)

    def test_describe_rule_ordinal(self):
        name, indices, feature = self.ordinal
        picked_class = randint(0, self.n_classes - 1)
        picked_class_name = self.class_representations[picked_class]
        index = indices[0]
        rule = Rule(attrs=[(index, True, 4.5)], stats=RuleStats(picked_class, 0.9, 150),
                    artificial=False)
        self.assertEqual(describe_rule(rule, self.fe),
                         "  %s ≥ %d\n"
                         "⇒ y = %s\n"
                         "Confidence: 0.900. Support: 150." % (
                             name, ceil(4.5), picked_class_name,
                         ))

    def test_describe_rule_categorical(self):
        name, indices, feature = self.categorical
        activated = randint(0, len(indices) - 1)
        activated_name = feature.names[activated]
        picked_class = randint(0, self.n_classes - 1)
        picked_class_name = self.class_representations[picked_class]
        index = indices[activated]
        rule = Rule(attrs=[(index, True, 0.5)], stats=RuleStats(picked_class, 0.9, 150),
                    artificial=False)
        self.assertEqual(describe_rule(rule, self.fe),
                         "  %s = %s\n"
                         "⇒ y = %s\n"
                         "Confidence: 0.900. Support: 150." % (
                             name, activated_name, picked_class_name,
                         ))

    def test_describe_rule_bag(self):
        name, indices, feature = self.bag
        activated = randint(0, len(indices) - 1)
        activated_name = feature.names[activated]
        not_activated = randint(0, len(indices) - 1)
        not_activated_name = feature.names[not_activated]
        picked_class = randint(0, self.n_classes - 1)
        picked_class_name = self.class_representations[picked_class]
        index = indices[activated]
        not_index = indices[not_activated]
        rule = Rule(attrs=[(index, True, 0.5), (not_index, False, 0.5)],
                    stats=RuleStats(picked_class, 0.9, 150), artificial=False)
        self.assertEqual(describe_rule(rule, self.fe),
                         "  %s in {%s} and not in {%s}\n"
                         "⇒ y = %s\n"
                         "Confidence: 0.900. Support: 150." % (
                             name, activated_name, not_activated_name, picked_class_name,
                         ))

    def test_describe_rule_left(self):
        feature_id = FeatureId.diff_line
        index = self.fe.feature_to_indices[FeatureGroup.left][0][feature_id][0]
        picked_class = randint(0, self.n_classes - 1)
        picked_class_name = self.class_representations[picked_class]
        rule = Rule(attrs=[(index, True, 4.5)], stats=RuleStats(picked_class, 0.9, 150),
                    artificial=False)
        self.assertEqual(describe_rule(rule, self.fe),
                         "  -1.%s ≥ %d\n"
                         "⇒ y = %s\n"
                         "Confidence: 0.900. Support: 150." % (
                             feature_id.name, ceil(4.5), picked_class_name,
                         ))

    def test_describe_rule_right(self):
        feature_id = FeatureId.length
        index = self.fe.feature_to_indices[FeatureGroup.right][0][feature_id][0]
        picked_class = randint(0, self.n_classes - 1)
        picked_class_name = self.class_representations[picked_class]
        rule = Rule(attrs=[(index, True, 4.5)], stats=RuleStats(picked_class, 0.9, 150),
                    artificial=False)
        self.assertEqual(describe_rule(rule, self.fe),
                         "  +1.%s ≥ %d\n"
                         "⇒ y = %s\n"
                         "Confidence: 0.900. Support: 150." % (
                             feature_id.name, ceil(4.5), picked_class_name,
                         ))

    def test_describe_rule_parent(self):
        feature_id = FeatureId.internal_type
        index = self.fe.feature_to_indices[FeatureGroup.parents][0][feature_id][0]
        picked_class = randint(0, self.n_classes - 1)
        picked_class_name = self.class_representations[picked_class]
        rule = Rule(attrs=[(index, True, 4)], stats=RuleStats(picked_class, 0.9, 150),
                    artificial=False)
        self.assertEqual(describe_rule(rule, self.fe),
                         "  ^1.%s = AnyTypeAnnotation\n"
                         "⇒ y = %s\n"
                         "Confidence: 0.900. Support: 150." % (
                             feature_id.name, picked_class_name,
                         ))


if __name__ == "__main__":
    unittest.main()
