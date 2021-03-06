# Test report for javascript / file:///tmp/top-repos-quality-repos-bz0i_ahe/react-native HEAD 1850906e5e557beb2234a1708cfc5fe8e7b4f0bf

### Classification report

PPCR: 0.931

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.968| 0.989| 0.972| 0.978| 0.970| 45992| 46775| 0.983 |
| `␣` | 0.963| 0.975| 0.911| 0.969| 0.936| 20479| 21917| 0.934 |
| `⏎` | 0.877| 0.882| 0.675| 0.880| 0.763| 5035| 6573| 0.766 |
| `⏎␣⁺␣⁺` | 0.916| 0.706| 0.538| 0.798| 0.678| 3324| 4368| 0.761 |
| `⏎␣⁻␣⁻` | 0.919| 0.818| 0.731| 0.865| 0.814| 3251| 3635| 0.894 |
| `'` | 0.905| 0.991| 0.944| 0.946| 0.924| 2521| 2646| 0.953 |
| `⏎⏎` | 0.712| 0.806| 0.567| 0.756| 0.631| 839| 1193| 0.703 |
| `␣'` | 0.873| 0.939| 0.823| 0.904| 0.847| 701| 800| 0.876 |
| `"` | 0.974| 0.644| 0.453| 0.775| 0.618| 348| 495| 0.703 |
| `"␣` | 1.000| 0.840| 0.781| 0.913| 0.877| 200| 215| 0.930 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 196| 279| 0.703 |
| `'␣` | 0.818| 0.628| 0.570| 0.711| 0.672| 129| 142| 0.908 |
| `⏎⏎'` | 0.933| 0.990| 0.990| 0.960| 0.960| 98| 98| 1.000 |
| `␣"` | 0.000| 0.000| 0.000| 0.000| 0.000| 70| 108| 0.648 |
| `⏎␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 45| 65| 0.692 |
| `⏎␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 33| 101| 0.327 |
| `"⏎` | 1.000| 0.172| 0.167| 0.294| 0.286| 29| 30| 0.967 |
| `'⏎` | 1.000| 0.500| 0.417| 0.667| 0.588| 10| 12| 0.833 |
| `⏎⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 10| 19| 0.526 |
| `⏎'` | 0.000| 0.000| 0.000| 0.000| 0.000| 7| 7| 1.000 |
| `"⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 4| 64| 0.062 |
| `macro avg` | 0.612| 0.518| 0.454| 0.544| 0.503| 83321| 89542| 0.931 |
| `weighted avg` | 0.947| 0.952| 0.886| 0.948| 0.909| 83321| 89542| 0.931 |
| `micro avg` | 0.952| 0.952| 0.886| 0.952| 0.917| 83321| 89542| 0.931 |

### Confusion matrix

|refusal|  ∅| ␣| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| '| ⏎⏎| ␣'| "| ⏎␣⁻␣⁻␣⁻␣⁻| '␣| "␣| ⏎⏎'| ⏎␣⁺␣⁺␣⁺␣⁺| ␣"| ⏎␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻| "⏎| "⏎␣⁻␣⁻| '⏎| ⏎⏎␣⁻␣⁻| ⏎'| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|783 |45479 |239 |22 |190 |62 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1438 |339 |19964 |133 |10 |29 |0 |4 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1538 |109 |175 |4439 |0 |24 |0 |262 |26 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1044 |647 |231 |29 |2348 |0 |60 |0 |7 |2 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|384 |306 |87 |192 |0 |2658 |0 |7 |1 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|125 |20 |0 |0 |0 |0 |2498 |0 |1 |2 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|354 |7 |0 |156 |0 |0 |0 |676 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|99 |0 |20 |3 |0 |0 |20 |0 |658 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|147 |20 |0 |0 |0 |0 |104 |0 |0 |224 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|83 |39 |2 |54 |0 |101 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|13 |17 |0 |0 |0 |0 |31 |0 |0 |0 |0 |81 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|15 |0 |0 |0 |0 |0 |14 |0 |0 |0 |0 |18 |168 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |1 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |97 |0 |0 |0 |0 |0 |0 |0 |0 |
|68 |11 |4 |1 |15 |0 |0 |0 |0 |2 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|38 |0 |1 |7 |0 |0 |1 |0 |61 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|20 |9 |0 |18 |0 |18 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1 |0 |0 |0 |0 |0 |24 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |5 |0 |0 |0 |0 |
|60 |0 |0 |0 |0 |0 |4 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|2 |2 |0 |0 |0 |0 |3 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |5 |0 |0 |
|9 |0 |5 |5 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |7 |0 |0 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.7750865051903114, "precision": 0.9739130434782609, "recall": 0.6436781609195402, "support": 348}, "\"\u23ce": {"f1-score": 0.29411764705882354, "precision": 1.0, "recall": 0.1724137931034483, "support": 29}, "\"\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 4}, "\"\u2423": {"f1-score": 0.9130434782608696, "precision": 1.0, "recall": 0.84, "support": 200}, "\u0027": {"f1-score": 0.9462121212121213, "precision": 0.9054005074302284, "recall": 0.9908766362554542, "support": 2521}, "\u0027\u23ce": {"f1-score": 0.6666666666666666, "precision": 1.0, "recall": 0.5, "support": 10}, "\u0027\u2423": {"f1-score": 0.7105263157894738, "precision": 0.8181818181818182, "recall": 0.627906976744186, "support": 129}, "macro avg": {"f1-score": 0.543632920283398, "precision": 0.6123094819055703, "recall": 0.5180167075455591, "support": 83321}, "micro avg": {"f1-score": 0.9517408576469317, "precision": 0.9517408576469317, "recall": 0.9517408576469317, "support": 83321}, "weighted avg": {"f1-score": 0.9484636867648648, "precision": 0.947419637047283, "recall": 0.9517408576469317, "support": 83321}, "\u2205": {"f1-score": 0.9780640443880514, "precision": 0.9675147853465516, "recall": 0.9888458862410854, "support": 45992}, "\u23ce": {"f1-score": 0.8795323954824649, "precision": 0.8774461355999209, "recall": 0.8816285998013903, "support": 5035}, "\u23ce\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 7}, "\u23ce\u23ce": {"f1-score": 0.756152125279642, "precision": 0.7123287671232876, "recall": 0.8057210965435042, "support": 839}, "\u23ce\u23ce\u0027": {"f1-score": 0.9603960396039605, "precision": 0.9326923076923077, "recall": 0.9897959183673469, "support": 98}, "\u23ce\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7976898250382197, "precision": 0.9161139289894654, "recall": 0.7063778580024067, "support": 3324}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 33}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8653752238320038, "precision": 0.9190871369294605, "recall": 0.8175945862811442, "support": 3251}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 196}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 45}, "\u2423": {"f1-score": 0.9689615841968597, "precision": 0.9631416441528368, "recall": 0.9748522877093608, "support": 20479}, "\u2423\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 70}, "\u2423\u0027": {"f1-score": 0.9044673539518902, "precision": 0.8726790450928382, "recall": 0.9386590584878745, "support": 701}},
  "cl_report_full": {"\"": {"f1-score": 0.6179310344827588, "precision": 0.9739130434782609, "recall": 0.45252525252525255, "support": 495}, "\"\u23ce": {"f1-score": 0.2857142857142857, "precision": 1.0, "recall": 0.16666666666666666, "support": 30}, "\"\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 64}, "\"\u2423": {"f1-score": 0.8772845953002611, "precision": 1.0, "recall": 0.7813953488372093, "support": 215}, "\u0027": {"f1-score": 0.9243293246993525, "precision": 0.9054005074302284, "recall": 0.9440665154950869, "support": 2646}, "\u0027\u23ce": {"f1-score": 0.5882352941176471, "precision": 1.0, "recall": 0.4166666666666667, "support": 12}, "\u0027\u2423": {"f1-score": 0.6721991701244814, "precision": 0.8181818181818182, "recall": 0.5704225352112676, "support": 142}, "macro avg": {"f1-score": 0.5031212552262099, "precision": 0.6123094819055703, "recall": 0.4541890529959519, "support": 89542}, "micro avg": {"f1-score": 0.9174895726673724, "precision": 0.9517408576469317, "recall": 0.8856179223157847, "support": 89542}, "weighted avg": {"f1-score": 0.9090747590549623, "precision": 0.9421825975756143, "recall": 0.8856179223157847, "support": 89542}, "\u2205": {"f1-score": 0.9698979537432956, "precision": 0.9675147853465516, "recall": 0.9722928915018707, "support": 46775}, "\u23ce": {"f1-score": 0.7632393397524072, "precision": 0.8774461355999209, "recall": 0.6753385060094326, "support": 6573}, "\u23ce\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 7}, "\u23ce\u23ce": {"f1-score": 0.6311858076563959, "precision": 0.7123287671232876, "recall": 0.5666387259010897, "support": 1193}, "\u23ce\u23ce\u0027": {"f1-score": 0.9603960396039605, "precision": 0.9326923076923077, "recall": 0.9897959183673469, "support": 98}, "\u23ce\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 19}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.6775357091328812, "precision": 0.9161139289894654, "recall": 0.5375457875457875, "support": 4368}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 101}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8144629998467902, "precision": 0.9190871369294605, "recall": 0.7312242090784044, "support": 3635}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 279}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 65}, "\u2423": {"f1-score": 0.936287958729042, "precision": 0.9631416441528368, "recall": 0.9108910891089109, "support": 21917}, "\u2423\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 108}, "\u2423\u0027": {"f1-score": 0.8468468468468467, "precision": 0.8726790450928382, "recall": 0.8225, "support": 800}},
  "ppcr": 0.9305242232695271
}
```
</details>
