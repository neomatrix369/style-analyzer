# Train report for javascript / file:///tmp/top-repos-quality-repos-ws0fk9mr/node HEAD 6eda924c189e44a36fc97a7cfae41b69483d5bfb

### Classification report

PPCR: 0.914

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.989| 0.998| 0.994| 0.993| 0.991| 515472| 517383| 0.996 |
| `␣` | 0.971| 0.984| 0.938| 0.977| 0.954| 205706| 215752| 0.953 |
| `'` | 0.998| 1.000| 0.986| 0.999| 0.992| 92493| 93788| 0.986 |
| `⏎` | 0.948| 0.895| 0.400| 0.921| 0.562| 32600| 73006| 0.447 |
| `⏎␣⁻␣⁻` | 0.919| 0.888| 0.792| 0.903| 0.851| 20632| 23134| 0.892 |
| `⏎␣⁺␣⁺` | 0.959| 0.871| 0.665| 0.913| 0.785| 20071| 26293| 0.763 |
| `⏎⏎` | 0.976| 0.519| 0.054| 0.678| 0.103| 2240| 21501| 0.104 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 866| 921| 0.940 |
| `⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 240| 247| 0.972 |
| `⏎␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 232| 261| 0.889 |
| `⏎⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 207| 1350| 0.153 |
| `"` | 1.000| 0.051| 0.050| 0.096| 0.095| 198| 201| 0.985 |
| `⏎␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 121| 210| 0.576 |
| `⏎⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 113| 115| 0.983 |
| `⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 109| 130| 0.838 |
| `⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 93| 223| 0.417 |
| `⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 76| 89| 0.854 |
| `␣␣` | 0.000| 0.000| 0.000| 0.000| 0.000| 54| 180| 0.300 |
| `⏎␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 28| 183| 0.153 |
| `⏎⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 27| 511| 0.053 |
| `micro avg` | 0.982| 0.982| 0.897| 0.982| 0.938| 891578| 975478| 0.914 |
| `macro avg` | 0.388| 0.310| 0.244| 0.324| 0.267| 891578| 975478| 0.914 |
| `weighted avg` | 0.979| 0.982| 0.897| 0.980| 0.918| 891578| 975478| 0.914 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| ⏎⏎␣⁻␣⁻| ⏎␣⁻␣⁻␣⁻␣⁻| ⏎⏎⏎| "| ⏎␣⁺␣⁺␣⁺␣⁺| ⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺| ⏎␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻| ⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺| ␣␣| ⏎␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻␣⁻| ⏎⏎␣⁺␣⁺| ⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺| ⏎␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺␣⁺| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1911 |514385 |1047 |0 |0 |1 |39 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|10046 |2009 |202390 |0 |312 |461 |534 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1295 |0 |0 |92493 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|40406 |505 |2881 |0 |29178 |17 |8 |11 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|6222 |1811 |672 |0 |110 |17478 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|2502 |1390 |601 |0 |239 |88 |18314 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|19261 |171 |31 |0 |875 |0 |0 |1163 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1143 |7 |99 |0 |12 |4 |85 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|55 |27 |0 |0 |28 |6 |805 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|484 |3 |1 |0 |6 |0 |0 |17 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|3 |0 |0 |188 |0 |0 |0 |0 |0 |0 |0 |10 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|29 |6 |202 |0 |4 |20 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|130 |4 |88 |0 |1 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|89 |0 |1 |0 |2 |0 |118 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|7 |2 |238 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|126 |11 |9 |0 |0 |34 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|155 |1 |1 |0 |0 |0 |26 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|2 |0 |0 |0 |0 |113 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|13 |0 |76 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|21 |1 |108 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| test/parallel/test-assert.js | 386 |
| test/parallel/test-repl.js | 189 |
| lib/internal/errors.js | 186 |
| test/parallel/test-fs-error-messages.js | 182 |
| test/parallel/test-readline-keys.js | 164 |
| lib/path.js | 151 |
| lib/internal/readline.js | 149 |
| test/parallel/test-util-isDeepStrictEqual.js | 130 |
| test/parallel/test-buffer-indexof.js | 122 |
| test/parallel/test-crypto-hmac.js | 120 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.09615384615384615, "precision": 1.0, "recall": 0.050505050505050504, "support": 198}, "\u0027": {"f1-score": 0.9989847386782162, "precision": 0.9979715367766856, "recall": 1.0, "support": 92493}, "macro avg": {"f1-score": 0.32402341347297514, "precision": 0.3880234307712719, "recall": 0.31024810973318423, "support": 891578}, "micro avg": {"f1-score": 0.9818669819129678, "precision": 0.9818669819129678, "recall": 0.9818669819129678, "support": 891578}, "weighted avg": {"f1-score": 0.9802110226353674, "precision": 0.9793071597259991, "recall": 0.9818669819129678, "support": 891578}, "\u2205": {"f1-score": 0.9932081810765541, "precision": 0.9885688587885066, "recall": 0.9978912530651519, "support": 515472}, "\u23ce": {"f1-score": 0.9209209841084476, "precision": 0.9483537556472844, "recall": 0.8950306748466258, "support": 32600}, "\u23ce\u23ce": {"f1-score": 0.6779364616729817, "precision": 0.9764903442485307, "recall": 0.5191964285714286, "support": 2240}, "\u23ce\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 27}, "\u23ce\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 113}, "\u23ce\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 207}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.9128561355861384, "precision": 0.9591702337833388, "recall": 0.8708086293657515, "support": 20071}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 232}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 93}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 76}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 109}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 240}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9030349350361183, "precision": 0.9189623162225902, "recall": 0.8876502520356727, "support": 20632}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 866}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 121}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 28}, "\u2423": {"f1-score": 0.9773729871472, "precision": 0.9709515699585023, "recall": 0.9838799062740027, "support": 205706}, "\u2423\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 54}},
  "cl_report_full": {"\"": {"f1-score": 0.09478672985781991, "precision": 1.0, "recall": 0.04975124378109453, "support": 201}, "\u0027": {"f1-score": 0.9920469354155382, "precision": 0.9979715367766856, "recall": 0.9861922634025675, "support": 93788}, "macro avg": {"f1-score": 0.26665581617270717, "precision": 0.3880234307712719, "recall": 0.2439180675222498, "support": 975478}, "micro avg": {"f1-score": 0.9377447703764643, "precision": 0.9818669819129678, "recall": 0.8974174712294896, "support": 975478}, "weighted avg": {"f1-score": 0.9179524450893779, "precision": 0.9753802646869582, "recall": 0.8974174712294896, "support": 975478}, "\u2205": {"f1-score": 0.9913791441974491, "precision": 0.9885688587885066, "recall": 0.9942054532135768, "support": 517383}, "\u23ce": {"f1-score": 0.5623428059321789, "precision": 0.9483537556472844, "recall": 0.399665780894721, "support": 73006}, "\u23ce\u23ce": {"f1-score": 0.10250308478759035, "precision": 0.9764903442485307, "recall": 0.05409050741825962, "support": 21501}, "\u23ce\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 511}, "\u23ce\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 115}, "\u23ce\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 1350}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7852633943614512, "precision": 0.9591702337833388, "recall": 0.6647396645494998, "support": 26293}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 261}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 223}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 89}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 130}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 247}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8505677727979937, "precision": 0.9189623162225902, "recall": 0.7916486556583384, "support": 23134}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 921}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 210}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 183}, "\u2423": {"f1-score": 0.9542264561041216, "precision": 0.9709515699585023, "recall": 0.9380677815269384, "support": 215752}, "\u2423\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 180}},
  "ppcr": 0.9139908844689475
}
```
</details>
