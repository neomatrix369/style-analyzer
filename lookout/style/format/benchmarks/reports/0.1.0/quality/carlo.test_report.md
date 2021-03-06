# Test report for javascript / file:///tmp/top-repos-quality-repos-7xvmh62d/carlo HEAD b8ce2bca042c757b13fc82a3e059980342ddd9a8

### Classification report

PPCR: 0.921

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.899| 0.988| 0.965| 0.941| 0.931| 1144| 1171| 0.977 |
| `␣` | 0.877| 0.859| 0.859| 0.868| 0.868| 474| 474| 1.000 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 55| 70| 0.786 |
| `⏎␣⁻␣⁻` | 1.000| 0.814| 0.565| 0.897| 0.722| 43| 62| 0.694 |
| `'` | 1.000| 0.946| 0.946| 0.972| 0.972| 37| 37| 1.000 |
| `⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 22| 91| 0.242 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 16| 41| 0.390 |
| `␣'` | 1.000| 1.000| 1.000| 1.000| 1.000| 14| 14| 1.000 |
| `"` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 0| 0.000 |
| `macro avg` | 0.531| 0.512| 0.482| 0.520| 0.499| 1805| 1960| 0.921 |
| `weighted avg` | 0.852| 0.898| 0.827| 0.874| 0.814| 1805| 1960| 0.921 |
| `micro avg` | 0.898| 0.898| 0.827| 0.898| 0.861| 1805| 1960| 0.921 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| "| ⏎⏎| ␣'| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |
|27 |1130 |14 |0 |0 |0 |0 |0 |0 |
|0 |67 |407 |0 |0 |0 |0 |0 |0 |
|0 |2 |0 |35 |0 |0 |0 |0 |0 |
|69 |5 |17 |0 |0 |0 |0 |0 |0 |
|15 |45 |10 |0 |0 |0 |0 |0 |0 |
|19 |3 |5 |0 |0 |0 |35 |0 |0 |
|25 |5 |11 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |0 |0 |0 |14 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u0027": {"f1-score": 0.9722222222222222, "precision": 1.0, "recall": 0.9459459459459459, "support": 37}, "macro avg": {"f1-score": 0.5198596029536081, "precision": 0.5306801071090018, "recall": 0.511812384567757, "support": 1805}, "micro avg": {"f1-score": 0.8980609418282549, "precision": 0.8980609418282548, "recall": 0.8980609418282548, "support": 1805}, "weighted avg": {"f1-score": 0.8735285193932715, "precision": 0.85218194862994, "recall": 0.8980609418282548, "support": 1805}, "\u2205": {"f1-score": 0.9412744689712621, "precision": 0.8989657915672236, "recall": 0.9877622377622378, "support": 1144}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 22}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 16}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 55}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8974358974358974, "precision": 1.0, "recall": 0.813953488372093, "support": 43}, "\u2423": {"f1-score": 0.8678038379530917, "precision": 0.8771551724137931, "recall": 0.8586497890295358, "support": 474}, "\u2423\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 14}},
  "cl_report_full": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u0027": {"f1-score": 0.9722222222222222, "precision": 1.0, "recall": 0.9459459459459459, "support": 37}, "macro avg": {"f1-score": 0.49916475483064576, "precision": 0.5306801071090018, "recall": 0.48156656160480726, "support": 1960}, "micro avg": {"f1-score": 0.8610889774236388, "precision": 0.8980609418282548, "recall": 0.8270408163265306, "support": 1960}, "weighted avg": {"f1-score": 0.8143004070185483, "precision": 0.8068675988006923, "recall": 0.8270408163265306, "support": 1960}, "\u2205": {"f1-score": 0.9308072487644151, "precision": 0.8989657915672236, "recall": 0.9649871904355252, "support": 1171}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 91}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 41}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 70}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.7216494845360826, "precision": 1.0, "recall": 0.5645161290322581, "support": 62}, "\u2423": {"f1-score": 0.8678038379530917, "precision": 0.8771551724137931, "recall": 0.8586497890295358, "support": 474}, "\u2423\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 14}},
  "ppcr": 0.9209183673469388
}
```
</details>
