# Train report for javascript / file:///tmp/top-repos-quality-repos-yz2yzwu1/meteor HEAD c3309b123a7220ac24cbe73661184ee946bca01f

### Classification report

PPCR: 0.834

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.967| 0.988| 0.974| 0.977| 0.971| 311076| 315550| 0.986 |
| `␣` | 0.939| 0.946| 0.869| 0.943| 0.902| 128978| 140485| 0.918 |
| `"` | 0.997| 1.000| 0.747| 0.999| 0.854| 52117| 69808| 0.747 |
| `⏎` | 0.969| 0.932| 0.631| 0.950| 0.764| 39879| 58895| 0.677 |
| `⏎␣⁻␣⁻` | 0.980| 0.860| 0.383| 0.916| 0.550| 8085| 18177| 0.445 |
| `⏎␣⁺␣⁺` | 0.991| 0.673| 0.244| 0.801| 0.392| 7276| 20021| 0.363 |
| `'` | 0.999| 0.909| 0.065| 0.952| 0.122| 1589| 22247| 0.071 |
| `⇥` | 0.981| 0.694| 0.560| 0.813| 0.713| 1511| 1870| 0.808 |
| `⏎⏎` | 0.991| 0.224| 0.021| 0.366| 0.040| 976| 10600| 0.092 |
| `⏎⇥⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 374| 1121| 0.334 |
| `⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 318| 1200| 0.265 |
| `⏎␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 218| 251| 0.869 |
| `⇥⇥` | 0.000| 0.000| 0.000| 0.000| 0.000| 215| 392| 0.548 |
| `⇥⇥⇥` | 0.000| 0.000| 0.000| 0.000| 0.000| 115| 161| 0.714 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 88| 629| 0.140 |
| `⏎⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 80| 614| 0.130 |
| `␣␣` | 0.000| 0.000| 0.000| 0.000| 0.000| 70| 181| 0.387 |
| `⇥⇥⇥⇥` | 0.000| 0.000| 0.000| 0.000| 0.000| 64| 84| 0.762 |
| `⏎␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 49| 225| 0.218 |
| `⏎␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 40| 277| 0.144 |
| `⏎⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 39| 128| 0.305 |
| `⏎⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 38| 342| 0.111 |
| `⏎⇥⁺⇥⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 20| 171| 0.117 |
| `micro avg` | 0.964| 0.964| 0.804| 0.964| 0.877| 553215| 663429| 0.834 |
| `macro avg` | 0.383| 0.314| 0.195| 0.336| 0.231| 553215| 663429| 0.834 |
| `weighted avg` | 0.961| 0.964| 0.804| 0.961| 0.844| 553215| 663429| 0.834 |

### Confusion matrix

|refusal|  ∅| ␣| "| ⏎| '| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| ⇥| ⏎⇥⁻| ⏎⇥⁺| ⏎␣⁻␣⁻␣⁻␣⁻| ⏎⏎␣⁻␣⁻| ⇥⇥| ⏎⏎⏎| ⏎␣⁺| ⏎␣⁺␣⁺␣⁺␣⁺| ⏎␣⁻| ⏎⇥⁺⇥⁺| ␣␣| ⇥⇥⇥| ⏎⏎⇥⁻| ⇥⇥⇥⇥| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|4474 |307368 |3656 |0 |2 |0 |0 |50 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|11507 |6816 |122036 |0 |78 |0 |19 |16 |0 |13 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|17691 |0 |0 |52115 |0 |2 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|19016 |908 |1792 |0 |37168 |0 |2 |1 |2 |6 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|20658 |0 |0 |144 |0 |1445 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|12745 |1344 |932 |0 |105 |0 |4894 |0 |0 |1 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|10092 |926 |127 |0 |76 |0 |0 |6956 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|9624 |88 |47 |0 |622 |0 |0 |0 |219 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|359 |37 |426 |0 |0 |0 |0 |0 |0 |1048 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|882 |196 |40 |0 |82 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|747 |41 |183 |0 |130 |0 |20 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|541 |26 |7 |0 |2 |0 |0 |53 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|534 |26 |18 |0 |17 |0 |0 |19 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|177 |10 |205 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|304 |6 |0 |0 |32 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|237 |1 |34 |0 |5 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|33 |13 |204 |0 |0 |0 |1 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|176 |5 |23 |0 |21 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|151 |6 |4 |0 |10 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|111 |9 |58 |0 |0 |0 |3 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|46 |2 |113 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|89 |16 |6 |0 |17 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|20 |0 |64 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| packages/deprecated/jquery-layout/jquery.layout.js | 3709 |
| packages/srp/biginteger.js | 1454 |
| packages/deprecated/amplify/amplify.js | 773 |
| packages/mongo/mongo_livedata_tests.js | 701 |
| packages/minimongo/minimongo_tests_client.js | 682 |
| packages/logic-solver/logic_tests.js | 347 |
| packages/minimongo/minimongo_tests_server.js | 340 |
| packages/test-in-browser/diff_match_patch_uncompressed.js | 316 |
| packages/deprecated/markdown/showdown.js | 306 |
| packages/ddp-client/test/livedata_tests.js | 272 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.9986012110063617, "precision": 0.9972444937714078, "recall": 0.9999616248057256, "support": 52117}, "\u0027": {"f1-score": 0.9519104084321476, "precision": 0.9986178299930891, "recall": 0.9093769666456891, "support": 1589}, "macro avg": {"f1-score": 0.33551886248859325, "precision": 0.38322139930476756, "recall": 0.3141983289486758, "support": 553215}, "micro avg": {"f1-score": 0.9639091492457724, "precision": 0.9639091492457724, "recall": 0.9639091492457724, "support": 553215}, "weighted avg": {"f1-score": 0.9614607445736013, "precision": 0.9611129403085578, "recall": 0.9639091492457724, "support": 553215}, "\u21e5": {"f1-score": 0.8127181077937184, "precision": 0.9812734082397003, "recall": 0.6935804103242885, "support": 1511}, "\u21e5\u21e5": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 215}, "\u21e5\u21e5\u21e5": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 115}, "\u21e5\u21e5\u21e5\u21e5": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 64}, "\u2205": {"f1-score": 0.9774470520892959, "precision": 0.9670404349303432, "recall": 0.9880800833236894, "support": 311076}, "\u23ce": {"f1-score": 0.9500293944738388, "precision": 0.968749185497954, "recall": 0.9320193585596429, "support": 39879}, "\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 374}, "\u23ce\u21e5\u207a\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 20}, "\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 318}, "\u23ce\u23ce": {"f1-score": 0.3659147869674186, "precision": 0.9909502262443439, "recall": 0.22438524590163936, "support": 976}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 39}, "\u23ce\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 38}, "\u23ce\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 80}, "\u23ce\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 40}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.8013098649201801, "precision": 0.9908888438955255, "recall": 0.6726223199560198, "support": 7276}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 218}, "\u23ce\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 49}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9164690382081686, "precision": 0.9804087385482735, "recall": 0.8603586889301175, "support": 8085}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 88}, "\u2423": {"f1-score": 0.9425339733465147, "precision": 0.9389190228890171, "recall": 0.9461768673727302, "support": 128978}, "\u2423\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 70}},
  "cl_report_full": {"\"": {"f1-score": 0.8538753307609755, "precision": 0.9972444937714078, "recall": 0.7465476736190695, "support": 69808}, "\u0027": {"f1-score": 0.121971807208576, "precision": 0.9986178299930891, "recall": 0.06495257787566863, "support": 22247}, "macro avg": {"f1-score": 0.23085367122079092, "precision": 0.38322139930476756, "recall": 0.19537171519144508, "support": 663429}, "micro avg": {"f1-score": 0.8765900296224697, "precision": 0.9639091492457724, "recall": 0.803777043210351, "support": 663429}, "weighted avg": {"f1-score": 0.844079963342398, "precision": 0.9585630938557232, "recall": 0.803777043210351, "support": 663429}, "\u21e5": {"f1-score": 0.7134104833219878, "precision": 0.9812734082397003, "recall": 0.560427807486631, "support": 1870}, "\u21e5\u21e5": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 392}, "\u21e5\u21e5\u21e5": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 161}, "\u21e5\u21e5\u21e5\u21e5": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 84}, "\u2205": {"f1-score": 0.9705428216876067, "precision": 0.9670404349303432, "recall": 0.9740706702582792, "support": 315550}, "\u23ce": {"f1-score": 0.7642861549217578, "precision": 0.968749185497954, "recall": 0.6310892265896936, "support": 58895}, "\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 1121}, "\u23ce\u21e5\u207a\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 171}, "\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 1200}, "\u23ce\u23ce": {"f1-score": 0.04047685056833934, "precision": 0.9909502262443439, "recall": 0.020660377358490568, "support": 10600}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 128}, "\u23ce\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 342}, "\u23ce\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 614}, "\u23ce\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 277}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.39214743589743595, "precision": 0.9908888438955255, "recall": 0.24444333449877628, "support": 20021}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 251}, "\u23ce\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 225}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.5504906616017727, "precision": 0.9804087385482735, "recall": 0.38268141057380206, "support": 18177}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 629}, "\u2423": {"f1-score": 0.902432892109739, "precision": 0.9389190228890171, "recall": 0.8686763711428266, "support": 140485}, "\u2423\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 181}},
  "ppcr": 0.8338722003409559
}
```
</details>
