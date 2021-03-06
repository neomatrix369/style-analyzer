# Train report for javascript / file:///tmp/top-repos-quality-repos-_kjxainl/evergreen HEAD ba22d511dad83c072842e47801ef42697d142f7c

### Classification report

PPCR: 0.850

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.972| 0.994| 0.921| 0.983| 0.946| 23908| 25800| 0.927 |
| `␣` | 0.961| 0.961| 0.788| 0.961| 0.866| 9884| 12054| 0.820 |
| `'` | 1.000| 1.000| 0.986| 1.000| 0.993| 5451| 5529| 0.986 |
| `⏎` | 0.972| 0.924| 0.583| 0.947| 0.729| 2299| 3644| 0.631 |
| `"` | 1.000| 1.000| 1.000| 1.000| 1.000| 1036| 1036| 1.000 |
| `⏎␣⁻␣⁻` | 0.974| 0.647| 0.282| 0.777| 0.437| 685| 1573| 0.435 |
| `⏎␣⁺␣⁺` | 0.917| 0.642| 0.269| 0.756| 0.416| 640| 1526| 0.419 |
| `⏎⏎` | 0.938| 0.960| 0.544| 0.948| 0.689| 470| 829| 0.567 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 12| 96| 0.125 |
| `⏎␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 10| 146| 0.068 |
| `micro avg` | 0.973| 0.973| 0.827| 0.973| 0.894| 44395| 52233| 0.850 |
| `macro avg` | 0.773| 0.713| 0.537| 0.737| 0.608| 44395| 52233| 0.850 |
| `weighted avg` | 0.972| 0.973| 0.827| 0.971| 0.879| 44395| 52233| 0.850 |

### Confusion matrix

|refusal|  ∅| ␣| ⏎| '| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| "| ⏎␣⁺␣⁺␣⁺␣⁺| ⏎␣⁻␣⁻␣⁻␣⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1892 |23773 |131 |0 |0 |0 |3 |1 |0 |0 |0 |
|2170 |310 |9496 |27 |0 |35 |7 |9 |0 |0 |0 |
|1345 |65 |89 |2124 |0 |1 |0 |20 |0 |0 |0 |
|78 |0 |0 |0 |5451 |0 |0 |0 |0 |0 |0 |
|886 |163 |66 |0 |0 |411 |0 |0 |0 |0 |0 |
|888 |139 |84 |19 |0 |0 |443 |0 |0 |0 |0 |
|359 |3 |0 |16 |0 |0 |0 |451 |0 |0 |0 |
|0 |0 |0 |0 |0 |0 |0 |0 |1036 |0 |0 |
|136 |2 |7 |0 |0 |1 |0 |0 |0 |0 |0 |
|84 |4 |6 |0 |0 |0 |2 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| packages/evergreen-buttons/src/styles/ButtonAppearances.js | 53 |
| packages/evergreen-alert/src/components/Alert.js | 35 |
| packages/evergreen-table/docs/index.js | 34 |
| packages/evergreen-positioner/src/components/Positioner.js | 27 |
| packages/evergreen-shared-styles/src/styles/CheckboxAppearances.js | 25 |
| packages/evergreen-buttons/src/components/Button.js | 25 |
| packages/evergreen-buttons/docs/index.js | 24 |
| packages/evergreen-switch/src/styles/SwitchAppearances.js | 24 |
| packages/evergreen-autocomplete/src/components/Autocomplete.js | 22 |
| packages/evergreen-select/src/components/Select.js | 20 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1036}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 5451}, "macro avg": {"f1-score": 0.7372353489078591, "precision": 0.7733488678087925, "recall": 0.7127455236679796, "support": 44395}, "micro avg": {"f1-score": 0.972744678454781, "precision": 0.972744678454781, "recall": 0.972744678454781, "support": 44395}, "weighted avg": {"f1-score": 0.9714333434802163, "precision": 0.9720423036212563, "recall": 0.972744678454781, "support": 44395}, "\u2205": {"f1-score": 0.9830256166394443, "precision": 0.9719530643117053, "recall": 0.9943533545256817, "support": 23908}, "\u23ce": {"f1-score": 0.9471571906354515, "precision": 0.9716376944190301, "recall": 0.9238799478033928, "support": 2299}, "\u23ce\u23ce": {"f1-score": 0.9484752891692955, "precision": 0.9376299376299376, "recall": 0.9595744680851064, "support": 470}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7555147058823529, "precision": 0.9174107142857143, "recall": 0.6421875, "support": 640}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.7771929824561404, "precision": 0.9736263736263736, "recall": 0.6467153284671533, "support": 685}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 12}, "\u2423": {"f1-score": 0.9609877042959064, "precision": 0.9612308938151635, "recall": 0.9607446377984622, "support": 9884}},
  "cl_report_full": {"\"": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1036}, "\u0027": {"f1-score": 0.9928961748633881, "precision": 1.0, "recall": 0.9858925664677157, "support": 5529}, "macro avg": {"f1-score": 0.6075317170836612, "precision": 0.7733488678087925, "recall": 0.5372978921357775, "support": 52233}, "micro avg": {"f1-score": 0.8938402947385851, "precision": 0.972744678454781, "recall": 0.8267761759807019, "support": 52233}, "weighted avg": {"f1-score": 0.8791254682322271, "precision": 0.9663908308112195, "recall": 0.8267761759807019, "support": 52233}, "\u2205": {"f1-score": 0.946019618376808, "precision": 0.9719530643117053, "recall": 0.9214341085271318, "support": 25800}, "\u23ce": {"f1-score": 0.7286449399656948, "precision": 0.9716376944190301, "recall": 0.5828759604829857, "support": 3644}, "\u23ce\u23ce": {"f1-score": 0.6885496183206107, "precision": 0.9376299376299376, "recall": 0.5440289505428226, "support": 829}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.41641337386018246, "precision": 0.9174107142857143, "recall": 0.26933158584534733, "support": 1526}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 146}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.4368836291913215, "precision": 0.9736263736263736, "recall": 0.28162746344564527, "support": 1573}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 96}, "\u2423": {"f1-score": 0.8659098162586059, "precision": 0.9612308938151635, "recall": 0.7877882860461257, "support": 12054}},
  "ppcr": 0.8499416077958378
}
```
</details>
