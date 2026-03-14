Video Lectures
============

[<img src=https://github.com/StarlangSoftware/Math/blob/master/video.jpg width="50%">](https://youtu.be/GhcoaVi0SMs)

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/Math-Cy), [Java](https://github.com/starlangsoftware/Math), [C++](https://github.com/starlangsoftware/Math-CPP), [C](https://github.com/starlangsoftware/Math-C), [Swift](https://github.com/starlangsoftware/Math-Swift), [Js](https://github.com/starlangsoftware/Math-Js), [Php](https://github.com/starlangsoftware/Math-Php), or [C#](https://github.com/starlangsoftware/Math-CPP) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-Math
	
## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Math will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/Math-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `Math-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [Vector](#vector)
+ [Matrix](#matrix)
+ [Distribution](#distribution)

## Vector

Bir vektör yaratmak için:

	Vector(self, values=None)

Vektörler eklemek için

	addVector(self, v: Vector)

Çıkarmak için

	subtract(self, v: Vector)
	difference(self, v: Vector) -> Vector

İç çarpım için

	dotProduct(self, v: Vector) -> float
	dotProductWithSelf(self) -> float

Bir vektörle cosinüs benzerliğini hesaplamak için

	double cosineSimilarity(Vector v)

Bir vektörle eleman eleman çarpmak için

	elementProduct(self, v: Vector) -> Vector

## Matrix

3'e 4'lük bir matris yaratmak için

	a = Matrix(3, 4)

Elemanları rasgele değerler alan bir matris yaratmak için

	Matrix(self, row, col, minValue=None, maxValue=None)

Örneğin, 

	a = Matrix(3, 4, 1, 5)
 
3'e 4'lük elemanları 1 ve 5 arasında değerler alan bir matris yaratır.

Matrisin i. satır, j. sütun elemanını getirmek için 

	getValue(self, rowNo: int, colNo: int) -> float

Örneğin,

	a.getValue(3, 4)

3. satır, 4. sütundaki değeri getirir.

Matrisin i. satır, j. sütunundaki elemanı değiştirmek için

	setValue(self, rowNo: int, colNo: int, value: float)

Örneğin,

	a.setValue(3, 4, 5)

3. satır, 4.sütundaki elemanın değerini 5 yapar.

Matrisleri toplamak için

	add(self, m: Matrix)

Çıkarmak için 

	subtract(self, m: Matrix)

Çarpmak için 

	multiply(self, m: Matrix) -> Matrix

Elaman eleman matrisleri çarpmak için

	elementProduct(self, m: Matrix) -> Matrix

Matrisin transpozunu almak için

	transpose(self) -> Matrix

Matrisin simetrik olup olmadığı belirlemek için

	isSymmetric(self) -> bool

Determinantını almak için

	determinant(self) -> float

Tersini almak için

	inverse(self)

Matrisin eigenvektör ve eigendeğerlerini bulmak için

	characteristics(self) -> list

Bu metodla bulunan eigenvektörler eigendeğerlerine göre büyükten küçüğe doğru 
sıralı olarak döndürülür.

## Distribution

Verilen bir değerin normal dağılımdaki olasılığını döndürmek için

	zNormal(z: float) -> float

Verilen bir olasılığın normal dağılımdaki değerini döndürmek için

	zInverse(p: float) -> float

Verilen bir değerin chi kare dağılımdaki olasılığını döndürmek için

	chiSquare(x: float, freedom: int) -> float

Verilen bir olasılığın chi kare dağılımdaki değerini döndürmek için

	chiSquareInverse(p: float, freedom: int) -> float

Verilen bir değerin F dağılımdaki olasılığını döndürmek için

	fDistribution(F: float, freedom1: int, freedom2: int) -> float

Verilen bir olasılığın F dağılımdaki değerini döndürmek için

	fDistributionInverse(p: float, freedom1: int, freedom2: int) -> float

Verilen bir değerin t dağılımdaki olasılığını döndürmek için

	tDistribution(T: float, freedom: int) -> float

Verilen bir olasılığın t dağılımdaki değerini döndürmek için

	tDistributionInverse(p: float, freedom: int) -> float

For Contibutors
============

### Setup.py file
1. Do not forget to set package list. All subfolders should be added to the package list.
```
    packages=['Classification', 'Classification.Model', 'Classification.Model.DecisionTree',
              'Classification.Model.Ensemble', 'Classification.Model.NeuralNetwork',
              'Classification.Model.NonParametric', 'Classification.Model.Parametric',
              'Classification.Filter', 'Classification.DataSet', 'Classification.Instance', 'Classification.Attribute',
              'Classification.Parameter', 'Classification.Experiment',
              'Classification.Performance', 'Classification.InstanceList', 'Classification.DistanceMetric',
              'Classification.StatisticalTest', 'Classification.FeatureSelection'],
```
2. Package name should be lowercase and only may include _ character.
```
    name='nlptoolkit_math',
```

### Python files
1. Do not forget to comment each function.
```
    def __broadcast_shape(self, shape1: Tuple[int, ...], shape2: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Determines the broadcasted shape of two tensors.

        :param shape1: Tuple representing the first tensor shape.
        :param shape2: Tuple representing the second tensor shape.
        :return: Tuple representing the broadcasted shape.
        """
```
2. Function names should follow caml case.
```
    def addItem(self, item: str):
```
3. Local variables should follow snake case.
```
	det = 1.0
	copy_of_matrix = copy.deepcopy(self)
```
4. Class variables should be declared in each file.
```
class Eigenvector(Vector):
    eigenvalue: float
```
5. Variable types should be defined for function parameters and class variables.
```
    def getIndex(self, item: str) -> int:
```
6. For abstract methods, use ABC package and declare them with @abstractmethod.
```
    @abstractmethod
    def train(self, train_set: list[Tensor]):
        pass
```
7. For private methods, use __ as prefix in their names.
```
    def __infer_shape(self, data: Union[List, List[List], List[List[List]]]) -> Tuple[int, ...]:
```
8. For private class variables, use __ as prefix in their names.
```
class Matrix(object):
    __row: int
    __col: int
    __values: list[list[float]]
```
9. Write \_\_repr\_\_ class methods as toString methods
10. Write getter and setter class methods.
```
    def getOptimizer(self) -> Optimizer:
        return self.optimizer
    def setValue(self, value: Optional[Tensor]) -> None:
        self._value = value
```
11. If there are multiple constructors for a class, define them as constructor1, constructor2, ..., then from the original constructor call these methods.
```
    def constructor1(self):
        self.__values = []
        self.__size = 0

    def constructor2(self, values: list):
        self.__values = values.copy()
        self.__size = len(values)

    def __init__(self,
                 valuesOrSize=None,
                 initial=None):
        if valuesOrSize is None:
            self.constructor1()
        elif isinstance(valuesOrSize, list):
            self.constructor2(valuesOrSize)
```
12. Extend test classes from unittest and use separate unit test methods.
```
class TensorTest(unittest.TestCase):

    def test_inferred_shape(self):
        a = Tensor([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual((2, 2), a.getShape())

    def test_shape(self):
        a = Tensor([1.0, 2.0, 3.0])
        self.assertEqual((3, ), a.getShape())
```
13. Enumerated types should be used when necessary as enum classes.
```
class AttributeType(Enum):
    """
    Continuous Attribute
    """
    CONTINUOUS = auto()
    """
    Discrete Attribute
    """
    DISCRETE = auto()
```	
