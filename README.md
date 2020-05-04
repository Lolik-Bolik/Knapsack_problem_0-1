# Lab №2. Knapsack Problem


## Results for *[Knapsack 0-1 Data](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)*
**Замечание:** Столбец `Optim value` содержит правильное значение ценности для рюкзака. Время указано в секундах.

Для того, чтобы не захламлять таблицу мы приняли решение не включать правильный набор предметов в таблицу,
только тот, который берем мы сами. По столбцу `Match` можно узнать, совпал ли этот набор с оптимальным
Поскольку в каждой группе есть алгоритм, выдающий правильный набор, то по нему можно определить, где какой алгоритм ошибся.
В основном, ошибается жадный алгоритм из-за своей изначальной неоптимальности.
Кроме того, в связи с недетерминированностью генетического алгоритма, он может ошибаться на некоторых сэмплах, что и видно из таблицы.
Число хромосом было установлено как `5 * n_items`
### knapsack_1

|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|DynamicSolver   |0.0004   |309          |309        |165          |165     |[1 1 1 1 0 1 0 0 0 0]|True |
|GeneticSolver   |0.0659   |309          |309        |165          |165     |[1 1 1 1 0 1 0 0 0 0]|True |
|ExhaustiveSearch|0.0011   |309          |309        |165          |165     |[1 1 1 1 0 1 0 0 0 0]|True |
|GreedySearch    |0.0      |309          |309        |165          |165     |[1 1 1 1 0 1 0 0 0 0]|True |
|BranchBound     |0.0221   |309          |309        |165          |165     |[1 1 1 1 0 1 0 0 0 0]|True |

### knapsack_2
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|BranchBound     |0.0094   |51           |51         |26           |26      |[0 1 1 1 0]          |True |
|ExhaustiveSearch|0.0      |51           |51         |26           |26      |[0 1 1 1 0]          |True |
|GreedySearch    |0.0      |47           |51         |23           |26      |[1 0 1 0 0]          |False|
|DynamicSolver   |0.0001   |51           |51         |26           |26      |[0 1 1 1 0]          |True |
|GeneticSolver   |0.0187   |51           |51         |26           |26      |[0 1 1 1 0]          |True |

### knapsack_3
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|DynamicSolver   |0.0003   |150          |150        |190          |190     |[1 1 0 0 1 0]        |True |
|GeneticSolver   |0.0211   |150          |150        |190          |190     |[1 1 0 0 1 0]        |True |
|ExhaustiveSearch|0.0001   |150          |150        |190          |190     |[1 1 0 0 1 0]        |True |
|GreedySearch    |0.0      |146          |150        |179          |190     |[1 1 0 1 0 0]        |False|
|BranchBound     |0.0086   |150          |150        |190          |190     |[1 1 0 0 1 0]        |True |


### knapsack_4
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|BranchBound     |0.0076   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |
|GreedySearch    |0.0      |102          |107        |48           |50      |[1 1 0 0 1 1 0]      |False|
|ExhaustiveSearch|0.0001   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |
|GeneticSolver   |0.0296   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |
|DynamicSolver   |0.0001   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |

### knapsack_5
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|DynamicSolver   |0.0002   |900          |900        |104          |104     |[1 0 1 1 1 0 1 1]    |True |
|GeneticSolver   |0.0391   |900          |900        |104          |104     |[1 0 1 1 1 0 1 1]    |True |
|ExhaustiveSearch|0.0003   |900          |900        |104          |104     |[1 0 1 1 1 0 1 1]    |True |
|GreedySearch    |0.0      |858          |900        |97           |104     |[1 1 0 1 1 1 1 1]    |False|
|BranchBound     |0.0083   |900          |900        |104          |104     |[1 0 1 1 1 0 1 1]    |True |


### knapsack_6
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|BranchBound     |0.0361   |1735         |1735       |169          |170     |[0 1 0 1 0 0 1]      |True |
|GreedySearch    |0.0      |1478         |1735       |140          |170     |[1 1 1 0 0 0 0]      |False|
|GeneticSolver   |0.0286   |1735         |1735       |169          |170     |[0 1 0 1 0 0 1]      |True |
|DynamicSolver   |0.0003   |1735         |1735       |169          |170     |[0 1 0 1 0 0 1]      |True |
|ExhaustiveSearch|0.0001   |1735         |1735       |169          |170     |[0 1 0 1 0 0 1]      |True |

### knapsack_7
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|GreedySearch    |0.0      |1441         |1458       |740          |750     |[1 1 1 0 0 0 1 1 1 0 0 0 0 1 1]|False|
|DynamicSolver   |0.0034   |1458         |1458       |749          |750     |[1 0 1 0 1 0 1 1 1 0 0 0 0 1 1]|True |
|GeneticSolver   |0.1789   |1456         |1458       |750          |750     |[0 1 1 1 0 0 1 1 1 0 0 0 0 1 1]|False|
|ExhaustiveSearch|0.0646   |1458         |1458       |749          |750     |[1 0 1 0 1 0 1 1 1 0 0 0 0 1 1]|True |
|BranchBound     |0.1096   |1458         |1458       |749          |750     |[1 0 1 0 1 0 1 1 1 0 0 0 0 1 1]|True |


В следующей таблице можно увидеть сравнение алгоритмов `BranchAndBound` и `ExhaustiveSearch`, поскольку оба эти алгоритма пробегают по дереву перебора.
Из этой таблицы можно увидеть, сколько узлов пробегает каждый алгоритм, а также можно увидеть основные time-killers первого алгоритма
В связи с тем, что выбранный солвер работает зачастую довольно медленно, в худшем случае `BranchAndBound` проигрывает `ExhaustiveSearch`, что можно увидеть на наборе данных, который будет представлен следующим
### BnB - Naive
|File name       |Method name|Work time|Match|Counter|Solve Time|Get Float Time       |
|----------------|-----------|---------|-----|-------|----------|---------------------|
|knapsack_1      |ExhaustiveSearch|0.0011   |True |1024   |0.0       |0.0                  |
|knapsack_1      |BranchBound|0.0221   |True |2      |0.0013    |0.0                  |
|knapsack_2      |BranchBound|0.0094   |True |24     |0.0048    |0.0001               |
|knapsack_2      |ExhaustiveSearch|0.0      |True |32     |0.0       |0.0                  |
|knapsack_3      |ExhaustiveSearch|0.0001   |True |64     |0.0       |0.0                  |
|knapsack_3      |BranchBound|0.0086   |True |22     |0.0041    |0.0001               |
|knapsack_4      |BranchBound|0.0076   |True |14     |0.0032    |0.0001               |
|knapsack_4      |ExhaustiveSearch|0.0001   |True |128    |0.0       |0.0                  |
|knapsack_5      |ExhaustiveSearch|0.0003   |True |256    |0.0       |0.0                  |
|knapsack_5      |BranchBound|0.0083   |True |22     |0.0042    |0.0001               |
|knapsack_6      |BranchBound|0.0361   |True |126    |0.021     |0.0004               |
|knapsack_6      |ExhaustiveSearch|0.0001   |True |128    |0.0       |0.0                  |
|knapsack_7      |ExhaustiveSearch|0.0646   |True |32768  |0.0       |0.0                  |
|knapsack_7      |BranchBound|0.1096   |True |378    |0.0633    |0.0013               |


## Results for *[Low-dimensional 0/1 knapsack problems](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/)*
**Замечание:** Файл `f5_l-d_kp_15_375` был удален, т.к в нем присутствуют дробные значения
### f1_l-d_kp_10_269
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|ExhaustiveSearch|0.0012   |295          |295        |269          |269     |[0 1 1 1 0 0 0 1 1 1]|True |
|GeneticSolver   |0.066    |295          |295        |269          |269     |[0 1 1 1 0 0 0 1 1 1]|True |
|DynamicSolver   |0.0006   |295          |295        |269          |269     |[0 1 1 1 0 0 0 1 1 1]|True |
|GreedySearch    |0.0      |294          |295        |260          |269     |[0 1 1 0 1 0 0 1 1 1]|False|
|BranchBound     |0.0078   |295          |295        |269          |269     |[0 1 1 1 0 0 0 1 1 1]|True |


### f2_l-d_kp_20_878
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|ExhaustiveSearch|1.392    |1024         |1024       |871          |878     |[1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1]|True |
|GeneticSolver   |0.4305   |1024         |1024       |871          |878     |[1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1]|True |
|DynamicSolver   |0.0081   |1024         |1024       |871          |878     |[1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1]|True |
|GreedySearch    |0.0      |1018         |1024       |837          |878     |[1 1 1 1 1 1 1 0 1 1 1 1 1 0 1 0 1 1 1 1]|False|
|BranchBound     |0.0066   |1024         |1024       |871          |878     |[1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1]|True |

### f3_l-d_kp_4_20

|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|GreedySearch    |0.0      |35           |35         |18           |20      |[1 1 0 1]            |True |
|BranchBound     |0.0032   |35           |35         |18           |20      |[1 1 0 1]            |True |
|ExhaustiveSearch|0.0      |35           |35         |18           |20      |[1 1 0 1]            |True |
|GeneticSolver   |0.0097   |35           |35         |18           |20      |[1 1 0 1]            |True |
|DynamicSolver   |0.0      |35           |35         |18           |20      |[1 1 0 1]            |True |


### f4_l-d_kp_4_11
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|DynamicSolver   |0.0      |23           |23         |11           |11      |[0 1 0 1]            |True |
|BranchBound     |0.0292   |23           |23         |11           |11      |[0 1 0 1]            |True |
|GreedySearch    |0.0      |16           |23         |6            |11      |[1 1 0 0]            |False|
|ExhaustiveSearch|0.0      |23           |23         |11           |11      |[0 1 0 1]            |True |
|GeneticSolver   |0.0101   |23           |23         |11           |11      |[0 1 0 1]            |True |


### f6_l-d_kp_10_60
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|BranchBound     |0.0083   |52           |52         |57           |60      |[0 0 1 0 1 1 1 1 1 1]|True |
|GreedySearch    |0.0      |52           |52         |57           |60      |[0 0 1 0 1 1 1 1 1 1]|True |
|ExhaustiveSearch|0.0012   |52           |52         |57           |60      |[0 0 1 0 1 1 1 1 1 1]|True |
|GeneticSolver   |0.0657   |52           |52         |58           |60      |[0 0 1 1 0 1 1 1 1 1]|True |
|DynamicSolver   |0.0002   |52           |52         |60           |60      |[0 0 1 1 1 0 1 0 0 0]|True |


### f7_l-d_kp_7_50
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|ExhaustiveSearch|0.0001   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |
|BranchBound     |0.0049   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |
|GreedySearch    |0.0      |102          |107        |48           |50      |[1 1 0 0 1 1 0]      |False|
|GeneticSolver   |0.0289   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |
|DynamicSolver   |0.0001   |107          |107        |50           |50      |[1 0 0 1 0 0 0]      |True |


### f8_l-d_kp_23_10000
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|GreedySearch    |0.0      |9751         |9767       |9750         |10000   |[1 1 1 1 1 1 1 0 0 1 0 0 0 0 0 1 1 0 0 0 0 1 0]|False|
|ExhaustiveSearch|11.3763  |9767         |9767       |9768         |10000   |[1 1 1 1 1 1 1 1 0 0 1 0 0 0 0 1 1 0 0 0 0 0 0]|True |
|GeneticSolver   |0.6345   |9756         |9767       |9767         |10000   |[1 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0]|False|
|DynamicSolver   |0.0668   |9767         |9767       |9768         |10000   |[1 1 1 1 1 1 1 1 0 1 0 0 0 0 0 1 1 0 0 0 0 0 0]|True |
|BranchBound     |1188.6169|9767         |9767       |9768         |10000   |[1 1 1 1 1 1 1 1 0 1 0 0 0 0 0 1 1 0 0 0 0 0 0]|True |


### f9_l-d_kp_5_80
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|GreedySearch    |0.0      |130          |130        |60           |80      |[1 1 1 1 0]          |True |
|DynamicSolver   |0.0001   |130          |130        |60           |80      |[1 1 1 1 0]          |True |
|GeneticSolver   |0.0148   |130          |130        |60           |80      |[1 1 1 1 0]          |True |
|ExhaustiveSearch|0.0      |130          |130        |60           |80      |[1 1 1 1 0]          |True |
|BranchBound     |0.0018   |130          |130        |60           |80      |[1 1 1 1 0]          |True |


### f10_l-d_kp_20_879.csv
|Method name     |Work time|Result Profit|Optim value|Result Weight|Capacity|Answer               |Match|
|----------------|---------|-------------|-----------|-------------|--------|---------------------|-----|
|BranchBound     |0.0075   |1025         |1025       |871          |879     |[1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 1 0 1 1 1]|True |
|GreedySearch    |0.0      |1019         |1025       |837          |879     |[1 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 0 1 1 1]|False|
|ExhaustiveSearch|1.3606   |1025         |1025       |871          |879     |[1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 1 0 1 1 1]|True |
|GeneticSolver   |0.4171   |1025         |1025       |871          |879     |[1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 1 0 1 1 1]|True |
|DynamicSolver   |0.005    |1025         |1025       |871          |879     |[1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 1 0 1 1 1]|True |


### BnB - Naive
В данной таблице можно увидеть, что в худшем случае при использовании данного солвера `BnB` может сильно проиграть `Naive Search`.
Данный случай выделен жирным

|File name       |Method name|Work time|Match|Counter|Solve Time|Get Float Time       |
|----------------|-----------|---------|-----|-------|----------|---------------------|
|f10_l-d_kp_20_879|BranchBound|0.0075   |True |22     |0.0039    |0.0001               |
|f10_l-d_kp_20_879|ExhaustiveSearch|1.3606   |True |1048576|NaN       |NaN                  |
|f1_l-d_kp_10_269|ExhaustiveSearch|0.0012   |True |1024   |NaN       |NaN                  |
|f1_l-d_kp_10_269|BranchBound|0.0078   |True |24     |0.0042    |0.0001               |
|f2_l-d_kp_20_878|ExhaustiveSearch|1.392    |True |1048576|NaN       |NaN                  |
|f2_l-d_kp_20_878|BranchBound|0.0066   |True |20     |0.0033    |0.0001               |
|f3_l-d_kp_4_20  |BranchBound|0.0032   |True |6      |0.0011    |NaN                  |
|f3_l-d_kp_4_20  |ExhaustiveSearch|0.0      |True |16     |NaN       |NaN                  |
|f4_l-d_kp_4_11  |BranchBound|0.0292   |True |14     |0.0048    |0.0001               |
|f4_l-d_kp_4_11  |ExhaustiveSearch|0.0      |True |16     |NaN       |NaN                  |
|f6_l-d_kp_10_60 |BranchBound|0.0083   |True |26     |0.0046    |0.0001               |
|f6_l-d_kp_10_60 |ExhaustiveSearch|0.0012   |True |1024   |NaN       |NaN                  |
|f7_l-d_kp_7_50  |ExhaustiveSearch|0.0001   |True |128    |NaN       |NaN                  |
|f7_l-d_kp_7_50  |BranchBound|0.0049   |True |14     |0.0024    |NaN                  |
|**f8_l-d_kp_23_10000**|ExhaustiveSearch|**11.3763**  |True |8388608|NaN       |NaN                  |
|**f8_l-d_kp_23_10000**|BranchBound|**1188.6169**|True |4407676|708.755   |14.8591              |
|f9_l-d_kp_5_80  |ExhaustiveSearch|0.0      |True |32     |NaN       |NaN                  |
|f9_l-d_kp_5_80  |BranchBound|0.0018   |True |2      |0.0006    |NaN                  |


## Results for *[Large-scale 0/1 knapsack problems](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/)*
**Замечание:** `ExhaustiveSearch` не использовался, поскольку ждать пару миллионов лет немного непозволительная роскошь.
Кроме того, начиная с некоторого набора данных возникли проблемы с солвером в `BnB`, который требует его купить (^_^) для решения настолько больших систем.
Поэтому было принято решения использовать бенчмарк не полностью

Результаты сгрупированны по числу предметов, доступных для выбора. Для генетического алгоритма число хромосом установлено как `n_items`, что негативно сыграло на точности

Кроме того, данная статистика не содержит поле `Answer`, т.к оно слишком большое и захламляет таблицу
### 100 Items
|File name       |Method name|Work time|Result Profit|Optim value|Result Weight|Capacity             |Match|
|----------------|-----------|---------|-------------|-----------|-------------|---------------------|-----|
|knapPI_1_100_1000_1|DynamicSolver|0.0207   |9147         |9147       |985          |995                  |True |
|knapPI_1_100_1000_1  |GeneticSolver|0.0308   |6301         |9147       |793          |995     |False|
|knapPI_1_100_1000_1|GreedySearch|0.0005   |8817         |9147       |908          |995                  |False|
|knapPI_1_100_1000_1|BranchBound|0.2167   |9147         |9147       |985          |995                  |True |
|knapPI_2_100_1000_1|GreedySearch|0.0001   |1487         |1514       |983          |995                  |False|
|knapPI_2_100_1000_1  |GeneticSolver|0.0315   |1158         |1514       |981          |995     |False|
|knapPI_2_100_1000_1|DynamicSolver|0.0237   |1514         |1514       |991          |995                  |True |
|knapPI_2_100_1000_1|BranchBound|0.8197   |1514         |1514       |991          |995                  |True |
|knapPI_3_100_1000_1  |GeneticSolver|0.031    |1396         |2397       |996          |997     |False|
|knapPI_3_100_1000_1|DynamicSolver|0.02     |2397         |2397       |997          |997                  |True |
|knapPI_3_100_1000_1|BranchBound|0.3791   |2397         |2397       |997          |997                  |True |
|knapPI_3_100_1000_1|GreedySearch|0.0001   |2375         |2397       |975          |997                  |False|

### 200 Items
|File name       |Method name|Work time|Result Profit|Optim value|Result Weight|Capacity             |Match|
|----------------|-----------|---------|-------------|-----------|-------------|---------------------|-----|
|knapPI_1_200_1000_1|BranchBound|0.4333   |11238        |11238      |987          |1008                 |True |
|knapPI_1_200_1000_1|GreedySearch|0.0001   |11227        |11238      |981          |1008                 |False|
|knapPI_1_200_1000_1  |GeneticSolver|0.0871   |6669         |11238      |941          |1008    |False|
|knapPI_1_200_1000_1|DynamicSolver|0.0412   |11238        |11238      |987          |1008                 |True |
|knapPI_2_200_1000_1|BranchBound|3.1694   |1634         |1634       |1006         |1008                 |True |
|knapPI_2_200_1000_1|DynamicSolver|0.041|1634         |1634       |1006         |1008                 |True |
|knapPI_2_200_1000_1  |GeneticSolver|0.0898   |1186         |1634       |999          |1008    |False|
|knapPI_2_200_1000_1|GreedySearch|0.0001   |1604         |1634       |1004         |1008                 |False|
|knapPI_3_200_1000_1|GreedySearch|0.0001   |2649         |2697       |949          |997                  |False|
|knapPI_3_200_1000_1  |GeneticSolver|0.0938   |1686         |2697       |986          |997     |False|
|knapPI_3_200_1000_1|DynamicSolver|0.0426   |2697         |2697       |997          |997                  |True |
|knapPI_3_200_1000_1|BranchBound|81.2847  |2697         |2697       |997          |997                  |True |

### 500 Items
|File name       |Method name|Work time|Result Profit|Optim value|Result Weight|Capacity             |Match|
|----------------|-----------|---------|-------------|-----------|-------------|---------------------|-----|
|knapPI_1_500_1000_1|BranchBound|0.6063   |28857        |28857      |2543         |2543                 |True |
|knapPI_1_500_1000_1|DynamicSolver|0.3468   |28857        |28857      |2543         |2543                 |True |
|knapPI_1_500_1000_1  |GeneticSolver|0.4528   |10364        |28857      |2414         |2543    |False|
|knapPI_1_500_1000_1|GreedySearch|0.0002   |28834        |28857      |2528         |2543                 |False|
|knapPI_2_500_1000_1|BranchBound|2.5387   |4566         |4566       |2543         |2543                 |True |
|knapPI_2_500_1000_1|DynamicSolver|0.3502   |4566         |4566       |2543         |2543                 |True |
|knapPI_2_500_1000_1  |GeneticSolver|0.424    |3096         |4566       |2529         |2543    |False|
|knapPI_2_500_1000_1|GreedySearch|0.0002   |4552         |4566       |2538         |2543                 |False|
|knapPI_3_500_1000_1  |GeneticSolver|0.4394   |3687         |7117       |2487         |2517    |False|
|knapPI_3_500_1000_1|BranchBound|183.2984 |7117         |7117       |2517         |2517                 |True |
|knapPI_3_500_1000_1|GreedySearch|0.0002   |7098         |7117       |2498         |2517                 |False|
|knapPI_3_500_1000_1|DynamicSolver|0.3439   |7117         |7117       |2517         |2517                 |True |

### 1000 Items
|File name       |Method name|Work time|Result Profit|Optim value|Result Weight|Capacity             |Match|
|----------------|-----------|---------|-------------|-----------|-------------|---------------------|-----|
|knapPI_1_1000_1000_1|BranchBound|7.1942   |54503        |54503      |5002         |5002                 |True |
|knapPI_1_1000_1000_1|GreedySearch|0.0006   |54386        |54503      |4991         |5002                 |False|
|knapPI_1_1000_1000_1 |GeneticSolver|1.6285   |15712        |54503      |4430         |5002    |False|
|knapPI_1_1000_1000_1|DynamicSolver|1.5454   |54503        |54503      |5002         |5002                 |True |
|knapPI_2_1000_1000_1|DynamicSolver|1.5515   |9052         |9052       |5002         |5002                 |True |
|knapPI_2_1000_1000_1 |GeneticSolver|1.5977   |5687         |9052       |4998         |5002    |False|
|knapPI_2_1000_1000_1|BranchBound|15.1673  |9052         |9052       |5002         |5002                 |True |
|knapPI_2_1000_1000_1|GreedySearch|0.0005   |9046         |9052       |4994         |5002                 |False|
|knapPI_3_1000_1000_1|BranchBound|18995.5164|14390        |14390      |4990         |4990                 |True |
|knapPI_3_1000_1000_1|GreedySearch|0.0005   |14374        |14390      |4974         |4990                 |False|
|knapPI_3_1000_1000_1 |GeneticSolver|1.6074   |6716         |14390      |4916         |4990    |False|
|knapPI_3_1000_1000_1|DynamicSolver|1.5119   |14390        |14390      |4990         |4990                 |True |

### 2000 Items
|File name       |Method name|Work time|Result Profit|Optim value|Result Weight|Capacity             |Match|
|----------------|-----------|---------|-------------|-----------|-------------|---------------------|-----|
|knapPI_1_2000_1000_1|GreedySearch|0.0009   |110547       |110625     |9996         |10011                |False|
|knapPI_1_2000_1000_1 |GeneticSolver|6.0955   |22488        |110625     |9909         |10011   |False|
|knapPI_1_2000_1000_1|DynamicSolver|6.5692   |110625       |110625     |10011        |10011                |True |
|knapPI_2_2000_1000_1|GreedySearch|0.001    |18038        |18051      |10010        |10011                |False|
|knapPI_2_2000_1000_1 |GeneticSolver|6.0934   |11073        |18051      |10008        |10011   |False|
|knapPI_2_2000_1000_1|DynamicSolver|6.4205   |18051        |18051      |10010        |10011                |True |
|knapPI_3_2000_1000_1 |GeneticSolver|5.8929   |12524        |28919      |9724         |9819    |False|
|knapPI_3_2000_1000_1|DynamicSolver|6.2337   |28919        |28919      |9819         |9819                 |True |
|knapPI_3_2000_1000_1|GreedySearch|0.0009   |28827        |28919      |9727         |9819                 |False|

### 5000 Items
|File name       |Method name|Work time|Result Profit|Optim value|Result Weight|Capacity             |Match|
|----------------|-----------|---------|-------------|-----------|-------------|---------------------|-----|
|knapPI_1_5000_1000_1|GreedySearch|0.0023   |276379       |276457     |25008        |25016                |False|
|knapPI_1_5000_1000_1 |GeneticSolver|36.5017  |36717        |276457     |24509        |25016   |False|
|knapPI_1_5000_1000_1|DynamicSolver|40.5078  |276457       |276457     |25016        |25016                |True |
|knapPI_2_5000_1000_1|DynamicSolver|42.0405  |44356        |44356      |25016        |25016                |True |
|knapPI_2_5000_1000_1 |GeneticSolver|36.1967  |26519        |44356      |24955        |25016   |False|
|knapPI_2_5000_1000_1|GreedySearch|0.0026   |44351        |44356      |25016        |25016                |False|
|knapPI_3_5000_1000_1|DynamicSolver|41.8174  |72505        |72505      |24805        |24805                |True |
|knapPI_3_5000_1000_1 |GeneticSolver|36.4495  |30178        |72505      |24778        |24805   |False|
|knapPI_3_5000_1000_1|GreedySearch|0.0029   |72446        |72505      |24746        |24805                |False|

### 10000 Items

|File name       |Method name|Work time|Result Profit|Optim value|Result Weight|Capacity             |Match|
|----------------|-----------|---------|-------------|-----------|-------------|---------------------|-----|
|knapPI_1_10000_1000_1|DynamicSolver|169.7613 |563647       |563647     |49877        |49877                |True |
|knapPI_1_10000_1000_1|GreedySearch|0.0048   |563605       |563647     |49876        |49877                |False|
|knapPI_1_10000_1000_1|GeneticSolver|140.322  |52585        |563647     |45655        |49877   |False|
|knapPI_2_10000_1000_1|DynamicSolver|164.3271 |90204        |90204      |49877        |49877                |True |
|knapPI_2_10000_1000_1|GeneticSolver|142.4558 |50951        |90204      |49654        |49877   |False|
|knapPI_2_10000_1000_1|GreedySearch|0.0049   |90200        |90204      |49877        |49877                |False|
|knapPI_3_10000_1000_1|GeneticSolver|143.7508 |58890        |146919     |49490        |49519   |False|
|knapPI_3_10000_1000_1|GreedySearch|0.0052   |146888       |146919     |49488        |49519                |False|
|knapPI_3_10000_1000_1|DynamicSolver|167.7399 |146919       |146919     |49519        |49519                |True |

### BnB Timekillers
Как видно из этой таблицы, в одном кейсе алгоритм работал более 5 часов. Из них 8000 секунд заняла работа солвера
Как мы предполагаем, также в данном случае time-killer'ом может выступать постоянное добавление и удаление ограничений в
системе, т.к там возможно использование питоновских структур данных, которые могут быть довольно медленными

Однако, это время не замерялось 

|File name       |Method name|Work time|Match|Counter|Solve Time|Get Float Time       |
|----------------|-----------|---------|-----|-------|----------|---------------------|
|knapPI_1_1000_1000_1|BranchBound|7.1942   |True |8652   |3.0255    |0.0308               |
|knapPI_1_100_1000_1|BranchBound|0.2167   |True |710    |0.1215    |0.002                |
|knapPI_1_200_1000_1|BranchBound|0.4333   |True |1186   |0.2276    |0.0034               |
|knapPI_1_500_1000_1|BranchBound|0.6063   |True |1150   |0.2837    |0.0035               |
|knapPI_2_1000_1000_1|BranchBound|15.1673  |True |18912  |6.2182    |0.0674               |
|knapPI_2_100_1000_1|BranchBound|0.8197   |True |2722   |0.4683    |0.0077               |
|knapPI_2_200_1000_1|BranchBound|3.1694   |True |8938   |1.7064    |0.0257               |
|knapPI_2_500_1000_1|BranchBound|2.5387   |True |4842   |1.1885    |0.0148               |
|knapPI_3_1000_1000_1|BranchBound|18995.5164|True |23504080|7944.3911 |82.7898              |
|knapPI_3_100_1000_1|BranchBound|0.3791   |True |1228   |0.2125    |0.0034               |
|knapPI_3_200_1000_1|BranchBound|81.2847  |True |219636 |43.1455   |0.6635               |
|knapPI_3_500_1000_1|BranchBound|183.2984 |True |344166 |85.2296   |1.0873               |


## Team Members
- *[Alexander Slavutin](https://github.com/AlexanderSlav)* 
- *[Pavel Semkin](https://github.com/PVSemk)*

Copyright (C) 2020-2021, Bolik&Lolik Inc. , all rights reserved.
